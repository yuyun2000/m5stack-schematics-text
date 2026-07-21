# [Unit Mini BPS](/zh_CN/unit/bps)

## 案例程序

获取空气压强和温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bps/uiflow_bps_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
bps_0 = unit.get(unit.BPS, unit.PORTA)

while True:
  print((str('temperature:') + str((bps_0.temperature()))))
  print((str('pressure:') + str((bps_0.pressure()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bps/uiflow_block_bps_get_pressure.svg">

```python
print((str('pressure:') + str((bps_0.pressure()))))
```

- 获取设备测量压强

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bps/uiflow_block_bps_get_temperature.svg">

```python
print((str('pressure:') + str((bps_0.pressure()))))
```

- 获取设备测量文档

