# Unit PoE CAM-W v1.1 Home Assistant 集成

本教程介绍 Unit PoE CAM-W v1.1 接入 Home Assistant 的操作方法。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe-cam-Home_Assistant_tutorial_cover_ZH.png" width="60%">

## 准备工作

- Home Assistant 主机
- 在 Home Assistant 中安装并启用[ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)
- [W5500 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/W5500_datasheet_v1.0.2_1_en.pdf)
- [OV3660 Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/OV3660_datasheet.pdf)
- 在 ESPHome 上查看最新配置范例：
- [Ethernet](https://esphome.io/components/ethernet/)
- [ESP32 Camera](https://esphome.io/components/esp32_camera/)

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 Unit PoE CAM-W v1.1 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/unit_poe_cam_w_v1_rev1_manifest_2026.3.0.json">一键烧录固件</EspWebTool>

## 注意事项

- 本教程中，套件在 ESPHome 2025.10.3 下编译和上传，如果遇见编译 / 上传问题，考虑将 ESPHome 切换至此版本。

## 创建设备

1. 打开 ESPHome Builder，点击右下角点击 `NEW DEVICE`，创建一个新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_1.webp" width="70%"/>

2. 弹窗点击`CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_2.webp" width="30%"/>

3. 选择`New Device Setup`，创建新的配置文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_3.webp" width="30%"/>

4. 为新的配置文件命名。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_esp_builder_5.webp" width="30%"/>

5. 选择设备类型，此处保持默认配置，选择`ESP32`即可。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_esp_builder_6.webp" width="30%"/>

6. 复制 Encryption Key 备用，点击`SKIP`跳过。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_7.webp" width="30%"/>

## 修改配置

1. 在生成的配置文件卡片下点击`EDIT`进行编辑。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_edit_config_1.webp" width="40%"/>

2. 打开配置文件进行修改，根据希望使用的网络类型，配置 Wi-Fi 或者以太网。

\#> 提示 | `Wi-Fi` 和 `Ethernet` 只能选择其中之一，默认情况下新建配置会提供一个 Wi-Fi 选项

如若使用以太网组件，需要注释掉 Wi-Fi 组件

```yaml line-num
# Wi-Fi or Ethernet, you can only enable one of it
# wifi:
#   ssid: !secret wifi_ssid
#   password: !secret wifi_password

#   # Enable fallback hotspot (captive portal) in case wifi connection fails
#   ap:
#     ssid: "unit-poe-cam-w-v1-rev1"
#     password: ""

ethernet:
  type: W5500
  clk_pin: GPIO23
  mosi_pin: GPIO13
  miso_pin: GPIO38
  cs_pin: GPIO4
  clock_speed: 20MHz
```

3. 添加 `I2C` 组件和`ESP32 Camera` 组件。

```yaml line-num
i2c:
  - id: cam_i2c
    sda: GPIO14
    scl: GPIO12

esp32_camera:
  name: "OV3660 Camera"
  i2c_id: cam_i2c
  external_clock:
    pin: GPIO27
    frequency: 20MHz
  data_pins: [GPIO32, GPIO35, GPIO34, GPIO5, GPIO39, GPIO18, GPIO36, GPIO19]
  vsync_pin: GPIO22
  href_pin: GPIO26
  pixel_clock_pin: GPIO21
  reset_pin: GPIO15
```

\#> 提示 | 如果需要配置相机（如分辨率，帧率，白平衡等）可以参考 [ESP32 Camera](https://esphome.io/components/esp32_camera/) 组件自行修改

4. 添加按键组件和 LED 组件。

```yaml line-num
binary_sensor:
  - platform: gpio
    name: "Button"
    pin:
      number: GPIO37
      inverted: true

output:
  - platform: ledc
    pin:
      number: GPIO0
      inverted: true
    id: status_led

light:
  - platform: monochromatic
    output: status_led
    name: "Status LED"
    id: sled
    restore_mode: RESTORE_DEFAULT_ON
```

5. 修改完成后，点击`SAVE` 和 `INSTALL`, 在弹出的选项中选择`Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_install_1.webp" width="40%"/>

\#> 提示 | 点击[此处](https://github.com/m5stack/esphome-yaml/blob/main/common/unit-poe-can-w-v1-rev1-base.yaml)查看完整配置文件范例；首次编译可能会需要较长时间，编译时间与 Home Assistant 主机性能和网络质量相关。

6. 编译完成后，点击`Download`按钮，选择`Factory Format`下载固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_install_2.webp" width="70%"/>

## 下载和烧录固件

1. 将套件通过烧录板连接至主机，打开[ESPHome Web](https://web.esphome.io/)，点击`CONNECT`连接设备。

\#> 注意 | 该设备需要[专用烧录工具](/zh_CN/arduino/m5poe_cam/program#2.%E7%83%A7%E5%BD%95%E5%B7%A5%E5%85%B7)进行程序烧录下载<br>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/poe_cam_download_board_01.png" width="80%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_web_esp_connect.webp" width="40%"/>

2. 点击`INSTALL`，选择之前编译的固件进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_web_esp_install.webp" width="40%"/>

3. 再次点击`INSTALL`进行烧录，等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_success.webp" width="30%"/>

## 开始使用

1. 完成固件烧录后，设备开机将自动进行 Wi-Fi 连接。Home Assistant 服务自动发现新设备，在 Notifications 中选中新设备并`Check it out`->`CONFIGURE`，按照弹框步骤将设备添加到指定的区域即可完成配置。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/m5cores3ha/guide_m5cores3_esphomeburnner_10.png" width="70%"/>

2. 若未收到新设备提示消息，也可导航至`Settings`->`Device & services`查看设备情况。点击`Add`即可添加设备至 Home Assistant。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_add_ha_integration.webp" width="30%"/>

Dashboard 示例：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_ha_dashboard.webp" width="30%"/>

点击相机实体，可以查看实时预览画面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/unit_poe_cam_w_v1_rev1_snapshot.webp" width="50%"/>

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115625133344824&bvid=BV1EVSLBYE32&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/uldebtRwAog?si=pqhdT0k_B2YAzONf" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
