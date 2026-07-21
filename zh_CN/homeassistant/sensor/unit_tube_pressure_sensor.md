# Unit Tube Pressure Home Assistant 集成

本教程将介绍如何使用 **Unit Tube Pressure** 正负压力表集成至 Home Assistant，实现气体压力实时监测。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/730/tube-Home_Assistant_tutorial_cover_ZH.png" width="60%">

## 准备工作

- Home Assistant 主机。
- 在 Home Assistant 中安装并启用 [ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。

## 注意事项

本教程中，固件使用 ESPHome 2025.12.5 进行编译和上传。如果遇到编译 / 上传问题，请考虑切换到此版本的 ESPHome。

## 创建设备

1. 创建新设备。点击右下角的绿色按钮创建设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%"/>

2. 创建设备名称。

- 点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%"/>

- 点击 `New Device Setup`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%"/>

- 输入设备名称并点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/730/HA62.webp" width="30%"/>

3. 选择设备类型。

- 点击 `ESP32-S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA5.webp" width="30%"/>

- 点击 `SKIP`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%"/>

- 开始编辑 YAML 文件。点击 `EDIT`。我们可以通过 YAML 文件自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/730/HA63.webp" width="70%"/>

## 修改配置

### 传感器配置

这里的 GPIO 引脚分配可能因使用的主控制器而异。例如，当使用 **AtomS3R** 作为主控制器时：

- 添加 [Sensor](https://esphome.io/components/sensor) 组件。

```yaml
sensor:
  - platform: adc
    pin: GPIO1
    id: adc_voltage
    attenuation: 11db
    update_interval: 100ms
    unit_of_measurement: "V"
    accuracy_decimals: 3

  - platform: template
    name: "Pressure"
    unit_of_measurement: "kPa"
    accuracy_decimals: 2
    update_interval: 100ms
    lambda: |-
      float K = 100.0;
      float B = 110.0;
      float voltage = id(adc_voltage).state;
      float P = voltage * K - B;
      return P;
```

## 下载和烧录固件

1. 修改完成后，点击右上角的 `SAVE` 和 `INSTALL`，在弹窗中选择 `Manual Download`进行编译。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

2. 固件编译完成后，点击 Download 并选择 `Factory format(Previously Modern)`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%"/>

\#> 提示 | 点击 [Unit Tube Pressure](https://github.com/m5stack/esphome-yaml/blob/main/examples/sensor/unit-tube-pressure.yaml) 查看完整的示例配置。首次构建可能需要一些时间，具体取决于 Home Assistant 主机的性能和网络质量。

3. 通过 USB Type‑C 线将设备连接到主机。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT` 连接到设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%"/>

4. 找到对应的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA13.webp" width="40%"/>

5. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%"/>

6. 选择编译好的固件进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/730/HA67.webp" width="40%"/>

7. 烧录完成后，重新启动设备。

## 开始使用

1. 点击 `Settings` -> `Device & services` 检查设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%"/>

2. 我们可以在 `Discover` 部分找到相应的设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/730/HA66.webp" width="40%"/>

3. 添加设备后，数据将正确显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/730/HA9.webp" width="40%"/>

4. 最后，我们将这些实体添加到仪表板，以下显示了它们的显示效果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/730/HA10.webp" width="40%"/>

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=116026914113223&bvid=BV1YfFnzYEb9&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/GvLSAkVfrUs?si=7uYTyKN2h2AfAumi" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
