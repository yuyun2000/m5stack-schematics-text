# 十产品原理图描述自动发布摘要

生成时间：2026-07-17

## 结论

本批 10 个产品均由专用子智能体完成单产品闭环：读取全部本地原理图页面、生成结构化事实、本地校验、确定性 Markdown 渲染、旧版备份、自动发布和幂等重跑。父智能体只负责任务编排与批次级验收，没有人工编写单份 Markdown。

批次共提取 163 个主要器件和 188 条硬件事实，其中 181 条为 `confirmed`、7 条为 `uncertain`。7 条不确定事实均有关联待确认项并进入发布文档“待确认事项”，没有阻塞其余事实发布。

## 发布结果

| 产品 | 事实 | confirmed | uncertain / 待确认 | 发布 SHA-256 |
| --- | ---: | ---: | ---: | --- |
| Module LTE | 21 | 21 | 0 / 0 | `0d00c7c2ec5b14a7f2915639a5ab7bbb4131662da60024104721a3eca1808634` |
| Atomic CAN Base | 19 | 19 | 0 / 0 | `ea4109e8d84d8444749192dff4748fae7c469f021625fa29d720e2954878c4c6` |
| Atomic RS485 Base | 20 | 19 | 1 / 1 | `7b6c9cb0bbd3af45160fdd98a2cf406fdab28cbe5d953a95f6d0e409b55fe6bf` |
| Unit Mini CAN | 18 | 18 | 0 / 0 | `57f983dd576c22c8ee47db9e15d58008a173892d815a3f99a114cb5ba6dd8e0a` |
| Unit INA226-1A | 19 | 19 | 0 / 0 | `d66bc7b94d200284b20e0ee7fbdbed155b861af043d920d07e92a30cadc0850e` |
| Unit INA226-10A | 25 | 24 | 1 / 1 | `d7ca7813656777d7d0ab36929d3e6708197329a09c6c5ae1741ea042cc4d4853` |
| Unit ENV-IV | 14 | 12 | 2 / 2 | `778ffb40e3e60d6223784ce5b393a6889ec3589e0cfc030c832bb6728a294b47` |
| Unit RTC | 13 | 11 | 2 / 2 | `59823a4460bfc1e85ed07c1f462c70a177a89b6d061d16dd728f4f26bd411513` |
| Stamp-S3 | 19 | 19 | 0 / 0 | `306f3bc76f5b0564e1b4c6c5e1c603803dfb2ad9c1a61ab1ffa0e9417c32ecb5` |
| AtomS3-Lite | 20 | 19 | 1 / 1 | `2508d9040fade15c49163ea581d55cfa53ad7bb91619f50497c60d6cbda76bdf` |

## PDF 结论

Module LTE 使用清单中的当前原理图地址：

`https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Modules/module_lte_sch.pdf`

本次重新请求远端资源后，下载内容与本地已验证 PDF 完全一致，抓取脚本返回 `UNCHANGED`。PDF 大小为 689812 字节，SHA-256 为 `2a5aa3d243864df9f47ccaf015a81286e51c9746d8e2fd30c542cbe2ed8ff1ed`，4 页渲染文件的哈希也全部匹配资源清单。因此不需要下载或保留另一份“新 PDF”；继续复用当前内容寻址文件即可。只有产品输入/URL 变化、显式刷新得到不同 SHA-256，或本地文件校验失败时才替换。

## 编排与并发

每个子智能体只处理一个产品，并使用独立的 `reports/<product_id>-publish.json`，因此事实、Markdown 和报告不会并发争写。当前运行环境共有 4 个并发槽，父智能体占用 1 个，最多同时运行 3 个子智能体；该限制不能在项目文件中提高到 5 个。父智能体采用连续补位队列，让三个子智能体槽保持工作。

## 验收

- 10/10 事实 JSON 通过 schema、产品清单、资源清单、哈希和证据页校验。
- 10/10 `generated_docs/` 与 `zh_CN/schematic/` 文件字节一致，发布 SHA-256 与独立报告一致。
- 10/10 文档包含快速信息、检索关键词、待确认事项和原理图来源。
- 10/10 独立发布报告为 `failed: 0`，相同输入重跑为 `unchanged`。
- 9 个被替换的历史文档已按旧 SHA-256 备份；Module LTE 为新增发布文件。
