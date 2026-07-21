# [Module COMX Zigbee](/zh_CN/module/comx_zigbee)

## 案例程序

以下案例演示由 Coordinator 和 End device 组成网络实现数据发送和接收。

### Coordinator


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_coordinator_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from comx.zigbee import Zigbee
import time

setScreenColor(0x222222)
zigbee = Zigbee(17, 16)
zigbee.set_param_module(1, 0x1617, 20, 1, 0x2345, 6, 1, '')
while True:
  zigbee.send_payload('Hello!')
  print((str('Send:') + str('Hello!')))
  wait(1)
  wait_ms(2)
```

### End device

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_end_device_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from comx.zigbee import Zigbee

setScreenColor(0x222222)

zigbee = Zigbee(17, 16)
zigbee.set_param_module(3, 0x1617, 20, 1, 0x2345, 6, 1, '')
while True:
  if zigbee.check_payload():
    print((str('Received:') + str((zigbee.recv_payload()))))
  wait_ms(2)
```

## 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_init.svg">

```python
from comx.zigbee import Zigbee
zigbee = Zigbee(17, 16)
```

- 初始化模组接口

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_set_module.svg">

```python
zigbee.set_param_module(3, 0x1617, 20, 1, 0x2345, 6, 1, '')
```

- 初始化模组参数：
  - Role:
    - 1:Coordinator
    - 2:Router
    - 3:End Device
  - PAN：0x0001-0xFF00
  - USER ADDRESS: 0x0001-0xFF00
- 相关参数介绍请参考使用手册：
  - [Zigbee_Module_Guide](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/Zigbee_CC2630/Zigbee_Module_Guide.pdf)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_set_reboot.svg">

```python
zigbee.reboot_module()
```

- 重启模组。(更改模组配置后， 执行重启进行保存)


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_check_payload.svg">

```python
zigbee.check_payload()
```

- 读取当前数据缓存长度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_recv_payload.svg">

```python
zigbee.recv_payload()
```

- 读取数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_send_payload.svg">

```python
zigbee.send_payload('Hello!')
```

- 发送数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_set_core_baudrate.svg">

```python
zigbee.core_baudrate(38400)
```

- 设置主控侧波特率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_get_param.svg">

```python
zigbee.get_param_module(index)
```

- 读取模组配置参数：
  - index:
    - 0:ROLE
    - 1:PAN ID
    - 2:CHANNEL
    - 3:MODE
    - 4:USER ADDR
    - 5:BAUDRATE
    - 6:ANTENNA
    - MAC
    - SHORT ADDR
    - PASSWORD


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_zigbee/uiflow_block_com_zigbee_get_version.svg">

```python
zigbee.version_module()
```

- 读取模组版本

