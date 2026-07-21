# Arduino Nesso N1

<span class="product-sku">SKU:DK001</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_01.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_02.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_03.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_04.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_05.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_06.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_07.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_08.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_09.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_10.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_11.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_12.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_13.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_14.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_15.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_16.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_main_pictures_17.jpg">
</PictureViewer>

## 描述

**Arduino Nesso N1** 是 M5Stack 与 Arduino 官方联名合作的一款高性能一体化开发板，专为远程监控和自动化控制而设计。设备采用 ESP32-C6 SoC，支持 2.4 GHz Wi-Fi 6，Thread, Zigbee, Matter 等通信协议。同时集成 SX1262 LoRa 收发器，支持 850 ~ 960 MHz 工作频段。配备 1.14" LCD 触摸屏、内置 6 轴 IMU 传感器、可编程按钮和可充电电池，是开发复杂物联网解决方案的理想工具。

## 教程 & 快速上手

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/arduino_nesso_n1/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Arduino Nesso N1 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/arduino_nesso_n1/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Arduino Nesso N1 设备。 |

## 产品特性

- ESP32-C6 核心主控:
  - 2.4 GHz Wi-Fi 6
  - Thread, Zigbee，Matter
- LoRa 通信:
  - SX1262 LoRa 收发器
  - 工作频率 850 ~ 960 MHz
- 内置 3.7V @ 250 mAh 锂电池
- 1.14" LCD 触摸屏
- 6 轴 IMU 传感器 BMI270
- 红外发射管
- 蜂鸣器
- 状态指示灯
- 拓展接口:
  - 2.54-8P 总线接口。(兼容 M5Stack Hat 系列拓展)
  - 1x Qwiic 接口

## 包装内容

- 1 x Arduino Nesso N1
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)

## 应用场景

- 远程监控
- 工业自动化
- IoT 应用开发

## 规格参数

