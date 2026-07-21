# Uint ENV-IV 传感器 Home Assistant 集成

本章节介绍将 Uint ENV-IV 传感器平台集成至 Home Assistant 的配置方法与实操步骤。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/724/Unit-env-IV-Home_Assistant_tutorial_cover_ZH.png" width="60%" />

## 准备工作

1. 确认使用的传感器支持 ESPHome 集成：

- BMP280 温度气压传感器：[BMP280 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ENV%E2%85%A3%20Unit/BMP280.pdf)
- SHT40 温湿度传感器：[SHT40 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ENV%E2%85%A3%20Unit/SHT40.pdf)

2. 参考 ESPHome 官方文档获取最新配置说明：

- [BMP280 温度气压传感器 ESPHome 配置](https://esphome.io/components/sensor/bmp280/)
- [SHT4X 温湿度传感器 ESPHome 配置](https://esphome.io/components/sensor/sht4x/)

## 注意事项

Unit ENV-IV 只是单独的传感器平台，需要额外的主控设备（如 Atom 系列、Stamp 系列， Stick 系列，Core/Basic 系列等）才能集成至 Home Assistant。

## 修改配置

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

Unit ENV-IV 配置的范例：

```yaml line-num
sensor:
  - platform: sht4x
    temperature:
      id: sht40_temp
      name: "Temperature"
    humidity:
      id: sht40_humi
      name: "Relative Humidity"
    address: 0x44

  - platform: bmp280_i2c
    temperature:
      name: "BMP280 Temperature"
      id: bmp280_temp
      oversampling: 16x
    pressure:
      name: "BMP280 Pressure"
      id: bmp_pressure
    address: 0x76
```

同样，你可以依据一些经验性的公式，计算如`海拔`，`绝对湿度`和`露点(温度)` （计算结果仅供参考）：

- [海拔计算](https://en.wikipedia.org/wiki/Atmospheric_pressure#Altitude_variation)
- [绝对湿度计算](https://wahiduddin.net/calc/density_altitude.htm)
- [露点温度计算](https://carnotcycle.wordpress.com/2017/08/01/compute-dewpoint-temperature-from-rh-t/)

```yaml line-num
sensor:
  ...
  # add the following under the previous sensor declarations
  - platform: template
    name: "Altitude"
    lambda: |-
      const float STANDARD_SEA_LEVEL_PRESSURE = 1013.25; //in hPa, see note
      return ((id(bmp280_temp).state + 273.15) / 0.0065) *
        (powf((STANDARD_SEA_LEVEL_PRESSURE / id(bmp_pressure).state), 0.190234) - 1); // in meter
    update_interval: 15s
    icon: 'mdi:signal'
    unit_of_measurement: 'm'

  - platform: absolute_humidity
    name: "Absolute Humidity"
    temperature: sht40_temp
    humidity: sht40_humi

  - platform: template
    name: "Dew Point"
    lambda: |-
      return (243.5*(log(id(sht40_humi).state/100)+((17.67*id(sht40_humi).state)/
      (243.5+id(sht40_temp).state)))/(17.67-log(id(sht40_humi).state/100)-
      ((17.67*id(sht40_temp).state)/(243.5+id(sht40_temp).state))));
    unit_of_measurement: °C
    icon: 'mdi:thermometer-alert'
```

\#> 提示 | 要使用 BMP280 气压传感器精确计算海拔高度，必须先获取您所在位置和当日的海平面标准气压值。可通过替换全局常量`STANDARD_SEA_LEVEL_PRESSURE`实现，例如从互联网实时获取该数值，或通过 MQTT 协议从固定传感器获取。

## 开始使用

1. 当添加至 Dashboard 之后，您可以在 Home Assistant 中查看传感器数据。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/724/unit_env_iv_dashboard.webp" width="30%" />

2. 监测温度变化曲线。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/724/unit_env_iv_line_chart_temp.webp" width="60%" />

\#> 提示 | 因为 BMP280 也有一个温度传感器，所以这里会有两条温度曲线。

3. 监测气压变化。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/724/unit_env_iv_line_chart_pressure.webp" width="60%" />

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115879543046487&bvid=BV1FQr8BsE6d&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/zKnmuiM3eYw?si=GKir_-RedKTzXZNh" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
