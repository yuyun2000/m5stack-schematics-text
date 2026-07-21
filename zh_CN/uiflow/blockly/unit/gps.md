# [Unit GPS](/zh_CN/unit/gps)

## 案例程序

> 获取本地时间，以及经纬度信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
gps_0 = unit.get(unit.GPS, unit.PORTC)

while True:
  print(gps_0.gps_time)
  print(gps_0.latitude)
  print(gps_0.longitude)
  print(gps_0.pos_quality)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_uart_init.svg">

```python
gps_0.uart_port_id(1)
```

- 设置 ID 参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_altitude.svg">

```python
print(gps_0.altitude)
```

- 获取海拔高度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_course.svg">

```python
print(gps_0.course)
```

- 获取道路

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_date.svg">

```python
print(gps_0.gps_date)
```

- 获取 GPS 数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_latitude.svg">

```python
print(gps_0.latitude)
```

- 获取纬度(string：dddmm.mmmmm)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_latitude_decimal.svg">

```python
print(gps_0.latitude_decimal)
```

- 获取纬度(string：dd.ddd)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_longitude.svg">

```python
print(gps_0.longitude_decimal)
```

- 获取经度(string：dddmm.mmmmm)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_longitude_decimal.svg">

```python
print(gps_0.longitude)
```

- 获取经度(float：dd.ddd)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_positioning_quality.svg">

```python
print(gps_0.pos_quality)
```

- 获取定位精度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_satellite_num.svg">

```python
print(gps_0.satellite_num)
```

- 获取搜星数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_speed.svg">

```python
print(gps_0.speed_knot)
```

- 获取对地速度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_get_state.svg">

```python
print(gps_0.gps_time)
```

-  获取本地时间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/gps/uiflow_block_unit_gps_set_time_zone.svg">

```python
gps_0.set_time_zone(0)
```

- 设置本地时区

