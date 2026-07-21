# Atom Stepmotor

<span class="product-sku">SKU:K047</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_step_motor/atomic_step_motor_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_step_motor/atomic_step_motor_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_step_motor/atomic_step_motor_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_step_motor/atomic_step_motor_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_step_motor/atomic_step_motor_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_step_motor/atomic_step_motor_06.webp">
</PictureViewer>

## 描述

**Atom Stepmotor** 是一款适用于 Atom-Lite 的步进电机驱动模块，内置 DRV8825 驱动芯片，可用于驱动步进电机，通过调整可变电阻，最高可提供 1.2A 的驱动能力，芯片自带过流保护功能。板载一个拨码开关，可灵活调整步进细分数。内置 DC-DC 芯片可通过外部电源为 ATOM 供电，在使用步进电机时需要提供外部电源供电 (9 ~ 18V) 。

## 产品特性

- 只适用于 Atom-Lite
- 内置 DC/DC 转换电路，外部电源可为 ATOM 供电
- 最高 32 细分
- 最高 1.2A 驱动电流
- 工作状态指示灯

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic Stepmotor Base
- 1 x Type-C 数据线 (20cm)
- 1 x M2\*8 螺丝
- 1 x 内六角扳手

## 应用场景

- 步进电机控制器

## 规格参数

| 规格     | 参数             |
| -------- | ---------------- |
| 细分数   | 最高 1/32        |
| 输出电流 | 最高 1.2A        |
| 供电电压 | 9V-18V           |
| 接口     | KF128L 2.54 6P   |
| 外壳材质 | Plastic （ PC ） |
| 产品重量 | 17g              |
| 毛重     | 53g              |
| 产品尺寸 | 48 x 24 x 18mm   |
| 包装尺寸 | 55 x 55 x 20mm   |

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

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_step_motor/atomic_step_motor_sch_01.webp" width="80%">

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

## 数据手册

- [DRV8825](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/DRV8825_en.pdf)

## 软件开发

### Arduino

- [Atom Stepmotor 测试程序](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_StepMotor)

### UiFlow1

- [Atom Stepmotor UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/stepmotor)

### EasyLoader

| Easyloader                     | 下载链接                                                                                                              | 备注 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---- |
| Atom Stepmotor Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/Easyloader_ATOMIC_StepMotor.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomStepMotor.mp4" type="video/mp4">
</video>
