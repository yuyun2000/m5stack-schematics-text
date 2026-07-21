# Module13.2 Dual Kmeter 温度传感器

<img 
src="https://static-cdn.m5stack.com/resource/docs/products/module/DualKmeter%20Module13.2/img-91942504-2fb3-4d8e-90d2-fbf0761bb1d1.webp" 
width="30%" 
/>

Module13.2 Dual Kmeter 是一款基于 "MAX31855KASA + STM32F030F4P6 + 电气隔离" 方案的双通道 K 型热电偶温度测量模块。
该模块具有两路 K 型热电偶传感器接口，通过信号继电器交替测量两个通道的温度值。
支持 -200°C 至 1350°C 的测量范围，精度为 ±2°C。
此外，模块内置 B0505LS-1WR2 和 CA-IS3020S 电压与信号隔离芯片，确保系统稳定性与安全性。
模块还内置 DIP 拨码开关，可方便地切换不同的 I2C 地址，以满足多样化的应用需求。
适用于工业自动化、仪器检测等场景。

`dual_kmeter` 传感器平台允许您在 ESPHome 中使用
[Module13.2 Dual Kmeter](https://docs.m5stack.com/en/module/DualKmeter%20Module13.2)
双通道 K 型热电偶温度模块。
该模块通过单条 I²C 总线提供两路独立的热电偶输入（Kmeter 1 和 Kmeter 2）
以及一路板载内部温度传感器。

\#> **注意** | 本模块设计用于与 M5Stack Core 系列主控配合使用。

使用本传感器前，需要在配置文件中设置好 [I²C 总线](/components/i2c)。

```yaml
# 示例配置
i2c:
  sda: GPIO21
  scl: GPIO22

sensor:
  - platform: dual_kmeter
    name: "热电偶通道 1"
    channel: KMETER_1
    update_interval: 60s
```

## 配置变量

- **channel** (**必填**): 要读取的测量通道，可选值如下：

  | 值 | 描述 |
  |-------|-------------|
  | `KMETER_1` | 输入 1 的 K 型热电偶 |
  | `KMETER_2` | 输入 2 的 K 型热电偶 |
  | `INTERNAL` | 板载内部温度传感器 |

- **unit** (*可选*): 传感器上报的温度单位，可选 `CELSIUS`（摄氏度）或 `FAHRENHEIT`（华氏度）。默认为 `CELSIUS`。

- **update_interval** (*可选*, [时间](https://esphome.io/guides/configuration-types#time)):
  传感器的轮询间隔。默认为 `60s`。

- **address** (*可选*, int): 模块的 I²C 地址。默认为 `0x11`。

- 其他所有选项请参考 [传感器组件](https://esphome.io/components/sensor)。

## 测量行为

### 热电偶通道（`KMETER_1` / `KMETER_2`）

当选择热电偶通道时，组件在每次 `update()` 周期中写入通道选择寄存器（`0x20`），
然后轮询就绪标志寄存器（`0x30`），直到模块表示新一次转换已完成。
组件最长等待 **300 ms**；若在此时间窗口内标志未置位，则跳过本次更新并记录警告日志：

```
[W][dual_kmeter]: Kmeter sampling timeout
```

模块固件以小端字节序的有符号 32 位整数存储温度值，比例因子为 **0.01**
（例如，寄存器值 `2537` 代表 25.37 °C）。

### 内部通道（`INTERNAL`）

内部通道直接读取模块板载热敏电阻，无需等待就绪标志。
该测量值始终可用，不受热电偶通道选择寄存器的影响。

## I²C 地址

M5Stack Module Dual Kmeter 默认使用固定 I²C 地址 **`0x11`**。
若已通过模块的 [DIP 拨码开关](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1028/M127-Module-DualKmeter-I2C-Protocol.pdf) 更改了硬件地址，
请使用 `address` 选项指定新地址：

```yaml
sensor:
  - platform: dual_kmeter
    name: "窑炉温度"
    channel: KMETER_2
    address: 0x12        # 非默认地址
```

\#> **注意** | 为确保固件成功上传至 M5Stack Core 系列主控，请在开始上传前将主控与模块分离。已知在堆叠状态下上传固件时存在兼容性问题。上传完成后，请先复位主控，再重新组合模块使用。

## 完整配置示例

```yaml
i2c:
  sda: GPIO21
  scl: GPIO22

sensor:
  # --- 热电偶通道 1，摄氏度 ---
  - platform: dual_kmeter
    name: "窑炉热电偶"
    channel: KMETER_1
    unit: CELSIUS
    update_interval: 30s
    filters:
      - sliding_window_moving_average:
          window_size: 5
          send_every: 5

  # --- 热电偶通道 2，华氏度 ---
  - platform: dual_kmeter
    name: "烤箱热电偶 (°F)"
    channel: KMETER_2
    unit: FAHRENHEIT
    # 为保持单位一致性，默认 unit_of_measurement 为摄氏度
    unit_of_measurement: "°F"
    update_interval: 30s

  # --- 板载内部温度 ---
  - platform: dual_kmeter
    name: "模块内部温度"
    channel: INTERNAL
    update_interval: 60s
```

CoreS3 与 Module13.2 Dual Kmeter 的[使用示例](https://github.com/m5stack/esphome-yaml/blob/main/examples/sensor/module-dual-kmeter.yaml)：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1028/dual_kmeter_esphome_result.jpg" width="30%" />

## 参见

- [传感器过滤器](/components/sensor#sensor-filters)
- [I²C 总线](https://esphome.io/components/i2c)
- [M5Stack Module13.2 Dual Kmeter 产品页面](https://docs.m5stack.com/en/module/DualKmeter%20Module13.2)
- [M5Stack Module13.2 Dual Kmeter 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1028/M127-Module-DualKmeter-I2C-Protocol.pdf)
