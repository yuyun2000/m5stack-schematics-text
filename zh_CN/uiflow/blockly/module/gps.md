# [Module GPS](/zh_CN/module/gps)

## 案例程序

串口打印设备所在的经度和纬度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

gps = module.get(module.GPS, (17, 16))

while True:
  print((str('Latitude: ') + str((gps.latitude))))
  print((str(' Longitude: ') + str((gps.longitude))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_altitude.svg">

```python
gps.altitude
```

- 获取海拔高度，以米为单位，返回一个字符串

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_course.svg">

```python
gps.course
```

- 获取航向信息，返回一个字符串。航向指的是相对于地球北极的方向

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_date.svg">

```python
gps.gps_date
```

- 获取日期信息，返回一个字符串

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_latitude.svg">

```python
gps.latitude
```

- 获取纬度信息，返回一个字符串。格式为度和分(ddmm.mmmmm)，并包含东西经(W/E)的标识

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_latitude_decimal.svg">

```python
gps.latitude_decimal
```

- 获取十进制格式的纬度值，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_longitude.svg">

```python
gps.longitude
```

- 获取经度信息，返回一个字符串。格式为度和分(dddmm.mmmmm)，并包含南北经(S/N)的标识

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_longitude_decimal.svg">

```python
gps.longitude_decimal
```

- 获取十进制格式的经度值，返回一个浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_positioning_quality.svg">

```python
gps.pos_quality
```

- 获取定位质量信息，返回一个字符串。通常用于表示 GPS 信号的质量或精度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_satellite_num.svg">

```python
gps.satellite_num
```

- 获取当前连接的卫星数量，返回一个字符串

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_speed.svg">

```python
gps.speed_knot
```

- 获取速度，单位为节(knot)，返回一个字符串。节是航速单位，通常用于海上和空中导航
  - knot: 速度单位为节，常用于航海和航空。
  - kph: 速度单位为千米每小时(kilometers per hour)，常用于陆地交通。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_get_state.svg">

```python
gps.gps_time
```

- 获取当前时间，返回一个字符串

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_set_custom.svg">

```python
module.get(module.GPS, (17, 16))
```

- 使用自定义引脚初始化，TX 引脚为17，RX 引脚为16。这用于设置自定义的串口通信引脚

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_set_time_zone.svg">

```python
gps.set_time_zone(8)
```

- 设置时区，范围是-12到12。在这个例子中，时区被设置为8

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/gps/uiflow_block_gps_uart_init.svg">

```python
gps.uart_port_id(1)
```

- 设置核心 UART 的 ID 号。这用于指定使用的 UART 接口
  - 1: 设置核心 UART 接口的 ID 号为1。
  - 2: 设置核心 UART 接口的 ID 号为2。

