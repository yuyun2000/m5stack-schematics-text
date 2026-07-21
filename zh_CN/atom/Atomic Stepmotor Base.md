# Atomic Stepmotor Base

<span class="product-sku">SKU:A132</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Stepmotor Base/img-59dd9dee-7858-48d9-a134-2ddf4965616e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Stepmotor Base/img-4c632d49-04b4-4e25-9af8-78ac25bd6674.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Stepmotor Base/img-d62ad36e-c498-4052-a4b5-0bc59e2426a1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Stepmotor Base/img-8395110d-7df8-4c8d-b613-9e52d7216eeb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Stepmotor Base/img-9a0aeedb-2f19-4436-b02d-ca7fab77fbcf.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Stepmotor Base/img-4b70ba5b-cf2f-4640-ba91-1e9552d844e0.webp">
</PictureViewer>

## 描述

**Atomic Stepmotor Base** 是一款适用于 ATOM 系列的步进电机驱动底座，内置 DRV8825 驱动芯片，可用于驱动步进电机，通过调整可变电阻，最高可提供 1.2A 的驱动能力，芯片自带过流保护功能。板载一个拨码开关，可灵活调整步进细分数。内置 DC-DC 芯片可通过外部电源为整机供电，在使用步进电机时需要提供外部电源供电 (9 ~ 18V) 。 适用于 3D 打印机、数控机床、机器人、自动化设备、摄像机云台等。

## 产品特性

- 内置 DC-DC 外部电源可为 ATOM 供电
- 最高 32 细分
- 最高 1.2A 驱动电流
- 工作状态指示灯
- 适用于 Atom-Lite/ATOMS3/AtomS3-Lite 等系列主机

## 包装内容

- 1 x Atomic Stepmotor Base

## 应用场景

- 步进电机控制器

## 规格参数

| 规格     | 参数            |
| -------- | --------------- |
| 细分数   | 最高 1/32       |
| 输出电流 | 最高 1.2A       |
| 供电电压 | 9V-18V          |
| 接口     | KF128L 2.54 6P  |
| 外壳材质 | Plastic (PC)    |
| 产品尺寸 | 48 x 24 x 18mm  |
| 产品重量 | 12g             |
| 包装尺寸 | 136 x 92 x 20mm |
| 毛重     | 14.4g           |

## 操作说明

### 细分设置

| 拨码开关  | 3   | 2   | 1   |
| --------- | --- | --- | --- |
| Full-step | Off | Off | Off |
| Half-step | On  | Off | Off |
| 1/4 step  | Off | On  | Off |
| 1/8 step  | On  | On  | Off |
| 1/16 step | Off | Off | On  |
| 1/32 step | On  | Off | On  |
| 1/32 step | Off | On  | On  |
| 1/32 step | On  | On  | On  |

### Decay mode

| 拨码开关 | 4   |
| -------- | --- |
| 缓慢衰减 | Off |
| 快速衰减 | On  |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Stepmotor Base/img-16a88fcb-fc50-42f5-9b58-7c25c5f55cce.webp" width="100%" />

## 管脚映射

::m5-bus-table
| PIN   | LEFT | RIGHT | PIN     |
| ----- | ---- | ----- | ------- |
|       |      | 1     | 3V3     |
| RESET | 2    | 3     | EN      |
| FAULT | 4    | 5     | STEP    |
| 5V    | 6    | 7     | DIR     |
| GND   | 8    | 9     | PWR-ADC |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Stepmotor Base/img-123b7b45-dce4-45a1-abd1-7c6fc60749de.jpg" width="100%" />

## 数据手册

- [DRV8825](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/DRV8825_en.pdf)

## 软件开发

### Arduino

- [Atomic Stepmotor Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_stepmotor_base)
- [Atomic Stepmotor Base 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/Atomic_StepMotor/Atomic_StepMotor)

### UiFlow1

- [Atomic Stepmotor Base UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/stepmotor)

### UiFlow2

- [Atomic Stepmotor Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/stepmotor.html)

### EasyLoader

| Easyloader                            | 下载链接                                                                                                                                           | 备注 |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atomic Stepmotor Base Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20Stepmotor%20Base/ezLoader-752628a3-7b42-46ae-8cf9-9747732a1e5f.exe) | /    |

## 相关视频

- 按下中间按键正转 5000 步，反转 5000 步

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomStepMotor.mp4" type="video/mp4"></video>
