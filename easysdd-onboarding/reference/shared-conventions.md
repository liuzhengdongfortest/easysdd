# easysdd 共享口径

本文件由 `easysdd-onboarding` 复制到项目的 `easysdd/reference/shared-conventions.md`。所有 easysdd 子技能在运行时用**项目相对路径** `easysdd/reference/shared-conventions.md` 引用本文件——这是跨子技能共享但不适合堆在单个技能里的规范的唯一权威版本。

skill 本身不共享文件系统（每个 skill 是独立安装单元），所以共享口径不能放在某个 skill 内部被别的 skill 引用。放在"工作项目"里，对所有 skill 都可达。

---

## 0. 目录结构与路径命名

onboarding 完成后，项目里应当存在如下骨架（`easysdd-onboarding` 负责搭建）：

```
easysdd/
├── architecture/          架构中心目录
│   └── DESIGN.md          架构总入口
├── features/              feature spec 聚合根
│   └── YYYY-MM-DD-{slug}/  每个 feature 一个目录
│       ├── brainstorm.md  （可选）
│       ├── design.md
│       ├── checklist.yaml
│       └── acceptance.md
├── issues/                issue spec 聚合根
│   └── YYYY-MM-DD-{slug}/  每个 issue 一个目录
│       ├── report.md
│       ├── analysis.md    （根因不显然时才有）
│       └── fix-note.md
├── compound/              沉淀类文档统一目录
│   └── YYYY-MM-DD-{doc_type}-{slug}.md
│                          doc_type ∈ {learning, trick, decision, explore}
├── architecture/          架构中心目录（如上）
├── tools/                 跨工作流共享脚本（由 onboarding 从技能包释放）
└── reference/             共享参考文档（由 onboarding 从技能包释放，即本文件所在目录）
```

### 命名规则

- feature 目录：`easysdd/features/YYYY-MM-DD-{slug}/`，日期用创建当天
- issue 目录：`easysdd/issues/YYYY-MM-DD-{slug}/`，日期用报告当天
- 沉淀类文档：`easysdd/compound/YYYY-MM-DD-{doc_type}-{slug}.md`，日期用**归档当天**（不是问题发生当天）
- `AGENTS.md` 在项目根目录，**不在 `easysdd/` 里**

### 要改目录结构

改 `easysdd-onboarding/reference/shared-conventions.md` 这个模板，新项目 onboarding 时会带上新版本。已有项目需要手动同步 `easysdd/reference/shared-conventions.md`。

---

## 1. 共享元数据口径

### feature spec

- `design.md` / `acceptance.md` 共用 `doc_type`、`feature`、`status`、`summary`、`tags` 这组核心字段
- 子技能只补充本阶段特有字段，不重复改写这组字段的含义

### issue spec

- `report.md` / `analysis.md` / `fix-note.md` 共用 `doc_type`、`issue`、`status`、`tags` 这组核心字段
- `severity`、`root_cause_type`、`path` 等属于阶段特有字段，由对应阶段按需补充

### 归档类文档

- `learning` / `trick` / `decision` / `explore` 四个子技能的产物**统一写入 `easysdd/compound/` 目录**
- 每个文档必须在 frontmatter 顶部带 `doc_type` 字段（`learning` / `trick` / `decision` / `explore`），作为跨子技能的归属判定
- 文件名统一用 `YYYY-MM-DD-{doc_type}-{slug}.md`——前缀即类型，`ls` 一眼能区分
- 各子技能在 `doc_type` 之外保留自己的专属 frontmatter（learning 的 `track`、trick 的 `type`、decision 的 `category`、explore 的 `type`）
- 各子技能只认自己的 `doc_type` 和文件名前缀，不读不写别的子技能的文档
- `status` 一类通用字段的语义必须和本文件保持一致，不另起一套口径
- 子技能里如果需要解释状态，只保留该工作流特有的状态流，不重新定义通用语义

### 面向外部读者的文档

- `guidedoc` / `libdoc` 的 frontmatter 由各自子技能定义
- 如无特殊说明：`draft` = 待 review，`current` = 当前有效，`outdated` = 代码已变更待同步

### 写作约束

