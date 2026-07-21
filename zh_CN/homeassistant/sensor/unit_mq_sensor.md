# Unit MQ 传感器 Home Assistant 集成<!--不需要重复介绍产品了-->

本章节介绍将 Unit MQ 可燃气体检测单元集成至 Home Assistant 的配置方法与实操步骤。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Unit-MQ-Home_Assistant_tutorial_cover_ZH.png" width="60%"/>

## 注意事项

Unit MQ 是单独的传感器平台，需要额外的主控设备（如 Atom 系列、Stamp 系列， Stick 系列，Core/Basic 系列等）才能集成至 Home Assistant。

## 准备工作

1. 查阅相关文档：

- [通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/MQ_I2C_Protocol_CN.pdf)
- [MQ5 Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Gas_Sensor_MQ-5_datasheet.pdf)

2. 准备兼容的主控设备（如 Atom 系列、Stamp 系列、Stick 系列、Core/Basic 系列等）。
3. 确认主控设备的 I2C 引脚定义（不同主控引脚不同）。

## 配置传感器

1. 需要在 ESPHome 配置中启用 [I²C](https://esphome.io/components/i2c/#i2c) 组件：

```yaml line-num
# Example configuration entry for ESP32
i2c:
  sda: GPIOXX
  scl: GPIOXX
  scan: true
```

这里的 GPIO 引脚会因为使用的主控设备不一而不同。比如使用 Atom Lite 作为主控：

```yaml line-num
# I2C Bus on Grove Port (HY2.0-4P)
i2c:
  sda: GPIO26
  scl: GPIO32
```

Unit MQ 配置的范例：

```yaml line-num
external_components:
  - source: github://m5stack/esphome-yaml/components@main
    components: m5stack_unit_mq
    refresh: 0s

sensor:
  - platform: m5stack_unit_mq
    heat_mode: SWITCH
    temperature:
      id: mq_temp
      name: "Unit MQ Temperature"
    mq_adc:
      id: mq_adc_val
      name: "MQ ADC"
    ntc_adc:
      id: ntc_adc_val
      name: "NTC ADC"
    ntc_resistance:
      id: ntc_resistance_val
      name: "NTC Resistance"
    reference_voltage:
      id: in_ref_volt
      name: "Internal Reference Voltage"
    mq_voltage:
      id: mq_volt
      name: "MQ Voltage"
    ntc_voltage:
      id: ntc_volt
      name: "NTC Voltage"
    led:
      id: mq_led
      name: "MQ LED Status"
    update_interval: 20s
```

可配置选项：

- **heat_mode** (**Required**): Unit MQ 加热模式，可选`CONTINUOUS` (持续加热)，`SWITCH` (间歇加热) 和 `OFF` 关闭
- **temperature** (_Optional_): 来自热敏电阻读转换得出的温度数据
- **mq_adc** (_Optional_): 12 Bit MQ ADC 读数
- **ntc_adc** (_Optional_)： 12 Bit NTC ADC 读数
- **ntc_resistance** (_Optional_): NTC 电阻阻值
- **reference_voltage** (_Optional_): 内部参考电压
- **mq_voltage** (_Optional_): MQ 电压读数
- **led** (_Optional_): LED 有效读数，当读数有效时，LED 会亮起

\#> 警告 | 设备需要加热一段时间后才能正常输出（至少需要加热到 29 摄氏度左右才会有 ADC 读数），配置加热模式 `heat_mode: CONTINUOUS` 时候，设备会一直加热，接触探头小心烫手。

## Dashboard 范例

配置完成并接入 Home Assistant 后的效果展示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/unit_mq_sensor_dashboard_example.webp" width="30%" />

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=116026863849441&bvid=BV19ZFnzPEgK&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/73uG7pVl8Qk?si=rFrhGEiWaPSkhMfV" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
