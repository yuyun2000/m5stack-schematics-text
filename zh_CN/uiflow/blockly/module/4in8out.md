# [Module13.2 4In8Out](/zh_CN/module/4in8out)

## 案例程序

打印输出固件版本， 控制输出通道通断， 读取输入通道状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4in8out/uiflow_block_4in8out_demo4.svg">


```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x222222)
i = None
module_4in8out = module.get(module.MODULE_4IN8OUT)

module_4in8out.init_i2c_address(0x45)
print((str('Module Firmware Version:') + str((module_4in8out.read_status(0XFE)))))
while True:
  for i in range(8):
    module_4in8out.write_output_pin(i, 1)
  wait(1)
  for i in range(8):
    module_4in8out.write_output_pin(i, 0)
  wait(1)
  for i in range(4):
    print((str('CH') + str(((str(i) + str(((str(' Input :') + str((module_4in8out.read_input_pin(i)))))))))))
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4in8out/uiflow_block_module_4in8out_init.svg">

```python
module_4in8out.init_i2c_address(0x45)
```

- 初始化设备的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4in8out/uiflow_block_module_4in8out_read_pin.svg">

```python
module_4in8out.read_input_pin(0)
```

- 获取输入通道的状态或数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4in8out/uiflow_block_module_4in8out_read_status.svg">

```python
module_4in8out.read_status(0XFE))
```

- 获取设备的状态信息，选择获取固件版本(FW_VERSION)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4in8out/uiflow_block_module_4in8out_set_address.svg">

```python
module_4in8out.set_i2c_address(0x45)
```

- 设置设备的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/4in8out/uiflow_block_module_4in8out_write_pin.svg">

```python
module_4in8out.write_output_pin(0, 1)
```

- 控制输出通道的状态。设置通道0的输出状态，可以选择“ON”(开启)或“OFF”(关闭)。用于控制连接到该通道的设备或电路，例如打开或关闭一个继电器或 LED 灯