- 子技能提到字段时，优先写"本技能额外字段"或"本阶段状态变化"
- 不要把整套通用字段定义在多个技能里重复展开

---

## 2. checklist.yaml 生命周期

- `checklist.yaml` 是 feature 工作流的唯一执行清单
- 由 `easysdd-feature-design` 或 `easysdd-feature-fastforward` 在 `design.md` 确认通过后一次生成

### design / fastforward 的职责

- 只负责从方案里提取 `steps` 和 `checks`
- 不预先把任何条目标成完成

### implement 的职责

- 只更新 `steps[].status`
- 状态流：`pending` → `done`
- 不改写 `checks` 的所有权和来源

### acceptance 的职责

- 只更新 `checks[].status`
- 状态流：`pending` → `passed` / `failed`
- 不回头重写 `steps`

### 写作约束

- 子技能描述 `checklist.yaml` 时，只补充本阶段具体要读/写哪一部分
- 不重新定义整份文件的生命周期

---

## 3. 阶段收尾推荐

### feature-acceptance

收尾时按顺序判断是否要推荐：

1. `easysdd-learning`：沉淀经验
2. `easysdd-decisions`：记录长期约束/选型
3. `easysdd-guidedoc`：更新开发者/用户指南
4. `easysdd-libdoc`：更新公开 API 参考
5. `scoped-commit`

### issue-fix

收尾时按顺序判断是否要推荐：

1. `easysdd-learning`：记录坑点
2. `easysdd-decisions`：如修复暴露出长期约束
3. `scoped-commit`

### 推荐动作的统一规则

- 一律一句话提示
- 用户说"不用"立刻跳过
- 推荐不是强制，不得把用户拖入新的工作流
- 上游技能负责主动提示，下游技能负责承接执行
- 不要出现下游说"应该由上游推荐"、上游却没有动作的漂移

---

## 4. 收尾提交（scoped-commit）

feature-acceptance 和 issue-fix 走完后要把本次产物提交为一个 commit。规则：

- **提交范围**：本次工作改到的代码 + 相关 spec 文档 + 本次实际更新过的架构 doc
- **不该进这个 commit**：和本次工作无关的顺手修改；属于"下次另起一个 feature / issue"的扩大范围
- **提交前确认**：用户没明确同意就不要 `git commit`
- **commit message**：一句话说清楚"这次做了什么"，不要把 spec 目录路径贴进 message

子技能只描述本阶段的特有提交范围（比如 acceptance 要带架构 doc），通用规则看这里。

---

## 5. 归档检索规则

feature-design / issue-analyze / issue-fix 在动手前要到 `easysdd/compound/` 里搜已有的沉淀：

- 总是先搜 `architecture/` 和 `compound/` 两个目录
- 在 `compound/` 里用 `doc_type` 字段按需过滤（learning / trick / decision / explore）
- 搜到的结果只作为参考输入，不盲目套用——可能已过期（`status=outdated`）或不适合当前上下文
- 搜到和当前方向冲突的 decision → 必须在方案 / 分析里正面回应"为什么仍然要这么做"或调整方向

子技能只补充本阶段的具体查询命令。完整搜索语法看 `easysdd/reference/tools.md`。

---

## 6. 归档类子技能共享守护规则

`easysdd-learning` / `easysdd-tricks` / `easysdd-decisions` / `easysdd-explore` 四个子技能共享下面这组规则。各子技能的正文只写本技能特有反模式，通用规则看这里：

1. **只增不删**——已归档的文档除非被明确取代（`status=superseded`），否则不删除；理由丢失的成本极高
2. **宁缺毋滥**——用户说不出理由的节直接省略，不要 AI 编造听起来合理的内容
3. **不替用户写实质内容**——AI 负责起草结构和串联语言，实质结论必须来自用户或可追溯的代码证据
4. **可发现性检查**——写完后检查 `AGENTS.md` / `CLAUDE.md` 里有没有指引 AI 查阅 `easysdd/compound/`，没有就**提示**用户（不替用户改）
5. **归档后查重叠**——写完后用 `search-yaml.py --query` 查语义重叠的旧文档，有重叠就在新文档末尾 `相关文档` 节列出来，提示用户确认是否合并或 supersede

各子技能只认自己的 `doc_type`，不读写别家产物。