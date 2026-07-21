# M5Stack 原理图描述流水线

本项目从 M5Stack 中文产品文档提取原理图链接，建立可追溯的产品与资源清单，并由 Codex 项目级 `schematic_describer` 子智能体生成结构化硬件事实。事实通过本地校验后，流水线直接生成内容丰富、便于其他智能体检索的 Markdown，并同步分发到 `zh_CN/schematic/`。

无法从原理图确定的内容不会被猜测补全，也不会阻塞发布。它们必须以 `uncertain` 事实和关联的 `needs_review` 记录保存，最终统一显示在 Markdown 的“待确认事项”章节。

## 目录

```text
.codex/agents/schematic-describer.toml  单产品原理图分析子智能体
scripts/                                清单、抓取、校验、渲染、发布脚本
schemas/                                结构化硬件事实 JSON Schema
state/product_manifest.json             产品、源文档和原理图 URL 清单
state/description_batch_100.json         已完成的首批 100 产品固定批次
state/description_batch_200.json         已完成的第二批 200 产品固定批次
state/description_batch_208.json         已完成的其余 208 产品固定批次
state/description_batch_*.claims.json    本地运行时派单租约，不进入版本控制
artifacts/schematics/                   已下载并校验的原理图资源
artifacts/facts/                        子智能体结构化事实输出
reports/                                校验、试点和发布报告
generated_docs/                         自动生成的 Markdown 镜像
zh_CN/schematic/                        对外分发的原理图描述
backups/published/                      被替换发布文档的内容寻址备份
downloaded_images/                      旧流水线图片缓存，仅作历史参考
tests/                                  不访问网络的单元测试
```

## 仓库存储边界与克隆

GitHub 仓库为 `https://github.com/yuyun2000/m5stack-schematics-text`。当前版本控制范围包含流水线代码、schema、测试、产品源文档、产品清单、固定批次、结构化事实、发布报告，以及 `generated_docs/` 和 `zh_CN/schematic/` 中的可检索 Markdown。

以下内容只保留在本机，不进入新的提交：

- `artifacts/schematics/`：从正式 URL 重新下载并渲染的原理图资源；
- `backups/`：发布器在本地生成的内容寻址回滚副本；
- `state/*.claims.json`：父智能体运行时租约，缺失时按空租约处理；
- Python 缓存、虚拟环境、日志和临时文件。

远端早期提交已经包含 `downloaded_images/` 旧图片缓存。为保留既有历史，本次不批量删除这些对象；新流水线不读取该目录，也不得继续更新或新增其中的文件。需要轻量工作区时使用部分克隆和稀疏检出，避免下载旧图片 blob：

```powershell
git clone --filter=blob:none --sparse 'https://github.com/yuyun2000/m5stack-schematics-text.git'
Set-Location '.\m5stack-schematics-text'
git sparse-checkout set '.codex' 'artifacts/facts' 'docs' 'generated_docs' 'reports' 'schemas' 'scripts' 'state' 'tests' 'zh_CN'
python -m pip install -r '.\requirements.txt'
python -m unittest -v
```

稀疏检出仍会包含仓库根目录的 README、AGENTS、清单导出和兼容入口。严格校验某个产品前，必须从当前清单重新建立本地资源，不能用 `downloaded_images/` 判断资源是否最新：

```powershell
python '.\scripts\fetch_schematics.py' --product-id '<product_id>'
```

## 当前覆盖范围

截至 2026-07-20：

- 产品清单包含 521 个产品；`artifacts/schematics/`、`artifacts/facts/` 和清单产品的富文本 Markdown 均为 `521/521` 覆盖。
- `state/description_batch_100.json`、`state/description_batch_200.json`、`state/description_batch_208.json` 分别为 `100/100`、`200/200`、`208/208 complete`，三批产品 ID 无交集；另有批次前 13 份结构化事实。
- 全项目共有 6,205 个主要器件和 10,366 条硬件事实，其中 8,430 条 `confirmed`、1,936 条 `uncertain`，保留 1,957 条待确认记录。完整统计见 `reports/schematic-catalog-521-publish-summary.md`。
- `generated_docs/` 与 `zh_CN/schematic/` 各有 526 份 Markdown：521 份对应当前产品清单，另外 5 份是保留的历史命名别名；521 对清单文档字节一致。
- `publish_descriptions.py --all` 只发布 `artifacts/facts/` 中已经存在的事实 JSON。目前这些事实恰好覆盖全部 521 个产品，但该命令本身不会为缺失产品自动调用模型生成事实。

