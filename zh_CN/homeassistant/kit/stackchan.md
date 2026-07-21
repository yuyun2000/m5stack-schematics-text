# StackChan Home Assistant 集成

<img
  src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/6-lookup2.webp"
  width="30%"
/>

StackChan 是一个超级可爱的 AI 桌面机器人，由 M5Stack 与用户社区共同创造。它使用 M5Stack 旗舰物联网开发套件 CoreS3 作为主机，搭载 ESP32-S3 主控，240 MHz 双核处理器，板载 16MB Flash 和 8MB PSRAM，支持 Wi-Fi 和 BLE。主机还包括 2.0 英寸高强度玻璃盖板电容触控屏、0.3 MP 摄像头、接近传感器、九轴姿态传感器（加速度 + 陀螺仪 + 地磁）、microSD 卡槽、1W 扬声器、双麦克风、开关机与复位按钮等外设。

本文将会介绍 StackChan 的各种外设的集成。如果您需要一个开箱即用的语音助手，请参考：

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/stackchan_voice_assistant_manifest_2026.4.4.json">一键烧录语音助手固件</EspWebTool>

\#> 提示 | 由于性能原因，语音助手并没有集成过多外设，仅包含基础的语音，显示和触摸，舵机控制功能。如若配网之后语音助手没有正常工作，请完全关机 StackChan 后重新开机。

