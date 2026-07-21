# AGENTS.md

## 项目目标

本项目维护 M5Stack 产品原理图索引、原理图资源、结构化硬件事实、可检索 Markdown 和发布文档。生成流程采用“确定性脚本 + 项目级 `schematic_describer` 子智能体 + 本地校验后自动发布”。

AI 输出是自动发布候选。能够从原理图明确定位的内容写为 `confirmed`；无法确定的内容写为 `uncertain`，并在最终 Markdown 的“待确认事项”章节中明确说明。不得为了消除待确认项而猜测硬件事实。

硬件事实冲突时按以下顺序判断：

1. 当前产品版本的正式原理图、网表或 PCB 设计资料。
2. 芯片官方 datasheet 和 M5Stack 已确认资料。
3. `zh_CN/` 中对应产品源文档。
4. `generated_docs/` 与 `zh_CN/schematic/` 中的历史描述。

默认使用中文。先检查真实文件、图片、清单、哈希和命令输出，再修改或下结论。

## 项目构成

| 路径 | 作用 | 修改边界 |
| --- | --- | --- |
| `.codex/agents/schematic-describer.toml` | 单产品原理图闭环子智能体 | 只处理被分配产品的事实、Markdown、备份和独立发布报告 |
| `scripts/build_product_manifest.py` | 扫描源文档并生成稳定产品清单 | 可生成 JSON/CSV/XLSX |
| `get_pdf.py` | 清单生成器兼容入口 | 不再维护独立实现 |
| `scripts/fetch_schematics.py` | 下载、校验、哈希并渲染原理图 | 只写 `artifacts/schematics/` |
| `scripts/validate_description.py` | 校验结构化事实、证据和清单一致性 | 只读，报告可写 `reports/` |
| `scripts/render_description.py` | 从已验证事实渲染 Markdown | 只写 `generated_docs/` |
| `scripts/publish_descriptions.py` | 校验、渲染、备份并自动分发 Markdown | 写 `generated_docs/`、`zh_CN/schematic/`、备份和报告 |
| `scripts/manage_description_batch.py` | 固定批次、派生进度、获取资源、租约和发布修复 | 父智能体专用；状态来自真实产物 |
| `schemas/schematic-description.schema.json` | 结构化事实契约 | 修改后必须重跑 schema 与单元测试 |
| `state/product_manifest.json` | 产品、源文档和原理图 URL 清单 | 由脚本生成，不手工编辑 |
| `state/description_batch_100.json` | 首批 100 产品固定批次和输入快照 | 已完成；恢复时不得重新选产品 |
| `state/description_batch_200.json` | 第二批 200 产品固定批次和输入快照 | 已完成；与首批产品 ID 无交集 |
| `state/description_batch_208.json` | 其余 208 产品固定批次和输入快照 | 已完成；与前两批及基线 facts 无交集 |
| `state/description_batch_*.claims.json` | 对应批次的父智能体运行时租约 | 本地生成且不提交；缺失时按空租约处理，子智能体禁止修改 |
| `artifacts/schematics/` | 新流水线原理图与资源清单 | 不使用旧缓存判断是否最新 |
| `artifacts/facts/` | 子智能体 JSON 输出 | 保存后必须通过本地校验 |
| `generated_docs/` | 自动渲染的 Markdown 镜像 | 与发布内容保持相同字节 |
| `zh_CN/schematic/` | 已自动分发的原理图描述 | 只由发布脚本写入 |
| `backups/published/` | 被替换发布文档的内容寻址备份 | 按产品 ID 和旧 SHA-256 保存 |
| `downloaded_images/` | 历史图片缓存 | 仅作参考，不参与新流水线状态判断 |
| `tests/` | 无网络单元测试 | 改动流水线后必须通过 |

项目 GitHub 远端为 `https://github.com/yuyun2000/m5stack-schematics-text`，默认分支为 `main`。远端早期历史已经包含旧 `downloaded_images/` 图片缓存；保留历史但不再更新该目录。新提交只维护代码、schema、测试、源文档、清单/固定批次、结构化事实、报告和 Markdown。`artifacts/schematics/`、`backups/`、`downloaded_images/` 与运行时 claims 均为本地数据，不得用 `git add -f` 纳入新提交。

