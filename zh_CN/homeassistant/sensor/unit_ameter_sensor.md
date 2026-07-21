# Unit AMeter Home Assistant 集成

本章节介绍将 Unit AMeter 电流计集成至 Home Assistant 的配置方法与实操步骤。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/712/ameter-Home_Assistant_tutorial_cover_ZH.png" width="60%">

## 注意事项

Unit AMeter 只是单独的传感器平台，需要额外的主控设备（如 Atom 系列、Stamp 系列、Stick 系列、Core/Basic 系列等）才能集成至 Home Assistant。

## 准备工作

1. 查阅 ADS1115 传感器数据手册：[ADS1115 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/ADS1115.PDF)；
2. 参考 ESPHome 官方最新配置说明：[ADS1115 4-Channel 16-Bit A/D Converter](https://esphome.io/components/sensor/ads1115/)；
3. 准备兼容的主控设备（如 Atom 系列、Stamp 系列、Stick 系列、Core/Basic 系列等）；
4. 确认主控设备的 I2C 引脚定义（不同主控引脚不同）。

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

Unit AMeter 配置范例：

1. 首先配置基础组件 ADS1115：

```yaml line-num
ads1115:
  - address: 0x48

sensor:
  - platform: ads1115
    multiplexer: "A0_A1"
    gain: 0.256
    sample_rate: 128
    name: "Unit AMeter A0_A1 Ref"
    id: diff
    update_interval: 10s
```

\#> 提示 | Unit AMeter 只使用了 `AIN0` 和 `AIN1` 两个通道，所以最多可以使用 3 个 `multiplexer`: `"A0_A1"`、`"A0_GND"`、`"A1_GND"`；而此处测量电流，仅用到了 `A0_A1` 参与电流计算。

2. 配置 EEPROM 读取校准参数，结合 `Template` Sensor 创建自定义数据：

```yaml line-num
i2c_device:
  id: eeprom
  address: 0x51

sensor:
  # Previous ads1115 declarations
  ...
  - platform: template
    name: "Input Current"
    id: input_cur
    unit_of_measurement: "A"
    icon: "mdi:current-dc"
    accuracy_decimals: 2
    update_interval: 10s
    lambda: |-
      float d = id(diff).state;

      if (isnan(d)) return NAN;

      const float PRESSURE_COEFF = 0.05f;

      const uint8_t EEPROM_REG = 0xF8;

      uint8_t calib[8];
      uint16_t hope, actual;

      if ( id(eeprom).read_register(EEPROM_REG, calib, 8) != i2c::ERROR_OK ) {
        ESP_LOGD("ameter.sensor", "Failed to read from EEPROM..");
        return NAN;
      }

      uint8_t xor_result = 0x00;

      for (uint8_t i = 0; i < 5; i++) {
          xor_result ^= calib[i];
      }

      if (xor_result != calib[5]) {
        return NAN;
      }

      hope   = (calib[1] << 8) | calib[2];
      actual = (calib[3] << 8) | calib[4];

      float calibration_ratio = (float)hope / actual;

      ESP_LOGD("ameter.sensor", "Factory calibration factor: %f", calibration_ratio);

      float ain = - d / PRESSURE_COEFF;

      ain = ain * calibration_ratio;

      return ain;
```

3. 在读取 EEPROM 的时候，需要根据 ADS1115 设置的 `gain` 值，修改 lambda 表达式中 `EEPROM_REG` 读取地址：

```c++ line-num
// In lambda expression
// remember to change the 'EEPROM_REG' if you changed the 'gain'
// for an example, when 'gain' is 0.256
const uint8_t EEPROM_REG = 0xF8;
```

| ADS1115 Gain | EEPROM Data Register | Max Input Current (theory) |
| :----------: | :------------------: | :------------------------: |
| 6.144        | 0xD0                 | -                          |
| 4.096        | 0xD8                 | -                          |
| 2.048        | 0xE0                 | -                          |
| 1.024        | 0xE8                 | -                          |
| 0.512        | 0xF0                 | 10 A                       |
| 0.256        | 0xF8                 | 5 A                        |

推荐的 `gain` 值为 **`0.256`**，分辨率 0.3mA，**仅能测量 `AIN0` 或 `AIN1` 其中一路**，请勿将两路都接上输入。

?> 警告 | 产品设计的最佳测量区间为 ±4V，内置熔断器，超过 4A 电流将会触发熔断，**请不要输入此范围之外的电流**，也避免空负载，以免设备损坏；EEPROM (0x51) 在出厂时内置了校准参数，**请勿对 EEPROM 进行写操作**，否则校准数据将被覆盖，可能导致测量结果不准确。

## 开始使用

当添加至 Dashboard 之后，您可以在 Home Assistant 中查看传感器数据。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/712/unit_ameter_ha_dashboard_example.webp" width="30%" />

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=116027014775076&bvid=BV1XJFnzFEtN&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/rCN3oTgtW6U?si=QulQYM7Vy1ycba7U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
