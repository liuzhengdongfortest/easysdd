# 什么是 Skill——写之前先读这份

在 Claude Code 里你经常干这种事：每开一个新会话，都要把同一份操作手册贴进聊天——部署步骤、提交规范、某个框架的 API 约定、某种文档的固定写法。贴久了烦，也容易忘贴。

Skill 就是把这份手册变成一个带着 YAML 头的 Markdown 文件，放在约定位置，Claude 会在需要的时候自己把它读进来。跟 CLAUDE.md 不同的地方是：CLAUDE.md 是每次会话一开始就全文塞进上下文的，skill 的正文平时不占上下文，只有 Claude 判断该用的时候才展开。所以你可以堆一堆长篇的参考材料，平时不花钱，用的时候才花。

Skill 和过去的 custom command 已经合并。`.claude/commands/deploy.md` 和 `.claude/skills/deploy/SKILL.md` 都生成 `/deploy` 斜杠命令。skill 比 command 多了一个目录装周边文件、支持 frontmatter 控制触发行为、以及让 Claude 自己按相关性调用。

---

## 放哪里

| 放的位置 | 路径 | 谁能用 |
|---|---|---|
| 个人 | `~/.claude/skills/<skill-name>/SKILL.md` | 你所有项目 |
| 项目 | `.claude/skills/<skill-name>/SKILL.md` | 只在这个项目 |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | 装了这个 plugin 的地方 |
| Managed | 企业统一下发 | 全组织 |

同名冲突时优先级：enterprise > personal > project。plugin 用 `plugin-name:skill-name` 命名空间隔离，不跟别的冲突。skill 和老的 `.claude/commands/` 同名时，skill 优先。

---

## 一个 skill 长什么样

每个 skill 是个目录，入口是 `SKILL.md`：

```
my-skill/
├── SKILL.md          ← 必须，主入口
├── reference.md      ← 可选，详细参考材料（按需加载）
├── examples.md       ← 可选，例子
└── scripts/
    └── helper.py     ← 可选，脚本，由 Claude 执行不加载为上下文
```

`SKILL.md` 必须有，其他都可选。周边文件要在 `SKILL.md` 里用链接或说明引用出来，Claude 才知道它们存在、什么时候该读。

---

## SKILL.md 的 frontmatter 字段

正文前面用 `---` 包一段 YAML，规定这个 skill 的行为：

```yaml
---
name: my-skill
description: 这个 skill 干什么、什么时候用
disable-model-invocation: false
user-invocable: true
allowed-tools: Read Grep
---
```

只有 `description` 是推荐填的。所有字段：

| 字段 | 作用 |
|---|---|
| `name` | 斜杠命令名。不填就用目录名。只能小写字母、数字、连字符，最多 64 字符 |
| `description` | **关键字段**。Claude 靠这个判断什么时候自动调用这个 skill。不填就取正文第一段 |
| `when_to_use` | 补充触发条件和常见触发词。跟 `description` 合起来在 skill 列表里最多 1536 字符，超了被截断 |
| `argument-hint` | 自动补全时提示参数形式，比如 `[issue-number]` |
| `disable-model-invocation` | `true` 时 Claude 不会自动调用，只能用户手动 `/name` 触发。适合有副作用的操作（部署、提交、发消息） |
| `user-invocable` | `false` 时不在 `/` 菜单里显示，只让 Claude 自己按需调用。适合"背景知识"型的 skill |
| `allowed-tools` | 这个 skill 激活时 Claude 可以免审核使用的工具。空格分隔 |
| `model` / `effort` | 这个 skill 激活时用哪个模型 / 花多少思考预算 |
| `context: fork` | 把这个 skill 放进 fork 出来的 subagent 跑，不污染主上下文 |
| `agent` | 搭配 `context: fork` 用，指定用哪种 agent（`Explore` / `Plan` / `general-purpose` / 自定义） |
| `hooks` | 绑定到这个 skill 生命周期的 hook |
| `paths` | glob 模式。设了以后 Claude 只在操作匹配路径的文件时自动调用 |
| `shell` | 内联 shell 命令用什么解释器，默认 `bash`，可选 `powershell` |

`name` 必须跟目录名一致。改 name 等于改目录名。

---

## description 为什么这么要紧

Claude 判断要不要调用一个 skill，只能看 `description` 和 `when_to_use` 两段话。正文平时不在它的上下文里。所以 description 必须：

1. **写清楚这个 skill 做什么**——不是"关于 X 的"，而是"用来做 X"
2. **写清楚什么时候该触发**——列具体的用户说法、文件类型、任务特征
3. **front-load 最常见的触发场景**——因为尾部可能被 1536 字符限制截掉

反面教材：`description: 一个关于 API 设计的 skill`——Claude 不知道是该在写 API 时触发、还是在 review API 时触发、还是在解释 API 给新人听时触发。

好例子：`description: 写新的 API endpoint 时触发——检查命名约定、错误返回格式、请求验证。触发词："加一个接口"、"新 endpoint"、"implement API"。不覆盖 GraphQL，只管 REST。`

写 description 时有个小陷阱：Claude 默认**偏少触发**，怕用错。所以 description 要**稍微往"推销"的方向写一点**——"即使用户没明说 X，只要任务有 Y 特征就触发"，比中性描述更有效。

---

## 渐进式加载（progressive disclosure）

Skill 体系有三层：

