# UnitV-M12

<span class="product-sku">SKU:U078-V-M12</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1057/unitv-m12_01.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT-V M12/img-eb4f374f-5811-4625-9f01-cce7705221fe.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1057/unitv-m12_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT-V M12/img-5d263563-8ee8-4c37-ac5e-5f8bae92ce2c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT-V M12/img-d5b2ed38-4919-49d1-b623-96386c0036eb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT-V M12/img-026640ab-53a1-4ef1-806a-6923b7ff1e2d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT-V M12/img-189283c0-71bd-4a66-b797-4478582502c2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT-V M12/img-f473d778-3d04-4c05-9136-fdf9d503bc66.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT-V M12/img-5e2b8148-f351-44cb-976f-ed09d805cf91.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1057/U078-V-M12.webp">
</PictureViewer>

## 描述

**Unit V-M12** 是一款独具特色的 AI 摄像头单元，采用 M12 镜头规格，搭载 K210 处理器。其内部集成了双核 64 位 RISC-V CPU 与神经网络处理器边缘计算片上系统，硬件配置强大。配备的**OV7740 广角摄像模组**遵循 M12 光学镜头规格，并且支持替换其他 M12 规格镜头，为不同场景下的拍摄需求提供了灵活性。

该摄像头机身设有两个可编程按键，方便用户进行特定功能的快捷操作，同时配备 microSD 卡扩展插槽，可满足数据存储需求。底部提供一个 HY2.0-4P 接口和一个 Type-C 接口，能够便捷地与主控设备实现数据连接。

**Unit V-M12** 体积小巧玲珑，这一特点使其易于嵌入各类设备之中。它具备出色的机器视觉处理能力，不仅支持多种图像识别功能，如实时获取被检测目标的大小、坐标以及种类等信息，还能够进行卷积神经网络计算，为用户提供了低门槛的机器视觉嵌入式解决方案，适用于各类对机器视觉有需求的应用场景。

## 产品特性

- 双核 64-bit RISC-V RV64IMAFDC (RV64GC) CPU / 400Mhz (Normal)
- 双精度 FPU
- 8MiB 64bit 片上 SRAM
- 神经网络处理器 (KPU) / 0.8Tops
- 可编程 I/O 阵列 (FPIOA)
- AES，SHA256 加速器
- 直接内存存取控制器 (DMAC)
- 支持 MicroPython
- 固件加密支持
- 板载硬件资源:
  - Flash: 16M
  - Camera :OV7740
  - 按键: button \* 2
  - 拓展卡接口: microSD 卡
  - 接口: HY2.0-4P/compatible GROVE

## 包装内容

- 1 x UnitV-M12
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 物体检测 / 分类
- 实时获取目标的大小和坐标
- 实时获取检测到的目标类型
- 形状识别
- 视频录制

## 规格参数

| 规格                 | 参数                                                         |
| -------------------- | ------------------------------------------------------------ |
| Kendryte K210        | 双核 64-bit RISC-V RV64IMAFDC (RV64GC) CPU / 400Mhz (Normal) |
| SRAM                 | 8M                                                           |
| Flash                | 16M                                                          |
| 输入电压             | 5V @ 500mA                                                   |
| KPU 神经网络参数大小 | 5.5M-5.9M                                                    |
| 接口                 | Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 1                      |
| 按键                 | 自定义按键 x 2                                               |
| 摄像头               | M12 规格 广角 OV7740                                         |
| FOV                  | 80°                                                          |
| 外部存储             | microSD 卡                                                   |
| 外壳材质             | Plastic (PC) +CNC 金属                                       |
| 产品尺寸             | 40.0 x 24.0 x 16.4mm                                         |
| 产品重量             | 13.4g                                                        |
| 包装尺寸             | 54.0 x 37.0 x 20.0mm                                         |
| 毛重                 | 20.0g                                                        |

## 操作说明

### microSD 卡测试

Unit V 目前并不能识别所有类型的 microSD 卡，我们对一些常见的 microSD 卡进行了测试，测试结果如下:

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv_ov7740/unitv_ov7740_11.webp" width="40%" height="40%"><br/>

| 品牌     | 内存 | 类型 | 传输速度 | 分区格式 | 测试结果  |
| -------- | ---- | ---- | -------- | -------- | --------- |
| Kingston | 8G   | HC   | Class4   | FAT32    | OK        |
| Kingston | 16G  | HC   | Class10  | FAT32    | OK        |
| Kingston | 32G  | HC   | Class10  | FAT32    | NO        |
| Kingston | 64G  | XC   | Class10  | exFAT    | OK        |
| SanDisk  | 16G  | HC   | Class10  | FAT32    | OK        |
| SanDisk  | 32G  | HC   | Class10  | FAT32    | OK        |
| SanDisk  | 64G  | XC   | Class10  | /        | NO        |
| SanDisk  | 128G | XC   | Class10  | /        | NO        |
| XIAKE    | 16G  | HC   | Class10  | FAT32    | OK (紫色) |
| XIAKE    | 32G  | HC   | Class10  | FAT32    | OK        |
| XIAKE    | 64G  | XC   | Class10  | /        | NO        |
| TURYE    | 32G  | HC   | Class10  | /        | NO        |

<!--## 原理图 暂时不开源 -->

## 管脚映射

### UnitV-M12

| UnitV    | G8      | G19      | G18      | G34，G35  |
| -------- | ------- | -------- | -------- | --------- |
| Hardware | RGB LED | Button A | Button B |           |
| HY2.0-4P |         |          |          | Interface |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT-V M12/img-0463d15d-73b2-4f6a-904d-20676f8a3197.jpg" width="100%" />

## 数据手册

- [Maixpy docs](https://wiki.sipeed.com/news/MaixPy/K210_usage.html)
- [K210 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/kendryte_datasheet.pdf)
- [OV7740 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/stickv/OV7740_datasheet.pdf)

## 软件开发

### 快速上手

- [V-Function](/zh_CN/guide/ai_camera/unitv/v_function)
- [V-Training](/zh_CN/guide/ai_camera/unitv/v-training)
- [Maixpy](/zh_CN/guide/ai_camera/unitv/maixpy)

### Arduino

- [UnitV-M12 Arduino 使用教程](/zh_CN/arduino/projects/unit/unitv)
- [UnitV-M12 Track Ball Example with RoverC](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/App/UnitV/track_ball)

## 相关视频

颜色识别示例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/unitV.mp4" type="video/mp4"></video>

## 产品对比

如需对比 UnitV 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/unitv_compare?select=U078-V-M12)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
