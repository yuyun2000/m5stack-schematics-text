# Unit Step16 Home Assistant 集成

本教程将介绍如何使用 **Unit Step16** 16 位旋转编码器控制单元集成至 Home Assistant，实现旋钮数值与灯光控制。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/step16-Home_Assistant_tutorial_cover_ZH.png" width="60%">

## 准备工作

- Home Assistant 主机。
- [Atom-Lite](/zh_CN/core/ATOM%20Lite)。
- 在 Home Assistant 中安装并启用 [ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。

## 注意事项

在本教程中，固件使用 ESPHome 2026.1.2 进行编译和上传。如果遇到编译 / 上传问题，请考虑将 ESPHome 切换到此版本。

## 创建设备

1. 创建新设备。点击右下角的绿色按钮创建设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%"/>

2. 创建设备名称。

- 点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%"/>

- 点击 `New Device Setup`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%"/>

- 输入设备名称并点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/HA7.webp" width="40%"/>

3. 选择设备类型。

- 点击 `ESP32`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA9.webp" width="30%"/>

- 点击 `SKIP`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%"/>

4. 开始编辑 YAML 文件。

- 点击 `EDIT`。我们可以通过 YAML 文件自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/HA5.webp" width="70%"/>

## 设备配置

以下是代码的核心部分。下面提供了相关的参考和说明。

### 外部组件配置

添加 [External](https://esphome.io/components/external_components/) 组件：

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: unit_step16
    refresh: 0s

unit_step16:
  id: my_step16
  i2c_id: bsp_iic
  address: 0x48
```

### I2C 配置

```yaml
i2c:
  - id: bsp_iic
    scl: GPIO32
    sda: GPIO26
    scan: True
```

### 传感器配置

添加 [Sensor](https://esphome.io/components/sensor) 组件：

```yaml
sensor:
  - platform: unit_step16
    unit_step16_id: my_step16
    name: "Encoder Value"
    update_interval: 100ms
    on_value:
      then:
        - logger.log:
            format: "Encoder value changed to: %.0f"
            args: ["x"]
```

### 输出配置

添加 [Output](https://esphome.io/components/output/) 组件：

```yaml
output:
  - platform: unit_step16
    id: led_brightness_output
    unit_step16_id: my_step16
    channel: led_brightness

  - platform: unit_step16
    id: rgb_brightness_output
    unit_step16_id: my_step16
    channel: rgb_brightness

  - platform: unit_step16
    id: rgb_red_output
    unit_step16_id: my_step16
    channel: rgb_red

  - platform: unit_step16
    id: rgb_green_output
    unit_step16_id: my_step16
    channel: rgb_green

  - platform: unit_step16
    id: rgb_blue_output
    unit_step16_id: my_step16
    channel: rgb_blue
```

### 灯光配置

添加 [Light](https://esphome.io/components/light/) 组件：

```yaml
light:
  - platform: rgb
    id: step16_rgb_light
    name: "Step16 RGB Light"
    red: rgb_red_output
    green: rgb_green_output
    blue: rgb_blue_output
    restore_mode: ALWAYS_ON
    default_transition_length: 0s

  - platform: monochromatic
    id: step16_led_display
    name: "Step16 LED Display"
    output: led_brightness_output
    restore_mode: ALWAYS_ON
    default_transition_length: 0s
```

### 数字配置

添加 [Number](https://esphome.io/components/number/) 组件：

```yaml
number:
  - platform: template
    name: "RGB Brightness"
    min_value: 0
    max_value: 100
    step: 1
    optimistic: true
    initial_value: 50
    on_value:
      then:
        - output.set_level:
            id: rgb_brightness_output
            level: !lambda "return x / 100.0;"
```

## 下载和烧录固件

1. 修改后，点击右上角的 `SAVE` 和 `INSTALL`，然后在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

2. 固件编译完成后，点击下载并选择 `Factory format (Previously Modern)`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%"/>

?> 提示 | 点击 [Unit Step16](https://github.com/m5stack/esphome-yaml/blob/main/examples/sensor/unit-step16.yaml) 查看完整的示例配置。首次构建可能需要一段时间，具体取决于 Home Assistant 主机的性能和网络质量。

3. 通过 USB Type-C 线缆将设备连接到主机。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT` 连接设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%"/>

4. 找到对应的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%"/>

5. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%"/>

6. 选择之前编译的固件，然后点击`INSTALL`进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/HA8.webp" width="40%"/>

7. 烧录完成后重新启动设备。

## 开始使用

1. 点击 `Settings` -> `Device & services` 检查设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%"/>

2. 我们可以在 `Discover` 部分找到相应的设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/HA6.webp" width="40%"/>

3. 添加设备后，数据将正确显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/HA4.webp" width="40%"/>

4. 最后，我们将这些实体添加到仪表板，以下显示了它们的显示结果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/HA2.webp" width="40%"/>

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=116181767818146&bvid=BV1zKPszFEnf&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/0Hzkyp_wt7A?si=dPQYrgVXJacz7WCx" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
