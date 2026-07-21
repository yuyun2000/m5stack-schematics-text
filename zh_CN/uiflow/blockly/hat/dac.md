# [Hat DAC](/zh_CN/hat/hat-dac)

## 案例程序

输出电压值和原始数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dac/uiflow_block_hat_dac_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat
import hat

setScreenColor(0x111111)

hat_dac_0 = hat.get(hat.DAC)

hat_dac_0.setVoltage(1,save=True)
hat_dac_0.writeData(1,save=True)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dac/uiflow_block_hat_dac_state.svg">

```python
hat_dac_0.setVoltage(1,save=True)
```

- 设置 DAC 输出电压，可以保存当前状态，保存选项为 True

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/dac/uiflow_block_hat_dac_writeData.svg">

```python
hat_dac_0.writeData(1,save=True)
```

- 使用原始数据设置 DAC 输出电压，并保存状态，保存选项为 True

