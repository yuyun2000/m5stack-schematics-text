# Stamp-S3 GroveBreakOut

<span class="product-sku">SKU:A144</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/StampS3 GroveBreakOut/img-ccf32b1b-526a-418a-8b85-d1c283052bca.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/StampS3 GroveBreakOut/img-a5a02606-f5a8-48f5-8a85-d1d1cc91acfa.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/StampS3 GroveBreakOut/img-6b7523ac-65be-48ca-b27f-d9cd3373a18c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/StampS3 GroveBreakOut/img-69457129-8943-4380-a7c8-a981b1247a57.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/StampS3 GroveBreakOut/img-febdd175-8533-451b-ae23-f8e1725803af.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/StampS3 GroveBreakOut/img-6676fdb1-6e9a-41eb-9463-07734a340cf0.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/StampS3 GroveBreakOut/img-5fff86d6-65f5-4ec0-8481-59659db6e2ec.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/StampS3 GroveBreakOut/img-e74cf02e-e8bd-433b-a332-1eca6a3d6c3e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/StampS3 GroveBreakOut/img-3c0612fd-10b7-40a2-8ad8-b5e7e2101bf6.webp">
</PictureViewer>

## 描述

**StampS3 GroveBreakOut** 是一款专为 Stamp-S3 设计的扩展板，配备了 6 个 Grove 接口，兼容 M5 的 portA/B/C 标准 (包括 I2C、IO (输入 / 输出) 和 UART 接口)。此扩展板内置了 16340/18350 型号的锂电池底座，以及 1.25mm@2P 锂电池接口，可以独立为整个系统供电，并配备了电池供电开关及 USB 与电池供电之间的切换开关。板载轻触开关分别连接 EN 引脚，用于复位控制。此外，该板还具备锂电池充电芯片和 5V 升压系统，以及电池电量检测电路，提供稳定而可靠的能源解决方案。预留的固定孔可方便用户安装固定。该产品适用于教育与原型开发、物联网 (IoT) 项目、可穿戴设备、自动化和机器人等领域。

## 注意事项

\#> 兼容性 | StampS3 GroveBreakOut 仅支持 Stamp-S3 PIN1.27 规格

## 产品特性

- 多 Grove 接口兼容性
- 独立电力系统
- 充电和电量检测
- 供电切换以及复位控制

## 包装内容

- 1 x StampS3 GroveBreakOut

## 应用场景

- 物联网 (IoT) 项目
- 可穿戴设备和移动设备
- 教育和原型开发
- 自动化系统
- 机器人技术

## 规格参数

| 规格           | 参数                    |
| -------------- | ----------------------- |
| Grove 接口     | 6xGrove (I2C/GPIO/UART) |
| 电池类型       | 16340/18350 锂电池规格  |
| 排母规格       | 1.27mm&2.54mm           |
| 锂电池接口     | 1.25mm@2P               |
| Grove 接口规格 | HY2.0-4P                |
| 固定孔尺寸     | 直径 3mm                |
| 工作温度       | 0- 40°C                 |
| 产品尺寸       | 47.5 x 38 x 23.2mm      |
| 包装尺寸       | 75 x 45 x 29mm          |
| 产品重量       | 10.0g                   |
| 毛重           | 22.1g                   |

## 原理图

- [Stamp-S3 GroveBreakOut 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/538/SCH_StampS3GroveBreakOut_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/538/SCH_StampS3GroveBreakOut_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

Grove Pin

| Stamp-S3 | IO2 | IO1 | 5V       | GND |
| -------- | --- | --- | -------- | --- |
| Grove1   | G1  | G2  | Grove_5V | GND |
| Grove2   | G4  | G3  | Grove_5V | GND |
| Grove3   | G6  | G5  | Grove_5V | GND |
| Grove4   | G10 | G11 | Grove_5V | GND |
| Grove5   | G9  | G7  | Grove_5V | GND |
| Grove6   | G15 | G13 | Grove_5V | GND |

Battery Detect

| Stamp-S3     | G8      |
| ------------ | ------- |
| Battery(ADC) | BAT_ADC |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/accessory/StampS3 GroveBreakOut/img-e8ab287a-1891-4198-b612-2fc70f785838.jpg" width="100%" />

## 数据手册

- [TP4057](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/M5GO%20BATT%20Bottom3/7EEA633644BAFD22D2FBC132F5380171.pdf)

## 相关视频

- Stamp-S3 GroveBreakOut 产品介绍以及示例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/accessory/StampS3%20GroveBreakOut/A144%20StampS3GroveBreakOut%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>
