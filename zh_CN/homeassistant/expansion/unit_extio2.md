# Unit EXT.IO2 / Stamp IO Home Assistant 集成

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio2/extio2_01.webp" width="30%" />

Unit EXT.IO2是一款IO 拓展单元，模块基于 STM32F030 主控开发，采用 I2C 通信接口，提供 8 路 IO 拓展。每路 IO 支持独立配置 数字输入 / 输出，ADC，SERVO 控制，RGB LED 控制模式。支持配置设备 I2C 地址，这意味着在同一 I2C 总线上允许用户挂载多个 Unit EXT.IO2 UNIT 拓展出更多的 IO 资源。适用于多路数字 / 模拟信号采集，与灯光 / 舵机控制等应用场景。

<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_io/stamp_io_01.webp" width="30%" />

Stamp IO 是一款IO 拓展板, 该拓展板基于 STM32F030 主控开发，采用 I2C 通信接口，提供 8 路 IO 拓展。每路 IO 支持独立配置数字输入 / 输出， ADC, SERVO 控制, RGB LED 控制模式。适用于多路数字 / 模拟信号采集，与灯光 / 舵机控制等应用场景。


这两个设备的通信协议一致，需要通过 I2C 连接外部主控才能使用


## 准备工作

- 一个主控设备
- Home Assistant 主机。
- 在 Home Assistant 中安装并启用[ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。


## 注意事项

Unit EXT.IO2/ Stamp IO 只是 IO 拓展平台，需要额外的主控设备（如 Atom 系列、Stamp 系列， Stick 系列，Core/Basic 系列等）才能集成至 Home Assistant。

## 添加功能

拓展功能需要 I2C 组件：

[I²C](https://esphome.io/components/i2c/#i2c) 组件：

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


在使用功能前，还需添加 Hub 组件：

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components@main
    components: [extio2]
    refresh: 0s

extio2:
  id: extio2_hub
```

### 可配置选项

- **id** (*可选*, [ID](https://esphome.io/guides/configuration-types#id)): 为 Hub 组件指定一个 ID。
- **address** (*可选*, int): I2C 地址，默认 `0x45`.
- **reset** (*可选*, boolean): 执行软件复位，所有引脚设置为输出模式，输出低电平，默认 `true`.
- **pwm_freq** (*可选*, enum): 所有通道的全局 PWM 频率，默认为 `1kHz` 可选：
  - `2kHz`
  - `1kHz`
  - `500Hz`
  - `250Hz`
  - `125Hz`
- 其它 [I2C Device](https://esphome.io/components/i2c#config-i2c) 所支持的内容。


## GPIO 引脚

EXT.IO2 的引脚可用于任何 ESPHome 接受标准 GPIO 引脚引用的场景，例如 `switch`、`binary_sensor` 等组件。

```yaml
# 数字输出 — 开关
switch:
  - platform: gpio
    name: "EXT.IO2 GPIO 0"
    pin:
      extio2_id: extio2_hub
      number: 0
      mode:
        output: true

# 数字输入 — 二值传感器
binary_sensor:
  - platform: gpio
    name: "EXT.IO2 GPIO 1"
    pin:
      extio2_id: extio2_hub
      number: 1
```

### 引脚配置项

- **extio2_id** （*必填*，[ID](https://esphome.io/guides/configuration-types#id)）：EXT.IO2 总线控制器的 ID。
- **number** （*必填*，int）：引脚编号，范围 `0`–`7`。
- **inverted** （*可选*，boolean）：反转引脚逻辑，默认为 `false`。

\#> **注意**：| 设备固件仅支持输入和输出两种模式。`pullup`、`pulldown`、`open_drain` 等选项在配置中不支持


## 传感器（ADC）

传感器平台可从 8 个支持 ADC 的引脚中读取模拟值。

```yaml
sensor:
  - platform: extio2
    extio2_id: extio2_hub
    name: "ADC 传感器 0"
    channel: ADC_0
    resolution: 12BIT
    update_interval: 5s
```

### 配置项

- **extio2_id** （*可选*，[ID](https://esphome.io/guides/configuration-types#id)）：EXT.IO2 总线控制器的 ID。
- **channel** （*必填*，枚举）：要读取的 ADC 通道，`ADC_0` 至 `ADC_7`。
- **resolution** （*可选*，枚举）：ADC 分辨率，默认为 `8BIT`。
  - `8BIT`：8 位分辨率，范围 0–255。
  - `12BIT`：12 位分辨率，范围 0–4095。
- **update_interval** （*可选*，[时间](https://esphome.io/guides/configuration-types#config-time)）：轮询间隔，默认为 `60s`。
- 其他选项参见 [传感器](https://esphome.io/components/sensor#config-sensor)。


## 输出（PWM）

输出平台将任意引脚驱动为 PWM 输出。占空比以 `0.0` 到 `1.0` 的浮点数表示，内部映射为 0–100%。

```yaml
output:
  - platform: extio2
    extio2_id: extio2_hub
    id: pwm_ch0
    channel: PWM_0

light:
  - platform: monochromatic
    name: "PWM 灯 0"
    output: pwm_ch0
    effects:
      - pulse:
```

### 配置项

- **extio2_id** （*可选*，[ID](https://esphome.io/guides/configuration-types#id)）：EXT.IO2 总线控制器的 ID。
- **id** （*必填*，[ID](https://esphome.io/guides/configuration-types#id)）：该输出的 ID。
- **channel** （*必填*，枚举）：要使用的 PWM 通道，`PWM_0` 至 `PWM_7`。
- 其他选项参见 [浮点输出](https://esphome.io/components/output#float-output)。

\#> **注意**：| PWM 频率通过总线控制器的 `pwm_freq` 全局设置，所有 PWM 通道共享同一频率。

## 数值（舵机）

数值平台用于控制舵机，提供两种控制模式：角度（度）和脉冲宽度（微秒）。

### 角度模式

以角度（0–180°）控制舵机位置。

```yaml
number:
  - platform: extio2
    extio2_id: extio2_hub
    name: "舵机 0"
    type: angle
    channel: SERVO_0
    min_value: 0
    max_value: 180
    step: 3
```

### 脉冲模式

以原始脉冲宽度（微秒）控制舵机。

```yaml
number:
  - platform: extio2
    extio2_id: extio2_hub
    name: "舵机 1"
    type: pulse
    channel: SERVO_1
    min_value: 500
    max_value: 2500
    step: 100
```

### 配置项

- **extio2_id** （*可选*，[ID](https://esphome.io/guides/configuration-types#id)）：EXT.IO2 总线控制器的 ID。
- **type** （*必填*，枚举）：舵机控制模式。
  - `angle`：以角度控制。
  - `pulse`：以脉冲宽度控制。
- **channel** （*必填*，枚举）：要使用的舵机通道，`SERVO_0` 至 `SERVO_7`。
- **min_value** （*可选*，float）：最小值，角度模式默认 `0.0`，脉冲模式默认 `500.0`。
- **max_value** （*可选*，float）：最大值，角度模式默认 `180.0`，脉冲模式默认 `2500.0`。
- **step** （*可选*，float）：步进值，角度模式默认 `3.0`，脉冲模式默认 `100.0`。
- 其他选项参见 [数值](https://esphome.io/components/number#config-number)。

| 模式 | 单位 | 最小值 | 最大值 | 步进 |
|---|---|---|---|---|
| `angle` | `°` | `0` | `180` | `3` |
| `pulse` | `us` | `500` | `2500` | `100` |

## 灯光

灯光平台支持两种模式：单个 RGB LED（指定某一引脚）或可寻址 LED 灯条（从引脚 0 开始的连续多个引脚）。

### 单个 RGB 灯

控制指定引脚上的一个 RGB LED。

```yaml
light:
  - platform: extio2
    extio2_id: extio2_hub
    name: "EXT.IO2 灯光 2"
    type: light
    channel: LIGHT_2
```

### 可寻址灯条

控制从引脚 0 开始的连续多个 RGB LED，支持所有 ESPHome 可寻址灯光效果。

```yaml
light:
  - platform: extio2
    extio2_id: extio2_hub
    name: "灯条"
    type: addressable_light
    num_leds: 8
```

### 配置项

- **extio2_id** （*可选*，[ID](https://esphome.io/guides/configuration-types#id)）：EXT.IO2 总线控制器的 ID。
- **type** （*必填*，枚举）：灯光模式。
  - `light`：单个 RGB LED。
  - `addressable_light`：可寻址 LED 灯条。
- **channel** （`light` 类型*必填*，枚举）：要使用的引脚，`LIGHT_0` 至 `LIGHT_7`。
- **num_leds** （`addressable_light` 类型*必填*，int）：LED 数量，范围 `1`–`8`，从引脚 0 开始依次分配。
- 其他选项参见 [灯光](https://esphome.io/components/light)。

\#> **注意**：| 可寻址灯条的引脚必须从引脚 0 开始连续分配。例如 `num_leds: 3` 将使用引脚 0、1、2。硬件不提供亮度控制寄存器，亮度通过软件缩放 RGB 值实现。

## 完整配置示例

```yaml
i2c:
  sda: GPIO2
  scl: GPIO1

extio2:
  id: extio2_hub
  address: 0x45
  reset: true
  pwm_freq: 1kHz

# GPIO — 数字输出
switch:
  - platform: gpio
    name: "EXT.IO2 GPIO 0"
    pin:
      extio2_id: extio2_hub
      number: 0
      mode:
        output: true

# GPIO — 数字输入
binary_sensor:
  - platform: gpio
    name: "EXT.IO2 GPIO 1"
    pin:
      extio2_id: extio2_hub
      number: 1
      mode:
        input: true
        pullup: true

# ADC 传感器
sensor:
  - platform: extio2
    extio2_id: extio2_hub
    name: "ADC 传感器 2"
    channel: ADC_2
    resolution: 12BIT
    update_interval: 5s

# PWM 输出，用作单色灯
output:
  - platform: extio2
    extio2_id: extio2_hub
    id: pwm_ch3
    channel: PWM_3

light:
  - platform: monochromatic
    name: "PWM 灯 3"
    output: pwm_ch3
    effects:
      - pulse:

  # 舵机 — 角度控制
  - platform: extio2
    extio2_id: extio2_hub
    name: "舵机 4"
    type: angle
    channel: SERVO_4

number:
  # 舵机 — 脉冲宽度控制
  - platform: extio2
    extio2_id: extio2_hub
    name: "舵机 5"
    type: pulse
    channel: SERVO_5

  # 单个 RGB LED
  - platform: extio2
    extio2_id: extio2_hub
    name: "RGB 灯光 6"
    type: light
    channel: LIGHT_6

  # 可寻址 LED 灯条（全部 8 个引脚）
  - platform: extio2
    extio2_id: extio2_hub
    name: "灯条"
    type: addressable_light
    num_leds: 8
```