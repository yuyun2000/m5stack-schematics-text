# AtomS3R + Atomic Voice Base 语音助手

本教程介绍如何将 AtomS3R + Atomic Voice Base 结合，集成语音助手功能进入 Home Assistant。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/S3R-Atomic-Home_Assistant_tutorial_cover_ZH.png" width="60%">

## 准备工作

- 参考[Home Assistant 官网文档](https://www.home-assistant.io/getting-started/)安装 Home Assistant `2025.12.3及以上版本`。
- 参考以下教程完成语音识别相关插件安装和配置。
  - [Home Assistant Cloud](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/)。
  - [Assist Pipeline](https://www.home-assistant.io/voice_control/voice_remote_local_assistant)。
- 在 `Setting` -> `Add-ons` -> `Add-ons STORE` 中安装 ESPHome 插件。
- ESPHome 插件安装成功后，在 ESPHome 管理页面点亮`Show in sidebar`将其添加至左侧导航栏。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_ha_setting_1.webp" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_ha_setting_2.webp" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_add_on_esp_builder.webp" width="70%"/>

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 AtomS3R + Atomic Voice Base 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/atoms3r_echo_base_voice_assistant_manifest_2026.3.0.json">一键烧录固件</EspWebTool>

## 注意事项

- 2026-02：解决新版 ESPHome API 变更导致的编译错误，新版本在 ESPHome 2025.1.2 下编译，如遇见问题可以考虑切换到此版本。

## 创建设备

1. 打开 ESPHome 插件页面，右下角点击 `NEW DEVICE`，创建一个新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_1.webp" width="70%"/>

2. 弹窗点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_2.webp" width="30%"/>

3. 选择 `New Device Setup`，创建新的配置文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_3.webp" width="30%"/>

4. 填写配置文件名称。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_esp_builder_naming.webp" width="30%"/>

5. 选择设备类型，点击`ESP32-S3`即可。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_esp_builder_select_device.webp" width="30%"/>

6. 复制 Home Assistant API Encryption Key 备用，点击 `Skip`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_7.webp" width="30%"/>

## 修改配置

1. 在新生成的配置处点击 `EDIT`，修改配置。(Wi-Fi 配置默认为当前 HA 服务器的 Wi-Fi 配置，也可以根据实际情况配置 `ssid`, `password` 等选项)。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_esp_builder_new_file.webp" width="40%"/>

2. 添加下方资源包配置链接，为设备添加语音助手的功能组件。

```yaml
packages:
  m5stack.atoms3r-with-echo-base: github://m5stack/esphome-yaml/common/atoms3r-with-echo-base.yaml@main
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_esp_builder_edit_config.webp" width="70%"/>

3. 点击右上角`SAVE`, `INSTALL`，弹出的安装方式中选择 `Manual download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_esp_builder_install_select.webp" width="40%"/>

\#> 固件编译提示：| 通过 HA 进行固件编译较为耗费资源，首次编译可能会需要较长时间进行资源下载，跟实际部署 HA 服务的设备以及网络质量相关。

## 下载和烧录固件

1. 完成固件编译后，点击 `Download` 按钮，选择 `Factory Format (Previously Modern)` 格式固件下载到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_esp_builder_download_select.webp" width="70%"/>

2. 点击 `Open ESPHome Web` 使用 web 烧录工具烧录。

\#> 提示 | 在下载选项界面可以点击 [`Open ESPHome Web`](https://web.esphome.io/)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_13.webp" width="40%"/>

3. 组装 AtomS3R 和 Atomic Voice Base，将 AtomS3R 设备通过 USB-C 数据线连接电脑，长按复位键直至绿灯亮起松开，使其进入下载模式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/download%20mode.gif" width="40%"/>

4. 在 Open ESPHome Web 中点击 `CONNECT` 连接设备，选择对应的设备端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_1.webp" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_2.webp" width="70%"/>

5. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_3.webp" width="70%"/>

6. 选择先前步骤完成编译的 `*.bin` 文件，再次点击 `INSTALL` 按钮进行烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_webesp_select_firmware.webp" width="40%"/>

等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_success.webp" width="40%"/>

## 开始使用

1. 完成固件烧录后，设备开机将自动进行 Wi-Fi 连接。同一局域网内的 Home Assistant 服务将会提示新设备发现，在 `Notifications` 中选中新设备并 `Check it out`->`CONFIGURE`，按照弹框步骤将设备添加到指定的区域即可完成配置。若未收到新设备提示消息，点击 `Settings`->`Device & services` 可查看设备情况。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_ha_device_discovery.webp" width="40%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_ha_device_discovery_add.webp" width="40%"/>

2. 接下来可以继续设置 Voice Assistant，也可以跳过此步骤之后再设置。

- 测试唤醒词。<br><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_setting_voice_assistant_1.webp" width="40%"/>

- 选择区域。<br><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_setting_voice_assistant_2.webp" width="40%"/>

- 选择 Pipeline。<br><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_setting_voice_assistant_3.webp" width="40%"/>

- 完成设置。<br><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_ha_va_configuration.webp" width="40%"/>

完成设备添加，以及在准备步骤环节 [Home Assistant Cloud](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/) 和 [Assist pipeline](https://www.home-assistant.io/voice_control/voice_remote_local_assistant) 插件的配置后。即可使用唤醒词 "Okay Nabu"，唤醒语音助手。

效果演示视频：

<video width="320" controls preload="auto">
<source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_echo_base_voice_assistant_demo.webm" type="video/webm">
</video>

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115998527065005&bvid=BV1JdFPzhEEz&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/BP2xPqK6Cnw?si=w2MYeIhkUTJnKhEX" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
