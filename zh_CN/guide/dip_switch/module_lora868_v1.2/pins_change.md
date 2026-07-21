# Module LoRa868 v1.2 拨码开关说明文档

## 1. 功能概述

为避免 Module LoRa868 v1.2 与主机堆叠时因引脚冲突产生问题，模块采用四组拨码开关（DIP switch）灵活切换关键引脚连接。

* **NSS、BUSY、RST、IRQ** 四个功能引脚可通过拨码开关选择不同的 GPIO。
* 兼容多款 M5Stack 主机：Core (Basic)、Core2、CoreS3等。
* 用户可根据项目需求，自行调整对应的引脚映射，确保系统稳定运行。

<img alt="核心主机兼容示意" src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="30%" /><img alt="Core2 主机兼容示意" src="https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_cover_01.webp" width="30%" /><img alt="Basic 主机兼容示意" src="https://static-cdn.m5stack.com/resource/docs/products/core/BASIC%20v2.6/img-e833c79c-1e8d-462c-ae21-55889c91b1f1.webp" width="30%" />

## 2. 拨码开关概述

### 2.1 拨码开关物理位置

模块底部四组拨码开关，如下图红框所示。 

<img alt="拨码开关位置总览" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/DIP_SWITCH_07.png" width="30%" /> <img alt="拨码开关特写" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/DIP_SWITCH_01.png" width="30%" />

### 2.2 管脚映射表

根据不同主机，关键引脚的可选映射如下：

| 模块型号     | MOSI | MISO | SCK | RST     | BUSY    | NSS           | IRQ         |
| ------------ | ---- | ---- | --- | ------- | ------- | ------------- | ----------- |
| Core (Basic) | G23  | G19  | G18 | G25/G13 | G36/G2  | G15/G12/G5/G0 | G35/G34/G26 |
| Core2        | G23  | G38  | G36 | G25/G19 | G36/G32 | G2/G27/G33/G0 | G35/G34/G26 |
| CoreS3       | G37  | G35  | PB4 | G5/G7   | G8/G2   | G13/G6/G1/G0  | G10/G14/G9  |


- 例如Module LoRa868 v1.2搭配**Core (Basic) 主机**使用时，则查看第一行Core相关的引脚映射：
  - **NSS**：可选 G15、G12、G5 或 G0（四选一）
  - **BUSY**：可选 G36 或 G2（二选一）
  - **RST**：可选 G25 或 G13（二选一）
  - **IRQ**：可选 G35、G34 或 G26（三选一）

> 选择对应引脚并将其拨至ON端即可。

## 3. 拨码开关配置示例

以下以 **Core (Basic) + Module LoRa868 v1.2** 为例，说明四组拨码开关的设置方式。

<img alt="拨码开关配置示例" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/DIP_SWITCH_02.png" width="70%" />

> 如上图拨码开关的位置被选择为：( Core (Basic) + Module LoRa868 v1.2 )
<br/>NSS → G12
<br/>BUSY → G2
<br/>RST → G13
<br/>IRQ → G35

- 完成拨码开关设置后，重新连接模块，并接通电源进行后续使用。
