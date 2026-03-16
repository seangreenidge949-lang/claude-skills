# Claude Code Skills

A collection of reusable skills for [Claude Code](https://claude.com/claude-code).

## Available Skills

### resume-writing

**Resume Writing & Optimization** — 简历撰写与优化

Two-phase workflow for crafting high-impact resumes:

1. **Master Resume** — Build a comprehensive material library through structured interviews
2. **Tailored Versions** — Customize for specific job descriptions with ATS optimization

Key features:
- Google XYZ formula for bullet points (Accomplished X, measured by Y, by doing Z)
- Inverted pyramid structure (most recent = most detailed)
- Packaging intensity gradient (L1-L5) to match claims with actual contributions
- Dual-dimension information audit (completeness × source credibility)
- Context-adaptive writing (external job search / internal transfer / promotion review)
- Fact correction pipeline with full-chain sync across all versions

### html-chart-gen

**HTML Chart Generator** — HTML/CSS 可视化图表生成器

Generate high-quality HTML/CSS charts with auto-screenshot to PNG. Designed for product docs — screenshots for Feishu/Lark, HTML links for AI consumption.

Supported chart types (13+):
- **comparison-table** — 方案对比、技术选型
- **funnel** — 转化漏斗、流失分析
- **timeline** — 路线图、里程碑
- **dashboard** — KPI 概览、月报
- **architecture** — 系统架构、技术栈
- **flowchart** — 业务流程、审批流
- **pie-donut** — 占比分布、用户画像
- **priority-matrix** — 需求排序、四象限
- **user-journey** — 用户体验地图
- **pros-cons** — 方案利弊评估
- **state-machine** — 生命周期、状态流转
- **raci** — 角色分工、职责矩阵
- **feature-list** — Sprint 进度、功能清单

Key features:
- 5 built-in themes: Ocean Blue, Warm Sunset, Forest Green, Slate Minimal, Midnight Glass
- User-driven selection — chart type and theme chosen via interactive prompts before generation
- Pure HTML + CSS, zero JavaScript, no external dependencies
- Auto-screenshot to PNG via bundled script or Playwright fallback
- Smart data analysis — extracts insights from structured data input

## Installation

```bash
# Install resume-writing
npx skills add seangreenidge949-lang/claude-skills@resume-writing

# Install html-chart-gen
npx skills add seangreenidge949-lang/claude-skills@html-chart-gen
```

## License

MIT
