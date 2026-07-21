# [Unit Light](/zh_CN/unit/LIGHT)

## 案例程序

读取设备测量光强度信号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/light/uiflow_light_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
light_0 = unit.get(unit.LIGHT, unit.PORTB)

while True:
  print(light_0.digitalValue)
  print(light_0.analogValue)
  wait(0.2)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/light/uiflow_block_light_a_read.svg">

```python
print((str('analog:') + str((light_0.analogValue))))
```

- 获取模拟信号输出数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/light/uiflow_block_light_d_read.svg">

```python
print((str('digital:') + str((light_0.digitalValue))))
```

- 获取数字信号输出数据

