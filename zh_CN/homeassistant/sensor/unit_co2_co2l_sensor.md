# Uint CO2/CO2L Home Assistant 集成

本教程将介绍如何使用 **Uint CO2/CO2L** 传感器集成至 Home Assistant，实现二氧化碳、温湿度实时监测。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/726/co2-Home_Assistant_tutorial_cover_ZH.png"  width="60%">

## 准备工作

- [SCD4x Datasheet](https://sensirion.com/media/documents/48C4B7FB/67FE0194/CD_DS_SCD4x_Datasheet_D1.pdf)
- [SCD4X CO₂ 与温湿度传感器](https://esphome.io/components/sensor/scd4x/)

## 注意事项

Unit CO2/CO2L 只是单独的传感器平台，需要额外的主控设备（如 Atom 系列、Stamp 系列， Stick 系列，Core/Basic 系列等）才能集成至 Home Assistant。

## 修改配置

需要在 ESPHome 配置中启用 [I²C](https://esphome.io/components/i2c/#i2c) 组件：

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

**Unit CO2/CO2L 配置的范例：**

```yaml line-num
sensor:
  - platform: scd4x
    co2:
      name: "CO2"
    temperature:
      name: "Temperature"
    humidity:
      name: "Humidity"
```

## 开始使用

当添加至 Dashboard 之后，您可以在 Home Assistant 中查看传感器数据

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/726/unit_co2_ha_scd40_41.png" width="30%" />

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115800941791462&bvid=BV1FmvpBpEpD&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/QfcLb382CG0?si=nvMC4epC4MsjNUvX" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
