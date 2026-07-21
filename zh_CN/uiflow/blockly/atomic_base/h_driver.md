# [Atomic HDriver Base](/zh_CN/atom/Atomic%20H-Driver%20Base)

## 案例程序

实现电机的周期性正反转控制，并实时监控电压和故障状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/h_driver/uiflow_block_hdriver_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.HDriver import HDriver
import time

hdriver = HDriver()
print((str('Input Voltage: ') + str((hdriver.get_voltage()))))
while True:
  print((str('Motor Fault Status: ') + str((hdriver.get_status()))))
  hdriver.set_speed(100)
  wait(1)
  hdriver.set_speed(0)
  wait(1)
  hdriver.set_speed(-100)
  wait(1)
  hdriver.set_speed(0)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/h_driver/uiflow_block_hdriver_init.svg">

```python
from base.HDriver import HDriver
hdriver = HDriver()
```

- 初始化 Atomic H-Driver

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/h_driver/uiflow_block_hdriver_get_status.svg">

```python
hdriver.get_status()
```

- 获取当前工作状态：
  - 0: Fault
  - 1: OK

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/h_driver/uiflow_block_hdriver_get_voltage.svg">

```python
hdriver.get_voltage()
```

- 读取输入电压值(V)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/h_driver/uiflow_block_hdriver_set_speed.svg">

```python
hdriver.set_speed(100)
```

- 控制电机转速：
  - 输入范围：-100~+100, 0为停止

