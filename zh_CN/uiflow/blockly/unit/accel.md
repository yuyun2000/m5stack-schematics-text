# [Unit Accel](/zh_CN/unit/accel)

## 案例程序

> 获取传感器检测的运动数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/accel/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
accel_0 = unit.get(unit.ACCEL, unit.PORTA)

while True:
  print((str('X ACC:') + str((accel_0.acceleration[0]))))
  print((str('Y ACC:') + str((accel_0.acceleration[1]))))
  print((str('Z ACC:') + str((accel_0.acceleration[2]))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/accel/uiflow_block_unit_accel_get_x_acc.svg">

```python
print((str('X ACC:') + str((accel_0.acceleration[0]))))
```

- 获取 X 加速值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/accel/uiflow_block_unit_accel_get_y_acc.svg">

```python
print((str('Y ACC:') + str((accel_0.acceleration[1]))))
```

- 获取 Y 加速值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/accel/uiflow_block_unit_accel_get_z_acc.svg">

```python
print((str('Z ACC:') + str((accel_0.acceleration[2]))))
```

- 获取 Z 加速值

