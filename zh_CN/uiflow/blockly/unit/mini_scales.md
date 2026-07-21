# [Unit Mini Scales](/zh_CN/unit/Unit-Mini%20Scales)

## 案例程序

> 显示所称量物体重量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
miniscales_0 = unit.get(unit.MINISCALE, unit.PORTA)

miniscales_0.setLed(255, 0, 0)
while True:
  print((str('weight:') + str(((str((miniscales_0.weight)) + str('g'))))))
  print((str('button status:') + str((miniscales_0.button))))
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_calibration.svg">

```python
miniscales_0.calibration(0, adc0, 100, adc1)
```

- 校准测量重量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_get_adc.svg">

```python
print(miniscales_0.adc)
```

- 获取 ADC 原始值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_get_average_filter.svg">

```python
print(miniscales_0.getAverageFilterLevel())
```

- 获取滤波器平均级别

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_get_button.svg">

```python
print(miniscales_0.button)
```

- 获取当前按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_get_ema_filter.svg">

```python
print(miniscales_0.getEMAFilterAlpha())
```

- 获取 EMA 过滤器 alpha 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_get_lowpass_filter.svg">

```python
print(miniscales_0.getLowPassFilter())
```

- 获取低过率滤波器状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_get_weight.svg">

```python
print(miniscales_0.weight)
```

- 获取当前重量(单位 g ，返回 Float)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_reset.svg">

```python
miniscales_0.reset()
```

- 重置信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_set_average_filter.svg">

```python
miniscales_0.setAverageFilterLevel(0)
```

- 设置平均滤波器的等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_set_ema_filter.svg">

```python
miniscales_0.setEMAFilterAlpha(0)
```

- 设置 EMA 过滤器 alpha 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_set_led.svg">

```python
miniscales_0.setLed(255, 0, 0)
```

- 设置 RGB 灯颜色值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_scales/uiflow_block_unit_miniscale_set_lowpass_filter.svg">

```python
miniscales_0.setLowPassFilter(True)
```

- 设置低通过率滤波器的状态

