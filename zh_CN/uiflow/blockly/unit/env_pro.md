# [Unit ENV-Pro](/zh_CN/unit/ENV%20Pro%20Unit)

## 案例程序

获取设备测量的大气温度、湿度、压强

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_example.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

envpro_0 = unit.get(unit.ENV_PRO, unit.PORTA)

while True:
  envpro_0.update_new_data_loop()
  print((str('temperature:') + str((envpro_0.get_temperature))))
  print((str('pressure:') + str((envpro_0.get_pressure))))
  print((str('humidity:') + str((envpro_0.get_humidity))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_unit_envpro_get_altitude.svg">

```python
print((str('altitude:') + str((envpro_0.get_altitude))))
```

- 根据压力读数检索计算的高度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_unit_envpro_get_gas_resistance.svg">

```python
print((str('gas resistance:') + str((envpro_0.get_gas_resistance))))
```

- 检索测得的气体电阻

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_unit_envpro_get_humidity.svg">

```python
print((str('humidity:') + str((envpro_0.get_humidity))))
```

- 检索测得的湿度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_unit_envpro_get_iir_filter_coefficient.svg">

```python
print((str('IIR filter:') + str((envpro_0.get_iir_filter_coefficient))))
```

- 检索 IIR 滤波器系数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_unit_envpro_get_over_sampling_rate.svg">

```python
print((str('oversampling rate:') + str((envpro_0.get_over_sampling_rate(1)))))
```

- 检索指定环境参数的过采样率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_unit_envpro_get_pressure.svg">

```python
print((str('pressure:') + str((envpro_0.get_pressure))))
```

- 检索测得的压力

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_unit_envpro_get_temperature.svg">

```python
print((str('temperature:') + str((envpro_0.get_temperature))))
```

- 检索测得的温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_unit_envpro_set_iir_filter_coefficient.svg">

```python
envpro_0.set_iir_filter_coefficient(0)
```

- 设置 IIR 滤波器系数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_unit_envpro_set_over_sampling_rate.svg">

```python
envpro_0.set_over_sampling_rate(1, 1)
```

- 设置指定环境参数的过采样率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/env_pro/uiflow_block_unit_envpro_update_data.svg">

```python
envpro_0.update_new_data_loop()
```

- 刷新数据

