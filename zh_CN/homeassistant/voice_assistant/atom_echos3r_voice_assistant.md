# Atom VoiceS3R 语音助手

本章节介绍如何将 Atom VoiceS3R 配置为 Home Assistant 语音助手。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/Echo-s3r-Home_Assistant_tutorial_cover_ZH.png" width="60%">

## 准备工作

- 参考 [Home Assistant 官网文档](https://www.home-assistant.io/getting-started/) 安装 Home Assistant。
- 在 `Setting` -> `Add-ons` -> `Add-ons STORE` 中安装 ESPHome Builder 插件。
- ESPHome Builder 插件安装成功后，在其管理页面选中 `Show in sidebar` 将其添加至左侧导航栏。
- 本教程参考自 [ESPHome 官方使用文档](https://esphome.io/guides/getting_started_hassio)，如有需要可自行访问。
- 参考以下教程完成语音识别相关插件安装和配置。
  - [Home Assistant Cloud](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/)。
  - [Assist Pipeline](https://www.home-assistant.io/voice_control/voice_remote_local_assistant)。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-1.png" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-2.png" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-3.png" width="70%"/>

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 Atom VoiceS3R 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/atom_echos3r_voice_assistant_manifest_2026.3.0.json">一键烧录固件</EspWebTool>

## 注意事项

\#> 更改日志 |
**2026-02** 解决新版 ESPHome API 变更导致的编译错误，新版本在 ESPHome 2025.1.2 下编译，如遇见问题可以考虑切换到此版本<br>
**2026-01** 优化使用体验，解决部分编译警告<br>
**2025-09** 在 ESPHome 2025.9.0 下编译测试

## 创建设备

1. 打开 ESPHome 插件页面，右下角点击 `NEW DEVICE`，创建一个新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-4.png" width="70%"/>

2. 出现 New device 提示界面，点击 `CONTINUE` 按钮。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-5.png" width="30%"/>

3. 点击`New Device Setup`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_new_device_setup_1.webp" width="30%"/>

4. 为配置取一个合适的名称。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_new_device_setup_2.webp" width="30%"/>

5. 首先取消勾选`Use recommended settings`，接着设备选择`ESP32S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_new_device_setup_3.webp" width="30%"/>

6. 弹窗会提示选择合适的设备，这里我们选用`Espressif ESP32-S3-Box`，继续下一步设置 Home Assistant API Key 和 YAML 配置文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_new_device_setup_4.webp" width="30%"/>

7. 复制 API Key 备用，之后点击`Skip`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_new_device_setup_5.webp" width="30%"/>

8. 在生成的配置文件下点击`Edit`继续修改生成的 YAML 文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_new_device_setup_6.webp" width="30%"/>

## 修改配置

1. YAML 配置文件示例如下，添加`packages`选项至末尾。

```yaml line-num
esphome:
  name: atom-echos3r-voice-assistant
  friendly_name: Atom Echo S3R Voice Assistant

esp32:
  board: esp32s3box
  framework:
    type: esp-idf

# Enable logging
logger:

# Enable Home Assistant API
api:
  encryption:
    key: "***********************"

ota:
  - platform: esphome
    password: "************************"

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Atom-EchoS3R-Voice-Assistant"
    password: ""

captive_portal:

# Add the external package here
packages:
  remote_package_files:
    url: https://github.com/m5stack/esphome-yaml
    files: [common/atom-echos3r-satellite-base.yaml]
    ref: main
    refresh: 0s
```

2. 点击`Save`，`Install`进行安装。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_save_install.webp" width="60%"/>

3. 根据实际情况，选择您的安装方式。一般情况下，如果设备已经连接至 Home Assistant 主机，并且进入了下载模式，可以选择`Plug into the computer running ESPHome Device Builder`，之后选择串口设备进行编译上传。

这里我们用`Manual download`做示范：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_install_options.webp" width="30%"/>

\#> 注意 | 初次安装时间可能较长，取决于您的网络连接和 Home Assistant 主机性能。

## 下载和烧录固件

1. 编译完成后，接着点击`Open ESPHome Web`，同时，选择`Factory format`下载固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_firmware_download.webp" width="50%"/>

2. 在 ESPHome Web 页面，点击`CONNECT`连接您的设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_1.webp" width="50%"/>

3. 选择正确的串行端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_espweb_select_device.webp" width="50%"/>

4. 点击`INSTALL`，上传固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_espweb_upload_firmware.webp" width="30%"/>

5. 等待烧录完成，RESET 设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_success.webp" width="30%"/>

## 开始使用

1. 设备上电后会自动连接 WiFi，同一局域网内的 Home Assistant 设备会提示发现新设备。可以在 Notifications 中找到设备，点击`Check it out`进行配置。
2. 如果没有通知提醒，可以点击`Settings -> Devices & Services`下寻找设备并配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_device_discovery_1.webp" width="60%"/>

3. 点击`Add`添加集成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echo_s3r_ha_discovery_2.webp" width="60%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echo_s3r_ha_add_integration.webp" width="30%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echo_s3r_ha_add_integration_2.webp" width="30%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_ha_va_config.webp" width="60%"/>

4. 设置了正确的 Pipeline 之后，尝试使用`Okay Nabu`唤醒词唤醒设备。

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115502139639192&bvid=BV13L2FBKEik&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/pQ5rE5gH4x4?si=BkvOBysZ8sd-_6-0" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