如需要自行下载固件，可以查看 [Github Release](https://github.com/m5stack/esphome-yaml/releases)

## 准备工作

- Home Assistant 主机。
- 在 Home Assistant 中安装并启用[ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 StackChan 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/stackchan_bsp_manifest_2026.4.4.json">一键烧录固件</EspWebTool>


\#> 固件更新记录 | 2026.5 添加了舵机校准按钮，将 ESPHome 版本升级到 2026.4.4<br>
2026.3 初始固件

## 创建设备

1. 在 Home Assistant 中打开 ESPHome Builder，创建配置文件。

- 点击右下角的 `NEW DEVICE` 按钮。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/esphome_builder_stackchan.webp" width="70%"/>

- 弹出框单击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_2.webp" width="40%" />

- 选择 `New Device Setup`

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_3.webp" width="30%"/>

- 填入名称

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/esphome_builder_naming_stackchan.webp" width="30%">

- 选择设备类型，首先取消勾选 `Use recommended settings`，之后点击 `ESP32-S3`，在列表中选择 `M5Stack CoreS3`

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_5.webp" width="30%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_6.webp" width="30%"/>

- 复制 API 备用，点击 `SKIP`

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_7.webp" width="30%"/>

- 在新生成的配置文件卡片处点击 `EDIT` 进行编辑

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/esphome_builder_edit_stackchan_config.webp" width="30%">

- 在文末添加功能包

```yaml
packages:
  remote_package_files:
    url: https://github.com/m5stack/esphome-yaml
    files: [examples/kit/stackchan-bsp.factory.yaml]
    ref: main
    refresh: 0s
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_add_package.webp" width="45%" /> 

2. 保存文件，进行编译

- 依次点击右上角 `SAVE` 和 `INSTALL`，在提示的安装方式中选择 `Manual Download`

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_esphome_build_1.webp" width="45%" />

\#> 提示 | 如果是第一次编译，可能会需要较长时间；具体取决于 Home Assistant 主机性能和网络连接情况。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_esphome_build_2.webp" width="45%" />

## 下载和烧录固件

1. 完成编译后，弹窗会提示选择固件格式，此处选择 `Factory Format` 下载即可

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_esphome_build_3.webp" width="45%" />

2. 完成下载后，使用 Web 工具烧录：

- 将 StackChan 设备通过 USB-C 数据线连接电脑，长按复位键直至绿灯亮起松开，使其进入下载模式。

- 打开浏览器，访问 [ESPHome Web](https://web.esphome.io/) 点击 `CONNECT` 连接设备，在弹窗中选择正确的设备连接

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_webesp_install_1.webp" width="45%" />

- 点击 `INSTALL`，选择之前下载的固件上传

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_webesp_install_2.webp" width="45%" />

- 再次点击 `INSTALL`，将固件烧录至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_webesp_install_3.webp" width="45%" />

等待烧录完成

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_webesp_install_4.webp" width="45%" />

- 完成烧录后，按下 StackChan 上的 RESET 按钮进行复位

## 开始使用

1. 完成固件烧录和复位后，设备开机将自动进行 Wi-Fi 连接。同一局域网内的 Home Assistant 服务将会提示新设备发现，点击 `Settings -> Devices & services` 查看设备发现

2. 找到设备后

- 在发现页面点击 `Add`

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_add_device_1.webp" width="45%" />

- 弹窗提示是否添加设备，选择 `Submit`

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_add_device_2.webp" width="30%">

- 如果之前使用了 API Key 进行加密，则需要输入正确的 Key 进行验证，如无则可根据实际情况继续配置

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_add_device_3.webp" width="30%">

完成添加后，既可在 ESPHome 集成下看见设备，参考设备实体以及 Dashboard

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_add_device_4.webp" width="45%">

## 外围设备说明

这一部分将介绍 StackChan 上的各种组件，主要分为 CoreS3 主机，Power  Board，Touch Board 上的 IC 设备

\#> 提示 | AXP2101, AW9523B 和 AW88298 暂时需要外部组件支持，并不对功能产生影响

主要引脚配置：

```yaml
i2s_audio:
  id: i2s_audio_bus
  i2s_lrclk_pin: GPIO33
  i2s_bclk_pin: GPIO34
  i2s_mclk_pin:
    number: GPIO0
    ignore_strapping_warning: true

i2c:
  - id: bsp_bus
    sda: GPIO12
    scl: GPIO11
    frequency: 100kHz
    scan: true

spi:
  - id: spi_bus
    clk_pin: GPIO36
    mosi_pin: GPIO37

uart:
  tx_pin: GPIO6
  rx_pin: GPIO7
  baud_rate: 1000000
```

### **PMIC** AXP2101

该组件需要 I2C 支持，使用 `output` 组件设置 LDO：

```yaml
axp2101:
  id: axp2101_pmu
  i2c_id: bsp_bus

output:
  - platform: axp2101
    type: range
    channel: DLDO1
    id: lcd_backlight_output
    min_voltage: 2600
    max_voltage: 3300

  - platform: axp2101
    channel: ALDO1
    voltage: 1800
  ...
```

### **IO 拓展芯片** AW9523B 

该组件需要 I2C 支持，组件支持 Pin Schema，此处多用于复位/开关功能，所有用于复位信号的开关均被标记为 `internal: true`，不提供 Home Assistant 前端控制。同时 `BOOST_EN`， `BUS_OUT_EN` 和 `USB_OTG_EN` 可以控制电源方向，可参考[电源管理案例](https://docs.m5stack.com/zh_CN/arduino/m5cores3/power)。在使用时需要先打开 `BOOST_EN` 开关，此后控制 `BUS_OUT_EN` 和 `USB_OTG_EN` 方可生效

```yaml
aw9523b:
  id: aw9523b_hub
  i2c_id: bsp_bus
  p0_drive_mode: PUSH_PULL


switch:
  - platform: gpio
    name: "AW RST P0_2"
    pin:
      aw9523b_id: aw9523b_hub
      number: 2
    internal: true
    restore_mode: RESTORE_DEFAULT_ON
    ...
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_power_ctrl.webp" width="30%" />

### **Audio ADC** ES7210 

该组件需要 I2C 支持，如果要使用语音助手，`sample_rate` 只能使用 `16000`

```yaml
audio_adc:
  - platform: es7210
    id: es7210_adc
    i2c_id: bsp_bus
    bits_per_sample: 16bit
    sample_rate: 16000
    mic_gain: 36
```

### 麦克风

该组件需要配置 I2S 支持，麦克风组件可以结合语音助手使用，实体不会显示在 HA 前端

```yaml
microphone:
  - platform: i2s_audio
    id: i2s_mic
    i2s_din_pin: GPIO14
    adc_type: external
    sample_rate: 16000
    bits_per_sample: 16bit
    i2s_audio_id: i2s_audio_bus
```

### **功放** AW88298 

```yaml
audio_dac:
  - platform: aw88298
    id: aw88298_dac
    i2c_id: bsp_bus
    sample_rate: 48000
```

### 扬声器/播放器

该组件需要配置 I2S 支持，在 Home Assistant 前端可以使用播放器播放音乐

```yaml
speaker:
  - platform: i2s_audio
    i2s_audio_id: i2s_audio_bus
    id: i2s_speaker
    dac_type: external
    i2s_dout_pin: GPIO13
    audio_dac: aw88298_dac

media_player:
  - platform: speaker
    name: None
    id: va_media_player
    volume_min: 0.5
    volume_max: 0.8
    announcement_pipeline:
      speaker: i2s_speaker
      format: FLAC
      sample_rate: 48000
      num_channels: 1
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_speaker_media_player_1.webp" width="30%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_speaker_media_player_2.webp" width="45%" />

### **LCD** ILI9342C

该组件需要 SPI 支持，最大 `data_rate` 只能到 40 MHz，注意设置 `invert_colors` 为 `true` 以对应正确的 RGB 颜色

```yaml
display:
  - platform: mipi_spi
    model: M5CORE
    dc_pin: GPIO35
    reset_pin:
      aw9523b_id: aw9523b_hub
      number: 9
    cs_pin:
      number: GPIO3
      ignore_strapping_warning: true
    data_rate: 40MHz
    invert_colors: true
    id: m5cores3_lcd
    show_test_card: true
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_lcd_test_card.jpg" width="45%" />

### **摄像头** GC0308

该组件需要 I2C 支持，启用该功能可以在 Home Assistant 前端看见实时视频流信息

```yaml
esp32_camera:
  name: "Camera"
  i2c_id: bsp_bus
  vsync_pin:
    number: GPIO46
    ignore_strapping_warning: true
  href_pin: GPIO38
  external_clock:
    pin: GPIO2
    frequency: 20MHz
  pixel_clock_pin:
    number: GPIO45
    ignore_strapping_warning: true
  data_pins: [GPIO39, GPIO40, GPIO41, GPIO42, GPIO15, GPIO16, GPIO48, GPIO47] # D0-D7
  max_framerate: 15.0 fps
  resolution: 320x240
  frame_buffer_count: 1
  pixel_format: RGB565
  jpeg_quality: 6
  agc_mode: manual
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_camera.webp" width="45%" />

### **RTC** BM8563

该组件需要 I2C 支持，可以通过调用组件的方法，实现连接互联网或者 Home Assistant 主机校时：

```yaml
esphome:
  ...
  on_boot: 
    then:
      # read the RTC time once when the system boots
      bm8563.read_time:

time:
  - platform: bm8563
    i2c_id: bsp_bus
    # repeated synchronization is not necessary unless the external RTC
    # is much more accurate than the internal clock
    update_interval: never
  - platform: homeassistant
    # instead try to synchronize via network repeatedly ...
    on_time_sync:
      then:
        # ... and update the RTC when the synchronization was successful
        bm8563.write_time:
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_bm8563_rtc_sync.webp" width="45%">

上述内容仅显示在串口日志中

### **接近传感器** LTR-553ALS-WA

该组件需要 I2C 支持，可以提供环境光/接近信息:

```yaml
sensor:
  - platform: ltr_als_ps
    address: 0x23
    i2c_id: bsp_bus
    update_interval: 10s
    type: ALS_PS
    ambient_light:
      name: "Ambient light"
    glass_attenuation_factor: 2.5
    auto_mode: true
    ps_cooldown: 5 s
    ps_high_threshold: 500
    # on_ps_high_threshold:
    #   then:
    #     - .... # do something - light up the screen for example
    ps_counts: "Proximity counts"
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ltr_553als_wa.webp" width="30%" />

### **六轴姿态传感器** BMI270 （WIP）

### **三轴磁力计** BMM150 （WIP）

### **多功能 IO 拓展芯片** M5IOE1 

该组件需要 I2C 支持

```yaml
m5ioe1:
  id: m5ioe1_hub
  i2c_id: bsp_bus
  reset: true

switch:
  - platform: gpio
    name: "M5IOE1 Pin 1"
    pin:
      m5ioe1_id: m5ioe1_hub
      number: 0
      mode:
        output: true
        pullup: true
    restore_mode: RESTORE_DEFAULT_ON
  ...
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_m5ioe1_switch.webp" width="30%">

此处 `M5IOE1 Pin1` 开关用于给舵机供电，`M5IOE1 Pin 14` 开关默认开启 NeoPixel 控制可寻址灯带。无需手动打开开关（拉高），由灯光组件自行控制

### **功率计** INA266

该组件需要 I2C 支持，用于提供电源功率监测（电压、电流），注： AXP2101 也可以监测电池电压

```yaml
sensor:
 - platform: ina226
    i2c_id: bsp_bus
    address: 0x41
    shunt_resistance: 0.01 ohm
    max_current: 3.2A
    # adc time used for both, Bus Voltage and Shunt Voltage
    adc_time: 140us
    adc_averaging: 128
    update_interval: 60s
    current:
      name: "INA226 Current"
    power:
      name: "INA226 Power"
    bus_voltage:
      name: "INA226 Bus Voltage"
    shunt_voltage:
      name: "INA226 Shunt Voltage"
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ina226_power_meter.webp" width="30%" />

### **舵机**

该组件需要 UART 支持，用于提供 StackChan 左右和上下移动脑袋

```yaml
ftservo:
  - platform: scs9009
    address: 1
    id: x_servo
  - platform: scs9009
    address: 2
    id: y_servo 

number:
  - platform: ftservo
    ftservo_id: x_servo
    angle:
      id: servo_x_angle
      name: "Servo X Angle"
      min_value: -164
      max_value: 164
      use_raw_angle: false
      angle_offset: 164
      step: 5
    speed:
      id: servo_x_speed
      name: "Servo X Speed"
      min_value: 100
      max_value: 1500
      step: 100

  - platform: ftservo
    ftservo_id: y_servo
    angle:
      id: servo_y_angle
      name: "Servo Y Angle"
      min_value: 0
      max_value: 90
      use_raw_angle: false
      angle_offset: 239
      step: 5
    speed:
      id: servo_y_speed
      name: "Servo Y Speed"
      min_value: 100
      max_value: 1500
      step: 100
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ftservo_control.webp" width="30%" />

此处的角度是**经过调整**以适配 StackChan 运动范围。目前设置的 X 方向上运动为 `-165°` 到 `165°`， Y 方向是 `0°` 到 `90°`，归零均是 `0°`

如果使用默认步长控制，可以启用：

```yaml
number:
  - platform: ftservo
    ftservo_id: x_servo
    position:
      id: servo_position
      name: "Servo X Position"
      min_value: 0
      max_value: 1024
```

默认步长最小值为 `0`，最大值为 `1024`。调整速度控制条可以控制每个舵机的运行速度，单位是 `步长/s`


#### 舵机校准

在 YAML 配置文件中有两个 template 按钮：

```YAML

button:
  - platform: template
    name: "Servo Calibration"
    on_press:
      - lambda: |-
          ESP_LOGD("ftservo", "Start calibration");
          float x_zero = id(servo_x_position).state;
          float y_zero = id(servo_y_position).state;
          // assign offset
          float x_offset = x_zero / 2.844f;
          float y_offset = y_zero / 2.844f;
          // override default offset setting
          id(servo_x_angle)->set_angle_offset(static_cast<int>(x_offset));
          id(servo_y_angle)->set_angle_offset(static_cast<int>(y_offset));
          // indicating we are using calibration value
          id(use_calib_value) = true;
          id(x_servo_zero_step) = static_cast<int>(x_zero);
          id(y_servo_zero_step) = static_cast<int>(y_zero);
      - delay: 1s
      - lambda: |-
          ESP_LOGD("ftservo", "Preferences sync requested");
          global_preferences->sync(); // sync at once
          ESP_LOGD("ftservo", "Done reading and saving zero position, X zero: %d, Y zero %d", 
                  id(x_servo_zero_step), id(y_servo_zero_step));

  - platform: template
    name: "Clear Calibration"
    on_press:
      - lambda: |-
          ESP_LOGD("ftservo", "Restore to default settings");
          id(use_calib_value)   = false;
          id(x_servo_zero_step) = ${servo_x_angle_offset};
          id(y_servo_zero_step) = ${servo_y_angle_offset};
      - delay: 1s
      - lambda: |-
          ESP_LOGD("ftservo", "Preferences sync requested");
          global_preferences->sync(); // sync at once
          ESP_LOGD("ftservo", "Done clear calibration");
```


<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_servo_calib_button.webp" width="30%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_servo_clear_calib_button.webp" width="30%" />

舵机配置中有几个组件需要使用到校准数据：

```yaml
esphome:
    ...
    # Servo calibration data
    - priority: -100
      then:
        - lambda: |-
            if (id(use_calib_value)) {
              ESP_LOGD("boot", "Restoring calibration: X=%d, Y=%d",
                      id(x_servo_zero_step),
                      id(y_servo_zero_step));
              float x_offset = id(x_servo_zero_step) / 2.844f;
              float y_offset = id(y_servo_zero_step) / 2.844f;
              // override default offset setting
              id(servo_x_angle)->set_angle_offset(static_cast<int>(x_offset));
              id(servo_y_angle)->set_angle_offset(static_cast<int>(y_offset));
            } else {
              ESP_LOGD("boot", "No calibration data, using defaults.");
            }

  - platform: ftservo
    id: x_servo_sensor
    ftservo_id: x_servo
    position:
      id: servo_x_position
      name: "Servo X Position"
      filters:
        - delta: 3.0
      on_value:
        - lambda: |-
            if ( !id(use_calib_value) ) {
              float val = ${servo_x_position_to_angle};
              id(servo_x_angle).publish_state(roundf(val)); 
            } else {
              float x = id(servo_x_position).state;
              float zero = static_cast<float>(id(x_servo_zero_step));
              float val = (x - zero) * 0.3710f;
              id(servo_x_angle).publish_state(roundf(val));
            }


  - platform: ftservo
    id: y_servo_sensor
    ftservo_id: y_servo
    position:
      id: servo_y_position
      name: "Servo Y Position"
      filters:
        - delta: 3.0
      on_value:
        - lambda: |-
            if ( !id(use_calib_value) ) {
              float val = ${servo_y_position_to_angle};
              id(servo_y_angle).publish_state(roundf(val)); // using angle 
            } else {
              float x = id(servo_y_position).state;
              float zero = static_cast<float>(id(y_servo_zero_step));
              float val = (x - zero) * 90.0f / 260.0f;
              id(servo_y_angle).publish_state(roundf(val));
            }
```

将 StackChan 连接至 Home Assistant，以下是舵机校准步骤：

1. 首先将 StackChan 移动到零点位置

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/K151_stack_chan_main_pictures_05.webp" width="45%" />

2. 按下 `Servo Calibration` 按钮

3. 等待1秒左右时间，让数据写入 ESP32 的 NVS 中 (如果查看串口日志，会发现有相关日志提示 NVS 写入)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_calib_serial_log_1.webp" width="45%" />

4. 重置设备，缓慢移动 Number 滑轨，检查标定的结果

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ha_calib_serial_log_2.webp" width="30%" />


\?> 警告 | 控制舵机运动的时候一定要确认可达范围，以免造成舵机损坏

### **红外发射器**

```yaml
remote_transmitter:
  pin: GPIO5
  carrier_duty_percent: 50%
  non_blocking: true
```

红外组件可以用于创建红外环境控制设备，比如空调。以下案例创建了一个美的空调实体：

```yaml
climate:
  - platform: coolix
    name: "Media AC"
    visual:
      min_temperature: 18
      max_temperature: 30
      temperature_step: 1
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ir_remote_climate_1.webp" width="30%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_ir_remote_climate_2.webp" width="45%" />

### **电容触摸传感器** Si12T

该组件需要 I2C 支持，可通过 `text_sensor`， 触碰 StackChan 的头部获取 Touch 结果

```yaml
si12t:
  id: touch_hub
  i2c_id: bsp_bus

text_sensor:
  - platform: si12t
    name: "Touch Sensor 1"
    channel: CH_1
    update_interval: 1s
  - platform: si12t
    name: "Touch Sensor 2"
    channel: CH_2    
    update_interval: 1s
  - platform: si12t
    name: "Touch Sensor 3"
    channel: CH_3
    update_interval: 1s
```

<div align="center" style="margin: 20px 0; display: flex; justify-content: start; flex-wrap: wrap; gap: 12px;">
  <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_si12t_touch_1.webp" width="30%" />
  <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_si12t_touch_2.webp" width="30%" />
</div>

触摸结果分为三个等级反馈至前端传感器：`HIGH`，`MEDIUM` 和 `LOW`，分别对应高强度，中强度和低强度。`No touch` 即为没有检测到触摸

### **NFC** ST25R3916 (WIP)

该功能需要 I2C 支持

### **RGB 灯条**

该功能依赖于 M5IOE1 片上的 `NeoPixel` 驱动，需要在 M5IOE1 中开启此功能：

```yaml
light:
  - platform: m5ioe1
    id: stackchan_light_bar
    name: "StackChan Light Bar"
    icon: mdi:led-strip
    num_led: 12
    effects:
      - random:
          name: "Random"
          transition_length: 1s
          update_interval: 1s
      - addressable_rainbow:
      - addressable_rainbow:
          name: Rainbow Effect With Custom Values
          speed: 10
          width: 50
      - addressable_twinkle:
      - addressable_twinkle:
          name: Twinkle Effect With Custom Values
          twinkle_probability: 5%
          progress_interval: 4ms
```

同时需要 BUS 提供 5V 供电，需要打开 `BOOST EN` 和 `BUS OUT EN` 开关（ GPIO 开关挂载在 AW9523B IO 拓展芯片上）：

```yaml
switch:
  - platform: gpio
    name: "BOOST_EN"
    pin:
      aw9523b_id: aw9523b_hub
      number: 15
    # BOOST_EN
    restore_mode: RESTORE_DEFAULT_ON

  - platform: gpio
    name: "BUS_OUT_EN"
    pin:
      aw9523b_id: aw9523b_hub
      number: 1
    # BUS_OUT_EN = 1
    restore_mode: RESTORE_DEFAULT_ON

```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_light_bar_1.webp" width="30%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_light_bar_2.webp" width="45%" />

打开灯光效果

<video
  width="320"
  autoplay
  loop
  muted
  playsinline
  preload="auto"> 
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan_lightbar_demo.webm" type="video/webm"> 
</video>

### **红外接收器**

```yaml
remote_receiver:
  pin: GPIO10
```

如果被控设备支持发送返回结果，可以使用 `remote_receiver` 进行接收和处理
