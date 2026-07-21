# [Unit Ultrasonic-IO](/zh_CN/unit/UNIT%20SONIC%20IO)


## 案例程序

> 获取 Sonic IO 采集的超声波测量数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/sonicio/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
sonic_io_0 = unit.get(unit.SONIC_IO, unit.PORTB)

while True:
  print(sonic_io_0.get_distance(1))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/sonicio/uiflow_block_sonic_io_get_distance.svg">

```python
print(sonic_io_0.get_distance(1))
```

- 获得设备 Sonic IO 采集的超声波测量数据，返回一个 float 类型