项目当前不包含无人值守的模型批处理驱动器。父智能体按产品维持任务队列；每个 `schematic_describer` 子智能体闭环完成事实 JSON、校验、确定性 Markdown 和单产品发布，父智能体只做编排、批次验收和失败重试。

三个固定批次均已完成。状态必须从真实产物派生，不依赖聊天记录：

```powershell
python '.\scripts\manage_description_batch.py' status
python '.\scripts\manage_description_batch.py' status --batch '.\state\description_batch_200.json'
python '.\scripts\manage_description_batch.py' status --batch '.\state\description_batch_208.json'
```

## 环境

```powershell
python -m pip install -r '.\requirements.txt'
python -m unittest -v
```

PDF 原理图优先使用依赖文件中的 PyMuPDF 渲染；系统 `pdftoppm` 仅作为备用路径。

## 1. 构建产品清单

先预览统计，不写文件：

```powershell
python '.\scripts\build_product_manifest.py' --dry-run --no-legacy-exports
```

确认源文档范围正确后生成 `state/product_manifest.json`，并兼容更新 CSV/XLSX：

```powershell
python '.\scripts\build_product_manifest.py'
```

`python '.\get_pdf.py'` 是同一命令的兼容入口。

## 2. 获取原理图

单产品下载会校验文件类型、大小和 SHA-256，不会上传任何数据：

```powershell
python '.\scripts\fetch_schematics.py' --product-name '485T'
```

同名产品必须使用清单中的 `product_id`。全量获取必须同时提供 `--all --confirm-all`。

## 3. 生成结构化事实

在 Codex 中使用 `schematic_describer` 子智能体处理一个 `product_id`。每个任务必须读取：

- `state/product_manifest.json` 中的单个产品条目；
- `artifacts/schematics/<product_id>/asset_manifest.json`；
- `schemas/schematic-description.schema.json`；
- 资源清单列出的全部本地原理图页面。

子智能体先写父智能体为当前任务指定的单个事实文件：

```text
artifacts/facts/<product_id>.json
```

写入后子智能体必须运行本地校验，再使用独立报告路径执行单产品发布：

```powershell
python '.\scripts\publish_descriptions.py' --facts '.\artifacts\facts\<product_id>.json' --report '.\reports\<product_id>-publish.json'
```

它只能写当前产品的事实、生成/发布 Markdown、备份目录和独立报告，无权修改其他产品或共享发布报告。父智能体只负责任务编排、汇总校验和失败重试。

输出应覆盖主要器件、电源、接口、总线、地址、时钟、复位、存储、音频、传感器、射频、调试和模拟链路等与该产品有关的事实。每条器件和事实都要带资源 SHA-256、页码及可定位的区域、位号或网络名。

## 4. 校验并自动发布 Markdown

单独校验一份结构化事实：

```powershell
python '.\scripts\validate_description.py' '.\artifacts\facts\<product_id>.json' --report '.\reports\<product_id>-validation.json'
```

预览所有待发布结果：

```powershell
python '.\scripts\publish_descriptions.py' --all --dry-run
```

正式自动发布：

```powershell
python '.\scripts\publish_descriptions.py' --all
```

也可用一个或多个 `--facts` 只发布指定产品。发布器会依次完成本地 schema、清单、资源哈希和证据页校验，渲染 Markdown，并同时写入 `generated_docs/` 与 `zh_CN/schematic/`。替换已有发布文件前，旧内容按 SHA-256 备份到 `backups/published/<product_id>/`。

校验会拒绝清单或哈希不匹配、无效证据页、重复事实 ID、未关联待确认项的 `uncertain` 事实，以及包含推测措辞的 `confirmed` 事实。有效的不确定项不会阻塞发布，而是进入“待确认事项”。相同输入重复执行应返回 `unchanged`。

## Markdown 输出结构

发布文档面向其他智能体的直接文本检索，固定提供：

- 快速信息、概述和检索关键词；
- 主要器件与分类后的硬件事实；
- 事实属性、网络、参数与信号索引；
- 待确认事项；
- 源文档、原理图 URL、页码和 SHA-256 证据。

项目不维护额外查询函数或查询索引；检索方直接读取 `zh_CN/schematic/*.md`。

## 安全与回滚

