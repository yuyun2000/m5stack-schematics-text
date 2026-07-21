# 原理图描述新增 200 产品批次扩展设计

日期：2026-07-17

## 目标

先完成当前 `state/description_batch_100.json` 中剩余产品并通过 `verify`，再新增一个固定、非重叠的 200 产品批次。两个批次均可在父智能体、子智能体、网络或机器中断后从磁盘状态恢复。

批量子智能体的推理档位由 `high` 下调为 `medium`。速度优化只来自推理档位和持续补位，不允许减少原理图页面读取、证据定位、结构化校验、自动发布或幂等复跑。

## 方案选择

1. 把现有 100 产品批次直接扩为 300：会改变已经冻结的产品集合和输入快照，破坏恢复语义，不采用。
2. 完成当前批次后创建独立 `state/description_batch_200.json`：保留第一批历史，第二批初始化时根据已存在的 facts 排除已完成产品，采用。
3. 引入数据库或常驻队列：并发能力更强，但当前只有三个子智能体槽位，运维和迁移成本没有收益，不采用。

## 执行顺序

1. 当前批次保持 `state/description_batch_100.json` 不变，使用三个固定 worker 继续处理到 `100/100 complete`。
2. 运行当前批次 `verify` 和全量单元测试。
3. 仅在当前 100 个产品全部存在有效 facts 后初始化第二批：

```powershell
python '.\scripts\manage_description_batch.py' init --batch '.\state\description_batch_200.json' --count 200 --batch-id 'schematic-rich-200-2026-07-17'
```

4. 验证两个批次的 `product_id` 交集为空，并记录第二批计划 SHA-256。
5. 获取并校验第二批全部资源；失败项保留在 `needs_fetch` 或 `assets_invalid`，不得开始错误产品的事实生成。
6. 三个 `medium` 子智能体逐产品执行事实、校验、Markdown、发布和幂等闭环；父智能体只管理租约、补位、确定性发布修复和批次验收。
7. 第二批达到 `200/200 complete` 后运行 `verify`、全量单元测试、UTF-8/备份/报告/双 Markdown 哈希验收并生成汇总报告。

## 恢复与并发

- 当前 100 批次和新增 200 批次使用各自的 plan 与 claims 文件，不能共享租约。
- 第二批只在第一批完成后初始化，否则尚无 facts 的第一批产品可能再次成为候选。
- 旧 worker 停止后，父智能体必须显式释放其未完成租约，再把同一产品分配给新 worker。
- 当前运行环境仍是父智能体加三个子智能体，共四个并发槽；降低推理档位不改变并发上限。

## 验收

- `.codex/agents/schematic-describer.toml` 可解析，推理档位为 `medium`。
- 单元测试覆盖第二批排除第一批已有 facts 的行为。
- 当前批次 `verify` 返回成功后才存在 `description_batch_200.json`。
- 第二批固定 200 个唯一产品，且与第一批 `product_id` 交集为 0。
- 两个批次最终分别为 `100/100 complete` 与 `200/200 complete`。
- 每个产品的 facts、资源证据、独立发布报告、生成稿、发布稿和内容寻址备份满足项目 `AGENTS.md` 的验收规则。
