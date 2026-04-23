import AVFoundation
import AppKit
import CoreImage
import Foundation

struct Manifest: Decodable {
    let width: Int
    let height: Int
    let fps: Int
    let audioPath: String
    let outputPath: String
    let reviewImageDir: String?
    let reviewOnly: Bool?
    let slides: [Slide]
}

struct Slide: Decodable {
    let title: String
    let body: String
    let accent: String
    let background: String
    let badge: String
    let footer: String
    let duration: Double
}

enum VideoBuilderError: Error {
    case invalidArguments
    case cannotCreateWriter
    case cannotCreateBuffer
    case exportFailed(String)
    case missingTrack(String)
}

func loadManifest() throws -> Manifest {
    guard CommandLine.arguments.count >= 2 else {
        throw VideoBuilderError.invalidArguments
    }
    let path = CommandLine.arguments[1]
    let data = try Data(contentsOf: URL(fileURLWithPath: path))
    return try JSONDecoder().decode(Manifest.self, from: data)
}

func color(hex: String) -> NSColor {
    let cleaned = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
    var value: UInt64 = 0
    Scanner(string: cleaned).scanHexInt64(&value)
    let red = CGFloat((value >> 16) & 0xFF) / 255.0
    let green = CGFloat((value >> 8) & 0xFF) / 255.0
    let blue = CGFloat(value & 0xFF) / 255.0
    return NSColor(red: red, green: green, blue: blue, alpha: 1.0)
}

func drawRoundedRect(_ rect: NSRect, radius: CGFloat, fill: NSColor) {
    fill.setFill()
    let path = NSBezierPath(roundedRect: rect, xRadius: radius, yRadius: radius)
    path.fill()
}

func textAttributes(size: CGFloat, weight: NSFont.Weight, color: NSColor) -> [NSAttributedString.Key: Any] {
    let paragraph = NSMutableParagraphStyle()
    paragraph.alignment = .left
    paragraph.lineBreakMode = .byWordWrapping
    return [
        .font: NSFont.systemFont(ofSize: size, weight: weight),
        .foregroundColor: color,
        .paragraphStyle: paragraph,
    ]
}

func measuredTextHeight(_ text: String, width: CGFloat, attributes: [NSAttributedString.Key: Any]) -> CGFloat {
    let attributed = NSAttributedString(string: text, attributes: attributes)
    let rect = attributed.boundingRect(
        with: NSSize(width: width, height: CGFloat.greatestFiniteMagnitude),
        options: [.usesLineFragmentOrigin, .usesFontLeading]
    )
    return ceil(rect.height)
}

func renderSlide(_ slide: Slide, width: Int, height: Int) -> CGImage {
    let size = NSSize(width: width, height: height)
    guard let bitmap = NSBitmapImageRep(
        bitmapDataPlanes: nil,
        pixelsWide: width,
        pixelsHigh: height,
        bitsPerSample: 8,
        samplesPerPixel: 4,
        hasAlpha: true,
        isPlanar: false,
        colorSpaceName: .deviceRGB,
        bytesPerRow: 0,
        bitsPerPixel: 0
    ) else {
        fatalError("无法创建 1x 渲染画布")
    }
    bitmap.size = size
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: bitmap)
    defer {
        NSGraphicsContext.restoreGraphicsState()
    }

    let backgroundRect = NSRect(x: 0, y: 0, width: width, height: height)
    color(hex: slide.background).setFill()
    backgroundRect.fill()

    let topBand = NSRect(x: 0, y: height - 220, width: width, height: 220)
    drawRoundedRect(topBand, radius: 0, fill: color(hex: slide.accent))

    let cardRect = NSRect(x: 96, y: 320, width: width - 192, height: height - 760)
    drawRoundedRect(cardRect, radius: 42, fill: NSColor.white)

    let badgeRect = NSRect(x: 96, y: height - 154, width: 190, height: 56)
    drawRoundedRect(badgeRect, radius: 28, fill: NSColor.white.withAlphaComponent(0.20))
    (slide.badge as NSString).draw(
        in: NSRect(x: 126, y: height - 140, width: 150, height: 30),
        withAttributes: textAttributes(size: 24, weight: .semibold, color: .white)
    )

    (slide.title as NSString).draw(
        in: NSRect(x: 96, y: height - 460, width: width - 192, height: 180),
        withAttributes: textAttributes(size: 72, weight: .bold, color: NSColor.black.withAlphaComponent(0.78))
    )

    let bodyLines = slide.body
        .split(separator: "\n", omittingEmptySubsequences: false)
        .map { String($0) }
    var currentY = cardRect.maxY - 160
    for (index, line) in bodyLines.enumerated() {
        let drawLine = index == 0 ? line : "• " + line
        let fontSize: CGFloat = index == 0 ? 42 : 38
        let weight: NSFont.Weight = index == 0 ? .bold : .regular
        let attributes = textAttributes(size: fontSize, weight: weight, color: .black)
        let textWidth = cardRect.width - 128
        let measuredHeight = measuredTextHeight(drawLine, width: textWidth, attributes: attributes)
        let rowHeight = max(index == 0 ? 96 : 76, measuredHeight + 18)
        (drawLine as NSString).draw(
            in: NSRect(x: cardRect.minX + 64, y: currentY, width: textWidth, height: rowHeight),
            withAttributes: attributes
        )
        currentY -= rowHeight + 24
    }

    let footerRect = NSRect(x: 96, y: 150, width: width - 192, height: 86)
    drawRoundedRect(footerRect, radius: 28, fill: NSColor.black.withAlphaComponent(0.88))
    let pageRect = NSRect(x: width - 250, y: 150, width: 154, height: 86)
    (slide.footer as NSString).draw(
        in: NSRect(x: 132, y: 168, width: pageRect.minX - 156, height: 48),
        withAttributes: textAttributes(size: 28, weight: .medium, color: .white)
    )

    drawRoundedRect(pageRect, radius: 28, fill: color(hex: slide.accent))
    ("PPT Demo" as NSString).draw(
        in: NSRect(x: width - 222, y: 175, width: 120, height: 28),
        withAttributes: textAttributes(size: 24, weight: .semibold, color: .white)
    )

    return bitmap.cgImage!
}

