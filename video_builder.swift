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
    let slides: [Slide]
}

struct Slide: Decodable {
    let sequence: Int
    let total: Int
    let role: String
    let eyebrow: String
    let headline: String
    let support: String
    let detail: String
    let chips: [String]
    let accent: String
    let background: String
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

func drawRoundedStroke(_ rect: NSRect, radius: CGFloat, stroke: NSColor, lineWidth: CGFloat = 2.0) {
    stroke.setStroke()
    let path = NSBezierPath(roundedRect: rect, xRadius: radius, yRadius: radius)
    path.lineWidth = lineWidth
    path.stroke()
}

func drawCircle(_ rect: NSRect, fill: NSColor) {
    fill.setFill()
    let path = NSBezierPath(ovalIn: rect)
    path.fill()
}

func textAttributes(
    size: CGFloat,
    weight: NSFont.Weight,
    color: NSColor,
    alignment: NSTextAlignment = .left
) -> [NSAttributedString.Key: Any] {
    let paragraph = NSMutableParagraphStyle()
    paragraph.alignment = alignment
    paragraph.lineBreakMode = .byWordWrapping
    return [
        .font: NSFont.systemFont(ofSize: size, weight: weight),
        .foregroundColor: color,
        .paragraphStyle: paragraph,
    ]
}

func drawPill(
    _ text: String,
    rect: NSRect,
    fill: NSColor,
    textColor: NSColor,
    size: CGFloat = 24,
    weight: NSFont.Weight = .semibold
) {
    drawRoundedRect(rect, radius: rect.height / 2, fill: fill)
    (text as NSString).draw(
        in: rect.insetBy(dx: 18, dy: 10),
        withAttributes: textAttributes(
            size: size,
            weight: weight,
            color: textColor,
            alignment: .center
        )
    )
}

func drawProgress(_ slide: Slide, accentColor: NSColor, width: Int, progress: CGFloat) {
    let totalCount = max(slide.total, 1)
    let capsuleGap: CGFloat = 18
    let capsuleWidth =
        (CGFloat(width) - 160 - CGFloat(totalCount - 1) * capsuleGap) / CGFloat(totalCount)
    let baseY: CGFloat = 124

    for index in 0..<totalCount {
        let rect = NSRect(
            x: 80 + CGFloat(index) * (capsuleWidth + capsuleGap),
            y: baseY,
            width: capsuleWidth,
            height: 18
        )
        drawRoundedRect(rect, radius: 9, fill: NSColor.black.withAlphaComponent(0.08))
        if index < slide.sequence - 1 {
            drawRoundedRect(rect, radius: 9, fill: accentColor.withAlphaComponent(0.30))
        } else if index == slide.sequence - 1 {
            let fillWidth = max(24, rect.width * max(0.16, min(progress, 1.0)))
            drawRoundedRect(
                NSRect(x: rect.minX, y: rect.minY, width: fillWidth, height: rect.height),
                radius: 9,
                fill: accentColor
            )
        }
    }

    (slide.eyebrow as NSString).draw(
        in: NSRect(x: 80, y: 82, width: 300, height: 28),
        withAttributes: textAttributes(size: 24, weight: .medium, color: NSColor.black.withAlphaComponent(0.54))
    )
}

func drawHookLayout(_ slide: Slide, in cardRect: NSRect, accentColor: NSColor) {
    drawPill(
        "问题不是没想法",
        rect: NSRect(x: cardRect.minX + 44, y: cardRect.maxY - 96, width: 220, height: 48),
        fill: accentColor.withAlphaComponent(0.10),
        textColor: accentColor,
        size: 22
    )

    let columnWidth = (cardRect.width - 128) / 2
    let leftRect = NSRect(x: cardRect.minX + 44, y: cardRect.maxY - 360, width: columnWidth, height: 210)
    let rightRect = NSRect(x: leftRect.maxX + 40, y: leftRect.minY, width: columnWidth, height: 210)

    drawRoundedRect(leftRect, radius: 34, fill: accentColor.withAlphaComponent(0.10))
    drawRoundedStroke(leftRect, radius: 34, stroke: accentColor.withAlphaComponent(0.20))
    drawRoundedRect(rightRect, radius: 34, fill: NSColor.black.withAlphaComponent(0.88))

    if slide.chips.count > 0 {
        drawPill(
            "表面上",
            rect: NSRect(x: leftRect.minX + 22, y: leftRect.maxY - 62, width: 110, height: 38),
            fill: NSColor.white.withAlphaComponent(0.74),
            textColor: NSColor.black.withAlphaComponent(0.72),
            size: 18
        )
        (slide.chips[0] as NSString).draw(
            in: NSRect(x: leftRect.minX + 24, y: leftRect.minY + 48, width: leftRect.width - 48, height: 96),
            withAttributes: textAttributes(size: 44, weight: .bold, color: NSColor.black.withAlphaComponent(0.82))
        )
    }

    if slide.chips.count > 1 {
        drawPill(
            "真正卡点",
            rect: NSRect(x: rightRect.minX + 22, y: rightRect.maxY - 62, width: 122, height: 38),
            fill: NSColor.white.withAlphaComponent(0.16),
            textColor: .white,
            size: 18
        )
        (slide.chips[1] as NSString).draw(
            in: NSRect(x: rightRect.minX + 24, y: rightRect.minY + 48, width: rightRect.width - 48, height: 96),
            withAttributes: textAttributes(size: 44, weight: .bold, color: .white)
        )
    }

    ("→" as NSString).draw(
        in: NSRect(x: leftRect.maxX + 4, y: leftRect.minY + 72, width: 32, height: 64),
        withAttributes: textAttributes(size: 48, weight: .bold, color: accentColor, alignment: .center)
    )

    let detailRect = NSRect(x: cardRect.minX + 44, y: cardRect.minY + 76, width: cardRect.width - 88, height: 96)
    drawRoundedRect(detailRect, radius: 26, fill: NSColor.white.withAlphaComponent(0.92))
    drawRoundedStroke(detailRect, radius: 26, stroke: accentColor.withAlphaComponent(0.18))
    (slide.detail as NSString).draw(
        in: detailRect.insetBy(dx: 28, dy: 22),
        withAttributes: textAttributes(size: 30, weight: .medium, color: NSColor.black.withAlphaComponent(0.74))
    )
}

func drawProcessLayout(_ slide: Slide, in cardRect: NSRect, accentColor: NSColor) {
    drawPill(
        "把散乱动作压成一条流程",
        rect: NSRect(x: cardRect.minX + 44, y: cardRect.maxY - 96, width: 310, height: 48),
        fill: accentColor.withAlphaComponent(0.10),
        textColor: accentColor,
        size: 22
    )

    let stepHeight: CGFloat = 132
    let gap: CGFloat = 24
    let baseY = cardRect.maxY - 248

    for (index, chip) in slide.chips.enumerated() {
        let rect = NSRect(
            x: cardRect.minX + 44,
            y: baseY - CGFloat(index) * (stepHeight + gap),
            width: cardRect.width - 88,
            height: stepHeight
        )
        let fillColor =
            index == 1
            ? accentColor.withAlphaComponent(0.12)
            : NSColor.white.withAlphaComponent(0.94)
        drawRoundedRect(rect, radius: 30, fill: fillColor)
        drawRoundedStroke(rect, radius: 30, stroke: accentColor.withAlphaComponent(0.18))

        let numberRect = NSRect(x: rect.minX + 24, y: rect.minY + 32, width: 68, height: 68)
        drawRoundedRect(numberRect, radius: 20, fill: accentColor)
        (String(format: "%02d", index + 1) as NSString).draw(
            in: numberRect.insetBy(dx: 8, dy: 14),
            withAttributes: textAttributes(size: 24, weight: .bold, color: .white, alignment: .center)
        )

        (chip as NSString).draw(
            in: NSRect(x: rect.minX + 120, y: rect.minY + 42, width: rect.width - 150, height: 48),
            withAttributes: textAttributes(size: 40, weight: .bold, color: NSColor.black.withAlphaComponent(0.82))
        )

        if index < slide.chips.count - 1 {
            let line = NSBezierPath()
            line.move(to: NSPoint(x: rect.midX, y: rect.minY - 8))
            line.line(to: NSPoint(x: rect.midX, y: rect.minY - 16))
            accentColor.withAlphaComponent(0.30).setStroke()
            line.lineWidth = 4
            line.stroke()
        }
    }

    let detailRect = NSRect(x: cardRect.minX + 44, y: cardRect.minY + 64, width: cardRect.width - 88, height: 90)
    drawRoundedRect(detailRect, radius: 24, fill: NSColor.black.withAlphaComponent(0.84))
    (slide.detail as NSString).draw(
        in: detailRect.insetBy(dx: 28, dy: 20),
        withAttributes: textAttributes(size: 28, weight: .medium, color: .white)
    )
}

func drawOutcomeLayout(_ slide: Slide, in cardRect: NSRect, accentColor: NSColor) {
    let bannerRect = NSRect(x: cardRect.minX + 44, y: cardRect.maxY - 224, width: cardRect.width - 88, height: 168)
    drawRoundedRect(bannerRect, radius: 36, fill: accentColor)
    (slide.support as NSString).draw(
        in: NSRect(x: bannerRect.minX + 32, y: bannerRect.minY + 58, width: bannerRect.width - 64, height: 52),
        withAttributes: textAttributes(size: 40, weight: .bold, color: .white)
    )

    let boxWidth = (cardRect.width - 116) / 2
    let leftRect = NSRect(x: cardRect.minX + 44, y: cardRect.minY + 248, width: boxWidth, height: 190)
    let rightRect = NSRect(x: leftRect.maxX + 28, y: leftRect.minY, width: boxWidth, height: 190)

    drawRoundedRect(leftRect, radius: 32, fill: NSColor.white.withAlphaComponent(0.96))
    drawRoundedRect(rightRect, radius: 32, fill: accentColor.withAlphaComponent(0.12))
    drawRoundedStroke(leftRect, radius: 32, stroke: accentColor.withAlphaComponent(0.18))
    drawRoundedStroke(rightRect, radius: 32, stroke: accentColor.withAlphaComponent(0.18))

    if slide.chips.count > 0 {
        drawPill(
            "先做什么",
            rect: NSRect(x: leftRect.minX + 22, y: leftRect.maxY - 58, width: 116, height: 36),
            fill: accentColor.withAlphaComponent(0.10),
            textColor: accentColor,
            size: 18
        )
        (slide.chips[0] as NSString).draw(
            in: NSRect(x: leftRect.minX + 22, y: leftRect.minY + 46, width: leftRect.width - 44, height: 84),
            withAttributes: textAttributes(size: 38, weight: .bold, color: NSColor.black.withAlphaComponent(0.82))
        )
    }

    if slide.chips.count > 1 {
        drawPill(
            "再做什么",
            rect: NSRect(x: rightRect.minX + 22, y: rightRect.maxY - 58, width: 116, height: 36),
            fill: NSColor.white.withAlphaComponent(0.70),
            textColor: accentColor,
            size: 18
        )
        (slide.chips[1] as NSString).draw(
            in: NSRect(x: rightRect.minX + 22, y: rightRect.minY + 46, width: rightRect.width - 44, height: 84),
            withAttributes: textAttributes(size: 38, weight: .bold, color: NSColor.black.withAlphaComponent(0.82))
        )
    }

    let detailRect = NSRect(x: cardRect.minX + 44, y: cardRect.minY + 74, width: cardRect.width - 88, height: 96)
    drawRoundedRect(detailRect, radius: 24, fill: NSColor.white.withAlphaComponent(0.92))
    drawRoundedStroke(detailRect, radius: 24, stroke: accentColor.withAlphaComponent(0.18))
    (slide.detail as NSString).draw(
        in: detailRect.insetBy(dx: 28, dy: 24),
        withAttributes: textAttributes(size: 30, weight: .medium, color: NSColor.black.withAlphaComponent(0.74))
    )
}

func renderSlide(_ slide: Slide, width: Int, height: Int, progress: CGFloat) -> CGImage {
    let size = NSSize(width: width, height: height)
    let image = NSImage(size: size)
    image.lockFocus()

    let backgroundRect = NSRect(x: 0, y: 0, width: width, height: height)
    let accentColor = color(hex: slide.accent)
    let backgroundColor = color(hex: slide.background)
    backgroundColor.setFill()
    backgroundRect.fill()
    if let gradient = NSGradient(
        starting: accentColor.withAlphaComponent(0.14),
        ending: backgroundColor
    ) {
        gradient.draw(in: backgroundRect, angle: 90)
    }

    drawCircle(
        NSRect(
            x: CGFloat(width) - 340 + progress * 18,
            y: CGFloat(height) - 420 + progress * 12,
            width: 360,
            height: 360
        ),
        fill: accentColor.withAlphaComponent(0.12)
    )
    drawCircle(
        NSRect(
            x: -100 - progress * 14,
            y: 220 - progress * 10,
            width: 260,
            height: 260
        ),
        fill: accentColor.withAlphaComponent(0.08)
    )

    drawPill(
        slide.eyebrow,
        rect: NSRect(x: 72, y: CGFloat(height) - 156, width: 180, height: 48),
        fill: accentColor.withAlphaComponent(0.12),
        textColor: accentColor,
        size: 22
    )
    drawPill(
        "\(slide.sequence)/\(slide.total)",
        rect: NSRect(x: CGFloat(width) - 186, y: CGFloat(height) - 156, width: 114, height: 48),
        fill: NSColor.black.withAlphaComponent(0.08),
        textColor: NSColor.black.withAlphaComponent(0.62),
        size: 22
    )

    (slide.headline as NSString).draw(
        in: NSRect(x: 72, y: CGFloat(height) - 484, width: CGFloat(width) - 144, height: 210),
        withAttributes: textAttributes(size: 72, weight: .black, color: NSColor.black.withAlphaComponent(0.86))
    )
    (slide.support as NSString).draw(
        in: NSRect(x: 72, y: CGFloat(height) - 570, width: CGFloat(width) - 144, height: 60),
        withAttributes: textAttributes(size: 32, weight: .medium, color: NSColor.black.withAlphaComponent(0.56))
    )

    let cardRect = NSRect(x: 72, y: 286, width: CGFloat(width) - 144, height: 840)
    drawRoundedRect(cardRect, radius: 48, fill: NSColor.white.withAlphaComponent(0.94))
    drawRoundedStroke(cardRect, radius: 48, stroke: accentColor.withAlphaComponent(0.18))
    let accentBarWidth = max(140, (cardRect.width - 120) * (0.24 + 0.16 * progress))
    drawRoundedRect(
        NSRect(x: cardRect.minX + 44, y: cardRect.maxY - 30, width: accentBarWidth, height: 12),
        radius: 6,
        fill: accentColor
    )

    switch slide.role {
    case "hook":
        drawHookLayout(slide, in: cardRect, accentColor: accentColor)
    case "process":
        drawProcessLayout(slide, in: cardRect, accentColor: accentColor)
    default:
        drawOutcomeLayout(slide, in: cardRect, accentColor: accentColor)
    }

    drawProgress(slide, accentColor: accentColor, width: width, progress: progress)

    image.unlockFocus()
    return image.cgImage(forProposedRect: nil, context: nil, hints: nil)!
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
        for frame in 0 ..< frameCount {
            waitUntilReady(input)
            let timestamp = CMTime(value: frameIndex, timescale: CMTimeScale(fps))
            let progress =
                frameCount == 1
                ? CGFloat(1.0)
                : CGFloat(frame + 1) / CGFloat(frameCount)
            let image = renderSlide(
                slide,
                width: manifest.width,
                height: manifest.height,
                progress: progress
            )
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
