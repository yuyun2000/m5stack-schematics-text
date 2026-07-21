# Unit ENV-Pro 传感器 Home Assistant 集成

本章节介绍将 Unit ENV-Pro 环境检测传感器集成至 Home Assistant 的配置方法与实操步骤。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/725/Unit-ENV-Pro-Home_Assistant_tutorial_cover_ZH.png" width="60%"/>

## 注意事项

因为 Unit ENV-Pro 只是单独的传感器平台，需要额外的主控设备（如 Atom 系列、Stamp 系列， Stick 系列，Core/Basic 系列等）才能集成至 Home Assistant，如上组件使用了专有软件 `BSEC2`，BSEC2 库仅在接受其[软件许可协议](https://www.bosch-sensortec.com/media/boschsensortec/downloads/software/bme688_development_software/2024_12/20241219_clickthrough_license_terms_bsec_bme680_bme688_bme690.pdf)后方可使用。通过在配置中启用此组件，即表示您**明确同意** BSEC 许可协议的条款。请注意，该许可**禁止分发**包含此组件的任何编译固件二进制文件。

## 准备工作

1. 参考 ESPHome 官方文档：[bme68x_bsec2](https://esphome.io/components/sensor/bme68x_bsec2/)
2. 准备兼容的主控设备（如 Atom 系列、Stamp 系列、Stick 系列、Core/Basic 系列等）
3. 确认主控设备的 I2C 引脚定义（不同主控引脚不同）

## 配置传感器

在 ESPHome 配置中启用 [I²C](https://esphome.io/components/i2c/#i2c) 组件：

```yaml
# Example configuration entry for ESP32
i2c:
  sda: GPIOXX
  scl: GPIOXX
  scan: true
```

这里的 GPIO 引脚会因为使用的主控设备不一而不同。比如使用 Atom Lite 作为主控：

```yaml
# I2C Bus on Grove Port (HY2.0-4P)
i2c:
  sda: GPIO26
  scl: GPIO32
```

Unit ENV-Pro 配置范例

- 组件声明

```yaml line-num
bme68x_bsec2_i2c:
  address: 0x77
  model: bme688
```

- 传感器

```yaml line-num
text_sensor:
  - platform: bme68x_bsec2
    iaq_accuracy:
      name: "BME68x IAQ Accuracy"
  - platform: template
    name: "BME68x IAQ Classification"
    lambda: |-
      if ( int(id(iaq).state) <= 50) {
        return {"Excellent"};
      }
      else if (int(id(iaq).state) >= 51 && int(id(iaq).state) <= 100) {
        return {"Good"};
      }
      else if (int(id(iaq).state) >= 101 && int(id(iaq).state) <= 150) {
        return {"Lightly polluted"};
      }
      else if (int(id(iaq).state) >= 151 && int(id(iaq).state) <= 200) {
        return {"Moderately polluted"};
      }
      else if (int(id(iaq).state) >= 201 && int(id(iaq).state) <= 250) {
        return {"Heavily polluted"};
      }
      else if (int(id(iaq).state) >= 251 && int(id(iaq).state) <= 350) {
        return {"Severely polluted"};
      }
      else if (int(id(iaq).state) >= 351) {
        return {"Extremely polluted"};
      }
      else {
        return {"error"};
      }

sensor:
  - platform: bme68x_bsec2
    temperature:
      name: "Temperature"
    pressure:
      name: "Pressure"
    humidity:
      name: "Humidity"
    iaq:
      id: iaq
      name: "IAQ"
    co2_equivalent:
      name: "CO2 Equivalent"
    breath_voc_equivalent:
      name: "Breath VOC Equivalent"
```

\#> 注意 | 由于使用了`BSEC2` 库，传感器的 `update_interval` 配置选项将无法使用（无法配置拉取间隔时间），数据由专有库中进行处理和发布。

## 开始使用

1. 完成配置和上传后，将传感器添加至 Home Assistant

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/725/unit_env_pro_sensor_ha_dash.webp" width="40%" />

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115879492716621&bvid=BV1FSr8BdECw&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/nAtJMryvmuI?si=Dz-ZoLFtU9avqt1s" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
