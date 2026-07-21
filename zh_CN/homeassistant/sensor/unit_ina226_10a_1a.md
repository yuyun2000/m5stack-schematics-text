# Unit INA226 10A/1A Home Assistant 集成

本教程将介绍如何使用 **Unit INA226 10A/1A** 直流电参数测量单元搭配 AtomS3R 主控，并将其集成到 Home Assistant 中，实现对直流电压、电流、功率的实时监测。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/Unit_INA226-10A_01.webp" width="30%" /> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_01.webp" width="30%" />

## 准备工作

1. 硬件清单

- 1 x [Unit INA226 10A](https://shop.m5stack.com/products/ina226-10a-current-voltage-power-monitor-unit) / [Unit INA226 1A](https://shop.m5stack.com/products/ina226-1a-current-voltage-power-monitor-unit)
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

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/unit_ina226_HA_create_device.png" width="40%" />

5. 选择设备类型，点击 `ESP32S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/751/PIR2.webp" width="30%" />

6. 点击 `SKIP`，跳过加密密钥设置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%" />

7. 点击 `EDIT`，进入 YAML 配置页面，自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/unit_ina226_HA_yaml_edit.png" width="70%" />

## 修改配置

### I2C 总线配置

添加 [I2C](https://esphome.io/components/i2c/) 组件，配置 Unit INA226 10A/1A 与 AtomS3R 之间的通信引脚。

```yaml
i2c:
  sda: GPIO2
  scl: GPIO1
  scan: true
```

?> 说明 | AtomS3R 的 PORT.A 接口对应 SDA: GPIO2，SCL: GPIO1。若使用其他端口，请根据实际引脚进行调整。

### 传感器配置

添加 [Sensor](https://esphome.io/components/sensor/) 组件，启用 INA226 传感器实体。

```yaml
sensor:
  - platform: ina226
    address: 0x41
    # 10A
    shunt_resistance: 0.08 ohm
    # 1A
    # shunt_resistance: 0.005 ohm
    adc_time:
      voltage: 140us
      current: 332us
    adc_averaging: 4
    update_interval: 2s
    current:
      name: "Current"
      accuracy_decimals: 4
    shunt_voltage:
      name: "Shunt_Voltage"
      accuracy_decimals: 5
    bus_voltage:
      name: "Bus_Voltage"
      accuracy_decimals: 4
    power:
      name: "Power"
      accuracy_decimals: 4
```

主要参数说明：

| 参数               | 值                   | 说明                                       |
| ------------------ | -------------------- | ------------------------------------------ |
| `address`          | 0x41                 | Unit INA226 10A/1A 的 I2C 地址。           |
| `shunt_resistance` | 0.08 ohm / 0.005 ohm | 10A 使用 0.08，1A 使用 0.005 的分流电阻。  |
| `adc_time`         | 140us / 332us        | ADC 转换时间，电压和电流可分别设置。       |
| `update_interval`  | 2s                   | 向 Home Assistant 更新测量数值的时间间隔。 |
| `current`          | Current              | 报告直流电流，单位为安培（A）。            |
| `shunt_voltage`    | Shunt Voltage        | 报告分流电压，单位为伏特（V）。            |
| `bus_voltage`      | Bus Voltage          | 报告总线电压，单位为伏特（V）。            |
| `power`            | Power                | 报告功率，单位为瓦特（W）。                |

- 上述配置说明可参考 ESPHome 官方文档：[INA226 直流电流和功率传感器](https://www.hasscn.top/esphome/components/sensor/ina226/)

## 下载和烧录固件

### 编译固件

1. 完成 YAML 修改后，点击右上角的 `SAVE` 保存配置，再点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/unit_ina226_HA_Install.png" width="70%" />

2. 在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/unit_ina226_HA_esp_builder_install_method.png" width="40%" />

3. 等待固件编译完成，点击 `Download` 并选择 `Factory format (Previously Modern)`，将固件保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/unit_ina226_HA_bin.png" width="70%" />

### 烧录固件

1. 使用 USB Type-C 线缆将 AtomS3R 连接到电脑。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%" />

2. 在弹出的串口选择窗口中，选择正确的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%" />

3. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%" />

4. 选择步骤 3 中下载的固件文件并开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/unit_ina226_HA_esp_home_install.png" width="40%" />

!> 注意 | 烧录完成后必须重置设备，否则固件可能无法正常启动。

## 开始使用

1. 在 Home Assistant 中依次点击 `Settings` > `Devices & Services`，进入集成管理页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%" />

2. 在 `Discovered` 区域找到 **Unit INA226 10A/1A** 设备，点击 `CONFIGURE` 并按照向导完成配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/unit_ina226_HA_discover.png" width="40%" />

3. 设备添加完成后，在设备详情页中可以看到多个传感器实体，例如 Bus_Voltage、Shunt_Voltage、Current 和 Power，并显示其实时数值。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/unit_ina226_HA_add_dashboard.png" width="40%" />

4. 最后，将这些传感器实体添加到仪表板中，即可实时监控直流电参数。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/unit_ina226_HA_example.png" width="40%" />
