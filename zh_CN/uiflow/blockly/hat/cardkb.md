# [Hat CardKB](/zh_CN/hat/hat-cardkb)

## 案例程序

打印按键的数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cardkb/uiflow_block_hat_cardkb_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_cardkb_1 = hat.get(hat.CARDKB)

print(hat_cardkb_1.keyData)
print(hat_cardkb_1.keyString)
print(hat_cardkb_1.isNewKeyPress())
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cardkb/uiflow_block_hat_cardkb_get_key.svg">

```python
hat_cardkb_0.keyData
```

- 获取按下的单个键值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cardkb/uiflow_block_hat_cardkb_get_pressed.svg">

```python
hat_cardkb_0.isNewKeyPress()
```

- 获取当前被按下的按键状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cardkb/uiflow_block_hat_cardkb_get_string.svg">

```python
hat_cardkb_0.keyString
```

- 获取输入的字符串

