# Unit KMeter-ISO Home Assistant 集成

本章节介绍将 Unit KMeter-ISO 传感器集成至 Home Assistant 的配置方法与实操步骤。<!--不需要重复介绍产品了**-->

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO%20Unit/img-794d033d-e060-4d83-8b2a-46c1a20bfcb1.webp" width="30%"> <!--放一张产品的场景图-->

## 准备工作

- [MAX31855KASA+ Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/STM32F030F4P6.PDF)
- [通信协议](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/KMeterISO%20Unit/i2c%20protol.png)
- 从 ESPHome 获取最新配置：[KMeterISO ESPHome](https://esphome.io/components/sensor/kmeteriso/)

## 注意事项

Unit KMeter-ISO 只是单独的传感器平台，需要额外的主控设备（如 Atom 系列、Stamp 系列， Stick 系列，Core/Basic 系列等）才能集成至 Home Assistant

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

**Unit KMeterISO 配置范例：**

```yaml line-num
sensor:
  - platform: kmeteriso
    temperature:
      name: "KMeterISO Temperature"
    internal_temperature:
      name: "Internal Temperature"
    update_interval: 10s
```

## 开始使用

当添加至 Dashboard 之后，您可以在 Home Assistant 中查看传感器数据

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/742/unit_kmeteriso_ha_dashboard.webp" width="60%">
