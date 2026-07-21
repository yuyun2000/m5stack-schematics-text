# [Module GNSS](/zh_CN/module/GNSS%20Module)

## 案例程序

这个程序的功能是初始化 GNSS 和 IMU 设备，获取当前的日期、时间、经纬度信息，并读取加速度计和陀螺仪在各个轴(X、Y、Z)上的原始数据，然后将这些信息连续打印输出

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_gnss_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

setScreenColor(0x222222)

gnss = module.get(module.GNSS)

gnss.init_gnss(1, 17, 16, 38400, 8, None, 1)
gnss.init_imu(0x68)
gnss.set_mode('normal')
while True:
  print((str('date：') + str((gnss.gnss_date))))
  print((str('time：') + str((gnss.gnss_time))))
  print((str('latitude：') + str((gnss.latitude))))
  print((str('longtitude：') + str((gnss.longitude))))
  print((str('IMU ACC rawX：') + str((gnss.get_accel(1)[0]))))
  print((str('IMU ACC rawY：') + str((gnss.get_accel(1)[1]))))
  print((str('IMU ACC rawZ：') + str((gnss.get_accel(1)[2]))))
  print((str('IMU GYRO rawX：') + str((gnss.get_gyro(1)[0]))))
  print((str('IMU GYRO rawY：') + str((gnss.get_gyro(1)[1]))))
  print((str('IMU GYRO rawZ：') + str((gnss.get_gyro(1)[2]))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_accel.svg">

```python
gnss.get_accel(0)[0]
```

- 获取加速度计在指定方向(如 X 轴)的加速度数据，以米每秒平方(m/s²)为单位，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_accel_raw.svg">

```python
gnss.get_accel(1)[0]
```

- 获取加速度计在指定方向(如 X 轴)的原始数据，返回一个整数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_altitude.svg">

```python
gnss.altitude
```

- 获取当前的海拔高度，以米为单位，返回一个字符串形式的高度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_course.svg">

```python
gnss.course
```

- 获取航向信息，返回一个字符串形式的航向值。航向指的是相对于地球北极的方向

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_date.svg">

```python
gnss.gnss_date
```

- 获取当前的日期信息，返回一个字符串形式的日期值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_gyro.svg">

```python
gnss.get_gyro(0)[0]
```

- 获取陀螺仪在指定方向(如 X 轴)的角速度数据，以度每秒(deg/s)为单位，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_gyro_raw.svg">

```python
gnss.get_gyro(1)[0]
```

- 获取陀螺仪在指定方向(如 X 轴)的原始数据，返回一个整数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_latitude.svg">

```python
gnss.latitude
```

- 获取纬度信息，返回一个字符串，格式为度和分(ddmm.mmmmm)，并包含东西经(W/E)的标识

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_latitude_decimal.svg">

```python
gnss.latitude_decimal
```

- 获取十进制格式的纬度值，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_longitude.svg">

```python
gnss.longitude
```

- 获取经度信息，返回一个字符串，格式为度和分(ddmm.mmmmm)，并包含南北经(S/N)的标识

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_longitude_decimal.svg">

```python
gnss.longitude_decimal
```

- 获取十进制格式的经度值，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_magneto.svg">

```python
gnss.get_magneto(0)[0]
```

- 获取磁力计在指定方向(如 X 轴)上的磁场强度，以微特斯拉(μT)为单位，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_magneto_raw.svg">

```python
gnss.get_magneto(1)[0]
```

- 获取磁力计在指定方向(如 X 轴)的原始数据，返回一个整数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_positioning_quality.svg">

```python
gnss.pos_quality
```

- 获取定位质量信息，返回一个字符串，通常用于表示 GNSS 信号的质量或精度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_pressure.svg">

```python
gnss.get_pressure
```

- 获取气压传感器的当前压力值，以百帕(hPa)为单位，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_satellite_num.svg">

```python
gnss.satellite_num
```

- 获取当前连接的卫星数量，返回一个字符串

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_speed.svg">

```python
gnss.speed_knot
```

- 获取速度，返回一个字符串。可以选择单位为节(knot)或千米每小时(kph)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_temp.svg">

```python
gnss.get_temperature
```

- 获取当前温度，以摄氏度(°C)为单位，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_get_time.svg">

```python
gnss.gnss_time
```

- 获取当前的时间，返回一个字符串形式的时间值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_init.svg">

```python
gnss.init_gnss(1, 17, 16, 38400, 8, None, 1)
```

- 初始化 GNSS 模块。设置 UART 通信的参数，包括 UART 端口、Tx(发送)引脚、Rx(接收)引脚、波特率、数据位数、校验位和停止位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_init_imu.svg">

```python
gnss.init_imu(0x68)
```

- 初始化 IMU 设备的 I2C 地址，这里设置的 I2C 地址为0x68，用于后续的 I2C 通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_set_accel_odr.svg">

```python
gnss.set_acc_odr(0x09)
```

- 设置加速度计的输出数据速率。这里选择了200Hz，表示加速度计每秒输出200次数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_set_accel_range.svg">

```python
gnss.set_acc_range(0x00)
```

- 设置加速度计的测量范围。这里选择了2G，表示加速度计的最大测量范围为±2个重力加速度(G)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_set_bmi_mode.svg">

```python
gnss.set_mode('normal')
```

- 将 BMI270传感器设置为正常工作模式。BMI270是一种 IMU 传感器，通常用于姿态感应和运动检测

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_set_gyro_odr.svg">

```python
gnss.set_acc_odr(0x09)
```

- 设置陀螺仪的输出数据速率。这里选择的速率是200Hz，表示陀螺仪每秒输出200次数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_set_gyro_range.svg">

```python
 gnss.set_gyr_range(0x01)
```

- 设置陀螺仪的测量范围。这里选择的范围是1000度每秒(dps)，表示陀螺仪的最大测量范围为±1000度每秒

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_set_magneto_odr.svg">

```python
 gnss.set_magneto_odr(0x00)
```

- 设置磁力计的输出数据速率。这里选择的是10Hz，表示磁力计每秒输出10次数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gnss/uiflow_block_module_gnss_set_time_zone.svg">

```python
gnss.set_time_zone(8)
```

- 设置时区。这里设置为8小时0分钟，通常用于调整时间以适应当地时区