func savePNG(_ image: CGImage, to url: URL) throws {
    let bitmap = NSBitmapImageRep(cgImage: image)
    guard let data = bitmap.representation(using: .png, properties: [:]) else {
        throw VideoBuilderError.exportFailed("无法创建 PNG review 图")
    }
    try data.write(to: url)
}

func writeReviewImages(_ manifest: Manifest) throws {
    guard let reviewImageDir = manifest.reviewImageDir else {
        return
    }

    let reviewURL = URL(fileURLWithPath: reviewImageDir)
    try FileManager.default.createDirectory(at: reviewURL, withIntermediateDirectories: true)

    for (index, slide) in manifest.slides.enumerated() {
        let image = renderSlide(slide, width: manifest.width, height: manifest.height)
        let fileName = String(format: "%02d_1x默认视图_no_zoom.png", index + 1)
        try savePNG(image, to: reviewURL.appendingPathComponent(fileName))
    }
}

func makePixelBuffer(from image: CGImage, width: Int, height: Int) throws -> CVPixelBuffer {
    var buffer: CVPixelBuffer?
    let attributes: [CFString: Any] = [
        kCVPixelBufferCGImageCompatibilityKey: true,
        kCVPixelBufferCGBitmapContextCompatibilityKey: true,
        kCVPixelBufferWidthKey: width,
        kCVPixelBufferHeightKey: height,
        kCVPixelBufferPixelFormatTypeKey: Int(kCVPixelFormatType_32ARGB),
    ]

    let status = CVPixelBufferCreate(
        kCFAllocatorDefault,
        width,
        height,
        kCVPixelFormatType_32ARGB,
        attributes as CFDictionary,
        &buffer
    )
    guard status == kCVReturnSuccess, let pixelBuffer = buffer else {
        throw VideoBuilderError.cannotCreateBuffer
    }

    CVPixelBufferLockBaseAddress(pixelBuffer, [])
    defer { CVPixelBufferUnlockBaseAddress(pixelBuffer, []) }

    guard let context = CGContext(
        data: CVPixelBufferGetBaseAddress(pixelBuffer),
        width: width,
        height: height,
        bitsPerComponent: 8,
        bytesPerRow: CVPixelBufferGetBytesPerRow(pixelBuffer),
        space: CGColorSpaceCreateDeviceRGB(),
        bitmapInfo: CGImageAlphaInfo.noneSkipFirst.rawValue
    ) else {
        throw VideoBuilderError.cannotCreateBuffer
    }

    context.clear(CGRect(x: 0, y: 0, width: width, height: height))
    context.draw(image, in: CGRect(x: 0, y: 0, width: width, height: height))
    return pixelBuffer
}

func waitUntilReady(_ input: AVAssetWriterInput) {
    while !input.isReadyForMoreMediaData {
        Thread.sleep(forTimeInterval: 0.02)
    }
}

