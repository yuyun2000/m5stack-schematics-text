# [Hat DAC2](/zh_CN/hat/Hat-DAC2)

## 案例程序

输出读取的电压值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dac2/uiflow_block_hat_dac2_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0x111111)

hat_dac2_0 = hat.get(hat.DAC2)

hat_dac2_0.setDACOutputVoltageRange(hat_dac2_0.RANGE_5V)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dac2/uiflow_block_hat_dac2_setDACOutputVoltageRange.svg">

```python
hat_dac2_0.setDACOutputVoltageRange(hat_dac2_0.RANGE_5V)
```

- 设置 DAC 输出电压范围，当前选择为 RANGE_5V

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dac2/uiflow_block_hat_dac2_setVoltage.svg">

```python
hat_dac2_0.setVoltage(5, channel=hat_dac2_0.CHANNEL_0)
```

- 为 Channel 0 设置输出电压为 5V

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dac2/uiflow_block_hat_dac2_setVoltageBoth.svg">

```python
hat_dac2_0.setVoltageBoth(5, 5)
```

- 同时为 Channel 0 和 Channel 1 设置输出电压，均为 5V

