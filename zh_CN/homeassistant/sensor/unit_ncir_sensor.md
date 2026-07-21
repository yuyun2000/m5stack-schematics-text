# Unit NCIR Home Assistant 集成

本教程将介绍如何使用 **Unit NCIR** 单点红外测温传感器集成至 Home Assistant，实现非接触温度监测。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/715/NCIR-Home_Assistant_tutorial_cover_ZH.png" width="60%">

## 准备工作

- ESPHome 支持 MLX90614：[MLX90614 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/MLX90614-Datasheet-Melexis_en.pdf)
- 最新的配置参考：[MLX90614 非接触式红外测温仪](https://esphome.io/components/sensor/mlx90614/)

## 注意事项

Unit NCIR 只是单独的传感器平台，需要额外的主控设备（如 Atom 系列、Stamp 系列， Stick 系列，Core/Basic 系列等）才能集成至 Home Assistant。

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

**Unit NCIR 配置的范例：**

```yaml line-num
sensor:
  - platform: mlx90614
    ambient:
      name: Ambient
    object:
      name: Object
    update_interval: 10s
```

## 开始使用

当添加至 Dashboard 之后，您可以在 Home Assistant 中查看传感器数据：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/715/unit_ncir_ha_dashboard.png" width="30%" />

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115904222396776&bvid=BV12nrkBPEkH&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/D50et0Ruqbw?si=usRdzW_S7g0vQ85l" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
