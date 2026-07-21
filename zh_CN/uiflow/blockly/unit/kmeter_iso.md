# [Unit KMeter-ISO](/zh_CN/unit/KMeterISO%20Unit)

## 案例程序

> 温度采集

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/kmeter_iso/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
KMeterISO_0 = unit.get(unit.KMETER_ISO, unit.PORTA)

KMeterISO_0.init_i2c_address(0x66)
print((str('Version:') + str((KMeterISO_0.get_firmware_version()))))
print((str('I2C address:') + str((KMeterISO_0.rw_i2c_address()))))
while True:
  print((str('thermocouple::') + str((KMeterISO_0.get_kmeter_thermo(1)))))
  print((str('internal:') + str((KMeterISO_0.get_kmeter_internal(1)))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/kmeter_iso/uiflow_block_unit_kmeteriso_init_i2c.svg">

```python
KMeterISO_0.init_i2c_address(0x66)
```

- 初始化设备的 i2c 地址，默认是0x66

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/kmeter_iso/uiflow_block_unit_kmeteriso_get_fw_version.svg">

```python
print(KMeterISO_0.get_firmware_version())
```

- 获取设备的固件版本号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/kmeter_iso/uiflow_block_unit_kmeteriso_get_i2c_address.svg">

```python
print(KMeterISO_0.rw_i2c_address())
```

- 获取设备的 i2c 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/kmeter_iso/uiflow_block_unit_kmeteriso_get_internal_temp.svg">

```python
print(KMeterISO_0.get_kmeter_internal(1))
```

- 获取芯片内部温度(摄氏度或者华氏度)
  - CELSIUS:摄氏度
  - FAHRENHEIT:华氏温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/kmeter_iso/uiflow_block_unit_kmeteriso_get_isready.svg">

```python
print(KMeterISO_0.get_isready())
```

- 设置设备开始测量温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/kmeter_iso/uiflow_block_unit_kmeteriso_get_str_internal_temp.svg">

```python
print(KMeterISO_0.get_kmeter_internal_string(1))
```

- 以字符串形式输出芯片的温度
  - CELSIUS:摄氏度
  - FAHRENHEIT:华氏温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/kmeter_iso/uiflow_block_unit_kmeteriso_get_str_thermo_temp.svg">

```python
print(KMeterISO_0.get_kmeter_thermo_string(1))
```

- 以字符串形式输出热电偶的温度
  - CELSIUS:摄氏度
  - FAHRENHEIT:华氏温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/kmeter_iso/uiflow_block_unit_kmeteriso_get_thermo_temp.svg">

```python
print(KMeterISO_0.get_kmeter_thermo(1))
```

- 获取热电偶温度
  - CELSIUS:摄氏度
  - FAHRENHEIT:华氏温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/kmeter_iso/uiflow_block_unit_kmeteriso_set_i2c_address.svg">

```python
KMeterISO_0.rw_i2c_address(0x66)
```

- 设置设备的 i2c 地址

