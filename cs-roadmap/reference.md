# cs-roadmap 参考模板

本文件提供 `cs-roadmap` 使用的主文档和 items.yaml 参考格式。SKILL.md 只保留流程骨架，具体格式在这里。

---

## 1. 主文档 `{slug}-roadmap.md`

### 1.1 frontmatter

```yaml
---
doc_type: roadmap
slug: permission-system
status: active          # active | paused | completed
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
tags: [permission, auth]
related_requirements: []    # 相关 req slug 列表，可空
related_architecture: []    # 相关 architecture doc slug 列表，可空
---
```

字段说明：

- `status`：`active` 进行中 / `paused` 暂停 / `completed` 所有条目 done 或 dropped
- `related_requirements`：本大需求涉及的 req slug，帮助读者跳转到"为什么要有这个能力"
- `related_architecture`：会被改到的 architecture doc slug，帮助读者理解"改了会触碰到哪些现状"

### 1.2 正文节

```markdown
# {大需求标题——直接说是什么，不玩比喻}

## 1. 背景

一两段讲这块大需求是什么、为什么要做。对象是"新加入这个项目、想知道接下来几个月在忙什么"的人。

## 2. 范围与明确不做

### 本 roadmap 覆盖

- 能力 A
- 能力 B
- 能力 C

### 明确不做（本 roadmap 不覆盖）

- 能力 X（理由）
- 能力 Y（理由或指向另一份 roadmap / req）

## 3. 模块拆分（概设）

这块大需求拆成哪几个模块 / 组件，各自做什么。一图（文字版结构树或 ASCII 框图都行）+ 每个模块一段说明。

```
{大需求名}
├── 模块 A：{一句话职责}
├── 模块 B：{一句话职责}
└── 模块 C：{一句话职责}
```

### 模块 A · {名称}

- **职责**：{一两句话讲清做什么、不做什么}
- **承载的子 feature**：{slug-1, slug-2}
- **触碰的现有代码 / 模块**：{已有的 X 模块 / 全新 / 重写某模块}

### 模块 B · {名称}

- **职责**：...
- **承载的子 feature**：...
- **触碰的现有代码 / 模块**：...

### 模块 C · ...

> 如果本大需求**不需要**模块拆分（比如纯粹改一个已有模块的内部行为），在本节明确写 "本大需求在已有模块 {X} 内完成，不引入新模块也不调整模块边界"，然后跳过第 4 节直接到第 5 节。

## 4. 模块间接口契约 / 共享协议（架构层详设）

定义模块之间怎么交互——这一节是 feature-design 的硬约束输入。**写到函数签名 / 数据结构 / 协议字段 / 错误码这一级**，不允许"两边商量" / "待定"含糊过去。

### 4.1 {接口 / 协议名 1}

**方向**：模块 A → 模块 B
**形式**：{HTTP API / 函数调用 / 消息事件 / 共享数据库表 / 文件协议 / ...}

**契约**：

```
{具体的接口定义——按形式不同选合适的表达}

# HTTP API 例：
POST /api/v1/permission/check
Request:  { user_id: str, resource: str, action: str }
Response: { allowed: bool, reason: str | null }
错误：    400 invalid_input, 404 user_not_found, 500 internal

# 函数签名例：
def check_permission(user_id: str, resource: str, action: str) -> PermissionResult
class PermissionResult: allowed: bool; reason: Optional[str]

# 事件例：
event_type: permission.changed
payload: { user_id: str, role: str, changed_at: ISO8601 }
```

**约束**：

- {如：调用方必须先确保 user_id 已认证}
- {如：response 的 reason 在 allowed=true 时必须为 null}
- {如：事件必须幂等消费}

### 4.2 {接口 / 协议名 2}

...

### 4.x 共享数据结构 / 状态

如果几个模块共享同一份数据结构 / 持久化存储 / 全局状态，在这里定义一次：

```
{表结构 / 类型定义 / 配置 schema}
```

> 如果本大需求**没有跨模块接口**（比如纯前端样式调整），本节明确写"本 roadmap 无跨模块接口"。不允许空着或写"暂无"。

## 5. 子 feature 清单

按依赖和推进顺序排列。每条对应 items.yaml 里一个条目，两份保持同步。每条要点明它落在第 3 节的哪个模块下。

1. **{子 feature slug}** — {一句话描述}
   - 所属模块：{模块 A / 模块 B / 跨模块——指明涉及哪些}
   - 依赖：{前置 slug 列表 / 无}
   - 状态：{planned | in-progress | done | dropped}
   - 对应 feature：{YYYY-MM-DD-{slug} / 未启动}
   - 备注：{可选，说明为什么这条排在这里}

2. **{子 feature slug}** — ...

**最小闭环**：第 {N} 条 `{slug}` 做完后，{描述能端到端跑通的最窄路径}。

## 6. 排期思路

一段短的，讲拆分逻辑和优先级判断：

- 为什么这样拆（按模块 / 按用户价值 / 按风险 / 按依赖）
- 第一条为什么选它作为最小闭环
- 中间有没有卡点（需要前置架构改动 / 外部依赖 / 设计决策）

## 7. 观察项

起草或刷新过程中发现、但本 roadmap 不处理的事情，交给用户决定：

- 发现 `codestable/architecture/X.md` 里对 Y 的描述已经过时，建议另起 architecture update
- 发现 requirement-Z 的边界和本 roadmap 第 5 条冲突，建议先对齐 req
- ...

## 8. 变更日志（update 模式才有）

- YYYY-MM-DD：{一句话描述本次改动；如果改了第 4 节接口契约，要单列"接口契约变化"和"受影响的已启动 feature 列表"}
```

