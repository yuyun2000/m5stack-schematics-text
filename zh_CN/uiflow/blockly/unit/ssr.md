# [Unit SSR](/zh_CN/unit/ssr)

## 案例程序

> 控制继电器状态 ON/OFF

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ssr/uiflow_block_ssr.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
ssr_0 = unit.get(unit.SSR, unit.PORTA)

while True:
  ssr_0.ssr_control(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ssr/uiflow_block_unit_ssr_control.svg">

```python
ssr_0.ssr_control(1)
```

- 开启或断开继电器
  - ON
  - OFF
