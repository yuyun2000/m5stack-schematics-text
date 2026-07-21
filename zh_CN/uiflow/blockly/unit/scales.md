# [Unit Scales](/zh_CN/unit/UNIT%20Scales)

## Example

> 测量重量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
scales_0 = unit.get(unit.SCALES, unit.PORTA)

scales_0.write_rgb_led(25, 72, 26)
scales_0.write_button_offset(1)
while True:
  print((str('weight:') + str(((scales_0.read_weight(0x14)/100) - -58344))))
  print((str('button:') + str((scales_0.read_button_status(0x20)))))
  wait(1)
  wait_ms(2)
```

## API

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_init_i2c.svg">

```python
scales_0.init_i2c_address(0x26)
```

- 初始化 Unit Scales I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_get_button.svg">

```python
print(scales_0.read_button_status(0x20))
```

- 获取按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_get_led.svg">

```python
print(scales_0.read_rgb_led(False))
```

- 获取 LED 状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_get_scale.svg">

```python
print(scales_0.read_weight(0x10))
```

- 获取 ADC 原始值状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_get_status.svg">

```python
print(scales_0.read_status(0xFE))
```

- 获取版本号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_set_adc.svg">

```python
scales_0.write_offset(5000)
```

- 设定偏移 ADC 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_set_adc_offset.svg">

```python
scales_0.write_soft_offset()
```

- 设置偏移电流 ADC 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_set_button_offset.svg">

```python
scales_0.write_button_offset(1)
```

- 设置按钮偏离

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_set_calibration.svg">

```python
scales_0.write_calibration_load(200)
```

- 设置负载校准

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_set_i2c.svg">

```python
scales_0.write_i2c_address(0x26)
```

- 重置 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_set_rgb.svg">

```python
scales_0.write_rgb_led(0, 0, 0)
```

- 设置 RGB 颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_set_rgb_sync.svg">

```python
scales_0.write_rgb_sync(0)
```

- 设置 RGB LED 同步状态
  - ENABLE
  - DISABLE 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/scales/uiflow_block_unit_scales_set_zero.svg">

```python
scales_0.write_calibration_zero()
```

- 设置校准器为零克

