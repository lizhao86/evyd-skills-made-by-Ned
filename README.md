# 技能 Skills 作坊

面向医疗健康产品团队（EVYD）的 AI 技能工具包，基于 Claude Code Skills 框架构建。覆盖从竞品调研、需求定义、设计落地到文档交付的完整产品流程。

## 项目简介

本项目整合了产品开发流程中最耗时的五个环节，让产品经理、设计师和工程师通过 AI 快速生成高质量的工作产出：

```
市场/竞品 → 竞品调研报告（飞书）
                  ↓
产品需求 → 用户故事 + AC → Figma 线框图脚本 → 低保真原型
                              ↓
                        User Manual（用户手册）
医疗 AI 概念 → 意图分类 → 范围边界规范
```

## 技能列表

### 1. 竞品调研 (Competitor Research)

**目录**：`evyd-competitor-research/`

医疗健康解决方案竞品分析，输出到飞书云盘。支持两种模式：

- **Mode 1 — 单个竞品深度调研**：并行召唤 5 个子 Agent，分别调研产品定位、合规安全、互操作集成、交付运营、市场足迹，合并输出结构化报告
- **Mode 2 — 竞品全景汇总**：读取飞书文件夹内已有调研文档，综合生成全景分析报告
- **追问模式**：调研完成后主动提 3 个深挖问题，用户追问后追加到原文档

**触发词**：`竞品调研`、`competitor research`、`竞品汇总`、`competitive landscape`

**输出**：飞书云文档，文件夹 `G1tGfI3wFldgE3d2JKscrj1InHc`

---

### 2. 用户故事编写器 (User Story Writer)

**目录**：`evyd-user-story-writer/`

将产品需求描述转换为结构化的用户故事文档，包含完整的验收标准。

**适用场景**：需求拆分、Sprint 规划、验收标准制定

**输入**：产品需求描述（平台、系统模块、功能目标）

**输出**：
- 标准格式的用户故事（标题 + 描述 + 验收标准）
- 使用 Given-When-Then 格式的验收标准，覆盖主流程、异常流程和边界场景
- 可选输出到飞书云文档

---

### 3. 低保真 Figma 脚本生成器 (LoFi Figma Maker)

**目录**：`evyd-lofi-figma-maker/`

将用户故事自动转换为可直接粘贴到 Figma Make 的线框图提示词。

**适用场景**：UI/UX 设计启动、快速原型制作

**输入**：用户故事文档（含验收标准）

**输出**：
- 针对每个 AC 场景生成对应屏幕的 Figma Make 提示词
- 使用标准化组件词汇表，确保 Figma AI 准确识别
- 可选输出到飞书云文档

---

### 4. 用户手册生成器 (User Manual)

**目录**：`evyd-user-manual/`

根据用户故事和验收标准，自动生成结构清晰、面向终端用户的操作手册。

**适用场景**：功能交付文档、帮助中心内容、产品培训材料

**输入**：用户故事 + 验收标准（AC），或功能描述

**输出**：
- 标准 Markdown 格式的 User Manual 章节
- 按任务分节，使用编号步骤和 UI 元素标注
- 包含常见问题 / Troubleshooting 部分
- 可选输出到飞书云文档

---

### 5. 医疗 AI 意图架构师 (AI Intention Brainstorm)

**目录**：`evyd-ai-intention-brainstorm/`

将医疗 AI 产品概念转换为结构化的意图分类和范围边界规范文档。

**适用场景**：AI 产品规划、合规性设计、跨团队对齐

**输入**：AI 功能概念和使用场景描述

**输出**：包含三层范围定义的规范文档：
- **IS（范围内）**：AI 可以处理的意图
- **HOOS（硬性范围外）**：绝对禁止的场景（如直接诊断）
- **SOOS（软性范围外）**：需转介医生的场景

---

## 完整工作流

```
1. [竞品调研] 了解市场格局
        ↓
2. 描述产品需求
        ↓
3. [用户故事编写器] 生成用户故事 + 验收标准
        ↓
4. [Figma 脚本生成器] 生成 Figma Make 提示词   →  [用户手册生成器] 生成 User Manual
        ↓
5. 设计师粘贴提示词，在 Figma Make 生成低保真线框图
        ↓
6. 进入视觉设计和开发阶段

[医疗 AI 意图架构师] — 独立使用，AI 产品规划阶段
```

## 项目结构

```
技能 skills 作坊/
├── README.md
├── evyd-ai-intention-brainstorm/   # 医疗 AI 意图架构师
│   ├── SKILL.md
│   └── Scope-Layer-Templates.md
├── evyd-competitor-research/       # 竞品调研
│   ├── SKILL.md
│   └── references/
├── evyd-lofi-figma-maker/          # 低保真 Figma 脚本生成器
│   ├── SKILL.md
│   └── Figma-Make-Prompt-Template.md
├── evyd-user-manual/               # 用户手册生成器
│   └── SKILL.md
└── evyd-user-story-writer/         # 用户故事编写器
    ├── SKILL.md
    └── EVYD-User-Story-Template.md
```

## 技术栈

- **框架**：[Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- **输出集成**：飞书云文档（Feishu Cloud Docs）

## 使用方式

在 Claude Code 中，直接通过对话触发对应技能。每个技能的 `SKILL.md` 描述了详细的触发词和工作流程。技能安装后，Claude Code 会自动识别触发条件并调用对应技能。
