# Chain DualKey Home Assistant 集成

本教程将介绍如何使用 **Chain DualKey** 可编程双键开发板集成至 Home Assistant，实现按键与扩展模块控制。

<div style="display: flex; gap: 15px; flex-wrap: wrap;">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_01.webp" width="30%"/>
</div>

## 准备工作

- Home Assistant 主机。
- 在 Home Assistant 中安装并启用 [ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。
- [Chain DualKey](/zh_CN/chain/Chain_DualKey)
- [Chain Angel](/zh_CN/chain/Chain_Angle)
- [Chain Encoder](/zh_CN/chain/Chain_Encoder)
- [Chain Key](/zh_CN/chain/Chain_Key)
- [Chain Joystick](/zh_CN/chain/Chain_Joystick)
- [Chain Tof](/zh_CN/chain/Chain_ToF)

## 注意事项

本教程中，固件在 ESPHome 2025.1.2 下编译和上传。如果遇到编译 / 上传问题，请考虑将 ESPHome 切换至此版本。

## 创建设备

1. 创建新设备。点击右下角的绿色按钮创建设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%"/>

2. 创建设备名称。

- 点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%"/>

- 点击 `New Device Setup`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%"/>

- 输入设备名称后点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/HA6.webp" width="40%"/>

3. 选择设备类型。

- 点击 `ESP32-S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA5.webp" width="30%"/>

- 点击 `SKIP`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%"/>

4. 编辑 YAML 文件。点击 `EDIT`，我们可以通过 YAML 文件自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/HA4.webp" width="70%"/>

## 设备配置

Master 作为系统的主控制器。在连接扩展传感器时，需要正确区分连接方向以及 ID 编号顺序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/chain_bus_device_id_01.jpg" width="70%">

### 方向选择

根据扩展传感器连接在 Master 的哪一侧，选择对应的 `uart_id`：

- 连接在 Master 左侧 → 使用 `chain_uart_left`。
- 连接在 Master 右侧 → 使用 `chain_uart_right`。

### ID 编号规则

`chain_id` 表示扩展传感器相对于 Master 的位置：

- 编号从距离 Master 最近的模块开始。
- ID 依次递增（ID:1 → ID:2 → ID:3 …）。
- 左右两侧分别独立编号。
- 可参考上图确定正确的顺序。

### 配置示例

- `uart_id:` `chain_uart_left`。
- `chain_id:` `1`。

### Chain DualKey

```yaml
uart:
  - id: chain_uart_right
    tx_pin: GPIO6
    rx_pin: GPIO5
    baud_rate: 115200

  - id: chain_uart_left
    tx_pin: GPIO48
    rx_pin: GPIO47
    baud_rate: 115200

sensor:
  - platform: adc
    pin: GPIO10
    name: "ADC_BAT"
    update_interval: 1s

  - platform: adc
    pin: GPIO2
    name: "ADC_VBUS"
    update_interval: 1s

  - platform: adc
    pin: GPIO9
    name: "ADC_CHARGE"
    update_interval: 1s

output:
  - platform: gpio
    id: pwr_en
    pin: GPIO40

light:
  - platform: esp32_rmt_led_strip
    id: key_light_raw
    internal: true
    pin: GPIO21
    num_leds: 2
    chipset: ws2812
    rgb_order: GRB
    restore_mode: ALWAYS_OFF

  - platform: partition
    name: "Key Light 1"
    id: key_light_1
    segments:
      - id: key_light_raw
        from: 0
        to: 0

  - platform: partition
    name: "Key Light 2"
    id: key_light_2
    segments:
      - id: key_light_raw
        from: 1
        to: 1

binary_sensor:
  - platform: gpio
    name: "KEY_2"
    pin:
      number: GPIO17
      inverted: true
      mode: INPUT_PULLUP
    filters:
      - delayed_on: 10ms
      - delayed_off: 10ms

    on_press:
      - light.turn_on:
          id: key_light_2
          transition_length: 0ms

    on_release:
      - light.turn_off: key_light_2

  - platform: gpio
    name: "KEY_1"
    pin:
      number: GPIO0
      inverted: true
      mode: INPUT_PULLUP
    filters:
      - delayed_on: 10ms
      - delayed_off: 10ms

    on_press:
      - light.turn_on:
          id: key_light_1
          transition_length: 0ms

    on_release:
      - light.turn_off: key_light_1

  - platform: gpio
    name: "SWITCH_1"
    pin:
      number: GPIO7
      mode: INPUT

  - platform: gpio
    name: "SWITCH_2"
    pin:
      number: GPIO8
      mode: INPUT
```

### Chain Key

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: [m5stack_chain_key]
    refresh: 0s

binary_sensor:
  - platform: m5stack_chain_key
    id: chain_key_1
    name: "Chain Key Button"
    uart_id: xx
    chain_id: xx
    update_interval: 50ms

output:
  - platform: m5stack_chain_key
    id: chain_key_rgb_r
    chain_key_id: chain_key_1
    channel: rgb_red

  - platform: m5stack_chain_key
    id: chain_key_rgb_g
    chain_key_id: chain_key_1
    channel: rgb_green

  - platform: m5stack_chain_key
    id: chain_key_rgb_b
    chain_key_id: chain_key_1
    channel: rgb_blue

light:
  - platform: rgb
    name: "Key RGB"
    red: chain_key_rgb_r
    green: chain_key_rgb_g
    blue: chain_key_rgb_b
```

### Chain Angle

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: [m5stack_chain_angle]
    refresh: 0s

sensor:
  - platform: m5stack_chain_angle
    id: chain_angle_1
    name: "Chain Angle"
    uart_id: xx
    chain_id: xx
    update_interval: 50ms

output:
  - platform: m5stack_chain_angle
    id: chain_angle_rgb_r
    chain_angle_id: chain_angle_1
    channel: rgb_red

  - platform: m5stack_chain_angle
    id: chain_angle_rgb_g
    chain_angle_id: chain_angle_1
    channel: rgb_green

  - platform: m5stack_chain_angle
    id: chain_angle_rgb_b
    chain_angle_id: chain_angle_1
    channel: rgb_blue

light:
  - platform: rgb
    name: "Angle RGB"
    red: chain_angle_rgb_r
    green: chain_angle_rgb_g
    blue: chain_angle_rgb_b
```

### Chain Encoder

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: [m5stack_chain_encoder]
    refresh: 0s

sensor:
  - platform: m5stack_chain_encoder
    id: chain_encoder_1
    name: "Chain Encoder"
    uart_id: xx
    chain_id: xx
    update_interval: 100ms

output:
  - platform: m5stack_chain_encoder
    id: chain_encoder_rgb_r
    chain_encoder_id: chain_encoder_1
    channel: rgb_red

  - platform: m5stack_chain_encoder
    id: chain_encoder_rgb_g
    chain_encoder_id: chain_encoder_1
    channel: rgb_green

  - platform: m5stack_chain_encoder
    id: chain_encoder_rgb_b
    chain_encoder_id: chain_encoder_1
    channel: rgb_blue

light:
  - platform: rgb
    name: "Encoder RGB"
    red: chain_encoder_rgb_r
    green: chain_encoder_rgb_g
    blue: chain_encoder_rgb_b

binary_sensor:
  - platform: m5stack_chain_encoder
    name: "Encoder Button"
    chain_encoder_id: chain_encoder_1
```

### Chain Joystick

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: [m5stack_chain_joystick]
    refresh: 0s

sensor:
  - platform: m5stack_chain_joystick
    id: chain_joystick_x
    name: "Chain Joystick X"
    uart_id: xx
    chain_id: xx
    axis: x
    update_interval: 50ms

  - platform: m5stack_chain_joystick
    name: "Chain Joystick Y"
    uart_id: xx
    chain_id: xx
    axis: y
    update_interval: 50ms

output:
  - platform: m5stack_chain_joystick
    id: chain_joystick_rgb_r
    chain_joystick_id: chain_joystick_x
    channel: rgb_red

  - platform: m5stack_chain_joystick
    id: chain_joystick_rgb_g
    chain_joystick_id: chain_joystick_x
    channel: rgb_green

  - platform: m5stack_chain_joystick
    id: chain_joystick_rgb_b
    chain_joystick_id: chain_joystick_x
    channel: rgb_blue

light:
  - platform: rgb
    name: "Joystick RGB"
    red: chain_joystick_rgb_r
    green: chain_joystick_rgb_g
    blue: chain_joystick_rgb_b

binary_sensor:
  - platform: m5stack_chain_joystick
    name: "Joystick Button"
    chain_joystick_id: chain_joystick_x
```

### Chain ToF

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: [m5stack_chain_tof]
    refresh: 0s

sensor:
  - platform: m5stack_chain_tof
    id: chain_tof_1
    name: "Chain ToF"
    uart_id: xx
    chain_id: xx
    update_interval: 100ms

output:
  - platform: m5stack_chain_tof
    id: chain_tof_rgb_r
    m5stack_chain_tof_id: chain_tof_1
    channel: rgb_red

  - platform: m5stack_chain_tof
    id: chain_tof_rgb_g
    m5stack_chain_tof_id: chain_tof_1
    channel: rgb_green

  - platform: m5stack_chain_tof
    id: chain_tof_rgb_b
    m5stack_chain_tof_id: chain_tof_1
    channel: rgb_blue

light:
  - platform: rgb
    name: "ToF RGB"
    red: chain_tof_rgb_r
    green: chain_tof_rgb_g
    blue: chain_tof_rgb_b
```

## 示例

下面的代码示例是根据上图所示的连接顺序进行配置的。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/example.png" width="70%"/>

### 外部组件

使用的模块：Chain Angle、Chain Encoder、Chain ToF、Chain Joystick、Chain Key。

- **添加 [External](https://esphome.io/components/external_components/) 组件**。此配置块用于引入所有 Chain 系列相关的外部组件。如果某个模块（例如 Chain Encoder 或 Chain ToF）不使用，可以从 components 列表中删除对应项。

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components:
      [
        m5stack_chain_angle,
        m5stack_chain_encoder,
        m5stack_chain_tof,
        m5stack_chain_joystick,
        m5stack_chain_key,
      ]
    refresh: 0s
```

### UART 组件

使用的模块：主控左 / 右侧 HY2.0 接口上的所有 Chain 系列模块共用的 UART 总线。

- **添加 [Uart](https://esphome.io/components/uart/) 组件**。在本示例中，`chain_uart_right` 和 `chain_uart_left` 分别对应主控右侧和左侧的 HY2.0 接口。后续 Chain 模组的 `uart_id` 需要与实际连接方向保持一致。

```yaml
captive_portal:
uart:
  - id: chain_uart_right
    tx_pin: GPIO6
    rx_pin: GPIO5
    baud_rate: 115200

  - id: chain_uart_left
    tx_pin: GPIO48
    rx_pin: GPIO47
    baud_rate: 115200
```

### 传感器组件

使用的模块：Chain Encoder、Chain Angle、Chain ToF、Chain Joystick（X/Y）、DualKey 电池相关 ADC 传感器。

- **添加 [Sensor](https://esphome.io/components/external_components/) 组件**。在本示例中，主控右侧按顺序连接了 Chain Encoder（ID 1）、Chain Angle（ID 2）、Chain ToF（ID 3），左侧连接了 Chain Joystick（ID 1，X/Y 两个轴）。同时还启用了电池电量相关的 ADC 通道（BAT、VBUS、CHARGE）作为传感器。

```yaml
sensor:
  - platform: m5stack_chain_encoder
    id: chain_encoder_1
    name: "Encoder"
    uart_id: chain_uart_right
    chain_id: 1
    update_interval: 100ms

  - platform: m5stack_chain_tof
    id: chain_tof_1
    name: "ToF Distance"
    uart_id: chain_uart_right
    chain_id: 3
    update_interval: 100ms

  - platform: m5stack_chain_angle
    id: chain_angle_1
    name: "Angle"
    uart_id: chain_uart_right
    chain_id: 2
    update_interval: 100ms

  - platform: m5stack_chain_joystick
    id: chain_joystick_x
    name: "Joystick X"
    uart_id: chain_uart_left
    chain_id: 1
    axis: x
    update_interval: 100ms

  - platform: m5stack_chain_joystick
    name: "Joystick Y"
    uart_id: chain_uart_left
    chain_id: 1
    axis: y
    update_interval: 100ms

  - platform: adc
    pin: GPIO10
    name: "ADC_BAT"
    update_interval: 1s

  - platform: adc
    pin: GPIO2
    name: "ADC_VBUS"
    update_interval: 1s

  - platform: adc
    pin: GPIO9
    name: "ADC_CHARGE"
    update_interval: 1s
```

### 输出组件

使用的模块：Chain Encoder、Chain Key、Chain Joystick、Chain Angle、Chain ToF 的 RGB 灯以及 DualKey 的电源控制。

- **添加 [Output](https://esphome.io/components/output/) 组件**。其中 `pwr_en` GPIO 输出用于控制 Chain 扩展总线的供电，通常需要保持开启，以保证连接在总线上的模块可以正常工作。

```yaml
output:
  - platform: gpio
    id: pwr_en
    pin: GPIO40

  - platform: m5stack_chain_encoder
    id: chain_encoder_rgb_r
    chain_encoder_id: chain_encoder_1
    channel: rgb_red

  - platform: m5stack_chain_encoder
    id: chain_encoder_rgb_g
    chain_encoder_id: chain_encoder_1
    channel: rgb_green

  - platform: m5stack_chain_encoder
    id: chain_encoder_rgb_b
    chain_encoder_id: chain_encoder_1
    channel: rgb_blue

  - platform: m5stack_chain_key
    id: chain_key_rgb_r
    chain_key_id: chain_key_1
    channel: rgb_red

  - platform: m5stack_chain_key
    id: chain_key_rgb_g
    chain_key_id: chain_key_1
    channel: rgb_green

  - platform: m5stack_chain_key
    id: chain_key_rgb_b
    chain_key_id: chain_key_1
    channel: rgb_blue

  - platform: m5stack_chain_joystick
    id: chain_joystick_rgb_r
    chain_joystick_id: chain_joystick_x
    channel: rgb_red

  - platform: m5stack_chain_joystick
    id: chain_joystick_rgb_g
    chain_joystick_id: chain_joystick_x
    channel: rgb_green

  - platform: m5stack_chain_joystick
    id: chain_joystick_rgb_b
    chain_joystick_id: chain_joystick_x
    channel: rgb_blue

  - platform: m5stack_chain_angle
    id: chain_angle_rgb_r
    chain_angle_id: chain_angle_1
    channel: rgb_red

  - platform: m5stack_chain_angle
    id: chain_angle_rgb_g
    chain_angle_id: chain_angle_1
    channel: rgb_green

  - platform: m5stack_chain_angle
    id: chain_angle_rgb_b
    chain_angle_id: chain_angle_1
    channel: rgb_blue

  - platform: m5stack_chain_tof
    id: chain_tof_rgb_r
    m5stack_chain_tof_id: chain_tof_1
    channel: rgb_red

  - platform: m5stack_chain_tof
    id: chain_tof_rgb_g
    m5stack_chain_tof_id: chain_tof_1
    channel: rgb_green

  - platform: m5stack_chain_tof
    id: chain_tof_rgb_b
    m5stack_chain_tof_id: chain_tof_1
    channel: rgb_blue
```

### 灯光组件

使用的模块：DualKey 上的 WS2812 按键灯，以及各 Chain 模组上的 RGB 指示灯。

- **添加 [Light](https://esphome.io/components/light/) 组件**。这一部分配置了 DualKey 上每个按键的 RGB 背光（通过 `key_light_raw` 分区成 `key_light_1` 和 `key_light_2`），同时也为各个 Chain 模组定义了对应的 RGB 灯光实体，方便在 Home Assistant 中分别控制。

```yaml
light:
  - platform: esp32_rmt_led_strip
    id: key_light_raw
    internal: true
    pin: GPIO21
    num_leds: 2
    chipset: ws2812
    rgb_order: GRB
    restore_mode: ALWAYS_OFF

  - platform: partition
    name: "Key1 LED"
    id: key_light_1
    segments:
      - id: key_light_raw
        from: 1
        to: 1

  - platform: partition
    name: "Key2 LED"
    id: key_light_2
    segments:
      - id: key_light_raw
        from: 0
        to: 0

  - platform: rgb
    name: "Encoder RGB"
    red: chain_encoder_rgb_r
    green: chain_encoder_rgb_g
    blue: chain_encoder_rgb_b

  - platform: rgb
    name: "Key RGB"
    red: chain_key_rgb_r
    green: chain_key_rgb_g
    blue: chain_key_rgb_b

  - platform: rgb
    name: "Joystick RGB"
    red: chain_joystick_rgb_r
    green: chain_joystick_rgb_g
    blue: chain_joystick_rgb_b

  - platform: rgb
    name: "Angle RGB"
    red: chain_angle_rgb_r
    green: chain_angle_rgb_g
    blue: chain_angle_rgb_b

  - platform: rgb
    name: "ToF RGB"
    red: chain_tof_rgb_r
    green: chain_tof_rgb_g
    blue: chain_tof_rgb_b
```

### 二进制传感器组件

使用的模块：DualKey 上的机械按键和侧边拨码开关，以及 Chain Key、Chain Encoder、Chain Joystick 上的按键。

- **添加 [Binary Sensor](https://esphome.io/components/binary_sensor/) 组件**。这一部分定义了所有与按键相关的输入：两个机械键（`KEY 1`、`KEY 2`）及其对应的背光联动、总线上一个 Chain Key 模组的按键、编码器按键、摇杆按键，以及两个侧边开关（`SWITCH 1`、`SWITCH 2`）。你可以根据实际使用场景在 Home Assistant 中重命名这些实体。

```yaml
binary_sensor:
  - platform: gpio
    name: "KEY 2"
    pin:
      number: GPIO17
      inverted: true
      mode: INPUT_PULLUP
    filters:
      - delayed_on: 10ms
      - delayed_off: 10ms

    on_press:
      - light.turn_on:
          id: key_light_2
          transition_length: 0ms

    on_release:
      - light.turn_off: key_light_2

  - platform: gpio
    name: "KEY 1"
    pin:
      number: GPIO0
      inverted: true
      mode: INPUT_PULLUP
    filters:
      - delayed_on: 10ms
      - delayed_off: 10ms

    on_press:
      - light.turn_on:
          id: key_light_1
          transition_length: 0ms

    on_release:
      - light.turn_off: key_light_1

  - platform: m5stack_chain_key
    id: chain_key_1
    name: "Key Module Button"
    uart_id: chain_uart_left
    chain_id: 2
    update_interval: 50ms

  - platform: m5stack_chain_encoder
    name: "Encoder Button"
    chain_encoder_id: chain_encoder_1

  - platform: m5stack_chain_joystick
    name: "Joystick Button"
    chain_joystick_id: chain_joystick_x

  - platform: gpio
    name: "SWITCH 1"
    pin:
      number: GPIO7
      mode: INPUT

  - platform: gpio
    name: "SWITCH 2"
    pin:
      number: GPIO8
      mode: INPUT
```

## 下载和烧录固件

1. 修改完成后，点击右上角的 `SAVE` 和 `INSTALL`，在弹出的对话框中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

2. 固件编译完成后，点击 `Download`，并选择 `Factory format(Previously Modern)` 选项下载固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%"/>

\#> 提示 | 点击 [m5stack_chain](https://github.com/m5stack/esphome-yaml/blob/main/examples/sensor/m5stack_chain_series.yaml) 查看完整示例配置。首次构建可能需要一些时间，具体取决于 Home Assistant 主机的性能和网络质量。

3. 使用 USB Type‑C 线将设备连接到主机。打开 [ESPHome Web](https://web.esphome.io/)，点击 `CONNECT` 连接设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%"/>

4. 找到对应的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%"/>

5. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%"/>

6. 选择编译好的固件进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/HA5.webp" width="30%"/>

7. 固件烧录完成后，需要重新上电以完成硬件复位。

## 开始使用

1. 在 Home Assistant 中点击 `Settings` -> `Device & services` 查看设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%"/>

2. 我们可以在 `Discover` 区域中找到对应的设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/HA3.webp" width="40%"/>

3. 添加设备后，数据会正确显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/HA0.webp" width="50%"/>

4. 最后，将这些实体添加到 Dashboard 中，即可获得如下显示效果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/HA9.webp" width="50%"/>
