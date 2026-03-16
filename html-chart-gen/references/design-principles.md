# 设计原则

这不是模板——这是你作为视觉设计师的工具箱。根据数据特征和表达意图，自由组合这些原则和技巧。

## 基础约束

这些是硬性要求，保证截图和 AI 阅读都不受影响：

```css
/* 每个文件必须包含 */
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "PingFang SC", sans-serif;
  background: /* 从当前主题取值：浅色主题 #f5f5f7，Midnight Glass #0f1729 */;
  display: flex;
  justify-content: center;
  padding: 40px;
}
```

- 卡片宽度 680-960px，圆角阴影
- **浅色主题**：卡片白色背景 `#fff`，浅灰边框/阴影
- **暗色主题（Midnight Glass）**：卡片渐变背景 + `rgba(255,255,255,0.06)` 边框 + 深色阴影
- 纯 HTML + CSS，零 JavaScript
- 不引用任何外部资源

## 视觉层次原则

信息层次是图表质量的核心。通过以下手段建立层次：

1. **字号梯度**：KPI 大数字(24-32px) → 区块标题(15-18px) → 正文(13-14px) → 辅助(11-12px)
2. **颜色深度**：标题深色 → 正文中性 → 次要浅灰 → 辅助极淡（具体值从当前主题取）
3. **间距呼吸**：区块间 24-40px → 元素间 12-16px → 紧凑组内 4-8px
4. **视觉权重**：用填充色块、加粗、对比色把最重要的信息从背景中"跳"出来

## 色彩使用

所有颜色从当前主题取值（见 `themes.md`）。在主题色系基础上，可按语义调整：

| 语义 | 用途 |
|------|------|
| 积极/成功/增长 | 主题的成功色 |
| 消极/下降/风险 | 主题的危险色 |
| 警告/注意/中等 | 主题的警告色 |
| 信息/主色调 | 主题的主色/强调色 |

**配色策略**：
- 单主色+灰度：适合简洁风格
- 多色区分：多数据系列时用色相区分，保持饱和度一致
- 渐变：用在 Header 等强调区域，方向 135deg
- 一张图表里控制在 3-5 种主色以内

## 排版参考

| 元素 | 字号 | 字重 |
|------|------|------|
| KPI 大数字 | 24-32px | 700-800 |
| 卡片/页面标题 | 20-26px | 600-700 |
| 区块标题 | 15-18px | 600 |
| 正文内容 | 13-14px | 400-500 |
| 标签/badge | 11-13px | 500-600 |
| 辅助说明 | 11-12px | 400 |

## CSS-Only 可视化技巧

以下是你的工具箱——根据数据特征选择合适的手法，自由组合。

### 水平条形图
```css
.bar-track { height: 20-32px; background: #f3f4f6; border-radius: 4-8px; overflow: hidden; }
.bar-fill { height: 100%; border-radius: inherit; /* width 用 inline style */ }
```
分离式（每个指标独立一行）对比更清晰；堆叠式更紧凑但对比性差。

### 饼图 / 环形图（conic-gradient）
```css
.pie { border-radius: 50%; background: conic-gradient(#色1 0% 35%, #色2 35% 55%, ...); }
.ring { /* 同上 */ -webkit-mask: radial-gradient(transparent 55%, #fff 56%); mask: radial-gradient(transparent 55%, #fff 56%); }
```
小型进度环（60-80px）适合展示转化率、完成度等单个百分比。**conic-gradient 百分比必须累加到 100%。**

### 进度条
```css
.progress { height: 6-8px; background: #f3f4f6; border-radius: 3px; }
.progress-fill { height: 100%; border-radius: inherit; }
```

### 漏斗图
通过递减宽度的条形实现，每层间用流失率文字连接。宽度按实际数据比例计算。

### 四象限矩阵
```css
.matrix { display: grid; grid-template-columns: auto 1fr 1fr; grid-template-rows: auto 1fr 1fr; }
```

