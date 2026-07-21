# [Hat ToF](/zh_CN/hat/hat-tof)

## 案例程序

获取传感器获取的距离数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/tof/uiflow_block_hat_tof_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_tof_0 = hat.get(hat.TOF)

while True:
  print(hat_tof_0.GetDistance())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/tof/uiflow_block_hat_tof_get_distance.svg">

```python
hat_tof_0.GetDistance()
```

- 获取距离数据