| 规格              | 参数                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------ |
| SoC               | ESP32-C6 @ RISC-V 32 位高性能单核处理器 160MHz + RISC-V 32 位低功耗单核处理器 20 MHz |
| Flash             | 16 MB                                                                                |
| Wi-Fi             | 2.4 GHz Wi-Fi 6                                                                      |
| 输入电源          | DC 5V                                                                                |
| 电池              | 3.7V @ 250 mAh                                                                       |
| LoRa              | SX1262                                                                               |
| LoRa 最大发射功率 | +22dBm                                                                               |
| 屏幕              | ST7789 (1.14" IPS LCD)<br/>分辨率：135 x 240                                         |
| 屏幕触摸          | FT6336                                                                               |
| 工作温度          | 0 ~ 40°C                                                                             |

## 操作说明

### 按键说明

- 单击：设备开机或复位
- 双击：设备关机
- 长按：进入程序下载模式

### 进入下载模式

设备连接 USB 线，长按机身左侧复位按键。当设备内部蓝色 LED 闪烁时，表示设备已成功进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_operate_01.gif" width="50%">

## 原理图

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001-sche_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001-sche.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_06.png">

</SchViewer>

## 管脚映射

- [Arduino Nesso N1 Full Pin Map](https://docs.arduino.cc/resources/pinouts/TPX00227-full-pinout.pdf)

### LCD

| ESP32-C6 | G21  | G20 | G17 | G16 |
| -------- | ---- | --- | --- | --- |
| ST7789   | MOSI | SCK | CS  | RS  |

### Touch & IMU

| ESP32-C6      | G10 | G8  | G3  |
| ------------- | --- | --- | --- |
| FT6336 (0x38) | SDA | SCL | INT |
| BMI270 (0x68) | SDA | SCL | INT |

### Power Management

| ESP32-C6       | G10 | G8  |
| -------------- | --- | --- |
| BQ27220YZFR () | SDA | SCL |
| AW32001ECSR () | SDA | SCL |

### LoRa

| ESP32-C6 | G21  | G22  | G20 | G23 | G19  | G15 |
| -------- | ---- | ---- | --- | --- | ---- | --- |
| SX1262   | MOSI | MISO | SCK | CS  | BUSY | IRQ |

### PI4IOE5V6408

| ESP32-C6              | G10 | G8  | ESP_RST |
| --------------------- | --- | --- | ------- |
| PI4IOE5V6408-0 (0x43) | SDA | SCL | RST     |
| PI4IOE5V6408-1 (0x44) | SDA | SCL | RST     |

| PI4IOE5V6408-1 (0x43) | E0.P0 | E0.P1 | E0.P5     | E0.P6     | E0.P7   |
| --------------------- | ----- | ----- | --------- | --------- | ------- |
| KEY1                  | INPUT |       |           |           |         |
| KEY2                  |       | INPUT |           |           |         |
| SX1262                |       |       | SX_LNA_EN | SX_ANT_SW | SX_NRST |

LoRa 模组初始化需要执行以下操作：

- 复位 LoRa 模组：将 SX_NRST 设置为低电平，持续 100 ms 后重新置为高电平。
- 使能射频天线开关：将 SX_ANT_SW 设置为高电平
- 使能 LNA 芯片开关： 将 SX_LNA_EN 设置为高电平

| PI4IOE5V6408-1 (0x44) | E1.P0         | E1.P1     | E1.P2          | E1.P5          | E1.P6         | E1.P7  |
| --------------------- | ------------- | --------- | -------------- | -------------- | ------------- | ------ |
| Device Power          | PWR_OFF_PULSE |           |                |                |               |        |
| LCD                   |               | LCD_RESET |                |                | LCD_BACKLIGHT |        |
| GROVE                 |               |           | GROVE_POWER_EN |                |               |        |
| USB                   |               |           |                | USB_VIN_DETECT |               |        |
| LED                   |               |           |                |                |               | LED_EN |

### Buzzer & IR

| ESP32-C6 | G11  | G9    |
| -------- | ---- | ----- |
| Buzzer   | BEEP |       |
| IR       |      | IR_TX |

### QWIIC Connector

::grove-table
| ESP32-C6 | GND | 3V3 | G10 | G8  |
| -------- | --- | --- | --- | --- |
| QWIIC    | GND | 3V3 | SDA | SCL |
::

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G5     | G4    |
::

### USB

| ESP32-C6 | G13    | G12    |
| -------- | ------ | ------ |
| USB      | USB_D+ | USB_D- |

### Hat Bus

| Hat Bus | Arduino Nesso N1 |
| ------- | ---------------- |
| 1       | 5V_IN            |
| 2       | 3V3              |
| 3       | BAT              |
| 4       | G6               |
| 5       | G2               |
| 6       | G7               |
| 7       | 5V_OUT           |
| 8       | GND              |

## 尺寸图

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001-model-size_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001-model-size_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001-model-size_03.png">
</SchViewer>

## 结构文件

- [Arduino Nesso N1 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/DK001_Arduino_Nesso_N1/Structures)

## 数据手册

- [Arduino Nesso N1 Datasheet](https://docs.arduino.cc/resources/datasheets/TPX00227-datasheet.pdf)
- [SX1262](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DS_SX1261_2_V2-2.pdf)
- [ESP32-C6](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/esp32-c6_datasheet_cn.pdf)

## 软件开发

### Arduino

- [Arduino Nesso N1 快速上手](/zh_CN/arduino/arduino_nesso_n1/program)
- [Arduino Nesso N1 官方用户手册](https://docs.arduino.cc/tutorials/nesso-n1/user-manual/)

### UiFlow2

- [Arduino Nesso N1 UiFlow2 快速上手](/zh_CN/uiflow2/arduino_nesso_n1/program)

## 相关视频

- Arduino Nesso N1 UiFlow2 教程视频

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/Arduino-Nesso-N1-on-UiFlow2.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115790791575344&bvid=BV1fSBrBCE3x&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/OxxhY7mcQhI?si=Z626glDJBPUVyndq" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
