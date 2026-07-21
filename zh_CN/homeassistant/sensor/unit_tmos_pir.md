# Unit TMOS PIR Home Assistant 集成

本教程将使用 **Unit TMOS PIR** 传感器搭配 AtomS3R 主控，并将其集成到 Home Assistant 中，实现人体存在与活动状态的实时监测与显示。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/4.webp" width="30%"/>

## 准备工作

1. 硬件清单。

- 1 x [Unit TMOS PIR](https://shop.m5stack.com/products/tmos-pir-unit-sths34pf80)。
- 1 x [AtomS3R](https://shop.m5stack.com/products/atoms3r)。
- 1 x HY2.0-4P Grove 连接线 (20cm)。
- 1 x Home Assistant 主机。

2. 软件与版本。

- Home Assistant 2026.2.0 及以上。
- [ESPHome Device Builder](https://esphome.io/) 2026.2.2 及以上。

## 创建设备

1. 打开 ESPHome Dashboard，若出现初始引导界面，点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%"/>

2. 点击右下角的绿色 **+** 按钮，开始创建新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%"/>

3. 点击 `New Device Setup`，进入设备创建向导。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%"/>

4. 输入设备名称，点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR3.webp" width="40%"/>

5. 选择设备类型，点击 `ESP32S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR2.webp" width="30%"/>

6. 点击 `SKIP`，跳过加密密钥设置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%"/>

7. 点击 `EDIT`，进入 YAML 配置页面，自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR1.webp" width="70%"/>

## 设备配置

### 外部组件配置

在 YAML 文件中添加 [External Components](https://esphome.io/components/external_components/) 配置，加载 STHS34PF80 传感器驱动。

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: sths34pf80
    refresh: 0s
```

### I2C 总线配置

- **添加 [I2C](https://esphome.io/components/i2c/) 组件**，配置 Unit TMOS PIR 与 AtomS3R 之间的通信引脚。

```yaml
i2c:
  sda: GPIO2
  scl: GPIO1
  scan: true
```

?> 说明 | AtomS3R 对应 SDA: GPIO2，SCL: GPIO1。若使用其他接口，请根据实际管脚进行调整。

### Sensor 传感器配置

- **添加 [Sensor](https://esphome.io/components/sensor/) 组件**，配置存在检测与运动检测功能。

```yaml
sensor:
  - platform: sths34pf80
    pres_flag:
      name: "TMOS Presence Detected"
    mot_flag:
      name: "TMOS Motion Detected"
    presence_threshold: 200
    presence_hysteresis: 50
    motion_hysteresis: 50
    odr: 8
    update_interval: 1s
```

主要参数说明：

| 参数                  | 值  | 说明                                                         |
| --------------------- | --- | ------------------------------------------------------------ |
| `presence_threshold`  | 200 | 存在检测阈值，数值越大灵敏度越低。                           |
| `presence_hysteresis` | 50  | 存在检测滞后值，防止状态频繁切换。                           |
| `motion_hysteresis`   | 50  | 运动检测滞后值。                                             |
| `odr`                 | 8   | 输出数据率 (Hz)，支持 0.25 / 0.5 / 1 / 2 / 4 / 8 / 15 / 30。 |
| `update_interval`     | 1s  | Home Assistant 中传感器状态更新间隔。                        |

## 下载和烧录固件

### 编译固件

1. 完成 YAML 修改后，点击右上角的 `SAVE` 保存配置，再点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6HA5.webp" width="70%"/>

2. 在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

3. 等待固件编译完成，点击 `Download` 并选择 `Factory format (Previously Modern)`，将固件保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%"/>

?> 提示 | 点击 [Unit TMOS](https://github.com/m5stack/esphome-yaml/blob/main/examples/sensor/unit_tmos.yaml) 查看完整的示例配置。首次构建可能需要一段时间，具体取决于 Home Assistant 主机的性能和网络质量。

### 烧录固件

4. 通过 USB Type-C 线缆将 AtomS3R 连接到电脑。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%"/>

5. 在弹出的串口选择窗口中，找到对应的串口号并选择。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%"/>

6. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%"/>

7. 选择步骤 3 中下载的固件文件进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR4.webp" width="40%"/>

!> 注意 | 烧录完成后必须重置设备，否则固件可能无法正常启动。

## 开始使用

1. 在 Home Assistant 中依次点击 `Settings` > `Devices & Services`，进入集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%"/>

2. 在 `Discovered` 区域找到已上线的 **Unit TMOS PIR** 设备，点击 `CONFIGURE` 并按照提示完成添加。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR5.webp" width="40%"/>

3. 添加成功后，设备页面将显示 `pres_flag`（存在检测）和 `mot_flag`（运动检测）两个传感器实体及其实时状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR6.webp" width="40%"/>

4. 最后，将传感器实体添加到仪表板，即可实时查看人体存在与运动状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR7.webp" width="40%"/>
