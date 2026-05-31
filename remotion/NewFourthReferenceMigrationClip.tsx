import React from 'react';
import {Video} from '@remotion/media';
import {
  AbsoluteFill,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

const SOURCE = 'reference_migration_20260601_010425/source_segment.mp4';

const COLORS = {
  matte: '#10151c',
  panel: '#f7f5ee',
  ink: '#161b22',
  muted: '#687386',
  teal: '#21b99a',
  amber: '#f3b23f',
  red: '#df5c4e',
  blue: '#477bd3',
  subtitle: '#f8fafc',
  bridge: '#202a36',
};

const lineGroups = [
  {
    start: 0,
    end: 5.5,
    label: '先定主变化',
    text: '这一步和手动翻不一样：不是边看边想，是边看边记录。',
    note: '商品页不是结论，只是原始证据。',
    rect: {left: 164, top: 226, width: 900, height: 362},
  },
  {
    start: 5.5,
    end: 11.5,
    label: '商品卡进表',
    text: '它会把这些商品，先整理成一张候选表。',
    note: '从散乱卡片，进入结构化记录。',
    rect: {left: 96, top: 115, width: 1084, height: 475},
  },
  {
    start: 11.5,
    end: 20.5,
    label: '一行一条记录',
    text: '原来是一张张商品卡，到了表格里，就变成一行一行可以判断的记录。',
    note: '只看当前证据窗口，不让整页信息淹没观众。',
    rect: {left: 84, top: 82, width: 1110, height: 356},
  },
  {
    start: 20.5,
    end: 31.5,
    label: '字段拆出来',
    text: '商品名、客单价、佣金、销量、店铺分、商品分、退货风险，都被拆开。',
    note: '一句只突出一个主判断：字段被拆开。',
    rect: {left: 122, top: 120, width: 880, height: 312},
  },
  {
    start: 31.5,
    end: 36.5,
    label: '下一步能判断',
    text: '为什么留下、为什么不能直接上、下一步还要核什么，也写清楚。',
    note: '桥接到可复查动作，而不是替人拍板。',
    rect: {left: 105, top: 140, width: 1000, height: 380},
  },
  {
    start: 36.5,
    end: 41.1,
    label: '不靠感觉',
    text: '这些东西一进表，选品就从靠感觉，变成逐项核对。',
    note: '结论回到“判断过程更清楚”。',
    rect: {left: 130, top: 116, width: 980, height: 350},
  },
];

const getActiveGroup = (seconds: number) =>
  lineGroups.find((group) => seconds >= group.start && seconds < group.end) ??
  lineGroups[lineGroups.length - 1];

const clamp = (value: number, min = 0, max = 1) =>
  Math.min(max, Math.max(min, value));

export const NewFourthReferenceMigrationClip: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const seconds = frame / fps;
  const active = getActiveGroup(seconds);
  const groupProgress = clamp((seconds - active.start) / Math.max(active.end - active.start, 0.1));
  const rectOpacity = interpolate(groupProgress, [0, 0.12, 0.88, 1], [0, 1, 1, 0.86]);
  const bridgeOpacity = interpolate(groupProgress, [0, 0.18, 1], [0.78, 1, 0.96]);
  const pulse = interpolate(Math.sin(seconds * Math.PI * 1.8), [-1, 1], [0.88, 1]);

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
          left: 48,
          top: 52,
          width: 326,
          height: 808,
          background: COLORS.bridge,
          border: '1px solid rgba(255,255,255,0.14)',
          boxShadow: '0 28px 70px rgba(0,0,0,0.34)',
          padding: '30px 28px',
        }}
      >
        <div
          style={{
            display: 'inline-flex',
            background: 'rgba(33,185,154,0.16)',
            color: COLORS.teal,
            border: '1px solid rgba(33,185,154,0.32)',
            fontSize: 22,
            fontWeight: 760,
            padding: '8px 12px',
          }}
        >
          low_density_bridge
        </div>
        <h1
          style={{
            color: COLORS.subtitle,
            fontSize: 48,
            lineHeight: 1.08,
            margin: '34px 0 22px',
            fontWeight: 800,
            letterSpacing: 0,
          }}
        >
          先告诉观众看哪里
        </h1>
        <div
          style={{
            height: 1,
            background: 'rgba(255,255,255,0.18)',
            margin: '28px 0',
          }}
        />
        <div style={{opacity: bridgeOpacity}}>
          <div style={{color: COLORS.amber, fontSize: 28, fontWeight: 800}}>
            {active.label}
          </div>
          <p
            style={{
              color: '#dbe3ee',
              fontSize: 25,
              lineHeight: 1.34,
              marginTop: 20,
              fontWeight: 620,
            }}
          >
            {active.note}
          </p>
        </div>
        <div
          style={{
            position: 'absolute',
            left: 28,
            right: 28,
            bottom: 30,
            color: '#aeb8c7',
            fontSize: 20,
            lineHeight: 1.4,
          }}
        >
          reference 迁移的是剪辑语言：证据窗口、字幕桥、主高亮，不复制人物或平台包装。
        </div>
      </div>

      <div
        style={{
          position: 'absolute',
          left: 410,
          top: 52,
          width: 1458,
          height: 820,
          background: COLORS.panel,
          boxShadow: '0 34px 88px rgba(0,0,0,0.38)',
          overflow: 'hidden',
          border: '1px solid rgba(255,255,255,0.18)',
        }}
      >
        <div
          style={{
            height: 72,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '0 28px',
            background: '#fbfaf5',
            borderBottom: '1px solid #ddd8cb',
          }}
        >
          <div style={{display: 'flex', alignItems: 'center', gap: 14}}>
            <div style={{fontSize: 27, fontWeight: 800}}>clean evidence container</div>
            <span
              style={{
                background: COLORS.amber,
                color: COLORS.ink,
                padding: '7px 12px',
                fontSize: 19,
                fontWeight: 800,
              }}
            >
              one_claim_one_highlight
            </span>
          </div>
          <div style={{display: 'flex', gap: 12, fontSize: 20, fontWeight: 760}}>
            <span style={{color: COLORS.red}}>source</span>
            <span style={{color: COLORS.muted}}>to</span>
            <span style={{color: COLORS.blue}}>structured proof</span>
          </div>
        </div>

        <div style={{position: 'relative', width: '100%', height: 748, background: '#111'}}>
          <Video
            src={staticFile(SOURCE)}
            objectFit="cover"
            style={{
              width: '100%',
              height: '100%',
            }}
          />

          <div
            style={{
              position: 'absolute',
              left: active.rect.left,
              top: active.rect.top,
              width: active.rect.width,
              height: active.rect.height,
              border: `6px solid ${COLORS.teal}`,
              boxShadow: `0 0 0 9999px rgba(16,21,28,0.18), 0 0 0 ${12 * pulse}px rgba(33,185,154,0.13)`,
              opacity: rectOpacity,
              pointerEvents: 'none',
            }}
          />

        </div>
      </div>

      <div
        style={{
          position: 'absolute',
          left: 410,
          right: 52,
          bottom: 54,
          minHeight: 122,
          background: 'rgba(0,0,0,0.72)',
          color: COLORS.subtitle,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '20px 48px',
          textAlign: 'center',
          fontSize: active.text.length > 34 ? 32 : 38,
          lineHeight: 1.28,
          fontWeight: 760,
          letterSpacing: 0,
        }}
      >
        {active.text}
      </div>
    </AbsoluteFill>
  );
};