常规同步必须使用正常的 fetch/pull/merge 流程，禁止 force push。远端历史较大时优先 `git fetch --filter=blob:none` 或 README 中的稀疏克隆命令，避免为比较文本改动下载旧图片 blob。

## 当前基线

截至 2026-07-20，`state/product_manifest.json` 的 521 个产品已全部具备结构化事实和富文本描述。首批 `state/description_batch_100.json`、第二批 `state/description_batch_200.json`、其余产品批次 `state/description_batch_208.json` 分别为 `100/100`、`200/200`、`208/208 complete`，三批产品 ID 无交集；另有 13 份批次启动前基线。全项目共记录 6,205 个主要器件、10,366 条硬件事实，其中 8,430 条 `confirmed`、1,936 条 `uncertain`，以及 1,957 条 `needs_review`。完整统计、计划哈希和验收结果见 `reports/schematic-catalog-521-publish-summary.md`。

`publish_descriptions.py --all` 只处理当前已经存在的 `artifacts/facts/*.json`。目前该目录恰好覆盖清单中的全部 521 个产品，但仍不得把 `--all` 表述为会为缺失产品自动调用模型生成事实。当前没有无人值守的模型批处理驱动器；父智能体按单产品调度专用子智能体，每个子智能体完成自己的事实、校验、Markdown 和发布闭环。

## 数据流

```text
zh_CN/**/*.md
  -> build_product_manifest.py
  -> state/product_manifest.json + CSV/XLSX
  -> fetch_schematics.py
  -> artifacts/schematics/<product_id>/asset_manifest.json + 本地页面
  -> schematic_describer 子智能体
  -> artifacts/facts/<product_id>.json
  -> publish_descriptions.py
       -> validate_description.py
       -> render_description.py
       -> generated_docs/<output_filename>
       -> 自动备份旧发布文件
       -> zh_CN/schematic/<output_filename>
```

只有结构化事实通过 schema、产品清单、资源清单、哈希和证据页校验后才能发布。不确定事实不阻塞发布，但必须与 `needs_review` 记录关联并进入“待确认事项”。

## 产品清单规则

- 扫描 `zh_CN/**/*.md`，明确排除 `zh_CN/schematic/`。
- 识别 `## 原理图` 章节；优先图片，只有无图片时才采用 PDF。
- 支持图片/PDF URL 查询参数，保留多个原理图顺序并去重。
- `product_id` 由产品名和源文档相对路径稳定生成；同名产品必须用 ID 操作。
- 清单记录源路径、源 SHA-256、输入 SHA-256、SKU、结构化 URL 和输出文件名。
- 源文档缺少一级标题时使用文件名作为产品名，并写入 `missing_product_titles` 告警。
- 同名输出会添加产品 ID 后缀，禁止静默覆盖。
- 清单输出应确定性生成；相同输入重跑不得改变 JSON 字节。

## 子智能体规则

- 批量生成默认使用 `.codex/agents/schematic-describer.toml` 中的 `model_reasoning_effort = "medium"`；不得通过减少证据页、跳过 schema 校验或省略幂等复跑来换取速度。
- 一次只处理一个清单产品，不接受未经筛选的全量目录。
- 必须读取产品条目、资源清单、事实 schema 和全部本地原理图页面。
- 覆盖与产品相关的主要器件、电源、接口、总线、地址、时钟、复位、存储、内存、音频、传感器、射频、调试和模拟链路。
- 每个 component/fact 必须提供资源 SHA-256、页码和 locator；locator 优先使用页内网格、位号、引脚或网络名。
- 不使用常识补全原理图没有显示的型号、地址、阻值、引脚或连接。
- 不确定事实使用 `confidence="uncertain"`，并添加引用该 fact ID 的 `needs_review`。字段名为结构化契约的兼容名称，渲染标题固定为“待确认事项”。
- `keywords` 应包含产品名、SKU、主要器件、接口、总线、关键网络和常见检索别名。
- 只允许写父智能体指定产品的事实 JSON、同名 `generated_docs/` 与 `zh_CN/schematic/` Markdown、该产品备份目录和 `reports/<product_id>-publish.json`；不得修改其他产品或共享发布报告。
- 写入事实后必须运行本地校验并修正错误，再使用 `publish_descriptions.py --facts ... --report reports/<product_id>-publish.json` 完成单产品闭环；不得使用 `--all`。
- 最终只向父智能体报告路径、事实数量、待确认数量、发布 SHA-256 和校验结果，不回传整份 JSON。
- 父智能体只负责任务队列、并发调度、汇总校验和失败重试，不人工编写 Markdown。
- 批次任务中子智能体不得修改 `state/description_batch_*.json` 或对应 claims 文件；父智能体收到完成回执并复核状态后才释放租约。

