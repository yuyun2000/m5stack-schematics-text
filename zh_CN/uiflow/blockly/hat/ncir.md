# [Hat NCIR](/zh_CN/hat/hat-ncir)

## 案例程序

串口打印传感器数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/ncir/uiflow_block_hat_ncir_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat
import hat

setScreenColor(0x111111)

hat_ncir_0 = hat.get(hat.NCIR)

while True:
  print(hat_ncir_0.temperature)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/ncir/uiflow_block_hat_ncir_read.svg">

```python
hat_ncir_0.temperature
```

- 从指定的红外温度传感器模块读取数据

