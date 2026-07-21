# [Unit PIR](/zh_CN/unit/PIR)

## 案例程序

检测红外状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pir/uiflow_pir_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
pir_0 = unit.get(unit.PIR, unit.PORTB)

while True:
  if (pir_0.state) == 1:
    print('PIR Status: Detected')
  else:
    print('PIR Status: Not detected')
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pir/uiflow_block_pir_read.svg">

```python
print((str('status:') + str((pir_0.state))))
```

- 获取设备感应状态