1. **Metadata**（name + description）——一直在 Claude 上下文里，判断是否触发用
2. **SKILL.md 正文**——触发后才加载进上下文
3. **周边文件 / 脚本**——Claude 按 SKILL.md 的指引按需读取；脚本是执行的，不加载为上下文

这决定了 SKILL.md 的体积管理：

- 官方建议 SKILL.md **控制在 500 行以内**
- 超了就把详细参考（API 细节、长例子、完整模板）拆到同目录 `reference.md` / `examples.md`
- 在 SKILL.md 里明确说"详细看 reference.md"，Claude 才知道什么时候读

注意：skill 一旦触发，SKILL.md 的渲染结果**进入会话就留在那里**，后面不会重新读文件。所以写 SKILL.md 要写成"贯穿整个任务的指引"而不是"一次性步骤"。

---

## Skill 内容的两种性质

思考一下你的 skill 属于哪一种，会影响怎么写：

**参考型（Reference）**——给 Claude 补一套背景知识，让它用在当前对话里。API 约定、代码规范、项目领域知识、某个库的坑。这类 skill 让 Claude 按需触发即可，`disable-model-invocation` 留默认。

**任务型（Task）**——指导 Claude 做一个特定的多步动作。部署、提交、生成某种文档。这类你通常希望自己手动触发（`/skill-name`），所以给它加 `disable-model-invocation: true`。

两种的写法也不同：参考型像文档（"遇到 X 时考虑 Y"），任务型像 playbook（"第一步、第二步、第三步"）。

---

## 传参数给 skill

skill 里用 `$ARGUMENTS` 拿到用户传的所有参数：

```yaml
---
name: fix-issue
description: 修 GitHub 上的某个 issue
disable-model-invocation: true
---

修 GitHub issue $ARGUMENTS，按项目代码规范来。
```

用户跑 `/fix-issue 123`，Claude 收到的就是"修 GitHub issue 123，按项目代码规范来"。

拿单个参数用 `$ARGUMENTS[N]` 或简写 `$N`（0-based）：

```yaml
Migrate $0 component from $1 to $2.
```

用户跑 `/migrate SearchBar React Vue`，`$0` = `SearchBar`、`$1` = `React`、`$2` = `Vue`。多词参数用引号包："hello world"。

---

## 动态注入上下文

SKILL.md 里可以写 `` !`<shell command>` ``，在 skill 发给 Claude 之前执行命令，把输出替换到 placeholder 里。适合给 skill 注入实时数据。

```yaml
---
name: pr-summary
description: 总结一个 PR 的改动
allowed-tools: Bash(gh *)
---

## PR 信息
- diff: !`gh pr diff`
- 评论: !`gh pr view --comments`

## 任务
总结这个 PR……
```

多行命令用 ` ```! ` 开头的代码块。Claude 收到的是命令**运行完的结果**，不是命令本身。

---

## 让 skill 在 subagent 里跑

加 `context: fork` + `agent: Explore`（或别的 agent 类型），skill 在一个新开的隔离上下文里跑，不看当前会话历史。适合"我要研究一下 X"这种只需要产出一份总结、不需要主会话上下文的任务。

```yaml
---
name: deep-research
description: 深入研究一个话题
context: fork
agent: Explore
---

深入研究 $ARGUMENTS：
1. 用 Glob 和 Grep 找相关文件
2. 读代码、分析
3. 总结发现，给出具体文件引用
```

注意：`context: fork` 只对有明确任务的 skill 有意义。纯"约定文档"型的 skill（"写 API 时用这些命名"）fork 进去只会看到约定但没任务，什么都不做就返回。

---

## 免审核工具 allowed-tools

`allowed-tools` 字段授权 skill 激活时可以免审核调用指定工具：

```yaml
allowed-tools: Bash(git add *) Bash(git commit *) Bash(git status *)
```

这不限制有哪些工具可用（别的工具还是能调，只是会触发权限提示），只是对列出的工具免审核。

---

## 常见坑

**Skill 不触发**
- 看 description 里有没有用户会自然说出的关键词
- 在 Claude Code 里问 "What skills are available?" 确认 skill 被发现了
- 重新措辞请求，往 description 里的说法靠
- 直接用 `/skill-name` 强制触发

**Skill 触发太频繁**
- description 写得更具体，缩小触发范围
- 加 `disable-model-invocation: true` 改成只手动触发

**Description 被截断**
- 多个 skill 挤在一起时，每个 description 会被截到适配字符预算
- 把最重要的触发场景前置到 description 开头
- 单个 skill 的 description + when_to_use 合起来 1536 字符上限，超了也被截
- 环境变量 `SLASH_COMMAND_TOOL_CHAR_BUDGET` 可以调高总预算

**Skill 触发后效果慢慢消失**
- SKILL.md 内容在会话里不会重新读取，只是模型可能选了别的工具/方式
- 写"贯穿任务的指引"而不是"一次性步骤"
- 用 hooks 做硬强制
- 长会话压缩后重新 `/skill-name` 再调用一次恢复上下文

---

## 进一步参考

- 官方文档：https://code.claude.com/docs/en/skills
- Agent Skills 开放标准：https://agentskills.io
- 相关：[Subagents](https://code.claude.com/docs/en/sub-agents)、[Plugins](https://code.claude.com/docs/en/plugins)、[Hooks](https://code.claude.com/docs/en/hooks)、[Permissions](https://code.claude.com/docs/en/permissions)
