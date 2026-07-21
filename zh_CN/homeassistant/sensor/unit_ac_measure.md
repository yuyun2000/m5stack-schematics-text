# Unit AC Measure Home Assistant 集成

本教程将介绍如何使用 **Unit AC Measure** 交流电参数测量单元搭配 AtomS3R 主控，并将其集成到 Home Assistant 中，实现对交流电压、电流、有功功率和能耗的实时监测。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AC Measure Unit/img-28a2411d-d63c-4596-b474-2db9d9b6dcc5.webp" width="30%" />

## 准备工作

1. 硬件清单

- 1 x [Unit AC Measure](https://shop.m5stack.com/products/ac-measure-unit-hlw8032)
- 1 x [AtomS3R](https://shop.m5stack.com/products/atoms3r)
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x Home Assistant 主机（服务器、迷你电脑、NAS 等）

2. 软件与版本

- Home Assistant 2026.2.0 及以上
- [ESPHome Device Builder](https://esphome.io/) 2026.2.2 及以上

## 创建设备

1. 打开 ESPHome Dashboard，若出现初始引导界面，点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%" />

2. 点击右下角的绿色 **+** 按钮，开始创建新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%" />

3. 点击 `New Device Setup`，进入设备创建向导。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%" />

4. 输入设备名称，点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/acmeasure3.webp" width="40%" />

5. 选择设备类型，点击 `ESP32S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR2.webp" width="30%" />

6. 点击 `SKIP`，跳过加密密钥设置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%" />

7. 点击 `EDIT`，进入 YAML 配置页面，自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/acmeasure4.webp" width="70%" />

## 修改配置

### 外部组件配置

在 YAML 文件中添加 [External Components](https://esphome.io/components/external_components/) 配置，加载 unit_acmeasure 传感器驱动。

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: unit_acmeasure
    refresh: 0s
```

### I2C 总线配置

添加 [I2C](https://esphome.io/components/i2c/) 组件，配置 Unit AC Measure 与 AtomS3R 之间的通信引脚。

```yaml
i2c:
  sda: GPIO2
  scl: GPIO1
  scan: true
```

?> 说明 | AtomS3R 的 PORT.A 接口对应 SDA: GPIO2，SCL: GPIO1。若使用其他端口，请根据实际引脚进行调整。

### 传感器配置

添加 [Sensor](https://esphome.io/components/sensor/) 组件，启用 AC 测量相关的传感器实体。

```yaml
sensor:
  - platform: unit_acmeasure
    id: acmeasure1
    address: 0x42
    update_interval: 2s
    voltage:
      name: AC Voltage
    current:
      name: AC Current
    power:
      name: Active Power
    apparent_power:
      name: Apparent Power
    power_factor:
      name: Power Factor
    energy:
      name: Energy
```

主要参数说明：

| 参数              | 值             | 说明                                           |
| ----------------- | -------------- | ---------------------------------------------- |
| `address`         | 0x42           | Unit AC Measure 的 I2C 地址。                  |
| `update_interval` | 2s             | 向 Home Assistant 更新 AC 测量数值的时间间隔。 |
| `voltage`         | AC Voltage     | 报告被测回路的交流电压（RMS）。                |
| `current`         | AC Current     | 报告交流电流（RMS）。                          |
| `power`           | Active Power   | 报告有功功率（瓦）。                           |
| `apparent_power`  | Apparent Power | 报告视在功率（伏安，VA）。                     |
| `power_factor`    | Power Factor   | 报告功率因数（有功功率与视在功率之比）。       |
| `energy`          | Energy         | 报告累计用电量。                               |

## 下载和烧录固件

### 编译固件

1. 完成 YAML 修改后，点击右上角的 `SAVE` 保存配置，再点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/HAInstall.webp" width="70%" />

2. 在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%" />

3. 等待固件编译完成，点击 `Download` 并选择 `Factory format (Previously Modern)`，将固件保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%" />

?> 提示 | 完整示例配置可参考 [Unit AC Measure](https://github.com/m5stack/esphome-yaml/blob/main/examples/sensor/unit_ac_measure.yaml)。首次构建可能需要一段时间，具体取决于 Home Assistant 主机的性能和网络环境。

### 烧录固件

4. 使用 USB Type-C 线缆将 AtomS3R 连接到电脑。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%" />

5. 在弹出的串口选择窗口中，选择正确的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%" />

6. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%" />

7. 选择步骤 3 中下载的固件文件并开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/acmeasure5.webp" width="40%" />

!> 注意 | 烧录完成后必须重置设备，否则固件可能无法正常启动。

## 开始使用

1. 在 Home Assistant 中依次点击 `Settings` > `Devices & Services`，进入集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%" />

2. 在 `Discovered` 区域找到 **Unit AC Measure** 设备，点击 `CONFIGURE` 并按照向导完成配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/acmeasure.webp" width="40%" />

3. 设备添加完成后，在设备详情页中可以看到多个传感器实体，例如 AC Voltage、AC Current、Active Power、Apparent Power、Power Factor 和 Energy，并显示其实时数值。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/acmeasure2.webp" width="40%" />

4. 最后，将这些传感器实体添加到仪表板中，即可实时监控交流电参数和用电情况。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/acmeasure1.webp" width="40%" />
