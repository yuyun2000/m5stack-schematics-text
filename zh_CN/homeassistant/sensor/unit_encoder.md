# Unit Encoder Home Assistant 集成

本教程将使用 **Unit Encoder** 旋转编码器搭配 Atom Lite 主控，并将其集成到 Home Assistant 中，实现旋钮数值读取、按键检测与 RGB LED 控制。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/encoder/encoder_05.webp" width="30%"/>

## 准备工作

1. 硬件清单。

- 1 x [Unit Encoder](https://shop.m5stack.com/products/unit-encoder)。
- 1 x [Atom Lite](https://shop.m5stack.com/products/atom-lite-esp32-development-board)。
- 1 x HY2.0-4P Grove 连接线 (20cm)。
- 1 x Home Assistant 主机。

2. 软件与版本。

- Home Assistant 2026.5.0 及以上。
- [ESPHome Device Builder](https://esphome.io/) 2026.4.5 及以上。

## 创建设备

1. 打开 ESPHome Dashboard，若出现初始引导界面，点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%"/>

2. 点击右下角的绿色 **+** 按钮，开始创建新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%"/>

3. 点击 `New Device Setup`，进入设备创建向导。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%"/>

4. 输入设备名称，点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/esphome1.png" width="30%"/>

5. 选择设备类型，先取消勾选 `Use recommended settings`，然后选择 `ESP32`，在详情页中找到 `Unit Encoder` 并选中，点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA9.webp" width="30%"/>

6. 点击 `SKIP`，跳过加密密钥设置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%"/>

7. 点击 `EDIT`，进入 YAML 配置页面，自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/esphome7.png" width="70%"/>

## 设备配置

### 外部组件配置

在 YAML 文件中添加 [External Components](https://esphome.io/components/external_components/) 配置，加载 Unit Encoder 驱动。

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: [m5unit_encoder]
    refresh: 0s
```

### I2C 总线配置

- **添加 [I2C](https://esphome.io/components/i2c/) 组件**，配置 Unit Encoder 与 Atom Lite 之间的通信引脚。

```yaml
i2c:
  sda: GPIO26
  scl: GPIO32
  scan: true
```

?> 说明 | Atom Lite Grove 接口对应 SDA: GPIO26，SCL: GPIO32。Unit Encoder 默认 I2C 地址为 0x40。若使用其他接口，请根据实际管脚进行调整。

### Sensor 传感器配置

- **添加 [Sensor](https://esphome.io/components/sensor/) 组件**，读取编码器旋转数值。

```yaml
sensor:
  - platform: m5unit_encoder
    id: unit_encoder_1
    name: "Encoder Value"
```

### Binary Sensor 按键配置

- **添加 [Binary Sensor](https://esphome.io/components/binary_sensor/) 组件**，检测编码器按键按下状态。

```yaml
binary_sensor:
  - platform: m5unit_encoder
    m5unit_encoder_id: unit_encoder_1
    name: "Encoder Button"
```

### Output 输出配置

- **添加 [Output](https://esphome.io/components/output/) 组件**，将两颗 SK6812 RGB LED 的每个颜色通道映射为独立输出，供 Light 组件调用。

```yaml
output:
  - platform: m5unit_encoder
    m5unit_encoder_id: unit_encoder_1
    led_index: 0
    channel: red
    id: led0_red
  - platform: m5unit_encoder
    m5unit_encoder_id: unit_encoder_1
    led_index: 0
    channel: green
    id: led0_green
  - platform: m5unit_encoder
    m5unit_encoder_id: unit_encoder_1
    led_index: 0
    channel: blue
    id: led0_blue
  - platform: m5unit_encoder
    m5unit_encoder_id: unit_encoder_1
    led_index: 1
    channel: red
    id: led1_red
  - platform: m5unit_encoder
    m5unit_encoder_id: unit_encoder_1
    led_index: 1
    channel: green
    id: led1_green
  - platform: m5unit_encoder
    m5unit_encoder_id: unit_encoder_1
    led_index: 1
    channel: blue
    id: led1_blue
```

### Light 灯光配置

- **添加 [Light](https://esphome.io/components/light/) 组件**，控制 Unit Encoder 内置的 2 颗 SK6812 可编程 RGB LED。

```yaml
light:
  - platform: rgb
    name: "LED 0"
    red: led0_red
    green: led0_green
    blue: led0_blue
  - platform: rgb
    name: "LED 1"
    red: led1_red
    green: led1_green
    blue: led1_blue
```

主要参数说明：

| 参数 | 说明 |
| ---- | ---- |
| `m5unit_encoder_id` | 关联到对应的 m5unit_encoder sensor 实例 ID |
| `led_index` | LED 索引，0 或 1，对应两颗 SK6812 LED |
| `channel` | 颜色通道，可选 `red`、`green`、`blue` |

## 下载和烧录固件

### 编译固件

1. 完成 YAML 修改后，点击右上角的 `SAVE` 保存配置，再点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/esphome2.png" width="70%"/>

2. 在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

3. 等待固件编译完成，点击 `Download` 并选择 `Factory format (Previously Modern)`，将固件保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%"/>

?> 提示 | 点击 [Unit Encoder](https://github.com/m5stack/esphome-yaml/blob/main/examples/sensor/m5unit_encoder.yaml) 查看完整的示例配置。首次构建可能需要一段时间，具体取决于 Home Assistant 主机的性能和网络质量。

### 烧录固件

4. 通过 USB Type-C 线缆将 Atom Lite 连接到电脑。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%"/>

5. 在弹出的串口选择窗口中，找到对应的串口号并选择。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%"/>

6. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%"/>

7. 选择步骤 3 中下载的固件文件进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/esphome6.png" width="40%"/>


## 开始使用

1. 在 Home Assistant 中依次点击 `Settings` > `Devices & Services`，进入集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%"/>

2. 在 `Discovered` 区域找到已上线的 **Unit Encoder** 设备，点击 `CONFIGURE` 并按照提示完成添加。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/esphome5.png" width="40%"/>

3. 添加成功后，设备页面将显示编码器数值、按键状态和 RGB LED 控制实体。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/sphome3.png" width="40%"/>

4. 最后，将传感器实体添加到仪表板，即可实时查看编码器数值与按键状态，并控制 LED 颜色。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/esphome4.png" width="40%"/>
