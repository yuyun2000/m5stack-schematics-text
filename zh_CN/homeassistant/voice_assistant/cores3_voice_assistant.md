# CoreS3 HA 语音助手

本章节介绍如何将 CoreS3 配置为 Home Assistant 语音助手。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-96063e2a-637a-4d11-ac47-1ce4f1cdfd3e.webp" width="40%"/>

## 准备工作

1. 参考[Home Assistant 官网文档](https://www.home-assistant.io/getting-started/)安装 Home Assistant。
2. 参考以下教程完成语音识别相关插件安装和配置。

- [Home Assistant Cloud](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/)。
- [Assist Pipeline](https://www.home-assistant.io/voice_control/voice_remote_local_assistant)。

3. 在`Setting`->`Add-ons`->`Add-ons STORE`中安装 ESPHome 插件。
4. ESPHome 插件安装成功后，在 ESPHome 管理页面点亮`Show in sidebar`将其添加至左侧导航栏。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_ha_setting_1.webp" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_ha_setting_2.webp" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_ha_setting_3.webp" width="70%"/>

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 CoreS3 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/cores3_voice_assistant_manifest_2026.3.0.json">一键烧录固件</EspWebTool>

## 注意事项

\#> 更改日志 |
**2026-02** 解决新版 ESPHome API 变更导致的编译错误，新版本在 ESPHome 2025.1.2 下编译，如遇见问题可以考虑切换到此版本<br>
**2026-01** 优化使用体验，解决部分编译警告<br>
**2025-10** 在 ESPHome 2025.10.0 下编译测试

- 通过 HA 进行固件编译较为耗费资源，首次编译可能会需要较长时间进行资源下载，跟实际部署 HA 服务的设备以及网络质量相关。
- 在下载选项界面可以点击[`Open ESPHome Web`](https://web.esphome.io/)。

## 创建设备

1. 打开 ESPHome 插件页面，右下角点击`NEW DEVICE`，创建一个新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_1.webp" width="70%"/>

2. 弹窗点击`CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_2.webp" width="30%"/>

3. 选择`New Device Setup`，创建新的配置文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_3.webp" width="30%"/>

4. 填写配置文件名称。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_4.webp" width="30%"/>

5. 选择设备类型，首先取消勾选`Use recommended settings`，然后点击`ESP32-S3`，选择`M5Stack CoreS3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_5.webp" width="30%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_6.webp" width="30%"/>

6. 复制 Home Assistant API Encryption Key 备用，点击`Skip`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_7.webp" width="30%"/>

## 修改配置

1. 点击设备左下角`EDIT`，修改 WiFi 连接配置。(Wi-Fi 配置默认为当前 HA 服务器的 Wi-Fi 配置，也支持直接修改为明文的方式:ssid:"xxxx")。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_8.webp" width="70%"/>

2. 添加下方资源包配置链接，为设备添加语音助手的功能组件。

```yaml
packages:
  remote_package_files:
    url: https://github.com/m5stack/esphome-yaml
    files: [common/cores3-satellite-base.yaml]
    ref: main
    refresh: 0s
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_9.webp" width="70%"/>

3. 之后点击右上角`SAVE`, `INSTALL`，弹出的安装方式中选择`Manual download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_10.webp" width="70%"/>

## 下载和烧录固件

1. 完成固件编译后，点击 `Download` 按钮，选择`Modern Format`格式固件下载到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_11.webp" width="70%"/>

2. 点击`Open ESPHome Web`使用 web 烧录工具烧录，或是通过 esptool 等其他工具进行烧录，固件烧录起始地址为 0x00。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_12.webp" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_13.webp" width="30%"/>

3. 将 CoreS3 设备通过 USB-C 数据线连接电脑，长按复位键直至绿灯亮起松开，使其进入下载模式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%"/>

4. Open ESPHome Web 中点击 Connect 连接设备，选择对应的设备端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_1.webp" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_2.webp" width="70%"/>

5. 点击 `INSTALL`，选择先前步骤完成编译的`*.bin`文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_3.webp" width="70%"/>

6. 再次点击`INSTALL` 按钮进行烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_4.webp" width="70%"/>

7. 等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_success.webp" width="30%"/>

## 开始使用

1. 完成固件烧录后，设备开机将自动进行 Wi-Fi 连接。同一局域网内的 Home Assistant 服务将会提示新设备发现，在 Notifications 中选中新设备并`Check it out`->`CONFIGURE`，按照弹框步骤将设备添加到指定的区域即可完成配置。若未收到新设备提示消息，点击`Settings`->`Device & services`可查看设备情况。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/m5cores3ha/guide_m5cores3_esphomeburnner_10.png" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_ha_add_device_1.webp" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_ha_add_device_2.webp" width="40%"/>

2. 接下来可以继续设置 Voice Assistant，也可以跳过此步骤之后再设置。

- 测试唤醒词。<br><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_setting_voice_assistant_1.webp" width="40%"/>

- 选择区域。<br><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_setting_voice_assistant_2.webp" width="40%"/>

- 选择 Pipeline。<br><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_setting_voice_assistant_3.webp" width="40%"/>

- 完成设置。<br><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_setting_voice_assistant_4.webp" width="40%"/>

3. 完成设备添加，以及在准备步骤环节[Home Assistant Cloud](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/)和[Assist pipeline](https://www.home-assistant.io/voice_control/voice_remote_local_assistant)插件的配置后。即可使用唤醒词 "ok nabu"，唤醒语音助手。

## 相关视频

<video loop playsinline controls width="100%" height="auto" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_voice_assistant_720p.webm"/>
