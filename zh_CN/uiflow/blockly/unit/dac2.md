# [Unit DAC2](/zh_CN/unit/Unit-DAC2)

## 案例程序

> DAC2（数模转换器）单元来输出不同的模拟电压值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dac2/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
dac2_0 = unit.get(unit.DAC2, unit.PORTA)

i = None

while True:
  for i in range(4):
    dac2_0.setVoltage(i, channel=dac2_0.CHANNEL_0)
    print((str(str(i)) + str('V')))
    wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dac2/uiflow_block_unit_dac2_setDACOutputVoltageRange.svg">

```python
dac2_0.setDACOutputVoltageRange(dac2_0.RANGE_5V)
```

- 设置 DAC 的电压
  - 范围(5V)
  - 范围(10V)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dac2/uiflow_block_unit_dac2_setVoltage.svg">

```python
dac2_0.setVoltage(5, channel=dac2_0.CHANNEL_0)
```

- 设置指定通道的输出电压

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dac2/uiflow_block_unit_dac2_setVoltageBoth.svg">

```python
dac2_0.setVoltageBoth(5, 5)
```

- 设置通道0和通道1的输出电压

