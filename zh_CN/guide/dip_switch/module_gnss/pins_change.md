
# Module GNSS 拨码开关说明文档

## 1. 功能概述

为避免 Module GNSS 与主机堆叠时因引脚冲突产生问题，模块采用拨码开关灵活切换关键引脚的连接方式。用户可根据所使用的主机（如 Core/Basics、Core2 或 CoreS3）调整对应的引脚配置，从而确保系统稳定运行。

<img alt="拨码开关示意图" src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="30%" /><img alt="拨码开关示意图" src="https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_cover_01.webp" width="30%" /><img alt="拨码开关示意图" src="https://static-cdn.m5stack.com/resource/docs/products/core/BASIC%20v2.6/img-e833c79c-1e8d-462c-ae21-55889c91b1f1.webp" width="30%" />

<img alt="拨码开关示意图" src="https://static-cdn.m5stack.com/resource/docs/products/module/GNSS%20Module/img-b0cdbc6c-d5d5-42bb-bdf6-69016e003b14.webp" style="display: block; margin: auto;" width="30%">


## 2. 拨码开关位置与管脚映射

### 2.1 拨码开关位置

拨码开关位于模块指定位置，见下图:

<img alt="模块外观" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/956/M135_dip_switch_01.png" width="30%" /><img alt="拨码开关局部" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/956/M135_dip_switch_02.png" width="30%" />

> 由上图可见，拨码开关用来切换四个功能引脚:**TXD,RXD,PPS**

### 2.2 管脚映射表

根据不同主机，关键引脚的可选映射如下：

|         | CORE | CORE2 | CORES3 |
| ------- | ---- | ----- | ------ |
| PPS | G34  | G34   | G14    |
|         | G35  | G35   | G10    |
|         | G0   | G0    | G0     |
| TXD | G0   | G0    | G0     |
|         | G12  | G27   | G6     |
|         | G15  | G2    | G13    |
|         | G17  | G14   | G17    |
| RXD | G35  | G35   | G10    |
|         | G34  | G34   | G14    |
|         | G13  | G19   | G7     |
|         | G16  | G13   | G18    |


**说明：**

- **TXD、RXD、PPS** 均可通过拨码开关选择具体连接的引脚。例如，**在 Core (Basic) 主机上**：
  - **PPS**：可选 G34,G35或G0(三选一)
  - **TXD**：可选 G0,G12,G15或G17(四选一)
  - **RXD**：可选 G35,G34,G13或G16(四选一)
  



## 3. 拨码开关切换操作

请按照以下步骤调整拨码开关配置：

1. **断电操作**  
   在调整拨码开关前，请确保模块完全断电，避免损坏硬件。

2. **设置拨码开关**  
   根据所使用的主机选择相应的引脚映射。

 <img alt="拨码开关设置示意图1" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/956/M135_dip_switch_03.png" width="30%" />

> 如上图拨码开关的位置被选择为：( Core (Basic) + Module GNSS )
<br/>PPS → G34
<br/>TXD → G34
<br/>RXD → G25

1. **重新接线并上电**  
   完成拨码开关设置后，重新连接模块，并接通电源进行后续使用。
