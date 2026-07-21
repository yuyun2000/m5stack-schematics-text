# [Module13.2 Dual Kmeter](/zh_CN/module/DualKmeter%20Module13.2)

## 案例程序

循环打印设备固件版本、选定的通道、热电偶温度(摄氏度和华氏度)、内部温度(摄氏度和华氏度)，每次循环等待250毫秒

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_dual_kmeter_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x230c0c)

dualkmeter = module.get(module.DUAL_KMETER)

label4 = M5TextBox(194, 0, "Thermo F", lcd.FONT_Ubuntu, 0x710000, rotate=0)

dualkmeter.init_i2c_address(0x11)
print((str('Firmware：') + str((dualkmeter.get_firmware_version()))))
while True:
  if dualkmeter.get_isready():
    print((str('Kmeter channel:') + str((dualkmeter.rw_select_kmeter()))))
    print((str('Temperature:') + str((dualkmeter.get_kmeter_thermo(1)))))
    print((str('Internal temperature(CELSIUS):') + str((dualkmeter.get_kmeter_internal(1)))))
    print((str('Thermocouple temperature:') + str((dualkmeter.get_kmeter_thermo(2)))))
    print((str('Internal temperature(FAHRENHEIT):') + str((dualkmeter.get_kmeter_internal(2)))))
  wait_ms(250)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_module_dualkmeter_get_channel.svg">

```python
dualkmeter.rw_select_kmeter()
```

- 获取选择的通道。返回当前选定的通道

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_module_dualkmeter_get_fw_version.svg">

```python
dualkmeter.get_firmware_version()
```

- 获取设备的固件版本。返回一个字符串，表示设备当前运行的固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_module_dualkmeter_get_internal_temp.svg">

```python
dualkmeter.get_kmeter_internal(1)
```

- 获取内部温度。可以选择单位为摄氏度(CELSIUS)或华氏度(FAHRENHEIT)，返回一个浮点数表示温度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_module_dualkmeter_get_isready.svg">

```python
dualkmeter.get_isready()
```

- 检查温度测量是否准备就绪。返回一个布尔值，表示温度测量是否可以进行

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_module_dualkmeter_get_str_internal_temp.svg">

```python
dualkmeter.get_kmeter_internal_string(1)
```

- 获取内部温度的字符串形式。可以选择单位为摄氏度(CELSIUS)或华氏度(FAHRENHEIT)，返回一个字符串表示温度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_module_dualkmeter_get_str_thermo_temp.svg">

```python
dualkmeter.get_kmeter_thermo_string(1)
```

- 获取热电偶温度的字符串形式。可以选择单位为摄氏度(CELSIUS)或华氏度(FAHRENHEIT)，返回一个字符串表示温度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_module_dualkmeter_get_thermo_temp.svg">

```python
dualkmeter.get_kmeter_thermo(1)
```

- 获取热电偶温度。可以选择单位为摄氏度(CELSIUS)或华氏度(FAHRENHEIT)，返回一个浮点数表示温度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_module_dualkmeter_init_i2c.svg">

```python
dualkmeter.init_i2c_address(0x11)
```

- 初始化设备的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_module_dualkmeter_set_channel.svg">

```python
 dualkmeter.rw_select_kmeter(0)
```

- 设置两路热电偶中的其中一路作为测量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dual_kmeter/uiflow_block_module_dualkmeter_set_channel2.svg">

```python
dualkmeter.rw_select_kmeter(0)
```

- 设置两路热电偶中的其中一路作为测量

