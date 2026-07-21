# [Unit Ultrasonic](/zh_CN/unit/Ultrasonic)

## 案例程序

> 获取 Ultrasonic 采集的超声波测量数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ultrasonic/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
Ultrasonic_0 = unit.get(unit.ULTRASONIC, unit.PORTA)

while True:
  print(Ultrasonic_0.distance)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ultrasonic/uiflow_block_Ultrasonic_distance.svg">

```python
print(Ultrasonic_0.distance)
```

- 获得设备 Ultrasonic 采集的超声波测量数据，返回一个 float 类型
