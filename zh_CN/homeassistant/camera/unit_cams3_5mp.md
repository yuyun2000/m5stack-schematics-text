# Unit CamS3-5MP Home Assistant 集成

本教程指导你将 Unit CamS3-5MP 摄像头模块接入 Home Assistant。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/CamS3-5MP-Home_Assistant_tutorial_cover_ZH.png" width="60%">

## 准备工作

- Home Assistant 主机
- 在 Home Assistant 中安装并启用 [ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 Unit CamS3-5MP 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/unit_cams3_5mp_manifest_2026.1.1.json">一键烧录固件</EspWebTool>

## 注意事项

- 本教程使用 ESPHome 2025.12.5 编译和上传固件。如果遇到编译 / 上传问题，请考虑切换 ESPHome 版本。

## 创建设备

1. 点击右下角的绿色按钮创建设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="90%"/>

2. 点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%"/>

3. 点击 `New Device Setup`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%"/>

4. 输入设备名称，然后点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/HA31.webp" width="30%"/>

5. 点击 `ESP32-S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA5.webp" width="30%"/>

6. 点击 `SKIP`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%"/>

7. 点击 `EDIT`。我们可以通过 YAML 文件自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/HA30.webp" width="50%"/>

## 修改配置

以下是代码的核心部分。下面提供了相关的参考和说明。

### PSRAM 配置

**添加 [PSRAM](https://esphome.io/components/psram/) 组件：**

```yaml
psram:
  mode: octal
  speed: 80MHz
```

### 开关配置

**添加 [Switch](https://esphome.io/components/switch/) 组件：**

```yaml
switch:
  - platform: gpio
    name: "Active LED"
    pin:
      number: GPIO14
      inverted: true
    restore_mode: ALWAYS_ON
```

### I2C 总线配置

**添加 [I2C](https://esphome.io/components/i2c/) 组件：**

```yaml
i2c:
  - id: camera_i2c
    sda: GPIO17
    scl: GPIO41
    scan: true
```

### 摄像头配置

**添加 [ESP32 Camera](https://esphome.io/components/esp32_camera/) 组件：**

```yaml
esp32_camera:
  name: "PY260 camera"
  external_clock:
    pin: GPIO11
    frequency: 20MHz
  i2c_id: camera_i2c
  data_pins: [GPIO6, GPIO15, GPIO16, GPIO7, GPIO5, GPIO10, GPIO4, GPIO13]
  vsync_pin: GPIO42
  href_pin: GPIO18
  pixel_clock_pin: GPIO12
  reset_pin: GPIO21
  resolution: 1024x768
  jpeg_quality: 12
```

## 下载和烧录固件

1. 进行更改后，点击右上角的 `SAVE` 和 `INSTALL`，然后在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

2. 固件编译完成后，点击 Download 并选择 `Factory format(Previously Modern)`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%"/>

\#> 提示 | 点击 [Unit CamS3-5MP](https://github.com/m5stack/esphome-yaml/blob/main/examples/camera/unit-cams3-5mp.yaml) 查看完整的示例配置。首次构建可能需要一些时间，具体取决于 Home Assistant 主机的性能和网络质量。

3. 上传固件，有两种方式：

- 硬件连接指南：将摄像头模块连接到 4 针电缆 → 将电缆的另一端插入 USB 适配器 → 使用 USB-C 数据线连接到计算机或电源 → 通电后，设备即可进行固件刷写或数据传输。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/CamS3_5MP_Connect.png" width="40%"/>

- 通过 USB Type‑C 数据线将设备连接到主机。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT` 以连接到设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%"/>

4. 定位相应的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA13.webp" width="40%"/>

5. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%"/>

6. 选择之前编译的固件上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/HA32.webp" width="40%"/>

7. 烧录完成后，重新启动设备。

## 开始使用

1. 点击 `Settings` -> `Device & services` 检查设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%"/>

2. 我们可以在 `Discover` 部分找到相应的设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/HA34.webp" width="40%"/>

3. 添加设备后，数据将正确显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/HA35.webp" width="40%"/>

4. 最后，我们将这些实体添加到 Dashboard，以下是其显示结果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/HA36.webp" width="40%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/HA37.webp" width="40%"/>

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115998493508939&bvid=BV1nXFPzYER5&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/NzMN4lFXivs?si=yOT258AzBRaiceFV" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
