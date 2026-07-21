# TimerCamera 系列 Home Assistant 集成

本教程详细讲解 TimerCamera 系列设备接入 Home Assistant 的方法，适用于 TimerCamera (U082), TimerCamera-X (U082-X), TimerCamera-F (U082-F)。

<div style="display: flex; gap: 15px; flex-wrap: wrap; justify-content: center;">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/timercam/timercam_01.webp" width="30%"/>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/timercam_x/timercam_x_01.webp" width="30%"/>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/timercam_f/timercam_f_01.webp" width="30%"/>
</div>

## 准备工作

- Home Assistant 主机
- 在 Home Assistant 中安装并启用[ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)
- [OV3660 Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/OV3660_datasheet.pdf)
- 在 ESPHome 上查看最新配置范例：[ESP32 Camera](https://esphome.io/components/esp32_camera/)

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 TimerCamera 系列 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/timercamera_f_manifest_2026.1.1.json">一键烧录 TimerCamera-F 固件</EspWebTool>

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/timercamera_x_manifest_2026.1.1.json">一键烧录 TimerCamera-X 固件</EspWebTool>

## 注意事项

- 本教程中，套件在 ESPHome 2025.12.3 下编译和上传，如果遇见编译 / 上传问题，考虑将 ESPHome 切换至此版本，在此处以 TimerCamera-X 作为范例配置，除去部分型号摄像头不一致，其余硬件配置一致，可根据自己的具体型号修改诸如名称等信息。

## 创建设备

1. 打开 ESPHome Builder，点击右下角点击 `NEW DEVICE`，创建一个新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_1.webp" width="60%"/>

2. 弹窗点击`CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_2.webp" width="30%"/>

3. 选择`New Device Setup`，创建新的配置文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_3.webp" width="30%"/>

4. 为新的配置文件命名。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_x_ha_config_naming.webp" width="30%"/>

5. 选择设备类型，此处保持默认配置，选择`ESP32`即可。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_esp_builder_6.webp" width="30%"/>

6. 复制 Encryption Key 备用，点击`SKIP`跳过。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_7.webp" width="30%"/>

## 修改配置

1. 在生成的配置文件卡片下点击`EDIT`进行编辑。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_x_edit_config.webp" width="40%"/>

2. 打开配置文件进行修改

- 添加 [PSRAM](https://esphome.io/components/psram/) 组件。

```yaml
psram:
  mode: quad
  speed: 80MHz
```

- 添加 [I2C](https://esphome.io/components/i2c/) 和 [ESP32 Camera](https://esphome.io/components/esp32_camera/) 组件。

```yaml line-num
i2c:
  - id: bsp_i2c
    sda: GPIO12
    scl: GPIO14
  - id: cam_i2c
    sda: GPIO25
    scl: GPIO23

esp32_camera:
  name: OV3660 Camera
  external_clock:
    pin: GPIO27
    frequency: 20MHz
  i2c_id: cam_i2c
  data_pins: [GPIO32, GPIO35, GPIO34, GPIO5, GPIO39, GPIO18, GPIO36, GPIO19]
  vsync_pin: GPIO22
  href_pin: GPIO26
  pixel_clock_pin: GPIO21
  reset_pin: GPIO15
  resolution: 640x480
  jpeg_quality: 10
```

此处采用的默认图像配置，如需更改配置可以参考 ESPHome 提供的配置范例。

- 添加 [RTC Time](https://esphome.io/components/time/bm8563/) 组件。

```yaml
esphome:
  name: timercamera-x
  friendly_name: timercamera-x
  ...
  on_boot:
    then:
      # read the RTC time once when the system boots
      bm8563.read_time:

...
time:
  - platform: bm8563
    i2c_id: bsp_i2c
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

系统会在启动的时候读取 RTC 中的时间信息，当连接到 Home Assistant 后，会自动同步 Home Assistant 的时间信息。

- 配置 LED。

```yaml line-num
output:
  - platform: ledc
    id: blue_led
    pin: GPIO2

light:
  - platform: monochromatic
    output: blue_led
    name: "Blue LED"
    restore_mode: RESTORE_DEFAULT_ON
```

蓝色 LED 会默认在设备上电后打开，可以在 Home Assistant 里面控制 LED 开关和亮度。

- 使用电池。

```yaml line-num
switch:
  - platform: gpio
    id: bat_hold_pin
    name: "Battery Hold Pin"
    pin: GPIO33
    restore_mode: RESTORE_DEFAULT_ON
```

此处 GPIO33 用于控制是否使用电池，开启并且保持拉高即可让电池工作，默认情况会一直保持拉高；如果关闭此开关，没有外接电源的情况下设备会关机。

- 监测电池电量信息。

TimerCamera-X 和 TimerCamera-F 上预装了电池，可以供过获取 GPIO38 的 ADC 读数来得到电池电压信息，转换后得到大致电池电量信息：

```yaml line-num
sensor:
  - platform: adc
    pin: GPIO38
    attenuation: 12dB
    name: "Battery Voltage"
    id: battery_voltage
    update_interval: 10s
    filters:
      - multiply: 1.51

  - platform: template
    id: battery_percent
    name: "Battery Percentage"
    unit_of_measurement: "%"
    accuracy_decimals: 0
    lambda: |-
      float voltage = id(battery_voltage).state;
      float min_voltage = 3.350f;
      float max_voltage = 4.150f;

      if (voltage <= min_voltage) return 0.0;
      if (voltage >= max_voltage) return 100.0;

      float percent = ((voltage - min_voltage) / (max_voltage - min_voltage)) * 100.0;
      return percent;
```

\#> 注意 | 电池电量仅在未接入外部 USB 供电，以及保持 BAT_HOLD_Pin （GPIO33）为高才能监测有效值；未保持 HOLD 状态将不会采用电池供电， ADC 读数会很低 (<1 V)；如果接入了外部 USB 供电以及保持了 HOLD 状态，这里的电压信息是充电电压。

## 下载和烧录固件

1. 修改完成后，点击右上角 `SAVE` 和 `INSTALL`, 在弹出的选项中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

\#> 提示 | 点击 [TimerCamera-X](https://github.com/m5stack/esphome-yaml/blob/main/examples/camera/timercamera-x-example.yaml)/[TimerCamera-F](https://github.com/m5stack/esphome-yaml/blob/main/examples/camera/timercamera-f-example.yaml)查看完整配置文件范例；首次编译可能会需要较长时间，编译时间与 Home Assistant 主机性能和网络质量相关。

2. 编译完成后，点击 `Download` 按钮，选择 `Factory Format` 下载固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_compile_finish.webp" width="60%"/>

3. 将套件通过 USB Type-C 数据线连接至主机，打开[ESPHome Web](https://web.esphome.io/)，点击`CONNECT`连接设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_web_esp_connect.webp" width="40%"/>

4. 之后点击`INSTALL`，选择之前编译的固件进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_webesp_install.webp" width="40%"/>

5. 再次点击`INSTALL`进行烧录，等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_success.webp" width="30%"/>

## 开始使用

1. 完成固件烧录后，设备开机将自动进行 Wi-Fi 连接。导航至 `Settings`->`Device & services` 查看设备情况。点击 `Add` 即可添加设备至 Home Assistant。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_x_ha_device_discovery.webp" width="30%"/>

2. Dashboard 示例：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timer_camera_x_ha_dashboard.webp" width="30%"/>

3. 点击相机实体，可以查看实时预览画面。

<div style="display: flex; gap: 15px; flex-wrap: wrap; justify-content: center;">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timer_camera_x_ha_preview.webp" width="45%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timer_camera_f_ha_preview.webp" width="45%"/>
</div>

TimerCamera (TimerCamera-X) 如左， TimerCamera-F 由于使用的是鱼眼镜头，所以呈现效果如右图所示。

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115982035061529&bvid=BV1Yw6eBnE1C&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/_h_nNy3K9iQ?si=COB0aRA3aRme0XM2" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
