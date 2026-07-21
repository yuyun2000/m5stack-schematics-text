
# [Hat ADC](/zh_CN/hat/hat-adc)

## 案例程序

串口打印获取的电压值和原始数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/adc/uiflow_block_hat_adc_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat
import hat

setScreenColor(0x111111)

hat_adc_1 = hat.get(hat.ADC)

print(hat_adc_1.voltage)
print(hat_adc_1.rawData())
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/adc/uiflow_block_hat_adc_raw_value.svg">

```python
hat_adc_0.rawData()
```

- 读取 ADC 的原始值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/adc/uiflow_block_hat_adc_state.svg">

```python
hat_adc_0.voltage
```

- 读取 ADC 的电压值

