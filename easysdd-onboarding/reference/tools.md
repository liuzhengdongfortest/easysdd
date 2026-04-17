# easysdd 工具用法参考

本文件由 `easysdd-onboarding` 复制到项目的 `easysdd/reference/tools.md`，所有 easysdd 子技能用项目相对路径 `easysdd/reference/tools.md` 引用。

`easysdd/tools/` 下共享脚本的完整用法参考。子技能里只写本技能特有的 1-2 行典型查询；完整语法和示例看这里。

---

## 1. search-yaml.py

通用 YAML frontmatter 搜索工具。从项目根目录运行，无需安装额外依赖（PyYAML 可选，有则用，无则内建 fallback parser）。

### 基本语法

```bash
python easysdd/tools/search-yaml.py --dir {目录} [--filter key=value]... [--query "全文关键词"] [--full] [--json]
```

### filter 语法

- `key=value`：字段精确匹配（大小写不敏感）
- `key~=value`：字符串字段子串匹配；列表字段元素包含匹配

### 常用命令

沉淀类文档统一在 `easysdd/compound/`，用 `doc_type` 字段区分四个子技能的产物，内部还有各自的细分字段：

```bash
# 按 doc_type 筛选
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=learning
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=decision --filter status=active
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=trick --filter status=active
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=explore --filter status=active

# doc_type + 子技能内部细分字段
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=learning --filter track=pitfall
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=decision --filter category=constraint
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=trick --filter type=pattern
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=explore --filter type=question

# 按 tag（列表元素包含匹配）
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter tags~=prisma

# 全文搜索
python easysdd/tools/search-yaml.py --dir easysdd/compound --query "shadow database"

# 按领域/框架/语言筛选
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=decision --filter area=frontend
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=trick --filter framework~=vue
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=trick --filter language=typescript

# 搜索 feature 方案 doc
python easysdd/tools/search-yaml.py --dir easysdd/features --filter doc_type=feature-design --filter status=approved

# 输出控制
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter doc_type=decision --filter status=active --full
python easysdd/tools/search-yaml.py --dir easysdd/compound --filter tags~=llm --json
```

### 典型使用场景

| 场景 | 命令建议 |
|---|---|
| feature-design 开始前查已有归档 | 搜 `easysdd/compound` 目录，按 `--query "{关键词}"` 全文搜；要分类看就加 `--filter doc_type={learning\|trick\|decision\|explore}` |
| issue-analyze 根因分析前查历史 | 搜 `easysdd/compound` `--filter doc_type=learning --filter track=pitfall`、再搜 `--filter doc_type=trick --filter type=library`，按相关组件/框架过滤 |
| 归档落盘后查重叠 | 搜 `easysdd/compound --query "{关键词}" --json`，看有无语义重叠 |
| 新人了解项目规约 | `--dir easysdd/compound --filter doc_type=decision --filter status=active` |
| 按技术栈浏览技巧 | `--dir easysdd/compound --filter doc_type=trick --filter language={语言} --filter status=active` |

---

## 2. validate-yaml.py

YAML 语法校验工具。用于验证 frontmatter 语法和必填字段。

```bash
# 校验单个文件的 YAML 语法
python easysdd/tools/validate-yaml.py --file {文件路径} --yaml-only

# 校验必填字段
python easysdd/tools/validate-yaml.py --file {文件路径} --require doc_type --require status

# 批量校验目录下所有文件
python easysdd/tools/validate-yaml.py --dir {目录} --require doc_type --require status
```
