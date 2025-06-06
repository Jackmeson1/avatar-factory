# 化身BOSS - AI重写工程化小说项目

## 项目概述

本项目是一个基于SaaS服务的AI辅助小说创作工程，专注于内容组织、元数据标注与版本可追溯性。通过结构化的协作方式，结合多种AI服务（OpenAI、Notion AI、NovelFlow等）进行高效的小说创作与重写。

## 目录结构

```
化身BOSS/
├── README.md                # 项目说明与导航（本文件）
├── OUTLINE.md               # 最新剧情/结构提纲（高频更新）
├── styleguide.md            # 语体规范（文风、角色语气等）
├── drafts/                  # 草稿区：AI产出 + 手动试写
│   ├── red-dragon_alt.md    # 章节名或角色名
│   └── vol2_rewrite_notes.md
├── chapters/                # 正式章节（已定稿）
│   ├── vol0_prologue.md
│   ├── vol1_maze.md
│   └── ...
├── characters/              # 人物小传（每个角色一个 .md）
│   ├── jiminghuan.md
│   └── black_cocoon.md
├── settings/                # 世界设定、能力系统等
│   ├── world_basics.md
│   ├── power_system.md
│   └── timeline.md
├── assets/                  # 地图、结构图、AI图像等媒体资源
├── prompts/                 # AI prompt 示例与注解（仅模板层）
│   ├── rewrite_hero.tpl.md
│   └── npc_monologue.tpl.md
└── CHANGELOG.md             # 修订记录（章节变动、重构说明）
```

## 核心特性

### ✅ 保留的核心功能
- **章节分卷管理**：利于故事结构宏观掌控
- **人物设定集中管理**：便于 prompt injection & consistency check
- **设定统一文档**：用于未来 prompt context 引导
- **草稿仓库**：所有 AI 产出/试验改写皆落地入档

### 🚫 简化删除的功能
- 复杂的CI/CD配置
- 构建产物目录（交由平台处理）
- 过度工程化的配置文件

### ✅ 新增的协作功能
- **CHANGELOG.md**：记录每次章节/设定大改，提供对比依据
- **Prompt模板存档**：所有 AI 调用的历史版本 prompt 可保留注释版本
- **AI产出标注**：章节头部注明AI生成信息

## 使用指南

### 快速开始
1. 查看 `OUTLINE.md` 了解当前故事进度
2. 参考 `styleguide.md` 确认写作规范
3. 阅读 `settings/power_system.md` 与 `settings/timeline.md` 获取核心设定
4. 在 `drafts/` 中进行实验性写作
5. 完成后移至 `chapters/` 并更新 `CHANGELOG.md`

### AI 协作流程
1. 使用 `prompts/` 中的模板进行AI调用
2. 将AI产出保存至 `drafts/` 并标注来源
3. 结合 `characters/` 和 `settings/` 进行一致性检查
4. 整理定稿后归档至 `chapters/`

## 版本控制

本项目采用文件级版本控制，每次重大修改请：
1. 更新 `CHANGELOG.md`
2. 在草稿中保留修改前版本
3. 标注修改原因和AI服务来源

## 贡献指南

- 所有创作内容遵循 `styleguide.md` 规范
- AI生成内容需标注模型和prompt版本
- 重大设定变更需在相关角色/世界观文档中同步更新

---

**开始你的AI辅助创作之旅！** 🚀 