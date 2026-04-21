# EasySDD

> 厌倦了 OpenSpec 太简单、Oh-My-OpenAgent 太复杂、SuperPowers 缺约束，我从 0 写了一套简单轻巧、但**自洽闭环**的 AI 工作流。

**从开发到解决问题再到沉淀知识，是一个闭环；这一次的产出会变成下一次的输入，越用越顺。**

---

## 缘由

我一直在自己开发一套 Harness Agent（[源码](https://github.com/liuzhengdongfortest/MA)）。一开始就是 VibeCoding，我写设计、AI 写代码改 bug，挺顺利的。直到有一天 Codex 反复解决不了一个并不复杂的问题，反复在同一个地方失败，我意识到项目得有一套工作流来约束，才能继续推进。

调研了一圈：OpenSpec 太简单，没有复利工程，生成的 spec 抽象到人根本没法读；SuperPowers 没有流程约束，不知道该用哪个；Oh-My-OpenAgent 又太重。没一个用着顺手的，所以自己写了 EasySDD。

---

## 它解决哪几类问题

AI 辅助开发里有几类场景反复出现——加新功能、修 bug、沉淀经验、做技术选型、读新模块的代码、接入新仓库。每种场景如果每次从零处理，都会出各自的典型问题：

- AI 给新功能起的术语跟老代码冲突，改到一半才发现
- bug 改完没人记得当时怎么诊断的，下次同类问题又从头查
- 上次遇到过的问题下次又遇到一遍
- AI 一次输出几百行代码才让人 review，等发现方向不对已经很难中止

EasySDD 把这几类场景各配一套子技能，产物放进统一的目录结构、带统一的 YAML frontmatter，互相之间可以检索引用。

---

## 技能分成三部分

### 做事：从想法到上线，从报告到修好

- **`easysdd-feature`** — 新功能，`brainstorm → design → implement → acceptance`
- **`easysdd-issue`** — 修 bug，`report → analyze → fix`

两类都不直接让 AI 写代码，而是先产出 spec（功能方案 / 问题分析），用户 review 后再动手，代码和 doc 一起交付。针对的是 AI 默认会出的三类问题：术语冲突、范围失控、改完不留存档。

阶段之间有人工 checkpoint，上一阶段的退出条件没满足就不开始下一阶段。两种例外：issue 根因一眼确定时跳过 analyze 直接 fix；feature 范围很小时走 `easysdd-feature-fastforward`，写完 spec 直接进实现。

### 沉淀：这次的产出变成下次的输入

这是 EasySDD 最核心的一部分。四个子技能共用 `easysdd/compound/` 目录，按记录内容的性质分：

- **`easysdd-learning`** — 回顾"做 X 时踩了 Y 这个坑"
- **`easysdd-tricks`** — 处方"以后做 X 就这样做"
- **`easysdd-decisions`** — 规定"全项目今后都按 X 来"
- **`easysdd-explore`** — 存档"调查了 X 问题，看到代码里是这样的"

**归档之后怎么召回？** EasySDD 只在需要的时候召回。`easysdd-feature-design` 起草设计前会显式去搜 compound 目录，`easysdd-issue-analyze` 分析 bug 时也会显式去查找。feature 和 issue 过程中积累的知识就这样反哺到下一次设计里，越往后越顺。

### 辅助：周边工具

- **`easysdd-onboarding`** — 把新仓库接入 easysdd 目录结构，空仓库和已有零散文档的仓库都能接
- **`easysdd-requirements`** — 起草或刷新 `easysdd/requirements/` 下的需求文档（"为什么要有这个能力"）
- **`easysdd-architecture`** — 架构一站式：起草新架构文档 / 刷新已有文档 / 做架构体检（design 自洽 / design↔代码一致 / architecture 目录多份文档间一致）
- **`easysdd-guidedoc`** — 写给外部读者的开发者指南 / 用户指南
- **`easysdd-libdoc`** — 为库的公开 API 逐条目生成参考文档

---

## 场景路由

仓库里还没有 `easysdd/` 目录，先用 `easysdd-onboarding` 初始化目录结构。之后按场景选子技能，不确定用哪个也没关系，根技能 `easysdd-core` 会自己路由。

| 场景 | 子技能 |
|---|---|
| 新功能 / 新能力 | `easysdd-feature` |
| BUG / 异常 / 文档错误 | `easysdd-issue` |
| 读代码、提问调研 | `easysdd-explore` |
| 补 / 更新需求文档 | `easysdd-requirements` |
| 补 / 更新 / 检查架构文档 | `easysdd-architecture` |
| 技术选型 / 约束 / 规约 | `easysdd-decisions` |
| 踩坑回顾、经验总结 | `easysdd-learning` |
| 可复用的编程模式、库用法 | `easysdd-tricks` |
| 开发者指南 / 用户指南 | `easysdd-guidedoc` |
| 库 API 参考 | `easysdd-libdoc` |

---

## EasySDD 跟其他框架不一样在哪

### 三层分离：需求 / 架构 / 特性

`requirements/` 管"为什么要做"，`architecture/` 管"系统长什么样"，`features/` 管"这次具体加什么"。三层解耦，改一层不会牵动另一层。

### 架构文档永远跟得上代码

每做完一个 feature，acceptance 阶段会自动把这次的变更合进 `easysdd/architecture/` 下对应的架构文档。下次再有人（或 AI）想理解系统现在的样子，有一份跟代码保持同步的入口。`easysdd-architecture` 还能反过来做一致性检查，把 design 和代码对不齐的地方列出来。

### 术语归一

统一术语，确保人讲的、AI 理解的、AI 讲回来的、人理解的，是同一个东西。这件事用过你就知道值了。

### 工作清单用 YAML

design 完成以后，模型会生成一份 yaml 格式的 checklist，而不是 markdown 或 csv。实测 yaml 的遵从率明显更高，我也不知道为啥，但能用。

### 共享口径集中管

目录结构、frontmatter 字段、checklist 生命周期、commit 约定这些跨技能共用的东西，统一放在项目的 `easysdd/reference/` 下，由 onboarding 一次性复制过来。要改口径改模板，新项目 onboarding 自动带上新版本。

---

## 一些实际效果

- **自动积累知识**：feature acceptance 阶段会自动写 learning，并更新 architecture 文档
- **过去的问题直接复用**：上次关于 Tauri 编译问题的沉淀，下次 design 时直接被搜到
- **feature 和 issue 显性存档**：要往回查"当时解决了哪些 issue"时有据可查
- **架构一致性可主动检查**：不用等出问题才发现 design 和代码对不上

---

## 模型适配

我自己在家和公司都在用。Claude 模型和 GLM 4.7 都能跑，但 Claude 可以一次处理一个大颗粒 feature，GLM 4.7 只能切小颗粒，每次 design 还得我把关。模型能力差距，没办法。

---

## 设计上的权衡

> 那 worktree、code-review、子代理开发这些技能呢？

这是设计取舍。小到 OpenSpec、大到 Oh-My-OpenAgent，每家都有自己的权衡。我并不想做一个大而全的框架，**够用就行**——能帮我持续推进项目、让项目持续受控、让我安心，就 OK。没有复杂的 Subagent 和 hook 来干扰你的 Claude 或 Codex。

---

## 怎么用

```bash
npx skills add https://github.com/liuzhengdongfortest/easysdd
```

进项目后对 Claude 说：

> 「在这个项目里初始化 easysdd」

然后开始第一件事：

> 「我要做 X 功能，走 easysdd-feature 流程」
>
> 「这里有个 bug，走 easysdd-issue 流程」

不知道用哪个子技能也没关系，根技能 `easysdd-core` 会自己路由。

---

## 最后

也不要全依赖 EasySDD。框架虽好不能解决所有情况。我自己只在特性复杂度足够高的时候才走完整流程——你既然约束了 AI 按流程办事，token 是会多消耗一些的。一般的小 UI 调整我直接截图 vibe 就行。一个完整 feature 走完，Claude Code 的 Opus 大概要 200k 左右的上下文。

GitHub：<https://github.com/liuzhengdongfortest/EasySDD>

---

## License

MIT

## 感谢

部分想法来自 [Linux Do 社区](https://linux.do/)。
