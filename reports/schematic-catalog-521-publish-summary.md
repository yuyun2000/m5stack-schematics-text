# 521 产品原理图描述发布汇总

生成时间：2026-07-20

## 结论

`state/product_manifest.json` 中的 521 个产品已经全部完成原理图资源获取、结构化事实生成、本地校验、确定性 Markdown 渲染、自动分发和幂等复跑。三个固定批次分别达到 `100/100`、`200/200`、`208/208 complete`，另有 13 个批次启动前基线产品；四组产品 ID 互不重复，合计正好覆盖清单全部产品。

全项目共提取 6,205 个主要器件和 10,366 条硬件事实，其中 8,430 条为 `confirmed`、1,936 条为 `uncertain`，保留 1,957 条 `needs_review` 记录。每个 uncertain 事实均有对应待确认记录；待确认内容不阻塞自动发布，也未被混入确定事实。

## 覆盖统计

| 范围 | 产品 | 器件 | 事实 | confirmed | uncertain | needs_review | 状态 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 批次前基线 | 13 | 192 | 228 | 220 | 8 | 8 | complete |
| `schematic-rich-100-2026-07-17` | 100 | 1,314 | 1,742 | 1,547 | 195 | 216 | `100/100 complete` |
| `schematic-rich-200-2026-07-17` | 200 | 2,258 | 3,679 | 3,046 | 633 | 633 | `200/200 complete` |
| `schematic-rich-remaining-208-2026-07-19` | 208 | 2,441 | 4,717 | 3,617 | 1,100 | 1,100 | `208/208 complete` |
| 合计 | 521 | 6,205 | 10,366 | 8,430 | 1,936 | 1,957 | `521/521` |

## 输入快照

| 文件 | SHA-256 |
| --- | --- |
| `state/product_manifest.json` | `1c293a2e1e3ec4ccfc7856509eaddee9069508cb1c3450361126b0b6c054d78a` |
| `state/description_batch_100.json` | `3594a34742453ec0a30adcb34f21cff9896fe283872393b2786defef9e9b973d` |
| `state/description_batch_200.json` | `c964f16b617a98ce52e43739621012037be23a6089b29cc970e4652c28562bb2` |
| `state/description_batch_208.json` | `ee01abab9b78da8cd6adafa6d1b143b77d89925ad6b6e29dcea0e5f92e43d849` |

## 资源与发布

- 521 份 `asset_manifest.json` 可解析，共记录 905 个原理图资源、908 个本地页面，总资源字节数 909,947,971。
- `artifacts/facts/` 包含 521 份 JSON，产品 ID 与清单一一对应，无缺失、无额外 ID、无 JSON 解析失败。
- 521 份独立发布报告均为 `published=1`、`failed=0`、`status=valid`，并且最终动作均为 `unchanged/unchanged`。
- 清单对应的 521 对 `generated_docs/` 与 `zh_CN/schematic/` Markdown 字节一致，无缺失或哈希差异。
- 两个 Markdown 目录各有 526 份文件；多出的 5 份为保留的历史命名别名：`Atom Echo.md`、`Atom EchoS3R.md`、`Atomic Echo Base.md`、`Module13.2 ODrive.md`、`Unit RFID-UHF.md`。它们不属于当前清单产品，不计入 521 产品覆盖。
- `backups/published/` 中共有 431 份内容寻址备份，文件内容 SHA-256 全部与文件名一致。
- 三个批次的 claims 文件均为空，无活动或持久化历史租约。

## 验收结果

- `python '.\scripts\manage_description_batch.py' verify --batch '.\state\description_batch_208.json'` 通过，返回 `208/208 complete`、`remaining=0`、`active_leases=0`。
- `python '.\scripts\publish_descriptions.py' --all --dry-run --report '.\reports\schematic-catalog-521-dry-run.json'` 返回 `published=521`、`failed=0`；521 项均为 `draft_action=unchanged`、`publish_action=unchanged`。
- `python -m unittest -v` 返回 22/22 通过。
- 1,936 条 uncertain 事实全部存在关联的 `needs_review`；额外 21 条 review 来自早期基线的非 uncertain 风险记录，不影响事实契约。
- facts、生成 Markdown、发布 Markdown 和独立报告共检查 2,094 个文件，均可严格解码为 UTF-8，且无 BOM。
- 521 对 Markdown、521 份报告、431 份备份及全部 claims 均通过独立交叉审计。

## 回滚与边界

发布器在覆盖旧文档前按旧内容 SHA-256 建立备份；需要回滚时恢复 `backups/published/<product_id>/<sha256>.md`，不修改 facts JSON。原理图与源文档版本冲突、型号后缀、地址、容量、性能、机械参数和固件行为等无法从图面确认的内容，均保留在各产品 Markdown 的“待确认事项”中。

历史源文件可能保留既有 BOM 或命名问题以维持固定批次的源 SHA-256，例如 `zh_CN/module/Module GPS v2.0.md` 和部分早期源文档；本次生成的 facts、报告及发布 Markdown 均不继承这些编码问题。
