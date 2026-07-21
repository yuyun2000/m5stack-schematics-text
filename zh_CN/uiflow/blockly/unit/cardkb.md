# [Unit CardKB](/zh_CN/unit/cardkb)

## 案例程序

> 获取点击按键的 ASIIC 数值和点击状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/cardkb/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
cardkb_0 = unit.get(unit.CARDKB, unit.PORTA)

while True:
  print(cardkb_0.keyData)
  print(cardkb_0.keyString)
  wait(0.1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/cardkb/uiflow_block_cardkb_getkey.svg">

```python
print(cardkb_0.keyData)
```

- 返回 ASIIC 数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/cardkb/uiflow_block_cardkb_getpress.svg">

```python
print(cardkb_0.isNewKeyPress())
```

- 返回字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/cardkb/uiflow_block_cardkb_getstring.svg">

```python
print(cardkb_0.keyString)
```

- 检测按键，按下返回真
