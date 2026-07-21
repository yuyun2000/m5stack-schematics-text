# Uint IR Home Assistant 集成

本章节介绍将 Unit IR 红外发射接收单元集成至 Home Assistant 的配置方法与实操步骤。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ir/ir_01.webp" width="30%"/>

## 注意事项

Unit IR 是单独的红外单元，需要额外的主控设备（如 Atom 系列、Stamp 系列， Stick 系列，Core/Basic 系列等）才能集成至 Home Assistant。

## 准备工作

1. 参考 ESPHome 官方最新 IR 配置文档：

- [Remote Transmitter](https://esphome.io/components/remote_transmitter/)
- [Remote Receiver](https://esphome.io/components/remote_receiver/)
- [Setting up RMT Devices](https://esphome.io/guides/setting_up_rmt_devices/#remote-setting-up-infrared)

2. 准备兼容的主控设备（如 Atom 系列、Stamp 系列、Stick 系列、Core/Basic 系列等）。
3. 确认主控设备的 GPIO 引脚定义（不同主控引脚不同）。

## 配置 IR Transmitter/Receiver

1. 基础配置示例：

```yaml
remote_receiver:
  pin: GPIOXX
  dump: all

remote_transmitter:
  pin: GPIOXX
  carrier_duty_percent: 50%
```

这里的 GPIO 引脚会因为使用的主控设备不一而不同。比如使用 AtomS3 系列作为主控：

```yaml
# GPIO1 input
remote_receiver:
  pin: GPIO1
  dump: all

# GPIO2 output
remote_transmitter:
  pin: GPIO2
  carrier_duty_percent: 50%
```

2. 当完成了 IR 的配置后，就可以添加 IR Climate 等设备，以美的空调为例：

```yaml
climate:
  - platform: coolix # or media_ir
    name: "Media AC"
    visual:
      min_temperature: 18
      max_temperature: 30
      temperature_step: 1
```

3. 保存完成后编译、上传固件，将设备添加进入 Home Assistant，就可以看见 IR 实体：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/833/unit_ir_ha_climate_example.webp" width="40%" />
