# [Unit Earth](/zh_CN/unit/earth)

## 案例程序

> 打印 Earth Unit 检测的模拟和数字量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/earth/uiflow_block_earth_demo.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
earth_0 = unit.get(unit.EARTH, unit.PORTB)

while True:
  print((str('Analog Value:') + str((earth_0.analogValue))))
  print((str('Digital Value:') + str((earth_0.digitalValue))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/earth/uiflow_block_earth_a_read.svg">

```python
earth_0.analogValue
```

- 获取指定设备 earth 的模拟值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/earth/uiflow_block_earth_d_read.svg">

```python
earth_0.digitalValue
```

- 获取指定设备 earth 的数字值

