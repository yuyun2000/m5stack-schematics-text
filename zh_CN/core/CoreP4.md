coming soon...

# CoreP4

## 产品特性

- ESP32-P4NRW32X 核心主控
  - 16MB Flash
  - 32MB PSRAM
- 2.64" LCD 触摸显示屏，分辨率 480x480
- 音频系统
  - ES8311 Audio Codec
  - AW8737A Audio AMP + 1W@8Ω 扬声器
  - ES7210 Audio ADC + 双路 MEMS 麦克风输入，带 AEC 回声消除
- 10/100M 以太网
- 九轴 IMU: 
  - BMI270 六轴姿态传感器
  - BMM150 三轴磁力传感器
- 红外发送 + 接收
- RTC RX8130CE
- 扩展接口:
  - HY2.0-4P (PORT.A)
  - M5-Bus
  - microSD 卡槽
  - 1x USB Type-C (Debug/Device, only Input)
  - 1x USB Type-C (OTG，only Output)
  - 1x USB-A (Host, only Output)
  - MIPI CSI (2-lane)
  - 预留 Wi-Fi 模组扩展接口，适配 Stamp-AddOn C6 For P4
- 供电方式
  - USB Type-C DC 5V 供电
  - M5-Bus DC 5V 供电
  - DC 3.7V 电池供电
- 电源 & 外设 管理
  - Stamp Timer Power2 电源管理模块，内置 M5PM1 芯片
  - 多级电源管理设计，支持低功耗唤醒
  - 两档电池充电电流调节 180/650mA
  - M5IOE1 IO 扩展芯片，外设管理

## 应用场景

- 智能家居控制
- 远程监控系统
- 物联网设备开发
- 工业自动化

## 规格参数

| 规格         | 参数                                                  |
| ------------ | ----------------------------------------------------- |
| 主控制器 SoC | ESP32-P4NRW32@RISC-V 32 位双核 400MHz + LP 单核 40MHz |
| Flash        | 16MB                                                  |
| PSRAM        | 32MB Octal                                            |
| 以太网       | 10/100M，IP101GRI                                     |
| 屏幕         | 2.64" LCD @ ST7102, 480x480, MIPI DSI 2-Lane          |
| 触摸         | 触控 IC @ CST3530                                     |
| 音频编解码   | ES8311 Audio Codec                                    |
| 扬声器       | AW8737A Audio AMP + 1W@8Ω 扬声器                      |
| 麦克风       | ES7210 Audio ADC + 双路 MEMS 麦克风输入 (AEC)         |
| IMU          | BMI270 六轴姿态传感器 + BMM150 三轴磁力传感器         |
| RTC          | RX8130CE                                              |
| PMU & IOE    | Stamp Timer Power2 (M5PM1) + M5IOE1                   |

## 操作说明

- PMIC 电源按键

长按下载
单击开机/复位
双击关机
