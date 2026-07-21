
# Module ExtPort For Core2 拨码开关说明文档

## 1. 功能概述

为避免 Module ExtPort For Core2 模块采用拨码开关灵活切换关键引脚的连接方式。用户可根据需要调整对应的Grove口引脚配置。

<img alt="拨码开关示意图" src="https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_cover_01.webp" width="30%" /><img alt="拨码开关示意图" src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_09.webp" width="30%">


## 2. 拨码开关位置与管脚映射

### 2.1 拨码开关位置

拨码开关位于模块指定位置，见下图:

<img alt="模块外观" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/976/M123_dip_switch_01.png" width="30%" /><img alt="拨码开关局部" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/976/M123_dip_switch_02.png" width="30%" />

> 由上图可见，拨码开关用来切换两个Grove口(Port D以及Port E)的信号引脚，Port D 以及Port E的线序分别是**VDD GND PortD2 PortD1**，**VDD GND PortE2 PortE1**

### 2.2 管脚映射表

根据不同主机，关键引脚的可选映射如下：

|            | CORE2 |
| ---------- | ----- |
| PortD1 | G34   |
|            | G22   |
|            | G3    |
| PortD2 | G35   |
|            | G21   |
|            | G1    |
| PortE1 | G27   |
|            | G2    |
|            | G0    |
| PortE2 | G19   |
|            | G25   |
|            | G2    |


**说明：**

- **PortD1、PortD2、PortE1、PortE2** 均可通过拨码开关选择具体连接的引脚。例如，**在 Core2 主机上**：
  - **PortD1**：可选 G34,G22或G3(三选一)
  - **PortD2**：可选 G35,G21或G1(三选一)
  - **PortE1**：可选 G27,G2或G0(三选一)
  - **PortE2**：可选 G19,G25或G2(三选一)



## 3. 拨码开关切换操作

请按照以下步骤调整拨码开关配置：

1. **断电操作**  
   在调整拨码开关前，请确保模块完全断电，避免损坏硬件。

2. **设置拨码开关**  
   根据所使用的主机选择相应的引脚映射。

 <img alt="拨码开关设置示意图1" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/976/M123_dip_switch_03.png" width="30%" />

> 如上图拨码开关的位置被选择为：( Core2 + Module ExtPort For Core2 )
<br/>PortD1 → G34
<br/>PortD2 → G35
<br/>PortE1 → G27
<br/>PortE2 → G19

1. **重新接线并上电**  
   完成拨码开关设置后，重新连接模块，并接通电源进行后续使用。
