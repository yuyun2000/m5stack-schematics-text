
# Module LLM 串口通信引脚切换教程

## 引脚切换说明

由于 M5Stack 的 Module 系列产品采用堆叠式设计，多个产品同时使用时可能出现引脚冲突。因此，Module LLM 支持用户手动切换通信引脚。采用串口通信方式，用户只需调整 RX 和 TX 引脚即可。根据所连接主机的不同，可灵活选择合适的引脚。

## 引脚切换位置

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20LLM/03.jpg" width="50%" height="30%">

- **管脚映射**

Module LLM 与不同主机连接时，可选择的 RX 和 TX 引脚如下：

| Module LLM   | RXD             | TXD            |
| ------------ | --------------- | -------------- |
| Core (Basic) | G16/G13/G34/G35 | G17/G15/G12/G0 |
| Core2        | G13/G19/G34/G35 | G14/G2/G27/G0  |
| CoreS3       | G18/G7/G14/G10  | G17/G13/G6/0   |

## 引脚切换操作

1. 以CoreS3 + Module LLM 搭配为例，默认情况下，出厂设置 G18 为 TX，G17 为 RX 进行通信。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/637/solderinig_01.png" width="50%" height="30%">

2. 若需切换 TX 引脚，将其从 G18 切换为 G7。使用刀片等锋利工具切断两个焊盘之间的连接（注意安全，防止割伤），必要时可用万用表检测焊盘是否切断。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/637/solderinig_02.png" width="50%" height="30%">

- 如下图所示，焊盘连接已成功切断：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/637/solderinig_03.png" width="50%" height="30%">

3. 接着，使用电烙铁将 G7 引脚焊接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/637/solderinig_04.png" width="50%" height="30%">

- 焊接完成后效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/637/solderinig_05.png" width="50%" height="30%">

至此，您已成功将 CoreS3 + Module LLM 的通信引脚切换为：G7 为 TX，G17 为 RX。如修改RX引脚，重复上述步骤，TX和RX引脚分别都只能是四选一。

