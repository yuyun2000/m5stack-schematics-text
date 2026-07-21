# [Module Plus](/zh_CN/module/plus)

## 案例程序

读取并打印连接的PLUS扩展模块的编码器和按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/plus/uiflow_block_plus_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

setScreenColor(0x222222)

plus = module.get(module.PLUS)

while True:
  print((str('Encoder') + str((plus.get_encode()))))
  print((str('Button') + str((plus.get_press()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/plus/uiflow_block_plus_clean_encode.svg">

```python
plus.clean_encode()
```

- 清除编码器的当前编码值，将其复位为零

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/plus/uiflow_block_plus_get_encode.svg">

```python
plus.get_encode()
```

- 获取当前编码器的编码值。返回的值是编码器的当前位置值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/plus/uiflow_block_plus_get_press.svg">

```python
plus.get_press()
```

- 获取按键的按压状态。返回的值表示当前按键是否被按下

