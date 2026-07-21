# AtomS3U

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3U/img-82d5d251-1bfd-4133-9324-404242e5acc7.webp" width="30%" />

AtomS3U 是一款U 盘形态的 ESP32-S3 多功能开发板，采用乐鑫 ESP32-S3 主控芯片，双核 Xtensa LX7 处理器，主频 240 MHz ，自带 Wi-Fi 功能。其接口包括 USB Type-A 接口 (支持 OTG) ，1 个 Grove 口，6Pin@2.54mm 排母 (含 4 个 GPIO) ，外设包括 1 个 PDM 麦克风 ，1 个红外发射管，1 个可编程 RGB-LED 。该产品可用于物联网人机交互、语音输入 / 识别 (STT) 、IO 控制等场景。

## 准备工作

- Home Assistant 主机。
- 在 Home Assistant 中安装并启用[ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。

## 注意事项

- 本教程中，套件在 ESPHome `2026.3.x` 下编译和上传，如果遇见编译 / 上传问题，考虑将 ESPHome 切换至此版本。

## 创建设备

1. 在 Home Assistant 中打开 ESPHome Builder，创建一个空的配置文件。

- 点击右下角的 `NEW DEVICE` 按钮。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/atoms3u_esphome_builder.webp" width="45%" />

- 弹出框单击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_2.webp" width="30%" />

- 选择 `Empty Configuration`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_create_empty_config.webp" width="30%" />

- 为文件命名（可选）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/atoms3u_esphome_builder_naming.webp" width="30%" />

- 在新生成的配置文件处点击 `EDIT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/atoms3u_esphome_builder_edit.webp" width="35%" />

2. 复制 [atoms3u.factory.yaml](https://github.com/m5stack/esphome-yaml/blob/main/examples/kit/atoms3u.yaml) 的内容到配置文件中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/atoms3u_esphome_config.webp" width="60%" />

3. 根据需要，更改网络配置或者是 API 信息等，比如创建一个 API Encryption Key 用于认证：

```yaml
api:
  encryption:
    key: "Your_Encryption_Key"
```

\#> 提示 | 如果需要一个 Key，可以访问 [native api](https://esphome.io/components/api/) 生成一个（在 encryption 下）。

或是使用 secret 里面已经定义的 SSID 和密码：

```yaml
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
```

若不提供，则可使用 `improv_serial` ，BLE 或者 AP 进行网络配置

4. 依次点击右上角 `SAVE` 和 `INSTALL`，选择 `Manual download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/atoms3u_esphome_builder_install_1.webp" width="40%" />

此时会生成代码并且编译工程。

\#> 提示 | 如果是第一次编译，可能会需要较长时间；具体取决于 Home Assistant 主机性能和网络连接情况。

5. 当编译完成后，选择 `Factory format` 下载固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/atoms3u_esphome_builder_install_2.webp" width="45%" />

## 下载和烧录固件

1. 下载固件：通过 ESPHome Builder 的`Manual download`方式下载 Factory Format 固件。

2. 使用 web 工具烧录固件：

- 打开浏览器，访问 [ESPHome Web](https://web.esphome.io/) 上传固件。

- 将 Atom 连接至主机，长按 RESET 按钮进入下载模式，点击 `CONNECT`，选择设备连接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_2.webp" width="70%" />

- 点击 `INSTALL`，选择之前下载的固件上传，再次点击 `INSTALL`，将固件烧录至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/atoms3u_web_esphome_install.webp" width="35%" />

- 当烧录完成后，按下 RESET 按钮进行复位。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_success.webp" width="35%" />

## 开始使用

### 添加设备至 Home Assistant 集成

1. 当设备重启后，会自动连接之前配置的网络，正常情况下可以在 `Settings` -> `Devices & services` 发现设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/atoms3u_device_discovery.webp" width="45%" />

2. 点击 `Add` 将 AtomS3U 集成进入 Home Assistant，如果此前设置了 API Encryption Key，此处可能需要填入 API Encryption Key 验证。
   AtomS3U 的 Dashboard 示例：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/atoms3u_ha_dashboard.webp" width="45%" />

## 外设说明

这一部分将针对配置文件中使用到的外设进行解释

### I2C、I2S

主要是 I2C 和 I2S 引脚

```yaml
i2c:
  sda: GPIO2
  scl: GPIO1

i2s_audio:
  i2s_lrclk_pin: GPIO39
```

### 红外发射器

红外 LED 连接在 GPIO12 上

```yaml
remote_transmitter:
  pin: GPIO12
  carrier_duty_percent: 50%
  non_blocking: true
  rmt_symbols: 48
```

可以添加 IR Remote Climate 组件，实现空调控制，比如：

```yaml
# Example IR Remote Climate
climate:
  - platform: coolix
    name: "Default AC"
    visual:
      min_temperature: 18
      max_temperature: 30
      temperature_step: 1
```

### RGB 灯光

一颗 RGB LED 通过 WS2812 连接到 GPIO35 上

```yaml
light:
  - platform: esp32_rmt_led_strip
    rgb_order: GRB
    pin: GPIO35
    num_leds: 1
    chipset: ws2812
    name: "Light"
    rmt_symbols: 48    
```

### PDM 麦克风

设备上带有一个 PDM 麦克风

```yaml
microphone:
  - platform: i2s_audio
    id: echo_microphone
    i2s_din_pin: GPIO38
    adc_type: external
    pdm: true
```