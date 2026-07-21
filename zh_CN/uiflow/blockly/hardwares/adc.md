# ADC

## 案例程序

使用 adc0通道在36引脚进行采样，读取数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/adc/uiflow_block_adc_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *
import machine

setScreenColor(0x222222)

adc0 = machine.ADC(36)
adc0.width(machine.ADC.WIDTH_12BIT)
adc0.atten(machine.ADC.ATTN_11DB)
while True:
  print(adc0.read())
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/adc/uiflow_block_adc_init.svg"> 

```python
adc0 = machine.ADC([pin])
```

- 设置采样通道引脚

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/adc/uiflow_block_adc_set_width.svg"> 

```python
adc0.width(machine.ADC.WIDTH_12BIT)
```

- 设置采样宽度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/adc/uiflow_block_adc_set_atten.svg"> 

```python
adc0.atten(machine.ADC.ATTN_11DB)
```

- 设置 ADC 输入衰减
  - `ADC.ATTN_0DB`: 0dB 衰减，提供最大1.00v 的输入电压
  - `ADC.ATTN_2_5DB`: 2.5dB 衰减，提供大约1.34v 的最大输入电压
  - `ADC.ATTN_6DB`: 6dB 衰减，提供大约2.00v 的最大输入电压
  - `ADC.ATTN_11DB`: 11dB 衰减，提供大约3.6v 的最大输入电压


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/adc/uiflow_block_adc_set_read_value.svg"> 

```python
adc0.read()
```

- 读取 ADC 数值

