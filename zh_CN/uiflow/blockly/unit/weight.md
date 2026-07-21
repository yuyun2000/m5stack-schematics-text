# [Unit Weight](/zh_CN/unit/WEIGHT)

## 案例程序

获取 Unit Weight 称重的重量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight/uiflow_block_example.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

weigh_0 = unit.get(unit.WEIGHT, unit.PORTA)

while True:
  print(weigh_0.weight)
  wait(0.1)
  if btnA.isPressed():
    wait(0.1)
    weigh_0.zero()
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight/uiflow_block_weigh_get_rawData.svg">

```python
print((str('weight:') + str((weigh_0.weight))))
```

- 读取 HX711 的原始重量值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight/uiflow_block_weigh_get_weight.svg">

```python
print((str('raw data:') + str((weigh_0.rawData))))
```

- 获取基于校准的缩放权重值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight/uiflow_block_weigh_set_calibrate_scale.svg">

```python
weigh_0.set_calibrate_scale(200)
```

- 使用已知砝码校准秤

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight/uiflow_block_weigh_zero.svg">

```python
weigh_0.zero()
```

- 将皮重设置为将秤清零
