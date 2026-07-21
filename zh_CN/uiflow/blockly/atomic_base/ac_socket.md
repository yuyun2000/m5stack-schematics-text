# [Atom AC Socket](/zh_CN/atom/atom_socket)

## 案例程序

关闭设备

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x111111)
acsocket_0 = unit.get(unit.AC_SOCKET, unit.PORTA)

acsocket_0.set_value(0)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ac_socket/uiflow_block_unit_acsocket_set_value.svg">

```python
acsocket_0.set_value(0)
```

- 设置开启或关闭状态

