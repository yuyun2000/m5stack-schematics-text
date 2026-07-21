# Unit Key Home Assistant 集成

本教程将介绍如何使用 **Unit Key** 单按键输入单元搭配 CoreS3 主控，并将其集成到 Home Assistant 中，实现按键状态获取与灯光控制。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/key/key_01.webp" width="30%" />

## 1. 准备工作

1. 硬件清单

- 1 x [Unit Key](https://shop.m5stack.com/products/mechanical-key-button-unit)
- 1 x [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x Home Assistant 主机（服务器、迷你电脑、NAS 等）

2. 软件与版本

- Home Assistant 2026.2.0 及以上
- [ESPHome Device Builder](https://esphome.io/) 2026.2.2 及以上

## 2. 创建设备

1. 打开 ESPHome Dashboard，若出现初始引导界面，点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%" />

2. 点击右下角的绿色 **+** 按钮，开始创建新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%" />

3. 点击 `New Device Setup`，进入设备创建向导。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%" />

4. 输入设备名称，点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/unit_key_HA_create_device.png" width="40%" />

5. 选择设备类型，点击 `ESP32S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR2.webp" width="30%" />

6. 点击 `SKIP`，跳过加密密钥设置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%" />

7. 点击 `EDIT`，进入 YAML 配置页面，自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/unit_key_HA_yaml_edit.png" width="70%" />

## 3. 设备配置

?> 说明 | 1\. CoreS3 的 PORT.B 接口对应 LED: GPIO9，BTN: GPIO1。若使用其他端口，请根据实际引脚进行调整。  
2\. CoreS3 的 PORT 接口电源由内部电源管理芯片控制，`board` 请务必使用 `m5stack-cores3`，`framework` 请务必使用 `arduino`， 才能正常使用 Unit Key。

### 3.1 传感器配置

添加 [Binary Sensor](https://esphome.io/components/sensor/) 组件以获取按键状态。

```yaml
binary_sensor:
  - platform: gpio
    name: "Button"
    id: unit_key_button
    pin:
      number: GPIO8 # CoreS3 PORT.B，请根据实际连接的 GPIO 引脚进行调整
      mode:
        input: true
        pullup: true
      inverted: true
    filters:
      - delayed_on: 10ms
      - delayed_off: 10ms
    on_press:
      then:
        - logger.log: "Pressed"
        - light.toggle: unit_key_led
    on_multi_click:
      - timing:
          - ON for at least 1s
        then:
          - logger.log: "Hold"
          - light.turn_off: unit_key_led
```

### 3.2 灯光配置

添加 [Light](https://esphome.io/components/light/) 组件以控制背光 RGB LED。

```yaml
light:
  - platform: neopixelbus
    name: "LED"
    id: unit_key_led
    type: GRB            
    variant: SK6812
    pin: GPIO9 # CoreS3 PORT.B，请根据实际连接的 GPIO 引脚进行调整
    num_leds: 1
    method:
      type: esp32_rmt
      channel: 0
    default_transition_length: 200ms
    restore_mode: RESTORE_DEFAULT_OFF
```

## 4. 下载和烧录固件

### 4.1 编译固件

1. 完成 YAML 修改后，点击右上角的 `SAVE` 保存配置，再点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/unit_key_HA_Install.png" width="70%" />

2. 在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/unit_key_HA_esp_builder_install_method.png" width="40%" />

3. 等待固件编译完成，点击 `Download` 并选择 `Factory format (Previously Modern)`，将固件保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/unit_key_HA_bin.png" width="70%" />

### 4.2 烧录固件

1. 使用 USB Type-C 线缆将 CoreS3 连接到电脑。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%" />

2. 在弹出的串口选择窗口中，选择正确的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%" />

3. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%" />

4. 选择步骤 3 中下载的固件文件并开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/unit_key_HA_esp_home_install.png" width="40%" />

!> 注意 | 烧录完成后必须重置设备，否则固件可能无法正常启动。

## 5. 开始使用

1. 在 Home Assistant 中依次点击 `Settings` > `Devices & Services`，进入集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%" />

2. 在 `Discovered` 区域找到 **Unit Key** 设备，点击 `CONFIGURE` 并按照向导完成配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/unit_key_HA_discover.png" width="40%" />

3. 设备添加完成后，在设备详情页中可以看到按键状态和 LED 灯光状态实时信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/unit_key_HA_add_dashboard.png" width="40%" />

4. 最后，将这些传感器实体添加到仪表板中，即可实时监控按键状态与灯光信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/unit_key_HA_example.png" width="40%" />
