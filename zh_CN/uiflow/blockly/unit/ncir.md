# [Unit NCIR](/zh_CN/unit/ncir)

## 案例程序

测量感应红外温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir/uiflow_ncir_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
ncir_0 = unit.get(unit.NCIR, unit.PORTA)

while True:
  print((str('temperature:') + str((ncir_0.temperature))))
  wait(0.2)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ncir/uiflow_block_unit_ncir_read.svg">

```python
print((str('temperature:') + str((ncir_0.temperature))))
```

- 获取设备感应的红外温度数据

