# [Unit Buzzer](/zh_CN/unit/buzzer)

## 案例程序

> 程序触发蜂鸣器发出身响

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/buzzer/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
buzzer_0 = unit.get(unit.BUZZER, unit.PORTB)

buzzer_0.set_buzzer(1)
while True:
  buzzer_0.set_freq(4000)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/buzzer/uiflow_block_unit_buzzer_set_freq.svg">

```python
buzzer_0.set_freq(4000)
```

- 设置频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/buzzer/uiflow_block_unit_buzzer_set_state.svg">

```python
buzzer_0.set_buzzer(1)
```

- 设置 Unit BUZZER 状态