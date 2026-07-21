# [Module13.2 AIN4-20mA](/zh_CN/module/AIN4-20mA%20Module%2013.2)

## 案例程序

获取四个通道的 ADC 值，电流值以及固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/ain4_20ma/uiflow_block_AIN4-20mA_demo1.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

setScreenColor(0x222222)

ain420 = module.get(module.AIN_420MA)

while True:
  print((str('ADC1 Value：') + str((ain420.get_adc_raw16_value(1)))))
  print((str('ADC2 Value：') + str((ain420.get_adc_raw16_value(2)))))
  print((str('ADC3 Value：') + str((ain420.get_adc_raw16_value(3)))))
  print((str('ADC4 Value：') + str((ain420.get_adc_raw16_value(4)))))
  print((str('Current') + str((ain420.get_ain_current_value(1)))))
  print((str('Firmware Version：') + str((ain420.get_firmware_status()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/ain4_20ma/uiflow_block_module_ain420ma_get_adc_raw16_value.svg">

```python
ain420.get_adc_raw16_value(1)
```

- 获取通道的16位 ADC 原始值。这是一个未经处理的数字信号表示，通过指定的通道读取

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/ain4_20ma/uiflow_block_module_ain420ma_get_current_value.svg">

```python
ain420.get_ain_current_value(1)
```

- 获取通道的电流值。这通常用于读取电流传感器的数据，表示通道上的实际电流值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/ain4_20ma/uiflow_block_module_ain420ma_get_firmware_version.svg">

```python
ain420.get_firmware_status()
```

- 获取设备的固件版本号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/ain4_20ma/uiflow_block_module_ain420ma_init.svg">

```python
ain420.init_i2c_address(0x55)
```

- 初始化设备的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/ain4_20ma/uiflow_block_module_ain420ma_set_i2c_address.svg">

```python
ain420.set_i2c_address(0x55)
```

- 设置设备的 I2C 从属地址

