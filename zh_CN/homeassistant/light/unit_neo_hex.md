# Unit NeoHEX Home Assistant 集成

本章节介绍如何将 Unit NeoHEX 集成至 Home Assistant。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neohex/neohex_03.webp" width="30%"/>

## 准备工作

- Unit NeoHEX 六边形 RGB LED 灯板
- 适配主控设备（Atom 系列、Stamp 系列、Stick 系列、Core/Basic 系列等）

## 注意事项

- `ESP32 RMT LED Strip` 组件仅支持 ESP-IDF 框架； Arduino 框架下的灯光组件为 `NeoPixelBus Light`。自 2026.1.0 版本后，[ESPHome 默认框架将变为 ESP-IDF](https://esphome.io/guides/esp32_arduino_to_idf/)，建议选用 `ESP32 RMT LED Strip` 作为灯光组件。
- 因为 Unit NeoHEX 只是单独的灯光硬件，需要额外的主控设备才能集成至 Home Assistant；由于设计原因，不同主控的驱动能力不完全一致，详情参考 [操作说明 -> 驱动情况](/zh_CN/unit/neohex#%E6%93%8D%E4%BD%9C%E8%AF%B4%E6%98%8E)

## 修改配置

1. 以 Atom VoiceS3R 作为主机，其信号线是`GPIO2`，配置示例如下：

```yaml line-num
light:
  - platform: esp32_rmt_led_strip
    rgb_order: GRB
    pin: GPIO2
    num_leds: 37
    chipset: WS2812
    name: "Unit NeoHex"
    id: neo_hex_light
    restore_mode: RESTORE_DEFAULT_OFF
    effects:
      - random:
          name: "Random"
          transition_length: 1s
          update_interval: 4s
    ...
```

2. 更多灯光设置和效果可参考：[Light Effects](https://esphome.io/components/light/)
3. 主要参考组件：[ESP32 RMT LED Strip](https://esphome.io/components/light/esp32_rmt_led_strip/)

## 下载和烧录固件

1. 完成配置后下载固件文件。
2. 将固件烧录至主控设备。

## 开始使用

完成配置并且成功上传程序后，在 Home Assistant 集成中找到灯光实体。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/532/unit_neo_hex_ha_dash.webp" width="40%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/532/unit_neo_hex_demo.jpg" width="40%"/>

\#> 注意 | 将灯光亮度调整至 100% 时，长时间工作接触灯光**小心烫手**；为了灯珠寿命，不建议长时间保持最高亮度。
