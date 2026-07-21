# PowerHub 控制器 Home Assistant 集成

本章节介绍将集成多路电源管理的可编程控制器 PowerHub 集成至 Home Assistant 的方法。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/PH-Home_Assistant_tutorial_cover_ZH.png" width="60%"/>

## 准备工作

- Home Assistant 主机。
- 在 Home Assistant 中安装并启用[ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 PowerHub 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/powerhub_manifest_2026.3.0.json">一键烧录固件</EspWebTool>

## 注意事项

- 本教程中，套件在 ESPHome `2025.11.2` 下编译和上传，如果遇见编译 / 上传问题，考虑将 ESPHome 切换至此版本。

## 创建设备

1. 在 Home Assistant 中打开 ESPHome Builder，创建一个空的配置文件。

- 点击右下角的 `NEW DEVICE` 按钮。

- 弹出框单击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_2.webp" width="40%" />

- 选择 `Empty Configuration`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_create_empty_config.webp" width="30%" />

- 为文件命名（可选）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_esphome_builder_naming.webp" width="30%" />

- 在新生成的配置文件处点击 `EDIT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_esohome_builder_new_file.webp" width="40%" />

2. 复制 [configurations.yaml](https://github.com/m5stack/esphome-yaml/blob/main/examples/kit/powerhub.factory.yaml) 的内容到配置文件中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_esphome_builder_configurations.webp" width="60%" />

3. 根据需要，更改网络配置或者是 API 信息等，比如创建一个 API Encryption Key 用于认证：

```yaml line-num
api:
  encryption:
    key: "Your_Encryption_Key"
```

\#> 提示 | 如果需要一个 Key，可以访问 [native api](https://esphome.io/components/api/) 生成一个（在 encryption 下）。

或者是更改时区设置：

```yaml line-num
timezone: Europe/London
```

改为合适的时区：

```yaml line-num
timezone: Asia/Shanghai
```

4. 依次点击右上角 `SAVE` 和 `INSTALL`，选择 `Manual download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_esphome_builder_install_method.webp" width="40%" />

5. 此时会生成代码并且编译工程。

\#> 提示 | 如果是第一次编译，可能会需要较长时间；具体取决于 Home Assistant 主机性能和网络连接情况。

6. 当编译完成后，选择 `Factory format` 下载固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_esphome_builder_compile.webp" width="60%" />

## 下载和烧录固件

1. 下载固件：通过 ESPHome Builder 的`Manual download`方式下载 Factory Format 固件。
2. 使用 web 工具烧录固件：

- 打开浏览器，访问 [ESPHome Web](https://web.esphome.io/) 上传固件。

- 使用 USB-C 数据线将 PowerHub 连接至主机，点击 `CONNECT`，选择设备连接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_2.webp" width="70%" />

- 点击 `INSTALL`，选择之前下载的固件上传，再次点击 `INSTALL`，将固件烧录至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_webesp_select_file.webp" width="40%" />

- 当烧录完成后，设备会自动重置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_success.webp" width="30%" />

## 开始使用

### 添加设备至 Home Assistant 集成

1. 当设备重启后，会自动连接之前配置的网络，正常情况下可以在 `Settings` -> `Devices & services` 发现设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_ha_device_discovery.webp" width="30%" />

2. 点击 `Add` 将 PowerHub 集成进入 Home Assistant，如果此前设置了 API Encryption Key，此处可能需要填入 API Encryption Key 验证。

PowerHub 的 Dashboard 示例：

<div
style="display: flex; gap: 16px; align-items: flex-start;"
>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_ha_controls.webp" style="object-fit: contain;" width="30%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_ha_sensors.webp" width="30%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_ha_selec_misc.webp" width="30%" />
</div>

3. 可以通过灯光开关、电源开关来具体控制每一路灯或者电源输出，下拉菜单设置 USB 工作模式，RS485 & CAN 接口的输出电压和电流限制（需要打开`RS485 & CAN Power Output`）。

### Component/Hub 配置说明

[I2C](https://esphome.io/components/i2c/) 是配置设备必要组件。

- 该设备提供 RS485 和 CAN 接口；如果需要使用 RS485/CAN 接口，需要额外配置诸如 [Modbus Controller](https://esphome.io/components/modbus_controller/) 和 [CAN Bus](https://esphome.io/components/canbus/#sidebar) 的组件。
- 你可以为 USB Type A 或 USB Type C 端口设置 USB 模式；如果需要通过 USB 接口进行通信，可能需要配置 [USB Host Interface](https://esphome.io/components/usb_host/) 和 [TinyUSB](https://esphome.io/components/tinyusb/)。

```yaml
# Example configuration entry
powerhub:
```

#### 配置变量

- **id**（可选，[ID](https://esphome.io/guides/configuration-types#id)）：为 PowerHub 组件指定一个 ID。
- **update_interval**（可选，[Time](https://esphome.io/guides/configuration-types#time)）：检查传感器的时间间隔。设置为 `never` 可禁用更新。默认值为 `10s`。

### Binary Sensor

`powerhub` 的 Binary Sensor 主要用于检测顶部 PMU 按钮是否被按下。

```yaml
binary_sensor:
  - platform: powerhub
    id: powerhub_binary_sensor
    button:
      name: "Top PMU Button"
```

#### 配置变量

- **powerhub_id**（可选，[ID](https://esphome.io/guides/configuration-types#id)）：PowerHub 的 ID。
- **button**（可选）：检测顶部 PMU 按钮（矩形）是否被按下。
  其它选项同 [Binary Sensor](https://esphome.io/components/binary_sensor#config-binary_sensor)。

### Sensor

`powerhub` 上的传感器会上报多种电压 / 电流等测量值。

```yaml
sensor:
  - platform: powerhub
    battery_voltage:
      name: "Battery Voltage"
      id: bat_volt_sensor
    battery_current:
      name: "Battery Current"
      id: bat_curr_sensor
    battery_level:
      name: "Battery Percentage"
      id: bat_level_sensor
    grove_red_voltage:
      name: "Port.A Voltage"
      id: grove_red_volt_sensor
    grove_red_current:
      name: "Port.A Current"
      id: grove_red_curr_sensor
    grove_blue_voltage:
      name: "Port.C Voltage"
      id: grove_blue_volt_sensor
    grove_blue_current:
      name: "Port.C Current"
      id: grove_blue_curr_sensor
    can_voltage:
      name: "CAN Voltage"
      id: can_volt_sensor
    can_current:
      name: "CAN Current"
      id: can_curr_sensor
    rs485_voltage:
      name: "RS485 Voltage"
      id: rs485_volt_sensor
    rs485_current:
      name: "RS485 Current"
      id: rs485_curr_sensor
    usb_voltage:
      name: "USB Voltage"
      id: usb_volt_sensor
    usb_current:
      name: "USB Current"
      id: usb_curr_sensor
```

\#> 提示 | 要使用传感器必须打开 `VAMeter Power` 开关和相应的输出通道，**只有接入相应负载后**，读数才有意义。

#### 配置变量

- **battery_voltage**（可选）：电池电压。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **battery_current**（可选）：电池电流。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **battery_level**（可选）：以百分比上报电池电量。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **grove_red_voltage**（可选）：grove red（Port.A）通道的电压。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **grove_red_current**（可选）：grove red（Port.A）通道的电流。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **grove_blue_voltage**（可选）：grove blue（Port.C）通道的电压。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **grove_blue_current**（可选）：grove blue（Port.C）通道的电流。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **can_voltage**（可选）：CAN 接口的电压。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **can_current**（可选）：CAN 接口的电流。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **rs485_voltage**（可选）：RS485 接口的电压。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **rs485_current**（可选）：RS485 接口的电流。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **usb_voltage**（可选）：USB 接口的电压。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **usb_current**（可选）：USB 接口的电流。
  其它选项同 [Sensor](https://esphome.io/components/sensor)。
- **powerhub_id**（可选，[ID](https://esphome.io/guides/configuration-types#id)）：PowerHub 的 ID。

### Text Sensor

`powerhub` 的 Text Sensor 以文本形式上报电源状态，同时上报设备的内部固件 /bootloader 版本。

```yaml
text_sensor:
  - platform: powerhub
    charge_status:
      name: "Battery Charge Status"
      id: bat_charge_status_text_sensor
    vin_status:
      name: "External Input Power Status"
      id: ext_vin_status_text_sensor
    firmware_ver:
      name: "Internal Firmware Version"
      id: int_firm_ver_text_sensor
    bootloader_ver:
      name: "Bootloader Version"
      id: boot_ver_text_sensor
```

#### 配置变量

- **charge_status**（可选）：检测电池是否处于充电状态。
  其它选项同 [Text Sensor](https://esphome.io/components/text_sensor#config-text_sensor)。
- **vin_status**（可选）：检测是否存在外部输入电源。
  其它选项同 [Text Sensor](https://esphome.io/components/text_sensor#config-text_sensor)。
- **firmware_ver**（可选）：上报设备的内部固件版本。
  其它选项同 [Text Sensor](https://esphome.io/components/text_sensor#config-text_sensor)。
- **bootloader_ver**（可选）：设备的 bootloader 版本。
  其它选项同 [Text Sensor](https://esphome.io/components/text_sensor#config-text_sensor)。
- **powerhub_id**（可选，[ID](https://esphome.io/guides/configuration-types#id)）：PowerHub 的 ID。

### Switch

`powerhub` 的开关允许你在前端启用或禁用各个电源通道。

```yaml
switch:
  - platform: powerhub
    led_pwr:
      name: "LED Power"
      id: led_pwr_switch
    usb_pwr:
      name: "USB Power"
      id: usb_pwr_switch
    grove_red_pwr:
      name: "Port.A Power"
      id: grove_red_pwr_switch
    grove_blue_pwr:
      name: "Port.C Power"
      id: grove_blue_pwr_switch
    rs485_can_pwr:
      name: "RS485&CAN Power"
      id: rs485_can_pwr_switch
    vameter_pwr:
      name: "VAMeter Power"
      id: vameter_pwr_switch
    charge_pwr:
      name: "Charge Power"
      id: charge_pwr_switch
    rs485_can_direction:
      name: "RS485&CAN Power Output"
      id: rs485_can_direction_switch
```

#### 配置变量

- **led_pwr**（可选）：开启 / 关闭 LED 电源。默认 `true`。
  其它选项同 [Switch](https://esphome.io/components/switch#config-switch)。
- **usb_pwr**（可选）：开启 / 关闭 USB 电源。
  其它选项同 [Switch](https://esphome.io/components/switch#config-switch)。
- **grove_red_pwr**（可选）：开启 / 关闭 Port.A（grove red）电源。
  其它选项同 [Switch](https://esphome.io/components/switch#config-switch)。
- **grove_blue_pwr**（可选）：开启 / 关闭 Port.C（grove blue）电源。
  其它选项同 [Switch](https://esphome.io/components/switch#config-switch)。
- **rs485_can_pwr**（可选）：开启 / 关闭 RS485 & CAN 电源。
  其它选项同 [Switch](https://esphome.io/components/switch#config-switch)。
- **vameter_pwr**（可选）：开启 / 关闭 VAMeter 电源。默认 `true`。
  其它选项同 [Switch](https://esphome.io/components/switch#config-switch)。
- **charge_pwr**（可选）：开启 / 关闭充电电源。默认 `true`。
  其它选项同 [Switch](https://esphome.io/components/switch#config-switch)。
- **rs485_can_direction**（可选）：控制 RS485 & CAN 电源的输出方向；开启即启用输出。
  其它选项同 [Switch](https://esphome.io/components/switch#config-switch)。
- **powerhub_id**（可选，[ID](https://esphome.io/guides/configuration-types#id)）：PowerHub 的 ID。

### Select

`powerhub` 的 select 可用于切换 USB Type A 或 USB Type C 接口的 USB 模式。

```yaml
select:
  - platform: powerhub
    usb_mode:
      name: "USB Mode"
      id: usb_mode_select
```

#### 配置变量

- **usb_mode**（可选）：设置 USB Type A 或 USB Type C 端口的 host/device 模式。请注意，不能同时将两个端口都设置为 USB host 模式。
  默认是 device 模式。可选值为 `Default`、`Host for USB-C` 或 `Host for USB-A`。
  其它选项同 [Select](https://esphome.io/components/select#config-select)。
- **powerhub_id**（可选，[ID](https://esphome.io/guides/configuration-types#id)）：PowerHub 的 ID。

### Number

可以通过 number 设置为 RS485 & CAN 接口设定输出电压与电流限制。

```yaml
number:
  - platform: powerhub
    rs485_can_output_voltage:
      name: "RS485&CAN Output Voltage"
    rs485_can_current_limit:
      name: "RS485&CAN Output Current Limit"
```

#### 配置变量

- **rs485_can_output_voltage**（可选）：设置 RS485 & CAN 接口的输出电压。默认 `3000` mV。
  需要开启开关 `rs485_can_direction` 才会生效。
  其它选项同 [Number](https://esphome.io/components/number#config-number)。
- **rs485_can_current_limit**（可选）：设置 RS485 & CAN 接口的输出电流限制。默认 `13` mA。
  需要开启开关 `rs485_can_direction` 才会生效。
  其它选项同 [Number](https://esphome.io/components/number#config-number)。
- **powerhub_id**（可选，[ID](https://esphome.io/guides/configuration-types#id)）：PowerHub 的 ID。

### Light

`powerhub` 的每个电源通道都带有状态 RGB LED，用于指示电源状态。

```yaml
light:
  - platform: powerhub
    usb_c_rgb:
      name: "USB C Light"
    usb_a_rgb:
      name: "USB A Light"
    grove_blue_rgb:
      name: "Port.C Light"
    grove_red_rgb:
      name: "Port.A Light"
    rs485_can_rgb:
      name: "RS485&CAN Light"
    bat_charge_rgb:
      name: "Battery Charge Light"
    pwr_l_rgb:
      name: "Power L Light"
    pwr_r_rgb:
      name: "Power R Light"
```

#### 配置变量

- **usb_c_rgb**（可选）：控制 USB Type C 接口下方的 RGB LED。
  其它选项同 [Light](https://esphome.io/components/light#config-light)。
- **usb_a_rgb**（可选）：控制 USB Type A 接口下方的 RGB LED。
  其它选项同 [Light](https://esphome.io/components/light#config-light)。
- **grove_blue_rgb**（可选）：控制 Port.C（grove blue）接口下方的 RGB LED。
  其它选项同 [Light](https://esphome.io/components/light#config-light)。
- **grove_red_rgb**（可选）：控制 Port.A（grove red）接口下方的 RGB LED。
  其它选项同 [Light](https://esphome.io/components/light#config-light)。
- **rs485_can_rgb**（可选）：控制 RS485 & CAN 接口下方的 RGB LED。
  其它选项同 [Light](https://esphome.io/components/light#config-light)。
- **bat_charge_rgb**（可选）：控制电池充电状态的 RGB LED。该 LED 位于黄色圆形按钮下方。
  其它选项同 [Light](https://esphome.io/components/light#config-light)。
- **pwr_l_rgb**（可选）：控制左侧电源指示 RGB LED。该 LED 位于顶部 PMU 按钮（矩形）左半部分内。
  其它选项同 [Light](https://esphome.io/components/light#config-light)。
- **pwr_r_rgb**（可选）：控制右侧电源指示 RGB LED。该 LED 位于顶部 PMU 按钮（矩形）右半部分内。
  其它选项同 [Light](https://esphome.io/components/light#config-light)。
- **powerhub_id**（可选，[ID](https://esphome.io/guides/configuration-types#id)）：PowerHub 的 ID。

灯光可以用来很方便的指示通道状态，可以根据各种 Sensor 的数据，选择性的更新灯光，比如在启动时打开 PMU 按键里面的灯光：

```yaml
esphome:
  ...
  on_boot:
    then:
      # Turn on the power (L/R) light
      - light.turn_on:
          id: led_pwr_l
          brightness: 100%

      - light.turn_on:
          id: led_pwr_r
          brightness: 100%
```

根据电池电量读数，来选择更新顶部的 PMU 按键灯光：

<div
style="display: flex; gap: 16px; align-items: flex-start;"
>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_ha_full_power.jpg" width="30%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_ha_mid_power.jpg" width="30%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_ha_low_power.jpg" width="30%" />
</div>

```yaml
sensor:
  - platform: powerhub
    ...
    battery_level:
      name: "Battery Percentage"
      id: bat_level_sensor
      on_value:
        - lambda: |-
            auto call_1 = id(led_pwr_l).turn_on();
            auto call_2 = id(led_pwr_r).turn_on();
            auto call_off_1 = id(led_pwr_l).turn_off();
            auto call_off_2 = id(led_pwr_r).turn_off();
            call_1.set_transition_length(1000);
            call_2.set_transition_length(1000);
            call_off_1.set_transition_length(1000);
            call_off_2.set_transition_length(1000);
            call_1.set_color_mode(ColorMode::RGB);
            call_2.set_color_mode(ColorMode::RGB);
            // if read battery level is unknown
            // set the LED color to white
            if ( std::isnan(x) ) {
              call_1.set_rgb(1.0, 1.0, 1.0);
              call_2.set_rgb(1.0, 1.0, 1.0);
              call_1.set_brightness(1.0);
              call_2.set_brightness(1.0);
              call_1.perform();
              call_2.perform();
              return;
            }

            if ( x > 80.0f && x <= 100.0f ) {
                call_1.set_rgb(0, 1.0, 0);
                call_2.set_rgb(0, 1.0, 0);
                call_1.set_brightness(1.0);
                call_2.set_brightness(1.0);
                call_1.perform();
                call_2.perform();
            } else if ( x > 50.0f && x <= 80.0f ) {
                call_1.set_rgb(0, 1.0, 0);
                call_2.set_rgb(0, 1.0, 0);
                call_1.set_brightness(1.0);
                call_2.set_brightness(0.8);
                call_1.perform();
                call_2.perform();
            } else if ( x > 20.0f && x <= 50.0f ) {
                call_1.set_rgb(1.0, 0.95, 0.19); // left only one LED on with YELLOW color suggest low power
                call_1.perform();
                call_off_2.perform();
            } else if ( x > 5.0f && x <= 20.0f ){
                call_1.set_rgb(1.0, 0.43, 0.32); // left only one LED on with RED color suggest extremely low power
                call_1.perform();
                call_off_2.perform();
            } else {
                call_1.set_rgb(1.0, 0.43, 0.32);
                call_1.set_brightness(0.8); // almost empty
                call_1.perform();
                call_off_2.perform();
            }
    ...
```

或者是打开 / 关闭通道开关时，对应的 LED 指示灯光打开 / 关闭：

```yaml
switch:
  - platform: powerhub
    ...
    usb_pwr:
      name: "USB Power"
      id: usb_pwr_switch
      on_turn_on:
        - light.turn_on:
            id: led_usb_a
            brightness: 90%
            # Color maybe
            # red: 100%
            # green: 100%
            # blue: 100%
        - light.turn_on:
            id: led_usb_c
            brightness: 90%
      on_turn_off:
        - light.turn_off:
            id: led_usb_a
        - light.turn_off:
            id: led_usb_c

    grove_red_pwr:
      name: "Port.A Power"
      id: grove_red_pwr_switch
      on_turn_on:
        - light.turn_on:
            id: led_grove_red
            brightness: 90%
      on_turn_off:
        - light.turn_off:
            id: led_grove_red

    grove_blue_pwr:
      name: "Port.C Power"
      id: grove_blue_pwr_switch
      on_turn_on:
        - light.turn_on:
            id: led_grove_blue
            brightness: 90%
      on_turn_off:
        - light.turn_off:
            id: led_grove_blue

    rs485_can_pwr:
      name: "RS485&CAN Power"
      id: rs485_can_pwr_switch
      on_turn_on:
        - light.turn_on:
            id: led_rs485_can
            brightness: 90%
      on_turn_off:
        - light.turn_off:
            id: led_rs485_can

    charge_pwr:
      name: "Charge Power"
      id: charge_pwr_switch
      restore_mode: RESTORE_DEFAULT_ON
      on_turn_on:
        - light.turn_on:
            id: led_bat_charge
            brightness: 90%
      on_turn_off:
        - light.turn_off:
            id: led_bat_charge
    ...
```

在电池充电时使用脉搏 / 呼吸灯指示充电状态（需要为灯光添加 `pulse` 效果）：

<video
autoplay
loop
muted
playsinline
preload="auto"
style="width: 320px; height: auto; display: block;"> <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/powerhub_ha_charging_light.webm" type="video/webm"> </video>

```yaml
light:
  - platform: powerhub
    ...
    bat_charge_rgb:
      id: led_bat_charge
      name: "Battery Charge Light"
      effects:
        - pulse:
            name: "Slow Pulse"
            transition_length: 500ms
            update_interval: 2s
    ...
```

```yaml
text_sensor:
  - platform: powerhub
    charge_status:
      name: "Battery Charge Status"
      id: bat_charge_status_text_sensor
      on_value:
        - lambda: |-
            static std::string last_state = "";
            if (last_state == x) return;
            last_state = x;

            auto call = id(led_bat_charge).turn_on();
            call.set_brightness(0.9);
            call.set_color_mode(ColorMode::RGB);

            if (x == "Charging") {
              // Pulse green
              call.set_rgb(0, 1.0, 0);
              call.set_effect("Slow Pulse");
            } else if (x == "Discharging") {
              // Solid green
              call.set_rgb(0, 1.0, 0);
              call.set_effect("None");
            } else {
              // Solid white
              call.set_rgb(1.0, 1.0, 1.0);
              call.set_effect("None");
            }
            call.perform();
```

### Time

`powerhub` 内置 RX8130 RTC 芯片，可作为设备的时间源。

```yaml
time:
  - platform: powerhub
    id: powerhub_time
```

#### 配置变量

- **powerhub_id**（可选，[ID](https://esphome.io/guides/configuration-types#id)）：PowerHub 的 ID。
- 其它选项同 [Base Time Configuration](https://esphome.io/time/base_time_config)。

### `powerhub.write_time` 动作

该 [Action](https://esphome.io/automations/actions#config-action) 会触发将当前系统时间同步到 RTC 硬件。

\#> 提示 | 未显式触发该动作时，powerhub 组件不会向 RTC 写入时间。

```yaml
on_...:
  - powerhub.write_time

  # 如果需要指定 powerhub 的 id
  - powerhub.write_time:
      id: powerhub_time
```

### `powerhub.read_time` 动作

该 [Action](https://esphome.io/automations/actions#config-action) 会触发从 RTC 硬件同步当前系统时间。

\#> 提示 | 默认情况下，powerhub 组件每 15 分钟会自动读取一次 RTC 时间，并在从 RTC 读取到有效时间戳时同步系统时钟。（可通过 `update_interval` 调整）<br>
此动作可用于触发额外的同步。

```yaml
on_...:
  - powerhub.read_time

  # 如果需要指定 powerhub 的 id
  - powerhub.read_time:
      id: powerhub_time
```

#### 配置示例

一般情况下，至少需要一个额外的时间源用于与 RTC 同步。此类外部时间源可能并非始终可用（例如网络受限）。
为了保证系统时间有效且可靠，系统应在启动时先读取一次 RTC，然后尝试与一个可靠的外部时间源同步。
当与其他时间源成功同步后，可以再将该时间写回 RTC 以重新同步。

```yaml
esphome:
  on_boot:
    then:
      # 系统启动时读取一次 RTC 时间
      powerhub.read_time:

time:
  - platform: powerhub
    # 如果外部 RTC 并不比内部时钟更精准，则无需重复同步
    timezone: Asia/Shanghai
    update_interval: never

  - platform: homeassistant
    # 改为通过网络重复尝试同步 ...
    on_time_sync:
      then:
        # ... 同步成功后更新 RTC
        powerhub.write_time:
```

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115783711588674&bvid=BV1RWBoB2EoW&&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/KxeiOrWAM1Q?si=svJ4XnGq-RM75Ixt" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
