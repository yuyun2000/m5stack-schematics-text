# [Unit AIN4-20mA](/zh_CN/unit/AIN4-20mA%20Unit)

## 案例程序

测量电路电流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ain4_20ma/uiflow_ain420ma_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
ain420ma_0 = unit.get(unit.AIN_420MA, unit.PORTA)

ain420ma_0.init_i2c_address(0x55)
while True:
  print((str('version:') + str((ain420ma_0.get_firmware_status()))))
  print((str('value:') + str((ain420ma_0.get_adc_raw16_value()))))
  print((str('current:') + str((ain420ma_0.get_ain_current_value()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ain4_20ma/uiflow_block_unit_ain420ma_init.svg">

```python
ain420ma_0.init_i2c_address(0x55)
```

- 4~20mA输入单元初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ain4_20ma/uiflow_block_unit_ain420ma_get_adc_raw16_value.svg">

```python
print((str('value:') + str((ain420ma_0.get_adc_raw16_value()))))
```

- 获取ADC原始16位数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ain4_20ma/uiflow_block_unit_ain420ma_get_current_value.svg">

```python
print((str('current:') + str((ain420ma_0.get_ain_current_value()))))
```

- 获取电流值（mA）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ain4_20ma/uiflow_block_unit_ain420ma_get_firmware_version.svg">

```python
print((str('version:') + str((ain420ma_0.get_firmware_status()))))
```

- 获取固件版本号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ain4_20ma/uiflow_block_unit_ain420ma_set_i2c_address.svg">

```python
ain420ma_0.set_i2c_address(0x55)
```

- 设置I2C通信地址

