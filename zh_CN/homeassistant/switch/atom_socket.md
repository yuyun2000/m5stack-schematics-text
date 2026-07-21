# Atom Socket Home Assistant 集成

本教程将介绍如何使用 **Atom Socket** 智能插座集成至 Home Assistant，实现开关控制与能源监控。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/atom-socket-Home_Assistant_tutorial_cover_ZH.png" width="60%">

## 准备工作

- Home Assistant 主机。
- 在 Home Assistant 中安装并启用 [ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 Atom Socket 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/atom_socket_manifest_2026.3.0.json">一键烧录固件</EspWebTool>

## 注意事项

本教程使用 ESPHome 2025.12.5 编译和上传固件。如果遇到编译 / 上传问题，请考虑切换 ESPHome 版本。

## 创建设备

1. 创建新设备。点击右下角的绿色按钮创建设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%"/>

2. 创建设备名称。

2.1 点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%"/>

2.2 点击 `New Device Setup`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%"/>

2.3 输入设备名称，然后点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA1.png" width="40%"/>

3. 选择设备类型。

3.1 点击 `ESP32`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA9.webp" width="30%"/>

3.2 点击 `SKIP`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%"/>

4. 开始编辑 YAML 文件。点击 `EDIT`。我们可以通过 YAML 文件自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA2.webp" width="70%"/>

## 设备配置

以下是代码的核心部分，同时提供了相关的参考和说明。

### Uart 配置

**添加 [uart](https://esphome.io/components/uart/) 组件：**

```yaml
uart:
  rx_pin: GPIO22
  baud_rate: 4800
  parity: EVEN
```

### 传感器配置

**添加 [传感器](https://esphome.io/components/sensor) 组件：**

主要芯片模块是 [HLW8032](https://esphome.io/components/sensor/hlw8032/) 能量计量芯片，负责收集和读取电压、电流和功率等传感器数据。

```yaml
sensor:
  - platform: hlw8032
    voltage:
      name: HLW8032 Voltage
      id: hlw8032_voltage
    current:
      name: HLW8032 Current
      id: hlw8032_current
    power:
      name: HLW8032 Power
      id: hlw8032_power
    apparent_power:
      name: HLW8032 Apparent Power
      id: hlw8032_apparent_power
    power_factor:
      name: HLW8032 Power Factor
      id: hlw8032_power_factor
```

### 开关配置

**添加 [开关](https://esphome.io/components/switch/) 组件：**

```yaml
switch:
  - platform: gpio
    name: "Atom Socket"
    pin:
      number: GPIO23
      inverted: False
    restore_mode: ALWAYS_ON
```

## 下载和烧录固件

1. 进行更改后，点击右上角的 `SAVE` 和 `INSTALL`，然后在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

2. 固件编译完成后，点击下载并选择 `Factory format(Previously Modern)`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%"/>

\#> 提示 | 点击 [Atom Socket](https://github.com/m5stack/esphome-yaml/blob/main/examples/Switch/atom-socket.yaml) 查看完整的示例配置。第一次编译可能需要一段时间，具体取决于 Home Assistant 主机的性能和网络质量。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/HA39.webp" width="70%"/>

3. 通过 USB Type-C 数据线将设备连接到您的主机。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT` 以连接到设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%"/>

4. 找到对应的串行端口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%"/>

5. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%"/>

6. 选择之前编译的固件进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA5.webp" width="40%"/>

7. 烧录完成后，重新启动设备。

## 开始使用

1. 在 Home Assistant 中依次点击 `Settings` > `Devices & Services`，进入集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%"/>

2. 点击`Add`将设备集成到 Home Assistant 中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA8.webp" width="40%"/>

3. 添加设备后，数据将正确显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA7.webp" width="40%"/>

4. 最后，我们将这些实体添加到仪表板，下面显示它们的显示结果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA41.webp" width="40%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA10.jpg" width="40%"/>

\#> 提示 | 仅当继电器开关打开时，**HLW8032 视在功率** 和 **HLW8032 功率** 才会显示数据。

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115998476733641&bvid=BV1JRFPzwEtr&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/aI0t43GAJd8?si=5-mVTc-Q4onHSVdw" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
