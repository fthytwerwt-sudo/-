import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

const COLORS = {
  matte: '#10141a',
  panel: '#f7f7f2',
  ink: '#151923',
  muted: '#657084',
  accent: '#34c6a4',
  warning: '#ffb84d',
  proof: '#d8efe8',
  bridge: '#1d2633',
  subtitle: '#f6f8fb',
};

const cardShadow = '0 28px 80px rgba(0, 0, 0, 0.32)';

export const GuidedProofToolchain: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const seconds = frame / fps;
  const bridgeProgress = spring({frame, fps, config: {damping: 18, stiffness: 80}});
  const highlightPulse = interpolate(
    Math.sin(seconds * Math.PI * 1.4),
    [-1, 1],
    [0.82, 1],
  );

  return (
    <AbsoluteFill
      style={{
        background: COLORS.matte,
        color: COLORS.ink,
        fontFamily:
          '-apple-system, BlinkMacSystemFont, "Inter", "Helvetica Neue", Arial, sans-serif',
      }}
    >
      <div
        style={{
          position: 'absolute',
          inset: 58,
          borderRadius: 28,
          border: '1px solid rgba(255,255,255,0.08)',
          background:
            'linear-gradient(135deg, rgba(52,198,164,0.14), rgba(255,184,77,0.10) 45%, rgba(255,255,255,0.04))',
        }}
      />

      <section
        style={{
          position: 'absolute',
          left: 110,
          top: 90,
          width: 410,
          height: 180,
          borderRadius: 22,
          background: COLORS.bridge,
          color: COLORS.subtitle,
          boxShadow: cardShadow,
          padding: '30px 34px',
          opacity: interpolate(bridgeProgress, [0, 1], [0.85, 1]),
          transform: `translateY(${interpolate(bridgeProgress, [0, 1], [18, 0])}px)`,
        }}
      >
        <div style={{fontSize: 24, color: COLORS.accent, fontWeight: 700}}>
          low_density_bridge_card
        </div>
        <div style={{fontSize: 42, lineHeight: 1.05, marginTop: 18, fontWeight: 760}}>
          先告诉观众看哪里
        </div>
      </section>

      <main
        style={{
          position: 'absolute',
          left: 565,
          top: 92,
          width: 1240,
          height: 720,
          borderRadius: 26,
          background: COLORS.panel,
          boxShadow: cardShadow,
          overflow: 'hidden',
        }}
      >
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            height: 74,
            padding: '0 34px',
            borderBottom: '1px solid #d8ded9',
            background: '#fbfbf7',
          }}
        >
          <div style={{fontSize: 24, fontWeight: 760}}>clean_evidence_container</div>
          <div style={{fontSize: 20, color: COLORS.muted}}>active evidence window</div>
        </div>

        <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 28, padding: 34}}>
          {['before / source', 'after / output'].map((title, index) => (
            <div
              key={title}
              style={{
                height: 500,
                borderRadius: 18,
                background: index === 0 ? '#eef3f7' : COLORS.proof,
                border: '1px solid #d5ddd8',
                padding: 26,
                position: 'relative',
              }}
            >
              <div
                style={{
                  display: 'inline-flex',
                  borderRadius: 999,
                  background: index === 0 ? '#dfe8ef' : '#c6e8dc',
                  padding: '8px 16px',
                  fontSize: 20,
                  fontWeight: 700,
                  color: '#24313a',
                }}
              >
                {title}
              </div>
              <div
                style={{
                  marginTop: 34,
                  display: 'grid',
                  gap: 18,
                }}
              >
                {[0, 1, 2, 3].map((row) => (
                  <div
                    key={row}
                    style={{
                      height: 34,
                      borderRadius: 10,
                      background: row === 1 && index === 1 ? '#9ddfc9' : '#cbd5dc',
                      opacity: row === 1 && index === 1 ? highlightPulse : 0.76,
                    }}
                  />
                ))}
              </div>
              {index === 1 ? (
                <div
                  style={{
                    position: 'absolute',
                    left: 22,
                    right: 22,
                    top: 138,
                    height: 54,
                    border: `5px solid ${COLORS.accent}`,
                    borderRadius: 14,
                    boxShadow: '0 0 0 8px rgba(52,198,164,0.16)',
                  }}
                />
              ) : null}
            </div>
          ))}
        </div>

        <div
          style={{
            position: 'absolute',
            right: 34,
            bottom: 28,
            borderRadius: 14,
            background: COLORS.warning,
            padding: '12px 18px',
            fontSize: 22,
            fontWeight: 760,
          }}
        >
          one_claim_one_highlight
        </div>
      </main>

      <footer
        style={{
          position: 'absolute',
          left: 565,
          right: 115,
          bottom: 96,
          height: 104,
          borderRadius: 24,
          background: 'rgba(0,0,0,0.54)',
          color: COLORS.subtitle,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: 34,
          fontWeight: 700,
          letterSpacing: 0,
        }}
      >
        subtitle_safe_zone：字幕只做注意力引导，不遮挡证据
      </footer>
    </AbsoluteFill>
  );
};