---

## 2. items.yaml 格式

```yaml
roadmap: permission-system
created: YYYY-MM-DD

items:
  - slug: permission-rbac-core
    description: 基础 RBAC 模型和数据表，提供角色/权限两张表和最小查询 API
    depends_on: []
    status: planned             # planned | in-progress | done | dropped
    feature: null               # 启动 feature 后填 YYYY-MM-DD-{slug}，未启动写 null
    minimal_loop: true          # 只有一条标 true，即"最小闭环"那条
    notes: null                 # 可选：备注、特殊约束、drop 理由

  - slug: permission-admin-ui
    description: 管理员配置角色和权限的页面
    depends_on: [permission-rbac-core]
    status: planned
    feature: null
    minimal_loop: false
    notes: null
```

### 字段规则

- `slug`：子 feature 的 slug，小写字母 / 数字 / 连字符；将来 feature 目录命名为 `YYYY-MM-DD-{slug}`
- `description`：一句话，能独立讲清楚这条做什么
- `depends_on`：前置 slug 列表。空数组表示无依赖。必须指向同 roadmap 里的其他条目
- `status`：`planned`（未启动）/ `in-progress`（feature 已 design）/ `done`（feature 验收完成）/ `dropped`（确定不做了）
- `feature`：启动后填 feature 目录名（`YYYY-MM-DD-{slug}`），用于 acceptance 反查
- `minimal_loop`：全表只有一条为 `true`，标记"最小闭环"那条
- `notes`：备注。drop 的条目必须在这里写理由

### 状态机

```
planned  → in-progress  （feature-design 启动时由 design 技能改）
in-progress → done      （feature-acceptance 完成时由 acceptance 技能改）
planned  → dropped      （用户决定不做，roadmap update 模式改）
done     （终态）
dropped  （终态，不删除条目，保留历史）
```

**不合法的跃迁**：从 `done` 回 `in-progress`（要改需求回退走新的 feature）；从 `dropped` 回 `planned`（要恢复重新加一条 slug 略改）。

### 校验

```bash
python codestable/tools/validate-yaml.py --file codestable/roadmap/{slug}/{slug}-items.yaml --yaml-only
```

---

## 3. 拆解 checklist（起草时对自己提问）

### 架构方案层（先问这几条）

- [ ] 模块拆分讲清了吗？每个模块的职责能用一句话说出来？模块边界讲得清吗（哪些事这个模块做、哪些不做）？
- [ ] 接口契约写到函数签名 / 数据结构 / 协议字段 / 错误码这一级了吗？feature-design 看完不需要再回来问就能直接照着实现？
- [ ] 共享数据结构 / 持久化 / 全局状态有没有列齐？
- [ ] 如果本大需求确实没有跨模块接口，是不是在第 4 节明确写了"无跨模块接口"，而不是空着 / "待定"？

### 子 feature 拆解层

- [ ] 这条能独立走完一次 feature 流程（design / implement / acceptance）吗？走不通就继续拆或合并
- [ ] 这条做完后能单独验证吗？能不能写出一句"完成后 {具体可观测现象}"
- [ ] 这条的 slug 和 `codestable/features/` 下已有目录冲突吗？grep 过了吗
- [ ] 这条标了"所属模块"吗？该模块在第 3 节存在吗？
- [ ] 依赖关系讲得清具体理由吗？"B 需要 A 提供的 {具体产物}" 这种
- [ ] 最小闭环那条真是"最窄的端到端路径"吗？还是只是"最容易的一条"
- [ ] 有没有条目其实应该是 requirement 变化而不是 feature？（比如"把 XX 能力的边界改一下"）那种转 `cs-req`

---

## 4. review 提示

> roadmap 已起草完成，请整体 review。**先看架构方案，再看 feature 拆解**——架构方案改了下游全要重排：
>
> **架构方案层**
> 1. 模块拆分对吗？模块边界划得合理吗？有没有该合并 / 该拆开的？
> 2. 接口契约定得够具体吗？feature-design 拿着这份能直接照做吗？还是有"两边商量"的含糊地带？
> 3. 共享数据结构 / 协议字段 / 错误码有没有遗漏？
>
> **feature 拆解层**
> 4. 拆解粒度合不合适？每条是不是都能独立做成一个 feature？
> 5. 每条落在哪个模块标对了吗？
> 6. 依赖关系对吗？有没有漏的前置或多余的依赖？
> 7. 最小闭环选得对吗？第一条做完真能端到端演示点什么吗？
> 8. "明确不做"有没有遗漏？有没有你其实想做但被我漏掉的？
> 9. 排期顺序符合你的产品优先级吗？
>
> 有修改意见直接说，确认后我落盘 roadmap 目录和 items.yaml。
