# Unit RollerCAN 使用教程

## 1. 设备供电

Unit RollerCAN 提供了以下两种供电方式选择:

- 通过 CAN (XT30 (2+2) PW-M) 接口进行供电：支持 6-16V@DC, 并集成 DC-DC 降压电路为控制器供电。
- 通过 Grove 接口进行供电: 5V@DC。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_can_port_01.JPG" width="50%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_i2c_port_01.JPG" width="50%">

## 2. 设备配置

### 配置模式

Unit-RollerCAN 集成了 OLED 和物理按键用于输入交互，在进行电机部署前，你可以根据使用的需求进行一些前期的配置。参考下方操作，进入配置模式。

- 1\. 长按底部按键 A
- 2\. 设备供电
- 3\. 进入配置模式
- 4\. 进入配置菜单后，旋转电机可切换选项，按下按键可进行选择 / 返回

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_setting_01.png" width="50%">

### 通信模式

Unit-RollerCAN 目前提供以下几种不同的通信方式，用户可以根据实际部署的情况选择适合的通信接口和协议。

- **I2C Mode**: 该模式下，电机通过 I2C 通信接口进行控制
- **CAN Mode**: 该模式下，电机通过 CAN 通信接口进行控制
- **CAN->I2C Mode**: 该模式下，电机通过 CAN 通信接口进行控制，同时支持使用 CAN->I2C 转发指令，可通过转接实现 I2C 设备数据读写。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_setting_02.png" width="50%">

### 通信地址

- **I2C ADDR**: 配置 I2C 通信模式下，设备作为从机的 I2C 地址。
- **CAN ID**: 配置 CAN 通信模式下，设备通信所使用的 ID, 配置范围为 0-255, 默认值为 168 (0xA8)。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_setting_03.png" width="50%">

### PID 预设

速度环与位置环模式的 PID 配置，根据不同的情况可以选择以下几种预设。不同的配置参数，对不同的使用场景进行了优化，推荐使用用户配置根据实际的情况进行微调。

- 默认用户配置
- 轻负载优化配置
- 中负载优化配置
- 高负载优化配置

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_setting_04.png" width="50%">

### CAN 波特率配置

配置 CAN 通信模式下，设备通信的速率 (bps) 目前支持: 1M, 500K, 125K

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_setting_BPS.png" width="50%">

### RGB 亮度

调节 RGB LED 的亮度：0-100%

### RGB 工作模式

- **系统自动模式**：根据当前电机运行状态切换颜色
  - **绿色**：Speed Mode
  - **蓝色**：Position Mode
  - **黄色**：Current Mode
  - **紫色**：Encoder Mode
  - **红色**：错误报警
- **用户模式**：由用户自定义控制指示灯颜色

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_setting_05.png" width="50%">

### JAM

设置电机堵转保护，当电机发生堵转情况的时候，将自动锁定电机，防止设备损坏。

### Range 保护

设置电机旋转范围保护。开启后当电机编码数值 <-2100000000 或> 2100000000 时，电机将停止旋转进入保护状态。

## 3. 电机工作模式

Unit Roller485 提供了 4 种工作模式，可通过通信指令进行配置 (参考页面底部案例程序与通信协议)：

- **Speed Mode (绿色)**: 控制电机运行在指定目标速度 (RPM)。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_speed_mode.png" width="50%">

- **Position Mode (蓝色)**: 控制电机转动至指定位置 (编码器数值)。

\#> 编码器数值与旋转角度 | 绝对位置模式下，编码器数值 36000 pos = 360° 。由于机械安装角度与编码器角度不是严格对应，因此实际可能存在大约 2° 左右误差。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_position_mode.png" width="50%">

- **Current Mode (黄色)**: 控制电机运行在指定目标电流 (mA)。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_current_mode.png" width="50%">

- **Encoder Mode (紫色状态灯)**: 电机作为输入设备，采集当前旋转编码器数值。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_encoder_mode.png" width="50%">

## 4. 设备接线

### CAN 控制

多个电机通过 XT30 接口，用[PwrCAN Cable](/zh_CN/accessory/PwrCAN%20Cable)连接实现多个连接组网，发送指令进行控制。使用前，需将设备配置成不同的 ID, 用于通信区分。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_can_bus_01.JPG" width="50%">

### I2C 控制

多个电机通过 I2C 控制可通过[Unit Hub](/zh_CN/unit/hub)连接器实现多个连接组网，访问从机寄存器进行控制。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/roller485/roller485_i2c_bus_01.jpg" width="50%">

## 5. 结构件

Unit RollerCAN 套装标配了法兰盘和 LEGO 兼容支架结构件，方便用户构建自己的控制装置，可参考下图进行固定和安装。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_structure_02.JPG" width="50%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/rollercan/rollercan_structure_01.JPG" width="50%">

## 6. 相关资源

- 案例程序:

  - [RollerCAN Unit Library](https://github.com/m5stack/M5Unit-Roller)

  - [M5Unit RollerCAN 内置固件](https://github.com/m5stack/M5Unit-RollerCAN-Internal-FW)

- 通信协议:

- I2C 协议

  - [RollerCAN Unit I2C协议表](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/ROLLERCAN_I2C%E5%8D%8F%E8%AE%AE_V2_20241011.pdf)

  - [RollerCAN Unit I2C 用户手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/779/Unit-RollerCAN-I2C-Protocol-CN.pdf)

- CAN 协议

  - [RollerCAN Unit CAN协议表](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/UnitBLDC_CAN_%E5%8D%8F%E8%AE%AE_V1_20241011-CN.pdf)

  - [RollerCAN Unit CAN用户手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/779/Unit-RollerCAN-CAN-Protocol-CN.pdf)