- 子智能体只闭环处理被分配的单个产品，并通过确定性脚本写 Markdown、备份和独立报告；父智能体不人工编写 Markdown。
- 不把产品文档或原理图上传到外部服务。
- 批量下载需要显式 `--all --confirm-all`；自动发布只处理已经存在且通过校验的事实 JSON。
- 发布前自动备份被替换文件；回滚时从对应 `backups/published/<product_id>/<sha256>.md` 恢复。
- 清单、抓取和发布脚本不会自动删除历史图片、事实、Markdown 或备份。

## 中断恢复

批次管理器从本地资源哈希、事实校验、确定性渲染结果和独立发布报告派生状态，不信任手工 `done` 标记。恢复顺序：

```powershell
python '.\scripts\manage_description_batch.py' init --count 100
python '.\scripts\manage_description_batch.py' status
python '.\scripts\manage_description_batch.py' status --batch '.\state\description_batch_200.json'
python '.\scripts\manage_description_batch.py' status --batch '.\state\description_batch_208.json'
python '.\scripts\manage_description_batch.py' fetch --limit 0
python '.\scripts\manage_description_batch.py' publish-ready --limit 0
python '.\scripts\manage_description_batch.py' claim-next --worker pilot_485t --worker pilot_makey --worker pilot_tab5
```

非默认批次的 `fetch`、`publish-ready`、`claim-next`、`release` 和 `verify` 必须显式传入对应 `--batch` 路径，例如 `state/description_batch_200.json` 或 `state/description_batch_208.json`。`init` 对已有批次返回 `UNCHANGED`，不会选择另一组产品。JSON、Markdown、备份和报告均使用同目录临时文件、`fsync` 和原子替换。过期租约不会自动被其他 worker 抢占；父智能体确认旧任务停止后才运行 `release`。最终以目标批次的 `verify` 返回成功且 `complete == target_count` 为完成标准。

## 下一轮增量更新

先同步远端并重建清单。第一次写入后立刻再运行一次，第二次的 `state/product_manifest.json` 必须报告 `UNCHANGED`；兼容 CSV/XLSX 会被重新导出，仍可能显示 `UPDATED`：

```powershell
git pull --ff-only origin main
python '.\scripts\build_product_manifest.py' --dry-run --no-legacy-exports
python '.\scripts\build_product_manifest.py'
python '.\scripts\build_product_manifest.py'
```

新增产品没有对应 `artifacts/facts/<product_id>.json` 时，创建一个新的固定批次。`<count>`、文件名和 `batch-id` 必须替换为本轮实际值，不能覆盖三个已完成批次：

```powershell
python '.\scripts\manage_description_batch.py' init --batch '.\state\description_batch_<YYYY-MM-DD>.json' --count <count> --batch-id 'schematic-rich-<count>-<YYYY-MM-DD>'
python '.\scripts\manage_description_batch.py' fetch --batch '.\state\description_batch_<YYYY-MM-DD>.json' --limit 0
python '.\scripts\manage_description_batch.py' claim-next --batch '.\state\description_batch_<YYYY-MM-DD>.json' --worker worker_1 --worker worker_2 --worker worker_3
```

父智能体把每个回执中的单个 `product_id` 交给 `schematic_describer`。子智能体按本页第 3、4 节完成事实、校验、Markdown 和独立报告闭环；父智能体复核为 `complete` 后释放租约并领取下一项。并发数以当前环境可用 agent 槽位为准，并至少为父智能体保留一个槽位。

既有产品的源文档、原理图 URL 或输入哈希变化时，不删除旧事实来伪装成新增产品。直接按 `product_id` 重新获取资源，再单独派发该产品；发布器会在覆盖 Markdown 前创建本地备份：

```powershell
python '.\scripts\fetch_schematics.py' --product-id '<product_id>'
python '.\scripts\publish_descriptions.py' --facts '.\artifacts\facts\<product_id>.json' --report '.\reports\<product_id>-publish.json'
```

第二条命令必须在子智能体依据新资源重写并校验事实 JSON 之后运行。批次完成后执行：

```powershell
python '.\scripts\manage_description_batch.py' verify --batch '.\state\description_batch_<YYYY-MM-DD>.json'
python '.\scripts\publish_descriptions.py' --all --dry-run
python -m unittest -v
```

验收要求是目标批次全部 `complete`、全量发布预览 `failed == 0` 且所有文档 `unchanged`、测试全部通过。提交时只纳入文本流水线及其确定性产物，不提交本地原理图、租约或备份。
