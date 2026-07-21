# [Module HMI](/zh_CN/module/HMI%20Module)

## 案例程序

打印 HMI Module 的拨轮旋转编码器的编码值、增加的编码值、按键的状态值以及固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/hmi/uiflow_block_hmi_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

setScreenColor(0x222222)

hmi = module.get(module.HMI)

hmi.init_i2c_address(0x41)
while True:
  print((str('counter value：') + str((hmi.get_counter_value()))))
  print((str('increment value：') + str((hmi.get_increment_value()))))
  print((str('button status：') + str((hmi.get_button_status(0)))))
  print((str('Firmware version：') + str((hmi.get_device_status(0xFE)))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/hmi/uiflow_block_module_hmi_get_button_status.svg">

```python
hmi.get_button_status(0)
```

- 获取指定按钮的状态。在下拉菜单中，有三个选项可供选择：根据选择的按钮，图块将返回相应按钮的当前状态，例如按下或未按下
  - 0: 获取按钮1的状态。
  - 1: 获取按钮2的状态。
  - 2: 获取按钮3的状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/hmi/uiflow_block_module_hmi_get_counter.svg">

```python
hmi.get_counter_value()
```

- 获取计数器的当前值。返回一个整数值，表示计数器的累计计数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/hmi/uiflow_block_module_hmi_get_device_status.svg">

```python
hmi.get_device_status(0xFE)
```

- 获取设备的固件版本。返回一个字符串，表示设备当前运行的固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/hmi/uiflow_block_module_hmi_get_increment.svg">

```python
hmi.get_increment_value()
```

- 获取增量值。返回一个整数值，表示编码器的增量变化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/hmi/uiflow_block_module_hmi_init.svg">

```python
hmi.init_i2c_address(0x41)
```

- 初始化设备的 I2C 地址，这个地址用于 I2C 总线上的通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/hmi/uiflow_block_module_hmi_reset_counter.svg">

```python
hmi.reset_counter_value()
```

- 重置计数器的值。将计数器的当前值清零

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/hmi/uiflow_block_module_hmi_set_counter.svg">

```python
hmi.set_counter_value(1000)
```

- 设置计数器的值。可以将计数器的值设置为指定的整数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/hmi/uiflow_block_module_hmi_set_i2c_address.svg">

```python
hmi.set_i2c_address(0x41)
```

- 设置设备的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/hmi/uiflow_block_module_hmi_set_led.svg">

```python
hmi.set_LED(0, 1)
```

- 设置 LED 1/2的状态。可以选择设置为 ON(打开)或 OFF(关闭)来控制 LED 的状态。这允许你控制不同 LED 的开启和关闭状态
  - LED: 可以选择控制的 LED 编号，选项有1和2。
  - state: 可以选择 LED 的状态，选和项有 ON(打开)OFF(关闭)。


