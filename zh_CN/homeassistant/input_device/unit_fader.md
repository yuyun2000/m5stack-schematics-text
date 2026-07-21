# Unit Fader Home Assistant 集成

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/fader/fader_01.webp" width="30%">

## 1. 准备工作

1. 硬件
  - 1 x [Unit Fader](https://shop.m5stack.com/products/fader-unit-with-b10k-potentiometer-sk6812)
  - 1 x [AtomS3R](https://shop.m5stack.com/products/atoms3r)
  - 1 x HY2.0-4P Grove 连接线 (20cm)
  - 1 x Home Assistant 主机（服务器、迷你主机、NAS 等）
2. 软件与版本
  - Home Assistant 2026.2.0 或更新版本
    - [ESPHome Device Builder](https://esphome.io/) 2026.2.2 或更新版本

## 2. 创建设备

1. 打开 ESPHome Dashboard，若出现初始向导，点击 `CONTINUE` 继续。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%">

2. 点击右下角绿色的 **+** 按钮，新建设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%">

3. 点击 `New Device Setup` 进入设备创建向导。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%">

4. 输入设备名称并点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/802/unit_fader2.webp" width="40%">

5. 选择设备类型并点击 `ESP32S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR2.webp" width="30%">

6. 点击 `SKIP` 跳过加密密钥设置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%">

7. 点击 `EDIT` 打开 YAML 编辑器，开始自定义设备配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/802/unit_fader1.webp" width="70%">

## 3. 设备配置

### 3.1 传感器配置

添加 [Sensor](https://esphome.io/components/sensor/) 组件以读取电位器数值。

```yaml
sensor:
  - platform: adc
    pin: GPIO1
    name: "Fader ADC"
    id: fader_adc
    update_interval: 100ms
    attenuation: 12db
    filters:
      - exponential_moving_average:
          alpha: 0.2
```

### 3.2 灯光配置

添加 [Light](https://esphome.io/components/light/) 组件以控制 LED 灯带。

```yaml
light:
  - platform: esp32_rmt_led_strip
    rgb_order: GRB
    pin: GPIO2
    num_leds: 14
    name: "Fader LED Strip"
    id: led_strip
    chipset: ws2812
```

## 4. 构建并烧录固件

### 4.1 构建固件

1. 编辑完成 YAML 配置后，点击右上角 `SAVE`，然后点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/802/unit_fader3.webp" width="70%">

2. 在弹出的对话框中选择 `Manual Download`（手动下载）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%">

3. 等待固件编译完成，点击 `Download`，选择 `Factory format (Previously Modern)`，将固件文件保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%">

?>Info| 完整的配置示例请参考 [Unit Fader](https://github.com/m5stack/esphome-yaml/blob/main/examples/sensor/unit_fader.yaml)。首次编译的时间可能根据 Home Assistant 主机性能和网络状况有所不同。

### 4.2 烧录固件

4. 使用 USB Type-C 数据线将 AtomS3R 连接到电脑，打开 [ESPHome Web](https://web.esphome.io/)，点击 `CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%">

5. 在串口选择对话框中，选择正确的串口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%">

6. 点击 `INSTALL` 开始安装。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%">

7. 选择第 3 步中下载的固件文件，开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/802/unit_fader7.webp" width="40%">

!>Warning| 烧录完成后必须重启设备，否则固件可能无法正常启动。


## 5. 在 Home Assistant 中使用

1. 在 Home Assistant 中，进入 `Settings` > `Devices & Services` 打开集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%">

2. 在 `Discovered` 区域找到 **Unit Fader** 设备，点击 `CONFIGURE`，并按照向导完成配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/802/unit_fader4.webp" width="40%">

3. 设备添加完成后，可以在设备列表中查看到该设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/802/unit_fader6.webp" width="40%">

4. 最后，将相关实体添加到 Dashboard 中，以便在界面上进行控制和监控。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/802/unit_fader5.webp" width="40%">
