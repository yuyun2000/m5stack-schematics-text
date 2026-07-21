# [Hat PIR](/zh_CN/hat/hat-pir)

## 案例程序

串口输出人体传感器的感应数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/pir/uiflow_block_hat_pir_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat
import hat

setScreenColor(0x111111)

hat_pir_0 = hat.get(hat.PIR)

while True:
  print(hat_pir_0.state)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/pir/uiflow_block_hat_pir_read.svg">

```python
hat_pir_0.state
```

- 用于获取指定 PIR 传感器的状态，通常用于检测是否有运动发生

