# Unit DLight 传感器 Home Assistant 集成

本章节介绍将 Unit DLight 数字环境光检测传感器集成至 Home Assistant 的配置方法与实操步骤。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/710/Unit-DLight-Home_Assistant_tutorial_cover_ZH.png" width="60%"/>

## 注意事项

Unit DLight 是单独的传感器平台，需要额外的主控设备（如 Atom 系列、Stamp 系列， Stick 系列，Core/Basic 系列等）才能集成至 Home Assistant。

## 准备工作

1. 查阅 BH1750FVI 传感器数据手册：[BH1750FVI 数据手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BH1750FVI.pdf)。
2. 参考 ESPHome 官方最新配置说明：[ESPHome BH1750 配置](https://esphome.io/components/sensor/bh1750/)。
3. 准备兼容的主控设备（如 Atom 系列、Stamp 系列、Stick 系列、Core/Basic 系列等）。
4. 确认主控设备的 I2C 引脚定义（不同主控引脚不同）。

## 配置传感器

1. 需要在 ESPHome 配置中启用 [I²C](https://esphome.io/components/i2c/#i2c) 组件：

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

以下是`sensor`配置范例：

```yaml line-num
sensor:
  - platform: bh1750
    name: "Unit DLight Illuminance"
    address: 0x23
    update_interval: 60s
```

## Dashboard 示例

完成添加至 Home Assistant 后：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/710/unit_dlight.webp" width="30%" />

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115879543048402&bvid=BV1fQr8BWEoo&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/CHT9PEZuFVM?si=0Cod6frMGoR96Gbh" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
