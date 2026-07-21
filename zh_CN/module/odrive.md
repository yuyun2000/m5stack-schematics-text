# Module13.2 BLDC Drvier

<span class="product-sku">SKU:M036</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/964/M036-Module13.2-ODrive_01.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/odrive/odrive_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/odrive/odrive_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/odrive/odrive_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/odrive/odrive_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/odrive/odrive_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/odrive/odrive_09.webp">
</PictureViewer>

## 描述

**Module13.2 BLDC Drvier** 是 M5Stack 推出的一款高性能伺服电机驱动模块，基于开源运动控制方案 ODrive 制作。支持控制单个三相伺服电机，峰值驱动电流可达 5A。具备高转速电机控制能力的同时提供编码器信号接口，能够实现高精度运动控制定位。模块使用 UART 通信接口，兼容 ODrive 官方配置工具与协议 (通过上位机工具还可配置不同的电机运动模式使电机工作更加的顺畅稳定) 。

## 产品特性

- 支持单个三相伺服电机驱动
- 峰值驱动电流 5A
- DC 12 ~ 24V 电源输入接口 (要求适配器输出电流可达 5A)
- 通信接口：UART
- 集成编码器信号接口

## 包装内容

- 1 x Module13.2 BLDC Drvier
- 1 x 3.96-3P 端子
- 1 x 3.96-2P 端子
- 1 x 2.54-5P 端子（带连接线）

## 应用场景

- 高精度运动控制
- 伺服电机驱动

## 规格参数

| 规格            | 参数                                             |
| --------------- | ------------------------------------------------ |
| 最大驱动电流    | 5A                                               |
| 接口类型        | 3.96-2P (电源), 3.96-3P (电机), 2.54-5P (编码器) |
| ODrive 硬件版本 | v3.5-24V                                         |
| ODrive 固件版本 | 0.5.1                                            |
| 输入电源        | DC 12 ~ 24V                                      |
| 产品尺寸        | 54.2 x 54.2 x 19.7mm                             |
| 产品重量        | 22.5g                                            |
| 包装尺寸        | 95.0 x 65.0 x 25.0mm                             |
| 毛重            | 42.3g                                            |

## 原理图

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/odrive/odrive_sch_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/odrive/odrive_sch_02.webp">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN        | LEFT | RIGHT | PIN        |
| ---------- | ---- | ----- | ---------- |
| GND        | 1    | 2     |            |
| GND        | 3    | 4     |            |
| GND        | 5    | 6     | RST        |
|            | 7    | 8     |            |
|            | 9    | 10    | TXD / STEP |
|            | 11   | 12    |            |
|            | 13   | 14    |            |
|            | 15   | 16    |            |
|            | 17   | 18    |            |
|            | 19   | 20    | RXD / DIR  |
| TXD / STEP | 21   | 22    | TXD / STEP |
| RXD / DIR  | 23   | 24    | RXD / DIR  |
|            | 25   | 26    |            |
|            | 27   | 28    | 5V         |
|            | 29   | 30    |            |
::

## 尺寸图

- [Module13.2 BLDC Drvier 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/964/module-odrive.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/964/module-odrive_page_01.png" width="100%">

## 数据手册

- [DRV8301 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/DRV8301.pdf)
- [温敏电阻SDNT1608X103F3450FTF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/odrive/SDNT1608X103F3450FTF_datasheet.pdf)
- [功率管NTMFS5C430NLT1G](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/odrive/C194661_NTMFS5C430NLT1G_2018-06-29.PDF)

## 软件开发

### Arduino

\#> 案例说明 | 该案例使用 ODrive 模块控制伺服电机高速精准转动。注意：使用前需要根据实际连接的电机型号，通过 ODriveTool 进行相应的参数配置。

- [Module13.2 BLDC Drvier Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/ODrive)

### UiFlow2

- [Module13.2 BLDC Drvier UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/odrive.html)

### ODriveTool

\#>odrivetool 是 ODrive 配套的配置和调试软件，通过它配置电机参数。该教程将演示在`Linux`平台下 odrivetool 的安装与基本使用。

- 使用下方命令，进行 odrivetool v0.5.1 的安装，环境要求:`python3`。

```bash
pip3 install odrive==0.5.1.post0

```

- 将 `~/.local/bin` 添加到系统环境变量中，执行下方命令，并插入`export PATH=$PATH:~/.local/bin`至文本末尾。

```bash
vim ~/.bashrc

```

- 命令行执行`odrivetool`运行工具。并将 ODrive 模块连接至电脑等待 odrivetool 识别。成功连接后输入`odrv0.vbus_voltage`测试获取驱动板电源电压。

```bash
$odrivertool

ODrive control utility v0.5.1.post0
Website: https://odriverobotics.com/
Docs: https://docs.odriverobotics.com/
Forums: https://discourse.odriverobotics.com/
Discord: https://discord.gg/k3ZZ3mS
Github: https://github.com/madcowswe/ODrive/

Please connect your ODrive.
You can also type help() or quit().

Connected to ODrive 306A396A3235 as odrv0

In [1]: odrv0.vbus_voltage

```

- 常用配置命令

```bash

//配置电机电流限制
odrv0.axis0.motor.config.current_lim [A].

//配置电机转速限制值
odrv0.axis0.controller.config.vel_limit

//配置功率耗散电阻的电阻值
odrv0.config.brake_resistance

//保存配置
odrv0.save_configuration()

```

- 更多详情内容，[请查看Odrive官方文档](https://docs.odriverobotics.com/#start-odrivetool)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/ODrive_VIDEO.mp4" type="video/mp4">
</video>
