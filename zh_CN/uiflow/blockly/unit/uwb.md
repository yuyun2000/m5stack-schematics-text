# [Unit UWB](/zh_CN/unit/uwb)

## 案例程序

> Anchor 模式，用于固定作为锚点

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_example01.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
uwb_0 = unit.get(unit.UWB, unit.PORTC)

uwb_0.init_uwb_mode(0)
uwb_0.set_mode(0)
while True:
  if uwb_0.check_device:
    print((str('distance') + str((uwb_0.device_id))))
  wait_ms(2)
```

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_example02.svg">

Tag 模式，移动点，获取定位

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
uwb_0 = unit.get(unit.UWB, unit.PORTC)

uwb_0.init_uwb_mode()
uwb_0.set_mode()
while True:
  if uwb_0.check_device:
    print((str('distance') + str((uwb_0.get_distance_measure[0]))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_init.svg">

```python
uwb_0.init_uwb_mode()
```

- 初始化 Unit，设置运行模式
  - tag:标签模式
  - Anchor:锚模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_uart_init.svg">

```python
uwb_0.uart_port_id(1)
```

- 设置部件 ID 编号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_check_device.svg">

```python
print(uwb_0.check_device)
```

- 检查设备是否可用

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_continuous_value_output.svg">

```python
uwb_0.continuous_output_value(0)
```

- 连续值输出输出
  - Enable
  - Disable

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_get_device_id.svg">

```python
print(uwb_0.device_id)
```

- 获取设备 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_get_distance_measure.svg">

```python
print(uwb_0.get_distance_measure[0])
```

- 获取到锚点的距离

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_get_version.svg">

```python
print(uwb_0.get_version())
```

- 获取当前固件版本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_set_anchor.svg">

```python
uwb_0.set_mode(0)
```

- 设置锚模式 ID 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_set_interval.svg">

```python
uwb_0.set_range_interval(5)
```

- 设置获取数据间隔次数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_set_tag.svg">

```python
uwb_0.set_mode()
```

- 设置标签模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/uwb/uiflow_block_unit_uwb_update_value_loop.svg">

```python
uwb_0.update_new_value_loop()
```

- 更新距离值

