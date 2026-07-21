# 原理图子智能体试点发布摘要

生成时间：2026-07-17

## 结论

三个代表产品均已完成原理图资源校验、结构化事实生成、本地规则校验、丰富 Markdown 渲染和自动分发。校验通过后直接发布；无法由原理图确定的内容写入文档“待确认事项”章节。

## 发布结果

| 产品 | product_id | 发布文件 | 发布 SHA-256 | 待确认事项 | 状态 |
| --- | --- | --- | --- | ---: | --- |
| 485T | `485t-ba3491b476d0` | `zh_CN/schematic/485T.md` | `afc76579ab7f5b3e62ad82b9bceee7899e757fb610f2edd37991dea84836320a` | 0 | 已发布 |
| 16-Key Capacitive Touch | `16-key-capacitive-touch-ff4446a15faf` | `zh_CN/schematic/16-Key Capacitive Touch.md` | `d647fe5ed42873d865ae65ec0e556b21d6d3708d8bf3f4f24b4779c8a9b632c6` | 1 | 已发布 |
| Tab5 | `tab5-2e8b5b5de1fb` | `zh_CN/schematic/Tab5.md` | `8eacafd9df300761418e05d47b336471125da53c61b8067715fee19dda721d37` | 0 | 已发布 |

`generated_docs/` 中的对应文件与上表发布文件字节一致，方便流水线内部复用；对外检索以 `zh_CN/schematic/` 为准。

## 源资料

| 产品 | 源文档 SHA-256 | 原理图资源 SHA-256 |
| --- | --- | --- |
| 485T | `b188913358e04e7c187fc0718c0dde36946a35a77d99ba9ab625954793e70db9` | `3bf44484efeb51773f0ebda50d64d6ed893ab07335e91748817119091354a64f` |
| 16-Key Capacitive Touch | `f44804bb62fefee5c285f62f224981bb1a08a3f15cda28ed6eae5263ca220403` | `62f6b72d6aa327063de5b1dfb5c80cd42b9668a8ddd8560dc9b841aef51627db` |
| Tab5 | `6c272963b453ca2eea49f0dbf65d1065e74422a1e0cba17252a0a7334acc459b` | 6 份资源，完整列表见 `artifacts/facts/tab5-2e8b5b5de1fb.json` |

## 待确认事项

### 16-Key Capacitive Touch

- 原理图只显示 I2C 物理连接，没有给出从机地址选择网络或固件地址定义；当前固件是否使用产品正文中的 `0x51` 仍待确认。

该疑点已保留在发布文档中，不影响其余已确认硬件事实的查询与使用。

## 回滚点

- `16-Key Capacitive Touch` 旧版：`backups/published/16-key-capacitive-touch-ff4446a15faf/892e7e573b4ed15695f90c658888ae5f1b07f44613595321b37f35de773c6f0b.md`
- `485T` 旧版：`backups/published/485t-ba3491b476d0/51feff9195cce9522970b5848a1e068257568abc98e2a9c960c762ee2a6eb617.md`
- `Tab5` 为首次发布，没有被替换的旧文件。
