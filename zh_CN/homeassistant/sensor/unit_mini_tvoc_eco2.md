# Unit Mini TVOC/eCO2 Home Assistant 集成

本教程将介绍如何使用 **Unit Mini TVOC/eCO2** 气体传感器单元搭配 AtomS3R 主控，并将其集成到 Home Assistant 中，实现对空气中 TVOC（总挥发性有机化合物）和 eCO2（等效二氧化碳）浓度的实时监测。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tvoc/tvoc_01.webp" width="30%" />

## 1. 准备工作

1. 硬件清单

- 1 x [Unit Mini TVOC/eCO2](https://shop.m5stack.com/products/tvoc-eco2-gas-unit-sgp30)
- 1 x [AtomS3R](https://shop.m5stack.com/products/atoms3r)
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

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/727/unit_tovceco2_HA_create_device.png" width="40%" />

5. 选择设备类型，点击 `ESP32S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR2.webp" width="30%" />

6. 点击 `SKIP`，跳过加密密钥设置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%" />

7. 点击 `EDIT`，进入 YAML 配置页面，自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/727/unit_tovceco2_HA_yaml_edit.png" width="70%" />

## 3. 设备配置

### 3.1 I2C 总线配置

添加 [I2C](https://esphome.io/components/i2c/) 组件，配置 Unit Mini TVOC/eCO2 与 AtomS3R 之间的通信引脚。

```yaml
i2c:
  sda: GPIO2
  scl: GPIO1
  scan: true
```

?> 说明 | AtomS3R 的 PORT.A 接口对应 SDA: GPIO2，SCL: GPIO1。若使用其他端口，请根据实际引脚进行调整。

### 3.2 传感器配置

添加 [Sensor](https://esphome.io/components/sensor/) 组件，启用 SPG30 传感器实体。

```yaml
sensor:
  - platform: sgp30
    address: 0x58
    update_interval: 2s
    store_baseline: true
    # Optional
    # baseline:
    #   eco2_baseline: 0x190 #400
    #   tvoc_baseline: 0x0   #0
    eco2:
      name: "eCO2"
    tvoc:
      name: "TVOC"
```

主要参数说明：

| 参数              | 值                  | 说明                                             |
| ----------------- | ------------------- | ------------------------------------------------ |
| `address`         | 0x41                | Unit Mini TVOC/eCO2 的 I2C 地址。                |
| `update_interval` | 2s                  | 向 Home Assistant 更新测量数值的时间间隔。       |
| `store_baseline`  | true                | 是否启用基线值存储功能。                         |
| `baseline`        | 可选配置项          | 预设基线值，可根据实际环境调整以提高测量准确性。 |
| `eco2`            | eCO2 传感器实体配置 | 配置 eCO2 传感器实体的名称等属性。               |
| `tvoc`            | TVOC 传感器实体配置 | 配置 TVOC 传感器实体的名称等属性。               |

- 上述配置说明可参考 ESPHome 官方文档：[SGP30 CO₂ 和挥发性有机化合物传感器](https://www.hasscn.top/esphome/components/sensor/sgp30/)

## 4. 下载和烧录固件

### 4.1 编译固件

1. 完成 YAML 修改后，点击右上角的 `SAVE` 保存配置，再点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/727/unit_tovceco2_HA_install.png" width="70%" />

2. 在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/727/unit_tovceco2_HA_esp_builder_install_method.png" width="40%" />

3. 等待固件编译完成，点击 `Download` 并选择 `Factory format (Previously Modern)`，将固件保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/727/unit_tovceco2_HA_bin.png" width="70%" />

### 4.2 烧录固件

1. 使用 USB Type-C 线缆将 AtomS3R 连接到电脑。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%" />

2. 在弹出的串口选择窗口中，选择正确的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%" />

3. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%" />

4. 选择步骤 3 中下载的固件文件并开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/727/unit_tovceco2_HA_esp_home_install.png" width="40%" />

!> 注意 | 烧录完成后必须重置设备，否则固件可能无法正常启动。

## 5. 开始使用

1. 在 Home Assistant 中依次点击 `Settings` > `Devices & Services`，进入集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%" />

2. 在 `Discovered` 区域找到 **Unit Mini TVOC/eCO2** 设备，点击 `CONFIGURE` 并按照向导完成配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/727/unit_tovceco2_HA_discover.png" width="40%" />

3. 设备添加完成后，在设备详情页中可以看到多个传感器实体，包括 `eCO2` 和 `TVOC`，点击 `Add to dashboard` 将它们添加到仪表板中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/727/unit_tovceco2_HA_add_dashboard.png" width="40%" />

4. 最后，将这些传感器实体添加到仪表板中，即可实时监测空气中的 TVOC 和 eCO2 浓度。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/727/unit_tovceco2_HA_example.png" width="40%" />
