# Unit Scroll Home Assistant 集成

本教程将介绍如何使用 **Unit Scroll** 滚轮形态的旋转编码器拓展单元搭配 CoreS3 主控，并将其集成到 Home Assistant 中，实现编码器数值监控、按键切换以及 RGB 灯光控制。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/4.webp" width="30%" />

## 准备工作

1. 硬件清单

- 1 x [Unit Scroll](https://shop.m5stack.com/products/scroll-unit-with-hollow-shaft-encoder-ec10e1220501)
- 1 x [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x Home Assistant 主机（服务器、迷你电脑、NAS 等）

2. 软件与版本

- Home Assistant 2026.2.0 及以上
- [ESPHome Device Builder](https://esphome.io/) 2026.2.2 及以上

## 创建设备

1. 打开 ESPHome Builder，点击右下角的蓝色 **+Create device** 按钮，开始创建新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/HA_create_device.png" width="70%" />

2. 点击 `Create new project`，进入设备创建向导。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/HA_create_project.png" width="40%" />

3. 在搜索栏输入设备名称，如 M5Stack CoreS3，然后点击 `+Select`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/HA_select_coard_cores3.png" width="40%" />

4. 输入设备名称 `Unit Scroll`，然后点击 `Finish setup`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/unit_scroll_HA_create_device.png" width="40%" />

5. 然后会自动进入 YAML 配置页面，可自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/unit_scroll_HA_yaml_edit.png" width="70%" />

## 修改配置

### 外部组件配置

添加 [External](https://esphome.io/components/external_components/) 组件，加载 Unit Scroll 自定义组件：

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: unit_scroll
    refresh: 0s

unit_scroll:
  id: my_scroll
  i2c_id: grove_i2c
  address: 0x40
  direction: true # false = 顺时针增加数值，true = 逆时针增加数值
  rgb_red: 0
  rgb_green: 255
  rgb_blue: 0
```

主要参数说明：

| 参数                                 | 值          | 说明                                                    |
| ------------------------------------ | ----------- | ------------------------------------------------------- |
| `id`                                 | my_scroll   | Unit Scroll 组件 ID，供后续传感器、输出和 Lambda 调用。 |
| `i2c_id`                             | grove_i2c   | 绑定的 I2C 总线 ID。                                    |
| `address`                            | 0x40        | Unit Scroll 默认 I2C 地址。                             |
| `direction`                          | true        | 编码器计数方向，可根据实际旋转方向调整。                |
| `rgb_red` / `rgb_green` / `rgb_blue` | 0 / 255 / 0 | 上电后的 RGB LED 初始颜色。                             |

### I2C 总线配置

添加 [I2C](https://esphome.io/components/i2c/) 组件，配置 Unit Scroll 与 CoreS3 之间的通信引脚。

```yaml
i2c:
  - id: grove_i2c
    sda: GPIO2
    scl: GPIO1
    scan: true
```

?> 说明 | CoreS3 的 PORT.A 接口对应 SDA: GPIO2，SCL: GPIO1。若使用其他端口，请根据实际引脚进行调整。

### 全局变量配置

添加 [Globals](https://esphome.io/components/globals/) 组件，用于保存 RGB LED 的启用状态：

```yaml
globals:
  - id: scroll_led_enabled
    type: bool
    restore_value: false
    initial_value: 'true'
```

### 轮询与灯光控制

添加 [Interval](https://esphome.io/components/interval/) 组件，周期性读取编码器数值与按键状态，并根据编码器数值更新 RGB 颜色。按下 Unit Scroll 按键时，可以切换 RGB LED 开 / 关。

```yaml
interval:
  - interval: 100ms
    then:
      - lambda: |-
          static bool last_button = false;
          static uint16_t last_value = 0;
          static bool has_last_value = false;

          bool button = id(my_scroll).get_button_state();
          bool led_toggled = false;
          if (button && !last_button) {
            id(scroll_led_enabled) = !id(scroll_led_enabled);
            led_toggled = true;
            if (!id(scroll_led_enabled)) {
              auto call = id(scroll_rgb_led).turn_off();
              call.perform();
            }
            ESP_LOGI("unit_scroll_demo", "RGB LED is now %s", id(scroll_led_enabled) ? "ON" : "OFF");
          }
          last_button = button;

          uint16_t value = id(my_scroll).get_value();
          id(scroll_encoder_value).publish_state(value);
          bool value_changed = !has_last_value || value != last_value;

          uint8_t position = static_cast<uint8_t>(value & 0xFF);
          uint8_t region = position / 43;
          uint8_t remainder = (position - (region * 43)) * 6;
          uint8_t p = 0;
          uint8_t q = 255 - remainder;
          uint8_t t = remainder;
          uint8_t r = 0;
          uint8_t g = 0;
          uint8_t b = 0;

          switch (region) {
            case 0: r = 255; g = t; b = p; break;
            case 1: r = q; g = 255; b = p; break;
            case 2: r = p; g = 255; b = t; break;
            case 3: r = p; g = q; b = 255; break;
            case 4: r = t; g = p; b = 255; break;
            default: r = 255; g = p; b = q; break;
          }

          if (id(scroll_led_enabled) && (value_changed || led_toggled)) {
            auto call = id(scroll_rgb_led).turn_on();
            call.set_rgb(r / 255.0f, g / 255.0f, b / 255.0f);
            call.perform();
          }

          if (value_changed) {
            ESP_LOGD("unit_scroll_demo", "Encoder %u -> RGB(%u, %u, %u), RGB LED %s", value, r, g, b,
                     id(scroll_led_enabled) ? "on" : "off");
            last_value = value;
            has_last_value = true;
          }
```

### 传感器配置

添加 [Sensor](https://esphome.io/components/sensor/) 组件，将编码器数值发布到 Home Assistant。

```yaml
sensor:
  - platform: template
    id: scroll_encoder_value
    name: "Encoder Value"
    icon: mdi:rotate-right
    accuracy_decimals: 0
    update_interval: never
```

主要参数说明：

| 参数              | 值                   | 说明                                             |
| ----------------- | -------------------- | ------------------------------------------------ |
| `platform`        | template             | 使用模板传感器接收 Lambda 中发布的编码器数值。   |
| `id`              | scroll_encoder_value | 供 Lambda 调用并发布状态。                       |
| `name`            | Encoder Value        | Home Assistant 中显示的实体名称。                |
| `update_interval` | never                | 不自动轮询，由 `interval` 中的 Lambda 主动更新。 |

### 输出配置

添加 [Output](https://esphome.io/components/output/) 组件，将 Unit Scroll 的 RGB 三个通道暴露为输出。

```yaml
output:
  - platform: unit_scroll
    id: scroll_rgb_red_output
    unit_scroll_id: my_scroll
    channel: rgb_red

  - platform: unit_scroll
    id: scroll_rgb_green_output
    unit_scroll_id: my_scroll
    channel: rgb_green

  - platform: unit_scroll
    id: scroll_rgb_blue_output
    unit_scroll_id: my_scroll
    channel: rgb_blue
```

### 灯光配置

添加 [Light](https://esphome.io/components/light/) 组件，将三个 RGB 输出组合为一个 RGB 灯实体。

```yaml
light:
  - platform: rgb
    id: scroll_rgb_led
    name: "RGB LED"
    red: scroll_rgb_red_output
    green: scroll_rgb_green_output
    blue: scroll_rgb_blue_output
    restore_mode: ALWAYS_OFF
    default_transition_length: 0s
```

## 下载和烧录固件

### 编译固件

1. 完成 YAML 修改后，点击右下角的 `Save` 保存配置，再点击 `Install`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/unit_scroll_HA_Install.png" width="70%" />

2. 在弹出窗口中先展开 `Advanced options`，再点击 `Download firmware binary`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/unit_scroll_HA_esp_builder_install_method.png" width="40%" />

3. 等待固件编译完成，固件会自动保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/unit_scroll_HA_bin.png" width="70%" />

### 烧录固件

1. 使用 USB Type-C 线缆将 CoreS3 连接到电脑。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%" />

2. 在弹出的串口选择窗口中，选择正确的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%" />

3. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%" />

4. 选择编译固件步骤 3 中下载的固件文件并开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/unit_scroll_HA_esp_home_install.png" width="40%" />

!> 注意 | 烧录完成后必须重置设备，否则固件可能无法正常启动。

## 开始使用

1. 在 Home Assistant 中依次点击 `Settings` > `Devices & Services`，进入集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%" />

2. 在 `Discovered` 区域找到 **Unit Scroll** 设备，点击 `Add` ，然后填入 YAML 配置中的 Encryption Key 后点击 `Submit` 。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/unit_scroll_HA_discover.png" width="40%" /><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/unit_scroll_HA_encryption_key.png" width="53%" />

3. 设备添加完成后，在设备详情页中可以看到编码器数值与 RGB LED 等实体，并显示其实时状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/unit_scroll_HA_add_dashboard.png" width="40%" />

4. 最后，将这些实体添加到仪表板中，即可实时查看编码器数值，并控制 Unit Scroll 的 RGB LED。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/unit_scroll_HA_example.gif" width="40%" />
