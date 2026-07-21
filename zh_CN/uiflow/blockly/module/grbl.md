# [Module13.2 GRBL](/zh_CN/module/grbl13.2)

## 案例程序

通过GRBL模块在距离模式下驱动三轴进行周期性往复运动

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x222222)
grbl = module.get(module.GRBL)

grbl.set_mode("distance")
while True:
  grbl.turn(10, 10, 10, 100)
  wait(5)
  grbl.turn((-10), (-10), (-10), 100)
  wait(5)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_set_mode.svg">

```python
grbl.set_mode("distance")
```

- 设置 GRBL 工作模式：
  - distance:距离控制模式
  - absolute:绝对位置控制模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_turn.svg">

```python
grbl.turn(10, 10, 10, speed)
```

- 在距离控制模式下， 控制步进电机移动指定距离

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_g_code.svg">

```python
grbl.g_code('')
```

- 发送 GRBL G-code 进行控制
  - 指令内容请参考[GRBL - Github](https://github.com/grbl/grbl/wiki)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_wait_idle.svg">

```python
grbl.wait_idle()
```

- 阻塞等待电机停止运行


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_in_lock.svg">

```python
grbl.in_lock()
```

- 判断电机是否处于锁定状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_lock_motor.svg">

```python
grbl.lock_motor()
```

- 电机运行结束后， 进行锁定

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_read_idle.svg">

```python
grbl.read_idle()
```

- 判断电机是否处于空闲状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_read_line.svg">

```python
grbl.read_line()
```

- 读取 GRBL 控制返回信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_unlock.svg">

```python
grbl.unlock()
```

- 解锁 limit 触发后的电机锁定状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_unlock_motor.svg">

```python
grbl.unlock_motor()
```

- 电机运行结束后， 不进行锁定

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/grbl/uiflow_block_grbl_read_clean.svg">

```python
grbl.read_clean()
```

- 清除 GRBL 返回数据信息

