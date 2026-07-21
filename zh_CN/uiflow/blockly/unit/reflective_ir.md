# [Unit Reflective IR](/zh_CN/unit/Unit-Reflective%20IR)

## 案例程序

> 红外测距

<img class="blockly_svg" src="example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
reflective_ir_0 = unit.get(unit.REFLECTIVE_IR, unit.PORTB)

while True:
  print((str('analog:') + str((reflective_ir_0.get_analog_output()))))
  print((str('digital:') + str((reflective_ir_0.get_digital_output()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/reflective_ir/uiflow_block_unit_reflectiveir_get_analog_output.svg">

```python
print(reflective_ir_0.get_analog_output())
```

- 读取反射 IR 单元的 ADC 值并返回一个整数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/reflective_ir/uiflow_block_unit_reflectiveir_get_digital_output.svg">

```python
print(reflective_ir_0.get_digital_output())
```

- 读取反射 IR 单元的数字值并返回一个整数值

