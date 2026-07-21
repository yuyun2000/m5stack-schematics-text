# [Unit Thermal](/zh_CN/unit/THERMAL)

## 案例程序

红外感应器测量温度

<img class="blockly_svg" src="example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
thermal_0 = unit.get(unit.THERMAL, unit.PORTA)

thermal_0.set_refresh_rate(0b000)
while True:
  print(thermal_0.get_temperature())
  thermal_0.update_temperature()
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal/uiflow_block_unit_thermal_get_center_temperature.svg">

```python
print(thermal_0.get_center_temperature())
```

- 获取中心区域温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal/uiflow_block_unit_thermal_get_max_temperature.svg">

```python
print(thermal_0.get_max_temperature())
```

- 获取最高温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal/uiflow_block_unit_thermal_get_min_temperature.svg">

```python
print(thermal_0.get_min_temperature())
```

- 获取最低温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal/uiflow_block_unit_thermal_get_pixel_temperature.svg">

```python
print(thermal_0.get_pixel_temperature(0 , 0))
```

- 获取像素级温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal/uiflow_block_unit_thermal_get_refresh_rate.svg">

```python
print(thermal_0.get_refresh_rate())
```

- 获取刷新频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal/uiflow_block_unit_thermal_get_temperature.svg">

```python
print(thermal_0.get_temperature())
```

- 获取当前温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal/uiflow_block_unit_thermal_set_refresh_rate.svg">

```python
thermal_0.set_refresh_rate(0b000)
```

- 设置刷新频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/thermal/uiflow_block_unit_thermal_update_temperature.svg">

```python
thermal_0.update_temperature()
```

- 更新温度数据

