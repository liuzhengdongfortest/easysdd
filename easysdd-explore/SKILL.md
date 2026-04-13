---
name: easysdd-explore
description: 探索归档子工作流——对仓库做定向代码探索并把结果归档，供后续 design/analyze/fix 复用。触发场景："先 explore 一下"、"这个仓库里 X 怎么实现"、"快速熟悉这个模块"、"把探索结果存档"。
---

# easysdd-explore

**探索归档子工作流** —— 把一次"提问 -> 读代码 -> 得结论"的过程沉淀为可检索证据，减少重复探索。

> "同一个问题第一次花 2 小时查代码，第二次应该 5 分钟内找到答案。"

---

## 一、适用场景

- 新人入仓，需要快速理解模块边界、调用链、入口文件
- 用户提出一个具体问题，但暂时不要求直接产出方案/修复
- feature-design / issue-analyze / issue-fix 前，先补一轮证据化探索
- 技术方向还在讨论，需要先做轻量 spike（只探索，不拍板）

不适用场景：

- 已经是明确的拍板动作（该用 `easysdd-decisions`）
- 已经是可复用处方总结（该用 `easysdd-tricks`）
- 已经在做 BUG 修复并且根因明确（直接走 `easysdd-issue-fix`）

---

## 二、涉及的路径

本技能在正文里用自然语言术语引用路径（**探索归档目录**），具体目录位置见主技能 `easysdd` 第二节"目录安排"。

**文件命名**：`YYYY-MM-DD-{slug}.md`（日期取归档当天，slug 为英文小写 + 连字符）。

---

## 三、三种探索文档类型

每条探索文档归属以下三类之一，在 YAML frontmatter 的 `type` 字段标注：

| 类型 | 适用情境 |
|---|---|
| `question` | 围绕一个具体问题查代码并给结论 |
| `module-overview` | 快速梳理某模块结构、边界、入口与依赖 |
| `spike` | 对多个可能方向做轻量技术探查（不做最终决策） |

---

## 四、文档格式

### YAML frontmatter

```yaml
---
type: question | module-overview | spike
date: YYYY-MM-DD
slug: {英文描述，连字符分隔}
topic: {一句话描述探索问题}
scope: {探索范围，如 auth module / cache pipeline / api layer}
keywords: []
status: active | outdated
confidence: high | medium | low
---
```

### 正文结构

所有类型共用一个结构，节的存在性用"必填 / 视情况 / 可省略"标注：

```markdown
## 问题与范围                ← 必填
## 速答                      ← 必填：结论前置，直接给出核心答案
## 关键证据                  ← 必填：支撑速答的 3–8 条引用
## 细节展开                  ← 视情况：有子问题或分支时展开，每个子问题一小节
## 未决问题                  ← 可省略：还不确定的点
## 后续建议                  ← 必填：路由到哪个工作流
## 相关文档                  ← 可省略
```

---

#### 各节写法说明

**`## 问题与范围`**

说明这次探索要回答的问题、覆盖哪些模块/目录、明确不看哪些范围。

---

**`## 速答`**

1–3 句话直接给出核心结论，不留悬念。读者看完这一节就应该能判断"这份探索和我当前的问题相关吗"。

如果结论涉及多个模块之间的协作关系、数据流或调用链，在速答节附一张 Mermaid 图。`module-overview` 和 `spike` 类型必须有图；`question` 涉及多步流程时必须有图；单模块内的局部问题可以省略。

```mermaid
graph LR
  A[调用方] --> B[核心模块]
  B --> C[持久层]
```

---

**`## 关键证据`**

挑选能让一个持怀疑态度的读者相信速答结论的最少证据，目标 3–8 条。

**写法**：每条引用写 `` `文件路径:行号` ``，用一句话说明这条证据支撑了哪个结论，而不是复述代码内容。同一文件的多条证据自然归组，复用同一个小标题；只有一两条证据时直接平铺，不必分组。

```markdown
### `crates/foo/src/bar.rs`

- **:42** — `TaskState` 是持久化结构体，说明任务状态不依赖运行时内存。
- **:87** — `save_state` 调用在每次 turn 完成后触发，证明持久化时机是 turn 粒度。

### `src-tauri/src/lib.rs`

- **:705** — `in_flight_turns` 以 `task_id` 为 key，发送互斥粒度是单个 task，不是全局锁。
```

---

**`## 细节展开`**（视情况）

速答之外需要进一步解释的子问题，每个子问题一个 `###` 小节。如果速答已经完整覆盖，省略本节。

---

