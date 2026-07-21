# Unit 4Relay Home Assistant 集成

本章节介绍将 Unit 4Relay 继电器集成至 Home Assistant 的配置方法与实操步骤。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/782/unit-4relay-Home_Assistant_tutorial_cover_ZH.png" width="60%">

## 注意事项

- 因为 Unit 4Relay 是单独的继电器 / 开关平台，需要额外的主控设备（如 Atom 系列、Stamp 系列、Stick 系列、Core/Basic 系列等）才能集成至 Home Assistant。
- 由于 Unit 4Relay 由内置的 STM32 控制，需要 `external_component` 以实现 I2C 通信控制。

## 配置继电器

需要在 ESPHome 配置中启用 [I²C](https://esphome.io/components/i2c/#i2c) 组件：

```yaml
# Example configuration entry for ESP32
i2c:
  sda: GPIOXX
  scl: GPIOXX
  scan: true
```

这里的 GPIO 引脚会因为使用的主控设备不同而不同。比如使用 Atom Lite 作为主控：

```yaml
# I2C Bus on Grove Port (HY2.0-4P)
i2c:
  sda: GPIO26
  scl: GPIO32
```

Unit 4Relay 配置范例：

```yaml line-num
external_components:
  - source: github://m5stack/esphome-yaml/components@main
    components: unit4relay
    refresh: 0s

unit4relay:

switch:
  - platform: unit4relay
    relay_1:
      name: "Relay Channel 1"
      restore_mode: RESTORE_DEFAULT_OFF
    relay_2:
      name: "Relay Channel 2"
      restore_mode: RESTORE_DEFAULT_OFF
    relay_3:
      name: "Relay Channel 3"
      restore_mode: RESTORE_DEFAULT_OFF
    relay_4:
      name: "Relay Channel 4"
      restore_mode: RESTORE_DEFAULT_OFF
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/782/unit_4_relay_pic.jpg" width="30%"/>

此处采用默认灯光控制，即开启对应通道的开关，相应 LED 会亮起。

### 可配置选项

#### 组件

```yaml
# Example configuration entry
unit4relay:
```

- **id** (_可选_, [ID](https://esphome.io/guides/configuration-types#id)): 为 Unit 4Relay 组件设置一个 id。

#### 开关

- **relay_1** (_可选_): 通道 **1** 的继电器开关。默认是 `false`（关闭），以及其它所有 [Switch](https://esphome.io/components/switch#config-switch) 支持的配置选项。

- **relay_2** (_可选_): 通道 **2** 的继电器开关。默认是 `false`（关闭），以及其它所有 [Switch](https://esphome.io/components/switch#config-switch) 支持的配置选项。

- **relay_3** (_可选_): 通道 **3** 的继电器开关。默认是 `false`（关闭），以及其它所有 [Switch](https://esphome.io/components/switch#config-switch) 支持的配置选项。

- **relay_4** (_可选_): 通道 **4** 的继电器开关。默认是 `false`（关闭），以及其它所有 [Switch](https://esphome.io/components/switch#config-switch) 支持的配置选项。

## 开始使用

将设备添加至 Dashboard 之后，您可以在 Home Assistant 中控制继电器开 / 关动作。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/782/unit_4_relay_ha_dash.png" width="30%"/>

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115926049489324&bvid=BV1AKkLBXE8c&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/RtKH7-revdA?si=sJwi7wJJ2ujOpGBi" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
