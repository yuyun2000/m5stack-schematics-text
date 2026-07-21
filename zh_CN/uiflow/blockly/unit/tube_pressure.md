# [Unit Tube Pressure](/zh_CN/unit/tube_pressure)

## 案例程序

获取设备测量的压强

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tube_pressure/uiflow_tubepressure_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
tube_0 = unit.get(unit.TUBE, unit.PORTB)

while True:
  print(tube_0.get_pressure())
  print(tube_0.average_analog_value())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tube_pressure/uiflow_block_unit_tube_get_adc_raw.svg">

```python
print(tube_0.average_analog_value())
```

- 获取模数转换原始值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tube_pressure/uiflow_block_unit_tube_get_pressure.svg">

```python
print(tube_0.get_pressure())
```

- 获取压力值

