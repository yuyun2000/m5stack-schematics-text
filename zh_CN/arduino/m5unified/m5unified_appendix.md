# M5Unified 库相关数据定义

## Boards

### M5.getBoard()

可通过 M5.getBoard () 获取的开发板类型枚举值：

```cpp
namespace boards
  { // Be careful not to change existing board numbers when adding values.
    enum board_t
    { board_unknown = 0
    , board_M5Stack
    , board_M5StackCore2
    , board_M5StickC
    , board_M5StickCPlus
    , board_M5StickCPlus2
    , board_M5StackCoreInk
    , board_M5Paper
    , board_M5Tough
    , board_M5Station
    , board_M5StackCoreS3
    , board_M5AtomS3
    , board_M5Dial
    , board_M5DinMeter
    , board_M5Cardputer
    , board_M5AirQ
    , board_M5VAMeter
    , board_M5StackCoreS3SE
    , board_M5AtomS3R
    , board_M5PaperS3
    , board_M5CoreMP135
    , board_M5StampPLC
    , board_M5Tab5

/// non display boards
    , board_M5AtomLite = 128
    , board_M5ATOM __attribute__ ((deprecated)) = board_M5AtomLite
    , board_M5Atom __attribute__ ((deprecated)) = board_M5AtomLite
    , board_M5AtomPsram
    , board_M5AtomU
    , board_M5Camera
    , board_M5TimerCam
    , board_M5StampPico
    , board_M5StampC3
    , board_M5StampC3U
    , board_M5StampS3
    , board_M5AtomS3Lite
    , board_M5AtomS3U
    , board_M5Capsule
    , board_M5NanoC6
    , board_M5AtomMatrix
    , board_M5AtomEcho
    , board_M5AtomS3RExt
    , board_M5AtomS3RCam

/// external displays
    , board_M5AtomDisplay = 192
    , board_M5ATOMDisplay = board_M5AtomDisplay
    , board_M5UnitLCD
    , board_M5UnitOLED
    , board_M5UnitMiniOLED
    , board_M5UnitGLASS
    , board_M5UnitGLASS2
    , board_M5UnitRCA
    , board_M5ModuleDisplay
    , board_M5ModuleRCA

    , board_FrameBuffer = 512
    };
  }
```

## Configs

### M5.config()

全局配置参数

| 参数名          | 类型     | 说明                            | 默认值 | 适用条件                                                                         |
| :-------------- | :------- | :------------------------------ | :----- | :------------------------------------------------------------------------------- |
| serial_baudrate | uint32_t | USB 串口波特率                  | 115200 | 仅限 Arduino-esp32 平台                                                          |
| clear_display   | bool     | 启动时是否清屏                  | true   | 仅带屏幕设备有效                                                                 |
| output_power    | bool     | 外部 5V 输出开关                | true   | 仅支持 AXP192 芯片的设备                                                         |
| pmic_button     | bool     | 是否启用 PMIC 按键              | true   | 仅支持 AXP192 芯片的设备                                                         |
| internal_imu    | bool     | 是否启用内置 IMU                | true   | 仅带 IMU 模块的设备                                                              |
| internal_rtc    | bool     | 是否使用内置 RTC                | true   | 仅带 RTC 模块的设备                                                              |
| internal_mic    | bool     | 是否使用内置麦克风              | true   | 仅带麦克风设备                                                                   |
| internal_spk    | bool     | 是否使用内置扬声器              | true   | 仅带扬声器设备                                                                   |
| external_imu    | bool     | 是否使用外接 IMU / 加速度计单元 | false  | 可连接设备： <br>Unit IMU <br>Unit Accel <br>Unit Mini IMU <br>Unit Mini IMU Pro |
| external_rtc    | bool     | 是否使用外接 RTC 单元           | false  | 可连接设备： <br>Unit RTC                                                        |
| disable_rtc_irq | bool     | 是否在启动时关闭 RTC 中断请求位 | true   | 仅带 RTC 模块的设备                                                              |
| led_brightness  | uint8_t  | 内置 LED 亮度 (0-255)           | 0      | 仅限单色 LED 设备 (RGB 灯无效)                                                   |

#### external_speaker

外部扬声器使能参数，以下两个可二选一，`external_speaker`使用形式为`external_speaker.<device_name>`。

| 参数名                 | 类型     | 说明                                                                                                                                                                                         | 默认值 | 适用条件               |
| :--------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----- | :--------------------- |
| external_speaker_value | uint16_t | 是否使用外接扬声器，按位使能                                                                                                                                                                 | 0x00   | 见下方结构体中成员定义 |
| external_speaker       | struct   | 是否使用外接扬声器，成员 (device_name) 如下：<br>（除特殊标注外均占用 1 位）<br>module_display <br>module_rca <br>hat_spk <br>atomic_spk <br>hat_spk2 <br>atomic_echo <br>reserve (2 位保留) | 0x00   | 适用成员定义中的设备   |

#### external_display

外部显示器使能参数，以下两个可二选一，`external_display`使用形式为`external_display.<device_name>`。

