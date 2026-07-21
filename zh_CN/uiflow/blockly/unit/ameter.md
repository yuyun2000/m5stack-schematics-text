# [Unit AMeter](/zh_CN/unit/Ameter%20Unit)

## 案例程序

测量电流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ameter/uiflow_ameter_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
AMeter_0 = unit.get(unit.AMETER, unit.PORTA)

while True:
  print((str('Current: ') + str(((str((AMeter_0.current())) + str(' mA'))))))
  wait(0.3)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ameter/uiflow_block_ameter_current.svg">

```python
print((str('Curent:') + str((AMeter_0.current()))))
```

- 获取测量电流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ameter/uiflow_block_ameter_raw.svg">

```python
print((str('raw:') + str((AMeter_0.raw()))))
```

- 获取测量电流原始数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ameter/uiflow_block_ameter_set_gain2.svg">

```python
AMeter_0.setGain(AMeter_0.PGA_256)
```

- 设置最大输入电流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ameter/uiflow_block_ameter_set_mode.svg">

```python
AMeter_0.setMode(AMeter_0.MODE_CONTINUOUS)
```

- 设置工作模式
  - continuous：连续模式
  - singleshot：单次触发模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ameter/uiflow_block_ameter_set_rate.svg">

```python
AMeter_0.setRate(AMeter_0.RATE_8)
```

- 设置每秒采样点