## Markdown 内容规则

- 内容面向其他智能体直接读取和全文检索，不建立额外查询函数。
- 必须包含快速信息、概述、检索关键词、主要器件、分类事实、参数与信号索引、待确认事项和证据来源。
- 器件型号、位号、网络名、引脚、电压、阻值、地址、频率和接口名称尽量保留原理图原文，便于精确查询。
- `confirmed` 与 `uncertain` 内容必须分开；待确认内容不得混入确定事实段落。
- 每份文档都要记录源文档 SHA-256、原理图 URL 和资源 SHA-256，保证可追溯。

## 标准操作

### 1. 测试

```powershell
python -m unittest -v
```

### 2. 生成清单

先 dry-run：

```powershell
python '.\scripts\build_product_manifest.py' --dry-run --no-legacy-exports
```

确认统计和告警后再写文件：

```powershell
python '.\scripts\build_product_manifest.py'
```

### 3. 获取原理图

```powershell
python '.\scripts\fetch_schematics.py' --product-name '<产品名>'
```

同名产品改用 `--product-id`。全量获取必须显式使用 `--all --confirm-all`。命令只下载，不上传数据。

### 4. 自动校验、生成与分发

先预览所有已有事实文件：

```powershell
python '.\scripts\publish_descriptions.py' --all --dry-run
```

正式发布全部通过校验的事实文件：

```powershell
python '.\scripts\publish_descriptions.py' --all
```

指定产品时传入一个或多个 `--facts '.\artifacts\facts\<product_id>.json'`。并行子智能体必须各自传入 `--report '.\reports\<product_id>-publish.json'`，避免争写共享报告。单产品失败不得影响其他产品。

### 5. 可恢复批次

固定批次；重复运行不会重新选择产品：

```powershell
python '.\scripts\manage_description_batch.py' init --count 100
python '.\scripts\manage_description_batch.py' status
python '.\scripts\manage_description_batch.py' status --batch '.\state\description_batch_200.json'
python '.\scripts\manage_description_batch.py' status --batch '.\state\description_batch_208.json'
```

恢复时按顺序修复资源和已生成但未完整发布的产品：

```powershell
python '.\scripts\manage_description_batch.py' fetch --limit 0
python '.\scripts\manage_description_batch.py' publish-ready --limit 0
python '.\scripts\manage_description_batch.py' fetch --batch '.\state\description_batch_200.json' --limit 0
python '.\scripts\manage_description_batch.py' publish-ready --batch '.\state\description_batch_200.json' --limit 0
```

父智能体使用固定 worker 名领取或续租；同一 worker 重启后会返回原产品：

```powershell
python '.\scripts\manage_description_batch.py' claim-next --worker pilot_485t --worker pilot_makey --worker pilot_tab5
python '.\scripts\manage_description_batch.py' claim-next --batch '.\state\description_batch_200.json' --worker medium_485t --worker medium_makey --worker medium_tab5
```

任务完成并复核为 `complete` 后释放对应租约，再领取下一项：

```powershell
python '.\scripts\manage_description_batch.py' release --product-id '<product_id>'
python '.\scripts\manage_description_batch.py' verify
python '.\scripts\manage_description_batch.py' verify --batch '.\state\description_batch_200.json'
python '.\scripts\manage_description_batch.py' verify --batch '.\state\description_batch_208.json'
```

