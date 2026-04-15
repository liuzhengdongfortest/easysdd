# easysdd reference

本目录存放 easysdd 技能家族共享的参考材料。原则：流程骨架留在各个 `SKILL.md`；模板、长示例、工具手册、维护说明放到这里。

## 当前文件

- `shared-conventions.md`：共享元数据口径、`checklist.yaml` 生命周期、收尾推荐
- `tools.md`：`search-yaml.py` / `validate-yaml.py` 的完整用法
- `maintainer-notes.md`：断点恢复和维护扩展说明
- `feature-design-reference.md`：`design.md` / `checklist.yaml` 模板与 review 提示
- `libdoc-reference.md`：manifest、条目文档模板、源码提取清单
- `tricks-reference.md`：技巧文档模板与示例
- `decisions-reference.md`：决策文档模板与示例
- `onboarding-reference.md`：`DESIGN.md` 与 `AGENTS.md` 骨架模板
- `issue-fix-reference.md`：修复汇报、日志调试、`fix-note.md` 模板
- `compound-reference.md`：pitfall / knowledge 两条轨道模板
- `explore-reference.md`：探索文档结构、写法说明、路由表

## 使用规则

- 共享说明优先放这里，不继续堆到根技能里
- 子技能里引用这里的文件名，不写脆弱的“见根技能第 X 节”
- 新增 reference 文件时，同时更新本索引和根技能目录安排