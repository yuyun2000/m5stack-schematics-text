# [Module GPS v2.0](/zn_CN/module/Module GPS v2.0)

## 案例程序

立即读取当前的纬度、经度、海拔高度和 UTC 时间，将结果通过串口（或终端）打印出来

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/uiflow_block_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import module

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

gpsv2_1 = module.get(module.GPSV2, (17, 16))

gpsv2_1.uart_port_id(1)
print((str('latitude:') + str((gpsv2_1.get_latitude()))))
print((str('longitude:') + str((gpsv2_1.get_longitude()))))
print((str('altitude:') + str((gpsv2_1.get_altitude()))))
print((str('local time:') + str((gpsv2_1.get_gps_time()))))
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/deinit.svg">

```python
gpsv2_1.deinit()
```

- 注销 GPS 模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_altitude.svg">

```python
print((str('altitude:') + str((gpsv2_1.get_altitude()))))
```

- 获取海拔高度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_antenna_state.svg">

```python
print((str('antena State:') + str((gpsv2_1.get_antenna_state()))))
```

- 获取天线状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_corse_over_ground.svg">

```python
print((str('degree:') + str((gpsv2_1.get_corse_over_ground()))))
```

- 获取对地航向

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_gps_date.svg">

```python
print((str('date:') + str((gpsv2_1.get_gps_date()))))
```

- 获取日期信息，返回一个包含年、月、日的列表

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_gps_date_time.svg">

```python
print((str('date and local time:') + str((gpsv2_1.get_gps_date_time()))))
```

- 获取经度信息，返回一个字符串。格式为度和分(dddmm.mmmmm)，并包含南北经(S/N)的标识

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_latitude.svg">

```python
print((str('latitude:') + str((gpsv2_1.get_latitude()))))
```

- 获取纬度信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_longitude.svg">

```python
print((str('longitude:') + str((gpsv2_1.get_longitude()))))
```

- 获取经度信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_pos_quality.svg">

```python
print((str('position quality:') + str((gpsv2_1.get_pos_quality()))))
```

- 获取定位质量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_satellite_num.svg">

```python
print((str('statellite number:') + str((gpsv2_1.get_satellite_num()))))
```

- 获取当前用于定位的卫星数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_speed_over_ground.svg">

```python
print((str('knot:') + str((gpsv2_1.get_speed_over_ground()))))
```

- 获取对地速度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_gps_time.svg">

```python
print((str('local time:') + str((gpsv2_1.get_gps_time()))))
```

- 获取本地时间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_time_zone.svg">

```python
print((str('zone offset:') + str((gpsv2_1.get_time_zone()))))
```

- 获取当前设置的时区偏移量（相对于 UTC）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_timestamp.svg">

```python
print((str('timestamp:') + str((gpsv2_1.get_timestamp()))))
```

- 获取自 1970 年 1 月 1 日以来的 Unix 时间戳（秒）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/get_work_mode.svg">

```python
print((str('work mode:') + str((gpsv2_1.get_work_mode()))))
```

- 获取当前工作模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/init.svg">

```python
gpsv2_1 = module.get(module.GPSV2, (17, 16))
```

- 使用指定的 TX（17）和 RX（16）引脚初始化 GPS 模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/set_time_zone.svg">

```python
gpsv2_1.set_time_zone(0)
```

- 设置时区偏移量（相对于 UTC）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/set_uart.svg">

```python
gpsv2_1.uart_port_id(1)
```

- 设置使用的 UART 接口 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/mpy_docs/module/gps_v2_0/set_work_mode.svg">

```python
gpsv2_1.set_work_mode(1)
```

- 设置 GPS 模块的工作模式