**`## 未决问题`**（可省略）

探索结束后仍不确定的点。如果有未决问题，`confidence` 降为 `medium` 或 `low`。

---

**`## 后续建议`**

根据结论建议下一步走哪个工作流：

- 需求未落方案 → `easysdd-feature-design`
- 需求已有方案 → `easysdd-feature-implement`
- 问题已成型但根因未明 → `easysdd-issue-analyze`
- 根因明确且用户确认 → `easysdd-issue-fix`
- 形成长期规范拍板 → `easysdd-decisions`
- 沉淀通用做法 → `easysdd-tricks`

---

**格式规则**：

- 速答必须先于证据出现。结论不能埋在证据堆后面
- 证据节比速答节长很多，是选证标准出了问题，不是格式问题——先精简证据，再考虑分组
- 结论必须可回溯到证据，不允许纯猜测结论
- 如果证据不足，`confidence` 必须是 `medium` 或 `low`
- 当代码变更导致旧探索不再成立时，将旧文档 `status` 标为 `outdated`，新增当前版本的探索文档

---

## 五、工作流阶段

### Phase 1：收敛探索问题

最多问用户两个问题：

1. "你最想先回答的一个问题是什么？"
2. "希望聚焦哪个模块/目录？"

如果用户描述已清楚，直接进入 Phase 2。

### Phase 2：证据化探索

- 用 Glob/Grep/Read 真实读代码，不靠猜
- 边读边积累证据；**同步思考每条证据支撑哪个结论**，不支撑任何结论的证据不记录
- 形成初步结论后，主动检查：已有证据能否说服一个持怀疑态度的人？够了就停，不必继续扩大搜索范围

### Phase 3：起草与确认

- 先写速答节，再回填关键证据
- AI 一次性起草完整 explore 文档，用户 review 后确认
- 有修改则按反馈修订后再落盘

### Phase 4：归档

- 写入探索归档目录，命名 `YYYY-MM-DD-{slug}.md`
- 归档后用搜索工具查有无语义重叠的历史探索
- 若存在冲突或过期记录，提示用户将旧文档标为 `outdated`

### Phase 5：向后续工作流回传

按第四节"后续建议"的路由表给出下一步建议。

---

## 六、搜索工具

`tools/search-yaml.py` 是通用 YAML frontmatter 搜索工具（路径见主技能 `easysdd` 第二节）。

```bash
# 全文检索 explore
python tools/search-yaml.py --dir easysdd/explores --query "auth flow"

# 按类型
python tools/search-yaml.py --dir easysdd/explores --filter type=module-overview

# 只看当前有效探索记录
python tools/search-yaml.py --dir easysdd/explores --filter status=active

# 按关键词
python tools/search-yaml.py --dir easysdd/explores --filter keywords~=cache

# JSON 输出（给 AI 解析）
python tools/search-yaml.py --dir easysdd/explores --query "retry" --json
```

---

## 七、与其他工作流的关系

- `easysdd-feature-design` 开始前：先搜索 explores，复用调用链与模块边界证据
- `easysdd-issue-analyze` 开始前：先搜索 explores，减少重复定位
- `easysdd-issue-fix` 开始前：搜索 explores，确认修复点与历史证据一致
- `easysdd-explore` vs `easysdd-tricks`：explore 记录"看到了什么"，tricks 记录"推荐怎么做"
- `easysdd-explore` vs `easysdd-decisions`：explore 是输入，decisions 是拍板

---

## 八、退出条件

- [ ] 已明确探索问题与范围
- [ ] 速答节已给出核心结论（结论前置，不埋在证据之后）
- [ ] 关键证据 3–8 条，每条标注文件:行号，并说明支撑哪个结论
- [ ] 涉及多模块协作或 module-overview/spike 类型时，速答节有 Mermaid 图
- [ ] 文档已归档到探索归档目录
- [ ] 已给出后续建议（路由到哪个子工作流）

---

## 九、反模式（看到就停）

- ❌ 不读代码直接给结论
- ❌ 证据只写"看起来像"，不写文件:行号
- ❌ 结论写在证据之后——速答节必须在关键证据节之前
- ❌ 证据节比速答节长数倍——先精简证据，选不支撑结论的条目删掉
- ❌ 跨模块流程没有 Mermaid 图，只靠文字描述多模块协作
- ❌ 把 explore 文档写成 decisions（提前拍板）
- ❌ 把 explore 文档写成 tricks（直接给处方，没有证据链）
- ❌ 历史 explore 已过期却继续引用，不做 `status` 标注