租约过期只告警，不自动允许其他 worker 抢占。只有父智能体确认旧 worker 已停止后才能显式释放，避免迟到结果覆盖新任务。完整设计和中断矩阵见 `docs/plans/2026-07-17-resumable-schematic-batch-design.md`。

### 6. 下一轮增量更新

1. `git pull --ff-only origin main` 后先运行清单 dry-run，再正式生成清单并复跑到 `state/product_manifest.json` 为 `UNCHANGED`。兼容 CSV/XLSX 重新导出时仍可能显示 `UPDATED`，不作为 JSON 幂等失败。
2. 新增产品使用新的 `state/description_batch_<YYYY-MM-DD>.json` 和唯一 `batch-id` 固定批次；不得覆盖三个已完成批次。`init` 只选择缺少 facts 且包含原理图的产品。
3. 既有产品输入发生变化时，不删除旧 facts 来绕过选择规则。按 `product_id` 重新获取资源，直接将该产品交给子智能体重写事实并单产品发布；旧 Markdown 由发布器自动备份。
4. 父智能体只负责任务队列、并发、租约、回执复核和失败重试。并发数以当前 Codex agent 槽位为准，至少保留一个槽位给父智能体。
5. 新批次的 `fetch`、`claim-next`、`release`、`publish-ready` 和 `verify` 每次都必须显式传入同一个 `--batch` 路径。
6. 完成后运行新批次 `verify`、全量发布 dry-run 和单元测试，再检查 UTF-8/BOM、提交文件体积和敏感信息。

新批次示例：

```powershell
python '.\scripts\manage_description_batch.py' init --batch '.\state\description_batch_<YYYY-MM-DD>.json' --count <count> --batch-id 'schematic-rich-<count>-<YYYY-MM-DD>'
python '.\scripts\manage_description_batch.py' fetch --batch '.\state\description_batch_<YYYY-MM-DD>.json' --limit 0
python '.\scripts\manage_description_batch.py' claim-next --batch '.\state\description_batch_<YYYY-MM-DD>.json' --worker worker_1 --worker worker_2 --worker worker_3
python '.\scripts\manage_description_batch.py' verify --batch '.\state\description_batch_<YYYY-MM-DD>.json'
```

命令中的尖括号是占位符，运行前必须替换为实际日期和数量。完整操作说明以 README 的“下一轮增量更新”为准。

## 验收标准

- 所有单元测试通过，JSON Schema 与 TOML 可解析。
- 清单相同输入连续运行两次，第二次 JSON 为 `UNCHANGED`。
- 每个资源文件类型、大小和 SHA-256 已验证；PDF 每页已渲染并入清单。
- 每个结构化事实通过 schema、产品清单、资源清单和证据页校验。
- `confirmed` 事实不包含推测措辞；每个 `uncertain` 事实都有对应待确认记录。
- `generated_docs/` 与 `zh_CN/schematic/` 中同产品文件 SHA-256 一致。
- 相同事实输入重跑发布器显示 `unchanged`；替换发布文件时存在旧 SHA-256 备份。
- Python、JSON、TOML、Markdown 均为严格 UTF-8；解析文件无 BOM，关键中文未变成 `?`。
- Git 暂存区不包含大于 100 MB 的文件，不包含凭据、本地原理图缓存、运行时租约或备份；推送后 `HEAD...origin/main` 为 `0 0`。

## 安全与回滚

- 不在代码、配置、日志或回复中写入凭据。
- 不把产品文档或原理图上传到外部服务，除非用户明确授权范围和目标。
- 不删除或批量移动历史缓存、事实、发布文档、索引或备份，除非用户明确授权并确认绝对路径。
- `fetch_schematics.py` 不自动删除历史目录；新资源写入独立 `artifacts/`。
- 子智能体只能闭环处理被分配的单个产品；自动发布器只处理通过严格校验的本地事实 JSON。
- 发布器在覆盖目标前按旧 SHA-256 创建备份；回滚时恢复对应备份，不修改事实 JSON 伪造旧状态。

## 交付要求

每次更新说明：产品和硬件版本、源文档与原理图 SHA-256、已确认和待确认事实、Markdown 生成/分发状态、验证结果、失败项和回滚点。
