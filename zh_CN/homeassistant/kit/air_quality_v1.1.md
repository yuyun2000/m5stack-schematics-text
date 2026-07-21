# Air Quality V1.1 套件 Home Assistant 集成

本章节介绍将 Air Quality v1.1 空气质量监测装置集成至 Home Assistant 的方法。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/AQ_Home_Assistant_tutorial_cover_ZH.png" width="60%"/>

## 准备工作

- Home Assistant 主机
- 在 Home Assistant 中安装并启用[ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)
- 参考文档：
  - [SEN55 Datasheet](https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/Sensirion_Datasheet_Environmental_Node_SEN5x.pdf-9e2861345ac4a2cd640cc28e0e2d2a07.pdf)
  - [SCD40 Datasheet](https://static-cdn.m5stack.com/resource/docs/datasheet/unit/co2/SCD40.pdf)
- ESPHome 配置范例参考：
  - [sen5x](https://esphome.io/components/sensor/sen5x/)
  - [scd4x](https://esphome.io/components/sensor/scd4x/)

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 Air Quality V1.1 套件 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/air_quality_v1.1_manifest_2026.3.0.json">一键烧录固件</EspWebTool>

## 注意事项

- 本教程中，套件在 ESPHome 2025.10.3 下编译和上传，如果遇见编译 / 上传问题，考虑将 ESPHome 切换至此版本。

## 创建设备

1. 打开 ESPHome Builder，点击右下角点击 `NEW DEVICE`，创建一个新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_1.webp" width="70%"/>

2. 弹窗点击`CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_2.webp" width="30%"/>

3. 选择`New Device Setup`，创建新的配置文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_3.webp" width="30%"/>

4. 填写配置文件名称。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_esp_builder_4.webp" width="30%"/>

5. 选择设备类型，首先取消勾选`Use recommended settings`，然后点击`ESP32-S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_5.webp" width="30%"/>

6. 选择`M5Stack StampS3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_esp_builder_5.webp" width="30%"/>

7. 复制 API Key 备用，点击`SKIP`跳过。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_7.webp" width="30%"/>

## 修改配置

1. 在生成的配置文件卡片下点击`EDIT`进行编辑：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_edit_config_1.webp" width="40%"/>

2. 在文件末尾添加：

```yaml line-num
packages:
  air_quality_base_config:
    url: https://github.com/m5stack/esphome-yaml
    files: common/air-quality-v1-rev1-base.yaml
    ref: main
    refresh: 1d
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_edit_config_2.webp" width="70%"/>

3. 点击右上角`SAVE`, `INSTALL`，弹出的安装方式中选择`Manual download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_install_1.webp" width="40%"/>

\#> 提示：| 首次编译可能会需要较长时间，编译时间与 Home Assistant 主机性能和网络质量相关。

4. 编译完成后，点击`Download`按钮，选择`Factory Format`下载固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_install_2.webp" width="70%"/>

## 下载和烧录固件

1. 下载固件：通过 ESPHome Builder 的`Manual download`方式下载 Factory Format 固件
2. 使用 web 工具烧录固件：

- 将套件通过 USB-C 数据线连接至主机，打开[ESPHome Web](https://web.esphome.io/)，点击`CONNECT`连接设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_webesp_connect.webp" width="40%"/>

\#> 提示 | 如果无法显示设备，请参照[操作说明](/zh_CN/core/Air_Quality_v1.1#%E6%93%8D%E4%BD%9C%E8%AF%B4%E6%98%8E)进入下载模式。

- 点击`INSTALL`，选择之前编译的固件进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_webesp_install.webp" width="40%"/>

- 再次点击`INSTALL`进行烧录，等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_success.webp" width="30%"/>

## 开始使用

1. 完成固件烧录后，设备开机将自动进行 Wi-Fi 连接。Home Assistant 服务自动发现新设备，在 Notifications 中选中新设备并`Check it out`->`CONFIGURE`，按照弹框步骤将设备添加到指定的区域即可完成配置。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/home_assistant/m5cores3ha/guide_m5cores3_esphomeburnner_10.png" width="70%"/>

2. 若未收到新设备提示消息，也可导航至`Settings`->`Device & services`查看设备情况。点击`Add`即可添加设备至 Home Assistant。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_add_ha_integration.webp" width="40%"/>

3. Dashboard 示例：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_ha_dashboard.webp" width="50%"/>

4. 按下 USER_A/USER_B 按键可以切换页面，显示更多信息。

<div style="display: flex; gap: 15px; flex-wrap: wrap; justify-content: center;">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_epaper_page_1.jpg" width="30%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_epaper_page_2.jpg" width="30%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/air_quality_v1_rev1_epaper_page_3.jpg" width="30%"/>
</div>

\#> 提示 | 1. 墨水屏屏显上的时间源来自 Home Assistant，当连接到 Home Assistant 后会自动同步时间。<br>2. 传感器数据需要一段时间采样后才能输出到屏显（最短 1 分钟）, 且开启 Wi-Fi 持续工作会导致功耗增加，电池电量消耗快，建议**连接电源**使用以获取更稳定的读数。

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115587166505549&bvid=BV13vUVB2EQm&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Mu7A06BUWls?si=6K3E6LYb9qQYt4rf" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
