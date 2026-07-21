# BALA 上手指南

> 为了使用 M5Bala, 需要 M5Stack FIRE 或 M5GO (白色)。

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/product_pics/app/bala_4.webp" width="25%">

## 开发环境

- [BALA 上手指南](#bala-上手指南)
  - [开发环境](#开发环境)
  - [UiFlow 编辑](#uiflow-编辑)
  - [Arduino IDE 编辑](#arduino-ide-编辑)

## UiFlow 编辑

1. [烧录 UiFlow 固件](/zh_CN/uiflow/uiflow_web)

<figure>
  <img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_pogopin.webp" width="40%">
</figure>

4. 单击 M5Core 侧边的红色按键开机 (快速双击为关机)

<figure>
  <img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_power_switch.webp" width="40%">
</figure>

5. 单击 M5Bala 底座的按键启动电源 (连续点击两次时关闭电源).

<figure>
  <img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_bala_power_switch.webp" width="40%">
</figure>
<figure>
  <img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_indicator.webp" width="40%">
</figure>

6. 访问 [UiFlow](http://flow.m5stack.com/) , 将编程模式`Blockly` 切换至 `Python`.

<figure>
  <img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_uiflow_01.webp" width="40%">
</figure>

7. 复制粘贴以下代码，并执行程序.

```cpp
from m5stack import *
from m5ui import *
from m5bala import M5Bala
import i2c_bus
clear_bg(0x111111)

m5bala = M5Bala(i2c_bus.get(i2c_bus.M_BUS))
btnA = M5Button(name="ButtonA", text="ButtonA", visibility=False)
btnB = M5Button(name="ButtonB", text="ButtonB", visibility=False)
btnC = M5Button(name="ButtonC", text="ButtonC", visibility=False)
title0 = M5Title(title="Title", fgcolor=0xFFFFFF, bgcolor=0x0000FF)

title0.setTitle('calirate start')
wait(2)
sampleCount = 2000
gyroXSum = 0
gyroYSum = 0
gyroZSum = 0

for _ in range(sampleCount):
    gyroXYZ = m5bala.imu.gyro
    gyroXSum += gyroXYZ[0] # X
    gyroYSum += gyroXYZ[1] # Y
    gyroZSum += gyroXYZ[2] # Z

gyroXMean = gyroXSum / sampleCount
gyroYMean = gyroYSum / sampleCount
gyroZMean = gyroZSum / sampleCount

m5bala.imu.setGyroOffsets(gyroXMean, gyroYMean, gyroZMean)

title0.setTitle('balance start')
while True:
    m5bala.balance()
    wait(0.001)
```

## Arduino IDE 编辑

1. - [安装 Arduino IDE](/zh_CN/arduino/arduino_ide)

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_18.webp" width="50%">

2. 在 Arduino IDE 的库管理安装`m5stack`库

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_19.webp" width="50%">

3. 在 Arduino IDE 的库管理安装`NeoPixelBus`库

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_20.webp" width="50%">

4. 在 Arduino IDE 的库管理安装`MPU6050_tockn`库

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_21.webp" width="50%">

5. 将 M5Core 连接至电脑。点击`Tools`->`Port`中选择设备使用的串行端口.

6. 开发板`Board`选项选择`M5Stack-Core-ESP32`或`M5Stack-Fire`.

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_22.webp" width="50%">

7. 使用 Shell 命令下载 **[M5Bala案例程序](https://github.com/m5stack/M5Bala.git)** . _如果你还未安装 Git, [请点击此处](https://git-scm.com/download/win) 进行下载._

```cpp
git clone --recursive https://github.com/m5stack/M5Bala.git
```

8. 点击 `Sketch` -> `Include Library` -> `Add .ZIP Library...` . 选择下载好的 `M5Bala` 的文件

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_14.webp" width="50%">

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_15.webp" width="50%">

9. 打开 BALA 程序案例：点击 `File` -> `Examples` -> `M5Bala` -> `Basic`.

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_16.webp" width="50%">

10. 编译并上传程序.

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/getting_started_pics/m5bala/bala_quick_start_23.webp" width="50%">

<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/product_pics/app/bala_3.webp" width="40%">
