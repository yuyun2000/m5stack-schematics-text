# AtomS3R-CAM Home Assistant 集成

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/4.webp" width="30%">

## 1. 准备工作

1. 硬件
  - 1 x [AtomS3R-CAM](https://shop.m5stack.com/products/atoms3r-camera-kit)
  - 1 x Home Assistant 主机（服务器、迷你主机、NAS 等）
2. 软件及版本
  - [ESPHome Device Builder](https://esphome.io/) 2026.3.0 或更高版本

## 2. 创建设备

1. 打开 ESPHome Dashboard。若出现初始向导，点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%">

2. 点击右下角绿色 **+** 按钮创建新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%">

3. 点击 `New Device Setup` 进入设备创建向导。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%">

4. 输入设备名称，点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/camha3.webp" width="40%">

5. 选择设备类型，点击 `ESP32S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR2.webp" width="30%">

6. 点击 `SKIP` 跳过加密密钥设置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%">

7. 点击 `EDIT` 打开 YAML 编辑器，自定义设备配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/camha4.webp" width="70%">

## 3. 设备配置

### 3.1 外部组件配置

添加 [External Components](https://esphome.io/components/external_components.html) 条目，从 M5Stack ESPHome 仓库加载 `early_init` 组件。

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: [early_init]
```

### 3.2 PSRAM 配置

添加 [PSRAM](https://esphome.io/components/psram.html) 组件，启用摄像头所需的片上八路 PSRAM。

```yaml
psram:
  mode: octal
  speed: 80MHz
```

### 3.3 I2C 总线配置

添加 OV3660 摄像头所需的 [I2C](https://esphome.io/components/i2c.html) 总线。

```yaml
i2c:
  - id: camera_i2c
    sda: GPIO12
    scl: GPIO9
    frequency: 100kHz
    timeout: 10ms
    scan: true
```

### 3.4 摄像头配置

添加 [ESP32 Camera](https://esphome.io/components/esp32_camera.html) 组件，通过 OV3660 摄像头进行视频流传输。

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

## 4. 构建并烧录固件

### 4.1 构建固件

1. 编辑完 YAML 配置后，点击右上角 `SAVE`，再点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/802/unit_fader3.webp" width="70%">

2. 在弹出对话框中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%">

3. 等待固件编译完成，点击 `Download` 并选择 `Factory format (Previously Modern)` 将固件文件保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%">

?>Info| 完整的配置示例请参见 [AtomS3R-CAM](https://github.com/m5stack/esphome-yaml/blob/main/examples/camera/atoms3r-cam-example.yaml)。首次构建可能需要较长时间，具体取决于 Home Assistant 主机性能及网络状况。

### 4.2 烧录固件

4. 使用 USB Type-C 线将 AtomS3R 连接到电脑。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%">

5. 在串口选择对话框中，选择正确的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%">

6. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%">

7. 选择步骤 3 中下载的固件文件，开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/camha8.png" width="40%">

!>Warning| 烧录完成后必须重置设备，否则固件可能无法正常启动。


## 5. 开始在 Home Assistant 中使用

1. 在 Home Assistant 中，前往 `Settings` > `Devices & Services` 打开集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%">

2. 在 `Discovered` 区域找到 **AtomS3R-CAM** 设备，点击 `CONFIGURE`，按向导完成设置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/camha6.webp" width="40%">

3. 设备添加后，可在设备列表中查看。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/camha1.png" width="40%">

4. 最后，将传感器实体添加到仪表板中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/camha2.png" width="40%">
