# AtomS3R-M12 Home Assistant 集成

本教程介绍如何将 AtomS3R-M12 集成到 Home Assistant 中。

<div style="display: flex; gap: 15px; flex-wrap: wrap;">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R-M12/4.webp" width="30%"/>
</div>

## 准备工作

- Home Assistant 主机。
- 在 Home Assistant 中安装并启用 [ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。
- [OV3660 数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/OV3660_datasheet.pdf)。
- 查看 ESPHome 上的最新配置示例：[ESP32 摄像头](https://esphome.io/components/esp32_camera/)。

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 AtomS3R-M12 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/atoms3r_m12_manifest_2026.1.1.json">一键烧录固件</EspWebTool>

## 注意事项

本教程使用 ESPHome 2025.12.5 编译和上传固件。如果遇到编译 / 上传问题，请考虑切换 ESPHome 版本。

## 创建设备

1. 点击右下角的绿色按钮创建设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%"/>

2. 点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%"/>

3. 点击 `New Device Setup`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%"/>

4. 输入设备名称，然后点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA4.webp" width="30%"/>

5. 点击 `ESP32-S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA5.webp" width="30%"/>

6. 点击 `SKIP`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%"/>

7. 点击 `EDIT`，我们可以通过 YAML 文件自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA20.webp" width="70%"/>

## 修改配置

以下是代码的核心部分。下面提供了相关的参考和说明。

### 基本信息和启动操作

**添加 [on_boot](https://esphome.io/components/esphome/#on_boot) 组件：**

```yaml
esphome:
  name: atoms3r-m12
  friendly_name: AtomS3R-M12
  on_boot:
    priority: 800
    then:
      - lambda: |-
          gpio_set_direction(GPIO_NUM_18, GPIO_MODE_OUTPUT);
          gpio_set_level(GPIO_NUM_18, 0);
          vTaskDelay(pdMS_TO_TICKS(1500));
```

\#> 注意 | 由于硬件电路设计，AtomS3R-M12 需要在上电后将 GPIO18 拉低，以启用正确的 I²C 通信。如果在 I²C 总线初始化或访问前没有将 GPIO18 设置为低电平，I²C 通信可能会失败。因此，GPIO18 控制必须分配最高优先级，以确保在系统启动的早期阶段被拉低。

### PSRAM 配置

**添加 [PSRAM](https://esphome.io/components/psram/) 组件：**

```yaml
psram:
  mode: octal
  speed: 80MHz
```

### 外部组件

**添加 [External Components](https://esphome.io/components/external_components/) 组件：**

```yaml
external_components:
  - source: github://DennisGaida/m5stack-atoms3r-components/components@main
    components: [bmi270_bmm150]
```

\#> 注意 | 由于 ESPHome 还没有提供官方的 BMI270 / BMM150 组件，该项目使用了由社区开发者贡献的第三方组件库。我们向[作者](https://github.com/DennisGaida/m5stack-atoms3r-components/tree/main/components/bmi270_bmm150)的贡献表示衷心感谢。

### I2C 总线配置

**添加 [I2C](https://esphome.io/components/i2c/) 组件：**

```yaml
i2c:
  - id: BMI270_150
    sda: GPIO45
    scl: GPIO0
  - id: camera_i2c
    sda: GPIO12
    scl: GPIO9
    frequency: 100kHz
    timeout: 10ms
```

### 传感器配置

**添加 [Sensor](https://esphome.io/components/sensor) 组件：**

```yaml
sensor:
  - platform: bmi270_bmm150
    i2c_id: BMI270_150
    address: 0x68
    update_interval: 3s
    acceleration_x:
      name: "BMI270 Accel X"
    acceleration_y:
      name: "BMI270 Accel Y"
    acceleration_z:
      name: "BMI270 Accel Z"
    gyroscope_x:
      name: "BMI270 Gyro X"
    gyroscope_y:
      name: "BMI270 Gyro Y"
    gyroscope_z:
      name: "BMI270 Gyro Z"
    temperature:
      name: "BMI270 Temperature"
```

### 摄像头配置

**添加 [ESP32 Camera](https://esphome.io/components/esp32_camera/) 组件：**

```yaml
esp32_camera:
  name: "OV3660 Camera"
  external_clock:
    pin: GPIO21
    frequency: 20MHz
  i2c_id: camera_i2c
  data_pins: [GPIO3, GPIO42, GPIO46, GPIO48, GPIO4, GPIO17, GPIO11, GPIO13]
  vsync_pin: GPIO10
  href_pin: GPIO14
  pixel_clock_pin: GPIO40
  resolution: 640X480
  jpeg_quality: 10
```

## 下载和烧录固件

1. 修改完成后，点击右上角的 `SAVE` 和 `INSTALL`，然后在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA16.webp" width="40%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

2. 选择 `Factory format(Previously Modern)`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%"/>

\#> 提示 | 点击 [AtomS3R-M12](https://github.com/m5stack/esphome-yaml/blob/main/examples/camera/atoms3r-m12-example.yaml) 查看完整的示例配置。首次构建可能需要一些时间，具体取决于 Home Assistant 主机的性能和网络质量。

3. 通过 USB Type‑C 数据线将设备连接到主机。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT` 以连接到设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%"/>

4. 定位相应的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA13.webp" width="40%"/>

5. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%"/>

6. 选择编译好的固件上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA11.webp" width="40%"/>

7. 下载完成后，重新启动设备。

## 开始使用

1. 点击 `Settings` -> `Device & services` 检查设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%"/>

2. 我们可以在 `Discover` 部分找到相应的设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA24.webp" width="40%"/>

3. 添加设备后，数据将正确显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA26.webp" width="40%"/>

4. 最后，我们将这些实体添加到 Dashboard，以下是其显示结果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA15.webp" width="40%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA29.webp" width="40%"/>
