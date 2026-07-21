# [Unit PaHUB](/zh_CN//unit/pahub)

## 案例程序

> 通过 Unit PaHUB 分线，连接多款 Unit ToF ，实现 Unit ToF 的激光测距功能

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pahub/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
pahub_0 = unit.get(unit.PAHUB, unit.PORTA, 0x70)
tof_0 = unit.get(unit.TOF, unit.PAHUB0)

label0 = M5TextBox(130, 119, "label0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
pahub_0.select(0, 1)
while True:
  print(tof_0.distance)
  label0.setText(str(tof_0.distance))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pahub/uiflow_block_pahub_only_on.svg">

```python
pahub_0 = unit.get(unit.PAHUB, unit.PORTA, 0x70)
```

- 设置通道状态为开启(通道选择)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pahub/uiflow_block_pahub_only_on_input.svg">

```python
pahub_0 = unit.get(unit.PAHUB, unit.PORTA, 0x70)
```

-置通道状态为开启(通过变量控制通道)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pahub/uiflow_block_pahub_port.svg">

```python
pahub_0 = unit.get(unit.PAHUB, unit.PORTA, 0x70)
```

- 设置通道对应 value 值(十六进制)，进行通讯

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pahub/uiflow_block_pahub_select.svg">

```python
pahub_0 = unit.get(unit.PAHUB, unit.PORTA, 0x70)
```

- 设置通道状态(通道选择)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/pahub/uiflow_block_pahub_select_input.svg">

```python
pahub_0 = unit.get(unit.PAHUB, unit.PORTA, 0x70)
```

- 通过变量设置通道状态(通道变量控制)
