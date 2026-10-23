# Stamp Timer Power2

<span class="product-sku">SKU:S021</span>

## 描述

**Stamp Timer Power2** 是一款面向低功耗嵌入式设备的电源管理模组，内置 M5PM1 电源管理芯片，采用多级供电控制架构，可按需管理主控及各类外设的电源使能，有效降低整机待机功耗并延长电池续航时间。
模组支持 DC 5V 输入 / 输出控制、DC 3.7V 锂电池供电及输入电压检测，并集成两档可调充电电流的锂电池充电电路；采用 1.27mm 邮票孔封装设计，除基本的电源输入，输出控制引脚外，还提供了 5 路可编程 IO，可复用为 GPIO、ADC、PWM、RGB LED 和 IRQ 等功能，同时支持定时唤醒与外部输入中断唤醒，便于构建按需上电、周期运行和事件触发的低功耗系统。

## 产品特性

- 内置 M5PM1 电源管理芯片
- I2C 通信接口 (0x6E) 
- 内置锂电池充电芯片，两档可调充电电流 (650mA/180mA)
- 5x 可编程扩展 IO (GPIO，ADC，PWM，RGB LED，IRQ)
- 支持 DC 5V / DC 3.7V 电池输入供电
- 外设 & 控制
  - 电源按键输入信号接口
  - 电源指示灯信号接口
  - Boot 控制接口，用于 MCU 下载模式控制
- 1.27mm @ 2x14P 邮票孔封装

## 包装内容

- 1 x Stamp Timer Power2

## 应用场景

- 嵌入式设备电源管理
- 智能家居
- 低功耗物联网设备

## 规格参数

| 规格         | 参数                                                  |
| ------------ | ----------------------------------------------------- |
| 电源管理芯片 | M5PM1                                                 |
| I2C 通信接口 | 通信地址 0x6E,  支持 100 kHz (default) / 400 kHz      |
| 功耗         | 关机: DC 4.2V@6.72uA <br> 低功耗休眠: DC 4.2V@12.27uA |
| 电池充电芯片 | LGS4056HDA                                            |
| 产品尺寸     |                                                       |
| 产品重量     |                                                       |
| 包装尺寸     |                                                       |
| 毛重         |                                                       |

## 原理图

- [Stamp Timer Power2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1294/S021_Stamp_Timer_Power2_SCH_V0.7.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1294/S021_Stamp_Timer_Power2_SCH_V0.7.1_page_01.png">
</SchViewer>

## 管脚映射

## 尺寸图

## PCB

## 数据手册

todo: markdown 版本的 通信协议 link

## 软件开发

### Arduino

- [M5PM1 Arduino 驱动库](https://github.com/m5stack/M5PM1)