| 参数名                 | 类型     | 说明                                                                                                                                                                                                                                            | 默认值 | 适用条件               |
| :--------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----- | :--------------------- |
| external_display_value | uint16_t | 是否使用外接显示器，按位使能                                                                                                                                                                                                                    | 0xFFFF | 见下方结构体中成员定义 |
| external_display       | struct   | 是否使用外接显示器，成员 (device_name) 如下：<br>（除特殊标注外均占用 1 位）<br>module_display <br>atom_display <br>unit_oled <br>unit_mini_oled <br>unit_lcd <br>unit_glass <br>unit_glass2 <br>unit_rca <br>module_rca <br>reserve (7 位保留) | 0xFFFF | 适用成员定义中的设备   |

相关外接设备:

- [Unit Accel](https://shop.m5stack.com/collections/m5-sensor/products/3-axis-digital-accelerometer-unit-adxl345?variant=17364934787162)
- [Unit IMU](https://shop.m5stack.com/collections/m5-sensor/products/6-axis-imu-unitmpu6886)
- [Unit Mini IMU](https://shop.m5stack.com/products/6-axis-imu-unitmpu6886)
- [Unit Mini IMU Pro](https://shop.m5stack.com/products/6-dof-imu-pro-mini-unit-bmi270-bmm150-bmp280)
- [Unit RTC](https://shop.m5stack.com/products/real-time-clock-rtc-unit-hym8563)
- [Hat SPK](https://shop.m5stack.com/products/m5stickc-speaker-hat)
- [Hat SPK2](https://shop.m5stack.com/products/m5stickcplus-speaker-2-hat-max98357)
- [Atomic Voice Base](https://shop.m5stack.com/products/atomic-echo-base-with-microphone-and-speaker)
- [Atomic SPK Base](https://shop.m5stack.com/products/atomic-speaker-base-ns4168)

### M5.Speaker.config()

扬声器配置参数

| 参数名           | 类型       | 说明                             | 默认值    | 备注                                                            |
| :--------------- | :--------- | :------------------------------- | :-------- | :-------------------------------------------------------------- |
| pin_data_out     | int        | I2S 数据输出引脚 (扬声器)        | -1        | 需指定 GPIO 引脚号                                              |
| pin_bck          | int        | I2S 位 / 串行时钟引脚 (BCK/SCLK) | -1        |                                                                 |
| pin_mck          | int        | I2S 主时钟引脚 (MCLK)            | -1        |                                                                 |
| pin_ws           | int        | I2S 声道选择引脚 (WS/LRCK)       | -1        |                                                                 |
| sample_rate      | uint32_t   | 采样率 (Hz)                      | 48000     |                                                                 |
| stereo           | bool       | 是否启用立体声                   | false     |                                                                 |
| buzzer           | bool       | 是否使用蜂鸣器输出               | false     | 启用时只需设置 data_out 引脚                                    |
| use_dac          | bool       | 是否使用内置 DAC 输出            | false     | 启用时只需设置 data_out 引脚，ESP32 仅支持 I2S_NUM_0、GPIO25/26 |
| dac_zero_level   | uint8_t    | DAC 零电平参考值                 | 0         | 0 表示动态调整                                                  |
| magnification    | uint8_t    | 输出值放大倍数                   | 16        |                                                                 |
| dma_buf_len      | size_t     | I2S DMA 缓冲区长度               | 256       | 最大为 1024                                                     |
| dma_buf_count    | size_t     | I2S DMA 缓冲区数量               | 8         |                                                                 |
| task_priority    | uint8_t    | 音频播放任务优先级               | 2         |                                                                 |
| task_pinned_core | uint8_t    | 音频播放任务绑定的 CPU 核心      | -1        |                                                                 |
| i2s_port         | i2s_port_t | 使用的 I2S 端口                  | I2S_NUM_0 | 可选 I2S0 或 I2S1                                               |

## Buttons

各型号设备的按键 GPIO 映射：

| 设备型号             | BtnA     | BtnB        | BtnC       | BtnPWR | BtnEXT |
| :------------------- | :------- | :---------- | :--------- | :----- | :----- |
| M5Basic/Gray/Go/Fire | G39      | G38         | G37        | -      | -      |
| M5Core2              | TouchA   | TouchB      | TouchC     |        | -      |
| M5Stick C/CPlus      | G39      | G37         | -          | AXP192 | -      |
| M5StickCPlus2        | G37      | G39         | G35        | -      | -      |
| M5CoreInk            | G37 (Up) | G38 (Press) | G39 (Down) | G27    | G5     |
| M5Paper              | G37 (Up) | G38 (Press) | G39 (Down) | -      | -      |
| M5Station            | G37      | G38         | G39        | AXP192 | -      |
| M5Tough              | -        | -           | -          | AXP192 | -      |
| M5AirQ               | G0       | G8          | -          | -      | -      |
| M5Atom-Lite/Matrix   | G39      | -           | -          | -      | -      |
| M5AtomS3/S3-Lite     | G41      | -           | -          | -      | -      |
| M5Capsule            | G42      | -           | -          | -      | -      |
| M5Cardputer          | G0       | -           | -          | -      | -      |
| M5Dial               | G42      | -           | -          | -      | -      |
| M5DinMeter           | G42      | -           | -          | -      | -      |
| M5StampPico          | G39      | -           | -          | -      | -      |
| M5StampC3/C3U        | G3       | -           | -          | -      | -      |
| M5StampS3/S3A        | G0       | -           | -          | -      | -      |
| M5StamPLC            | P2       | P1          | P0         | -      | -      |