func buildVideoOnly(_ manifest: Manifest, outputURL: URL) throws {
    try? FileManager.default.removeItem(at: outputURL)
    guard let writer = try? AVAssetWriter(outputURL: outputURL, fileType: .mp4) else {
        throw VideoBuilderError.cannotCreateWriter
    }

    let settings: [String: Any] = [
        AVVideoCodecKey: AVVideoCodecType.h264,
        AVVideoWidthKey: manifest.width,
        AVVideoHeightKey: manifest.height,
    ]
    let input = AVAssetWriterInput(mediaType: .video, outputSettings: settings)
    input.expectsMediaDataInRealTime = false
    let adaptor = AVAssetWriterInputPixelBufferAdaptor(
        assetWriterInput: input,
        sourcePixelBufferAttributes: [
            kCVPixelBufferPixelFormatTypeKey as String: Int(kCVPixelFormatType_32ARGB),
            kCVPixelBufferWidthKey as String: manifest.width,
            kCVPixelBufferHeightKey as String: manifest.height,
        ]
    )

    writer.add(input)
    writer.startWriting()
    writer.startSession(atSourceTime: .zero)

    let fps = manifest.fps
    var frameIndex: Int64 = 0

    for slide in manifest.slides {
        let frameCount = max(1, Int(round(slide.duration * Double(fps))))
        let image = renderSlide(slide, width: manifest.width, height: manifest.height)

        for _ in 0 ..< frameCount {
            waitUntilReady(input)
            let timestamp = CMTime(value: frameIndex, timescale: CMTimeScale(fps))
            let buffer = try makePixelBuffer(from: image, width: manifest.width, height: manifest.height)
            adaptor.append(buffer, withPresentationTime: timestamp)
            frameIndex += 1
        }
    }

    input.markAsFinished()
    let semaphore = DispatchSemaphore(value: 0)
    writer.finishWriting {
        semaphore.signal()
    }
    semaphore.wait()

    if writer.status != .completed {
        throw VideoBuilderError.exportFailed(writer.error?.localizedDescription ?? "视频写入失败")
    }
}

func exportWithAudio(videoURL: URL, audioURL: URL, outputURL: URL) throws {
    try? FileManager.default.removeItem(at: outputURL)
    let composition = AVMutableComposition()

    let videoAsset = AVURLAsset(url: videoURL)
    let audioAsset = AVURLAsset(url: audioURL)

    guard let sourceVideoTrack = videoAsset.tracks(withMediaType: .video).first else {
        throw VideoBuilderError.missingTrack("缺少视频轨道")
    }
    guard let compositionVideoTrack = composition.addMutableTrack(
        withMediaType: .video,
        preferredTrackID: kCMPersistentTrackID_Invalid
    ) else {
        throw VideoBuilderError.missingTrack("无法创建视频轨道")
    }
    try compositionVideoTrack.insertTimeRange(
        CMTimeRange(start: .zero, duration: videoAsset.duration),
        of: sourceVideoTrack,
        at: .zero
    )
    compositionVideoTrack.preferredTransform = sourceVideoTrack.preferredTransform

    if let sourceAudioTrack = audioAsset.tracks(withMediaType: .audio).first,
       let compositionAudioTrack = composition.addMutableTrack(
           withMediaType: .audio,
           preferredTrackID: kCMPersistentTrackID_Invalid
       ) {
        let duration = CMTimeMinimum(videoAsset.duration, audioAsset.duration)
        try compositionAudioTrack.insertTimeRange(
            CMTimeRange(start: .zero, duration: duration),
            of: sourceAudioTrack,
            at: .zero
        )
    }

    guard let exportSession = AVAssetExportSession(
        asset: composition,
        presetName: AVAssetExportPresetHighestQuality
    ) else {
        throw VideoBuilderError.exportFailed("无法创建导出任务")
    }

    exportSession.outputURL = outputURL
    exportSession.outputFileType = .mp4
    exportSession.shouldOptimizeForNetworkUse = true

    let semaphore = DispatchSemaphore(value: 0)
    exportSession.exportAsynchronously {
        semaphore.signal()
    }
    semaphore.wait()

    if exportSession.status != .completed {
        throw VideoBuilderError.exportFailed(exportSession.error?.localizedDescription ?? "导出失败")
    }
}

do {
    let manifest = try loadManifest()
    try writeReviewImages(manifest)

    if manifest.reviewOnly == true {
        exit(0)
    }

    let outputURL = URL(fileURLWithPath: manifest.outputPath)
    let tempVideoURL = outputURL.deletingLastPathComponent().appendingPathComponent("video_only.mp4")
    let audioURL = URL(fileURLWithPath: manifest.audioPath)

    try buildVideoOnly(manifest, outputURL: tempVideoURL)
    try exportWithAudio(videoURL: tempVideoURL, audioURL: audioURL, outputURL: outputURL)
    try? FileManager.default.removeItem(at: tempVideoURL)
} catch {
    FileHandle.standardError.write(Data("\(error)\n".utf8))
    exit(1)
}
