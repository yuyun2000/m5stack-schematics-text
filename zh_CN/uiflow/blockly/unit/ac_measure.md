# [Unit AC Measure](/zh_CN/unit/AC%20Measure%20Unit)

## 案例程序

测量电流与电压

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_acmeasure_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x000000)
ac_measure_0 = unit.get(unit.AC_MEASURE, unit.PORTA)

isdata = None

ac_measure_0.init_i2c_address(0x42)
print((str('FW VER:') + str((ac_measure_0.get_device_status(0xFE)))))
while True:
  isdata = ac_measure_0.get_data_ready()
  if isdata:
    print((str('VOLTAGE:') + str((ac_measure_0.get_voltage_str()))))
    print((str('CURRENT:') + str((ac_measure_0.get_current_str()))))
    print((str('POWER:') + str((ac_measure_0.get_active_power_str()))))
    print((str('KW/H') + str((ac_measure_0.get_kwh_str()))))
  wait(1)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_init.svg">

```python
ac_measure_0.init_i2c_address(0x42)
```

- 通过设置 I2C 端口和 地址来初始化 AC Measure 单元

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_data_ready.svg">

```python
print((str('ready:') + str((ac_measure_0.get_data_ready()))))
```

- 数据就绪状态检查

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_active_power.svg">

```python
print((str('active power:') + str((ac_measure_0.get_active_power_str()))))  
```

- 获取有功功率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_active_power_raw.svg">

```python
print((str('active power raw:') + str((ac_measure_0.get_active_power_byte()))))
```

- 获取原始有功功率数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_apparent_power.svg">

```python
print((str('apparent power:') + str((ac_measure_0.get_apparent_power_str()))))
```

- 获取视在功率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_apparent_power_raw.svg">

```python
print((str('apparent power raw:') + str((ac_measure_0.get_apparent_power_byte()))))
```

- 获取原始视在功率数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_current.svg">

```python
print((str('current:') + str((ac_measure_0.get_current_str()))))
```

- 获取电流值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_current_coefficient.svg">

```python
print((str('current coefficient:') + str((ac_measure_0.get_current_coeff()))))
```

- 获取电流校准系数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_current_raw.svg">

```python
print((str('current raw:') + str((ac_measure_0.get_current_byte()))))
```

- 获取原始电流数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_fw.svg">

```python
print((str('firmware:') + str((ac_measure_0.get_device_status(0xFE)))))
```

- 获取固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_kwh.svg">

```python
print((str('kw:') + str((ac_measure_0.get_kwh_str()))))
```

- 获取累计电能（千瓦时）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_kwh_raw.svg">

```python
print((str('kw raw:') + str((ac_measure_0.get_kwh_byte()))))
```

- 获取原始电能数据（千瓦时）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_power_factor.svg">

```python
print((str('power factor:') + str((ac_measure_0.get_power_factor_str()))))
```

- 获取功率因数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_power_factor_raw.svg">

```python
print((str('power factor raw:') + str((ac_measure_0.get_power_factor_byte()))))
```

- 获取原始功率因数数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_voltage.svg">

```python
print((str('voltage:') + str((ac_measure_0.get_voltage_str()))))
```

- 获取电压值（伏特）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_voltage_coefficient.svg">

```python
print((str('voltage coefficient:') + str((ac_measure_0.get_voltage_coeff()))))
```

- 获取电压校准系数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_get_voltage_raw.svg">

```python
print((str('voltage raw:') + str((ac_measure_0.get_voltage_byte()))))
```

- 获取原始电压数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_set_current_coefficient.svg">

```python
ac_measure_0.set_current_coeff(100)
```

- 设置电流校准系数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_set_i2c_address.svg">

```python
ac_measure_0.set_i2c_address(0x42)
```

- 设置I2C通信地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_set_save_coeff.svg">

```python
ac_measure_0.set_save_coeff()
```

- 保存校准系数到非易失性存储器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_measure/uiflow_block_unit_acmeasure_set_voltage_coefficient.svg">

```python
ac_measure_0.set_voltage_coeff(100)
```

- 设置电压校准系数