### 连接线（时间线/流程图）
```css
.connector { width: 2px; background: #dbeafe; min-height: 16px; }
```

### 架构图分层
每层用不同颜色的底色区分，层间用箭头符号（▼）连接。常见分层：客户端→接入→服务→数据→基础设施。

### 状态机
圆角节点 + 箭头标签，不同颜色表示不同状态（草稿=灰, 待审=黄, 通过=绿, 驳回=红）。

### RACI 矩阵
表格中用彩色 badge：R(红) A(琥珀) C(蓝) I(紫)。每任务必须且仅有一个 A。

## 组件参考

### KPI 概览卡
多个核心指标并排展示，每个带大数字+标签+变化趋势。可以用左边框颜色区分类别。

### 数据表格
表头浅灰背景，行悬停高亮，数字右对齐+等宽。在表格旁边或下方配合可视化更有力。

### Badge / 标签
```css
.badge { display: inline-flex; padding: 2-4px 8-12px; border-radius: 6px; font-size: 11-12px; font-weight: 500-600; }
```
用颜色编码表达语义（高/中/低、好/中/差）。

## Footer 洞察

图表底部应包含一句面向决策者的关键洞察或行动建议：
- 以 emoji 开头（💡📈⚡🎯⚠️等）增加辨识度
- 一句话点出数据背后的"so what"
- 面向决策，不是技术细节

## 设计灵感

好的数据可视化不是罗列数据，而是讲故事。思考：

- **对比**：把关键对比放在最显眼的位置（最大 vs 最小、目标 vs 实际）
- **聚焦**：不是所有数据同等重要，用视觉权重引导读者看到重点
- **组合**：一张图表可以融合多种可视化——表格提供精确数据，条形图提供直观对比，环形图展示关键指标
- **留白**：不要填满每一寸空间，让设计呼吸

## 暗色主题（Midnight Glass）适配要点

使用暗色主题时，以下组件需要对应调整——核心原则是：**用 rgba 半透明替代硬编码的浅色值**。

| 组件 | 浅色主题 | 暗色主题 |
|------|---------|---------|
| body 背景 | `#f5f5f7` | `#0f1729` |
| 卡片背景 | `#fff` | `linear-gradient(145deg, #1a2540, #162035)` |
| 卡片边框 | `1px solid #e5e7eb` | `1px solid rgba(255,255,255,0.06)` |
| 卡片阴影 | `0 2px 12px rgba(0,0,0,0.06)` | `0 4px 24px rgba(0,0,0,0.3)` |
| 条形图底色 | `#f3f4f6` | `rgba(255,255,255,0.06)` |
| 表头背景 | `#f8f9fa` | `rgba(255,255,255,0.04)` |
| 表格行悬停 | `#faf5ff` | `rgba(255,255,255,0.03)` |
| 表格边线 | `#e8eaed` | `rgba(255,255,255,0.06)` |
| Badge 底色 | `#eff6ff` 等实色 | `rgba(色值, 0.15)` 半透明 |
| 进度条底色 | `#f3f4f6` | `rgba(255,255,255,0.06)` |
| 连接线/分隔 | `#dbeafe` | `rgba(255,255,255,0.08)` |
| 文字颜色 | `#111827 → #9ca3af` | `#f1f5f9 → #64748b`（反转层级） |

**暗色专属效果**（浅色主题不用）：
- 数据色块加发光：`box-shadow: 0 0 12px rgba(主题色, 0.3)`
- 标题渐变文字：`background: linear-gradient(...); -webkit-background-clip: text; -webkit-text-fill-color: transparent`
- Header 可用整段渐变文字替代渐变背景条

## 禁止事项

- 不使用 JavaScript（任何 `<script>` 标签）
- 不引用外部资源（CDN、Google Fonts、图片 URL）
- 不使用动画（截图时无意义）
- 不做响应式——固定宽度优化截图效果
