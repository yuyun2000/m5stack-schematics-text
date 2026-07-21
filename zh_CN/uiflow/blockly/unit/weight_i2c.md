# [Unit Weight-I2C](/zh_CN/unit/Unit-Weight%20I2C)

## 案例程序

Unit Weight-I2C 重量测量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_weight_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
weight_i2c_0 = unit.get(unit.WEIGHT_I2C, unit.PORTA)

weight_i2c_0.init_i2c_address(0x26)
while True:
  print(weight_i2c_0.get_weight_int)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_init.svg">

```python
weight_i2c_0.init_i2c_address(0x26)
```

- 初始化称重采集变送器单元

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_get_adc_raw_value.svg">

```python
print((str('value:') + str((weight_i2c_0.get_adc_raw))))
```

- 获取的 ADC（模数转换器）原始值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_get_average_filter_level.svg">

```python
print((str('filter:') + str((weight_i2c_0.get_average_filter_level))))
```

- 获取的平均滤波级别

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_get_device_spec.svg">

```python
print((str('detail:') + str((weight_i2c_0.get_device_spec(0xFE)))))
```

- 获取的设备规格信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_get_ema_filter_alpha.svg">

```python
print((str('filter:') + str((weight_i2c_0.get_ema_filter_alpha))))
```

- 获取的指数移动平均（EMA）滤波器的 alpha 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_get_lowpass_filter.svg">

```python
print((str('filter:') + str((weight_i2c_0.get_lowpass_filter))))
```

- 获取的低通滤波器设置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_get_weight_in_float.svg">

```python
print((str('weight:') + str((weight_i2c_0.get_weight_float))))
```

- 以浮点数形式获取测量的重量值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_get_weight_in_int.svg">

```python
print((str('weight:') + str((weight_i2c_0.get_weight_int))))
```

- 以整数形式获取测量的重量值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_get_weight_in_str.svg">

```python
print((str('weight:') + str((weight_i2c_0.get_weight_str))))
```

- 以字符串形式获取测量的重量值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_reset_offset.svg">

```python
weight_i2c_0.set_reset_offset()
```

- 重置的零点偏移

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_set_average_filter_level.svg">

```python
weight_i2c_0.set_average_filter_level(0)
```

- 设置的平均滤波级别

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_set_calibration.svg">

```python
weight_i2c_0.set_calibration(0, 0, 100, 100)
```

- 设置的校准参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_set_ema_filter_alpha.svg">

```python
weight_i2c_0.set_ema_filter_alpha(0)
```

- 设置的指数移动平均（EMA）滤波器的 alpha 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_set_i2c_address.svg">

```python
weight_i2c_0.set_i2c_address(0x26)
```

- 设置的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/weight_i2c/uiflow_block_unit_weighti2c_set_lowpass_filter.svg">

```python
weight_i2c_0.set_lowpass_filter(True)
```

- 设置的低通滤波器参数

