# Atomic Audio-3.5 Base (Echo Base) Home Assistant 集成

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3R/3.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_02.webp" width="20%">

## 1. 准备工作

1. 硬件
  - 1 x [AtomS3R](https://shop.m5stack.com/products/atoms3r-dev-kit)
  - 1 x [Atomic Audio-3.5 Base (Echo Base)](https://shop.m5stack.com/products/atomic-audio-3-5-base)
  - 1 x Home Assistant 主机（服务器、迷你电脑、NAS 等）
2. 软件及版本
  - [ESPHome Device Builder](https://esphome.io/) 2026.4.0 或更高版本

## 2. 创建设备

1. 打开 ESPHome Dashboard。如果出现初始向导，点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%">

2. 点击右下角的绿色 **+** 按钮创建新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%">

3. 点击 `New Device Setup` 进入设备创建向导。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%">

4. 输入设备名称，然后点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/AtomicHA7.png" width="30%">

5. 选择设备类型，点击 `ESP32S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR2.webp" width="30%">

6. 点击 `SKIP` 跳过加密密钥设置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%">

7. 点击 `EDIT` 打开 YAML 编辑器并自定义设备配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/AtomicHA4.png" width="50%">

## 3. 设备配置

### 3.1 基础配置

- **添加 [psram](https://esphome.io/components/psram/) 组件**

- **添加 [I2C](https://esphome.io/components/i2c/) 组件**

```yaml
esp32:
  variant: esp32s3
  flash_size: 8MB
  cpu_frequency: 240MHz
  framework:
    type: esp-idf
    sdkconfig_options:
      CONFIG_ESP32S3_DEFAULT_CPU_FREQ_240: "y"
      CONFIG_ESP32S3_DATA_CACHE_64KB: "y"
      CONFIG_ESP32S3_DATA_CACHE_LINE_64B: "y"

psram:
  mode: octal
  speed: 80MHz

i2c:
  - id: bsp_bus
    sda:
      number: GPIO45
      ignore_strapping_warning: true
    scl:
      number: GPIO0
      ignore_strapping_warning: true
    scan: true
  - id: ext_bus
    sda: GPIO38
    scl: GPIO39
```

?> 注意 | AtomS3R 对应 SDA: GPIO38, SCL: GPIO39。如果使用其他接口，请根据实际引脚进行调整。

### 3.2 音频配置

- **添加 [i2s_audio](https://esphome.io/components/i2s_audio/) 组件**

- **添加 [audio_dac](https://esphome.io/components/audio_dac/) 组件**

- **添加 [speaker](https://esphome.io/components/speaker/) 组件**

```yaml
i2s_audio:
  - id: i2s_audio_bus
    i2s_lrclk_pin: GPIO6
    i2s_bclk_pin: GPIO8

audio_dac:
  - platform: es8311
    id: es8311_dac
    i2c_id: ext_bus
    bits_per_sample: 16bit
    sample_rate: 48000
    use_microphone: false
    use_mclk: false

speaker:
  - platform: i2s_audio
    id: i2s_speaker
    i2s_audio_id: i2s_audio_bus
    i2s_dout_pin: GPIO5
    dac_type: external
    audio_dac: es8311_dac
    sample_rate: 48000
    channel: left
```

### 3.3 媒体播放器配置

- **添加 [media_player](https://esphome.io/components/media_player/) 组件**

```yaml
media_player:
  - platform: speaker
    name: "${friendly_name}"
    id: speaker_media_player
    volume_min: 0.5
    volume_max: 0.8
    announcement_pipeline:
      speaker: i2s_speaker
      format: FLAC
      sample_rate: 48000
      num_channels: 1
```

### 3.4 SPI 和字体配置

- **添加 [spi](https://esphome.io/components/spi/) 组件**

- **添加 [font](https://esphome.io/components/font/) 组件**

```yaml
spi:
  clk_pin: GPIO15
  mosi_pin: GPIO21

font:
  - file: "gfonts://Roboto"
    id: font_medium
    size: 14
```

### 3.5 扬声器功放配置

- **添加 [pi4ioe5v6408](https://esphome.io/components/pi4ioe5v6408/) 组件**

- **添加 [switch](https://esphome.io/components/switch/) 组件**

```yaml
pi4ioe5v6408:
  - id: pi4ioe5v6408_hub
    i2c_id: ext_bus
    address: 0x43

switch:
  - platform: gpio
    name: "Speaker Enable"
    id: speaker_enable
    pin:
      pi4ioe5v6408: pi4ioe5v6408_hub
      number: 0
      mode:
        output: true
    icon: "mdi:volume-high"
    restore_mode: RESTORE_DEFAULT_ON
```

### 3.6 显示屏和 LED 配置

- **添加 [output](https://esphome.io/components/output/) 组件**

- **添加 [light](https://esphome.io/components/light/) 组件**

- **添加 [display](https://esphome.io/components/display/) 组件**

```yaml
lp5562:
  id: lp5562_led
  i2c_id: bsp_bus
  use_internal_clk: true
  white_current: 17.5

output:
  - platform: lp5562
    id: lp5562_white_channel
    lp5562_id: lp5562_led
    channel: white

light:
  - platform: monochromatic
    name: "LCD Backlight"
    id: lcd_backlight
    output: lp5562_white_channel
    icon: "mdi:television"
    restore_mode: RESTORE_DEFAULT_ON

display:
  - platform: mipi_spi
    id: atoms3r_lcd
    model: ST7789V
    dc_pin: GPIO42
    reset_pin: GPIO48
    cs_pin: GPIO14
    data_rate: 40MHz
    update_interval: 1s
    dimensions:
      height: 128
      width: 128
      offset_width: 2
      offset_height: 1
    invert_colors: true
    rotation: 180°
    lambda: |-
      it.fill(Color::BLACK);
      it.print(
        it.get_width() / 2,
        it.get_height() / 2,
        id(font_medium),
        Color::WHITE,
        TextAlign::CENTER,
        "Audio-3.5 Base"
      );
```

## 4. 构建和烧录固件

### 4.1 构建固件

1. 编辑完 YAML 配置后，点击右上角的 `SAVE`，然后点击 `INSTALL`。

2. 在弹出的对话框中，选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%">

3. 等待固件编译完成，然后点击 `Download` 并选择 `Factory format (Previously Modern)` 将固件文件保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%">

?>提示| 完整的示例配置请参见 [atomic-audio3.5-base.yaml](https://github.com/m5stack/esphome-yaml/blob/main/examples/sensor/atomic-audio3.5-base.yaml)。首次构建可能需要一些时间，具体取决于 Home Assistant 主机的性能和网络状况。

### 4.2 烧录固件

4. 使用 USB Type-C 数据线将 AtomS3R 连接到计算机。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%">

5. 在串口选择对话框中，选择正确的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%">

6. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%">

7. 选择步骤 3 中下载的固件文件并开始烧录。

!>警告| 烧录完成后，必须重置设备；否则固件可能无法正常启动。

## 5. 在 Home Assistant 中使用

1. 在 Home Assistant 中，进入 `设置` > `设备与服务` 打开集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%">

2. 在 `已发现` 区域找到在线设备，点击 `配置`，按照提示完成添加。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/Atomic6.png" width="40%"/>

3. 添加成功后，设备页面将显示三个传感器实体。
  
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/atomicHA1.png" width="40%">

4. 最后，将传感器实体添加到仪表盘中。
   
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/AtomicHA2.png" width="40%">
