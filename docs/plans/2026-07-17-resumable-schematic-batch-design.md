# 可恢复原理图描述批处理设计

日期：2026-07-17

## 需求

固定更新 100 个尚未迁移的产品。任务可能因 Codex 会话、子智能体、网络、进程或机器中断而停止；恢复后必须保留已获取资源、已验证事实、已发布 Markdown 和备份，只重做缺失或无效的单产品阶段。三个子智能体并行处理不同产品，不能争写共享报告。

## 方案比较

1. 只在一个 JSON 中维护人工更新的 `pending/running/done`。实现简单，但状态容易与真实文件漂移，半写或漏写 `done` 会造成重复工作。
2. 使用固定批次计划，并从资源、事实、Markdown 和独立报告派生实时状态；另用带 TTL 的小型租约文件防止重复派单。无需外部服务，状态可由磁盘事实重建。
3. 引入数据库和常驻任务队列。并发控制更强，但对当前单机、三个子智能体的规模属于过度设计，并增加新的恢复依赖。

采用方案 2。

## 持久状态

`state/description_batch_100.json` 固定 100 个 product_id、顺序和输入快照。再次执行 `init` 不重新选产品，也不静默更新源哈希；当前 manifest 与快照不同时标记为 `stale_input`，必须显式处理后才能继续。所有状态均由以下文件计算：

```text
asset_manifest + 本地资源哈希
  -> needs_fetch / assets_invalid / ready_for_analysis
facts JSON + schema/证据校验
  -> facts_invalid / ready_to_publish
rendered Markdown + 发布 Markdown + 单产品报告
  -> complete
```

`state/description_batch_100.claims.json` 只保存父智能体派单租约。租约默认 180 分钟；过期只产生告警，不允许其他 worker 自动抢占。重启后使用相同 worker 名调用 `claim-next` 会续租并返回原任务；只有任务完成或父智能体确认旧 worker 已停止后显式释放，产品才可重新派发。

## 原子性与幂等

JSON、Markdown、发布报告和备份先写入目标目录中的临时文件，`fsync` 后用 `os.replace` 原子替换。资源清单最后写入；若下载或 PDF 渲染中断，状态检查会发现缺失/哈希不符并只重新获取该产品。事实半写会进入 `facts_invalid`；发布在草稿与目标之间中断会进入 `ready_to_publish`，确定性发布器可安全重跑。备份按旧 SHA-256 命名，重复执行不会产生副本。

## 并发边界

当前环境共有 4 个槽位，父智能体占 1 个，因此三个子智能体使用固定 worker 名连续补位。子智能体只闭环处理租约指定的单个产品，并写独立 `reports/<product_id>-publish.json`。父智能体负责 `claim-next`、最终释放和批次校验，不允许子智能体并发修改共享 claims 文件。

## 恢复顺序

1. 重新运行 `init`，确认固定产品集合和输入快照未变化。
2. 运行 `status` 查看真实阶段和未过期租约。
3. 运行 `fetch` 修复 `needs_fetch/assets_invalid`。
4. 运行 `publish-ready` 修复已有效但未完整发布的产品。
5. 用相同 worker 名运行 `claim-next`，恢复原租约或领取下一产品。
6. 全部完成后运行 `verify`，只有 100/100 为 `complete` 才通过。

## 失败验证矩阵

| 中断点 | 磁盘表现 | 恢复行为 |
| --- | --- | --- |
| 资源下载中 | 无清单或源文件哈希不符 | `fetch` 重取单产品 |
| PDF 渲染中 | 页面缺失/哈希不符 | `fetch` 重渲染单产品 |
| 事实写入中 | JSON 无法解析 | `facts_invalid`，原任务重派 |
| 草稿写入中 | 原文件或新文件二选一 | `publish-ready` 原子重写 |
| 发布写入中 | 草稿/发布哈希不一致 | `publish-ready` 修复 |
| 报告写入前 | Markdown 正确但报告缺失 | `publish-ready` 生成独立报告 |
| 父智能体中断 | 租约仍在 | 同 worker 恢复；TTL 后可重派 |
