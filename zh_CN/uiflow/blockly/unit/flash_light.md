# [Unit FlashLight](/zh_CN/unit/FlashLight)

## 案例程序

> 设备每间隔 2 秒进行一次闪光

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/flash_light/uiflow_block_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
flash_0 = unit.get(unit.FLASH_LIGHT, unit.PORTB)

flash_0.flash_ctrl(7, False, 2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/flash_light/uiflow_block_unit_flashlight_control.svg">

```python
flash_0.flash_ctrl(0, False, 2)
```

- 设置 flash 控制(设置占空比30%-100%，和开关 FlashLight)

