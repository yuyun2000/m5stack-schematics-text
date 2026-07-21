# [Unit ADC v1.1](/zh_CN/unit/Unit-ADC_V1.1)

## 案例程序

> 转换模拟电压信号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/adc_v1.1/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
adc_v11_0 = unit.get(unit.ADCV11, unit.PORTA)

adc_v11_0.set_gain(0x00)
adc_v11_0.set_sample_rate(0x00)
adc_v11_0.set_mode(0x01)
while True:
  print((str('ADC Value:') + str((adc_v11_0.get_adc_raw_value()))))
  print((str('Voltage:') + str((adc_v11_0.get_voltage()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/adc_v1.1/uiflow_block_unit_adcv11_get_adc_raw_value.svg">

```python
print((str('ADC raw value:') + str((adc_v11_0.get_adc_raw_value()))))
```

- 获取 ADC 模拟数据原始值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/adc_v1.1/uiflow_block_unit_adcv11_get_voltage.svg">

```python
print((str('voltage:') + str((adc_v11_0.get_voltage()))))
```

- 获取测得的电压

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/adc_v1.1/uiflow_block_unit_adcv11_set_gain.svg">

```python
adc_v11_0.set_gain(0x00)
```

- 设置 ADC 的 gain 配置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/adc_v1.1/uiflow_block_unit_adcv11_set_mode.svg">

```python
adc_v11_0.set_mode(0x01)
```

- 设置 ADC 的工作模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/adc_v1.1/uiflow_block_unit_adcv11_set_sample_rate.svg">

```python
adc_v11_0.set_sample_rate(0x00)
```

- 配置 ADC 的采样率

