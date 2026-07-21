# [Unit ADC](/zh_CN/unit/adc)

## 案例程序

> 转换模拟电压信号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/adc/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
adc_0 = unit.get(unit.ADC, unit.PORTA)

while True:
  print(adc_0.voltage)
  wait(0.1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/adc/uiflow_block_unit_adc_state.svg">

```python
print((str('voltage:') + str((adc_0.voltage))))
```

- 获取测量的模拟电压

