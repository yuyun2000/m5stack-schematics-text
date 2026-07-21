# Uint ToF Home Assistant 集成

本教程将介绍如何使用 **Unit ToF** 高精度激光测距传感器集成至 Home Assistant，实现非接触式距离监测。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-1389686c-b643-4b4f-a74b-4dc070a32103.webp" width="30%" />

## 准备工作

- [VL53L0X datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/VL53L0X_en.pdf)
- 可参考 ESPHome 以查看最新的配置：[VL53L0X Time Of Flight Distance Sensor](https://esphome.io/components/sensor/vl53l0x/)

## 注意事项

\#> 注意 | 因为 Unit ToF 只是单独的传感器平台，需要额外的主控设备（如 Atom 系列、Stamp 系列， Stick 系列，Core/Basic 系列等）才能集成至 Home Assistant。

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

**Unit ToF 配置的范例：**

```yaml line-num
sensor:
  - platform: vl53l0x
    name: "VL53L0x Distance"
    address: 0x29
    update_interval: 60s
    long_range: true
```

保存配置文件，编译并且上传固件后，可以将设备添加至 Home Assistant 集成。
