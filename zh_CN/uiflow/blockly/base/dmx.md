# [Base DMX](/zh_CN/base/DMX_Base)

## 案例程序

### Master

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dmx/uiflow_block_module_dmx_master_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x222222)
dmx = module.get(module.DMX512)

dmx.dmx_init(13, 35, 12, 1)
while True:
  dmx.write_dmx_data(1, 0)
  wait(1)
  dmx.write_dmx_data(2, 0)
  wait(1)
  dmx.write_dmx_data(3, 0)
  wait(1)
  dmx.write_dmx_data(1, 255)
  wait(1)
  dmx.write_dmx_data(2, 255)
  wait(1)
  dmx.write_dmx_data(3, 255)
  wait(1)
  wait_ms(2)
```

### Slave

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dmx/uiflow_block_module_dmx_slave_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

setScreenColor(0x222222)

dmx = module.get(module.DMX512)

dmx.dmx_init(13, 35, 12, 2)
while True:
  print((str('ch1:') + str((dmx.read_dmx_data(1)))))
  print((str('ch2:') + str((dmx.read_dmx_data(2)))))
  print((str('ch3:') + str((dmx.read_dmx_data(3)))))
  dmx.clear_dmx_buffer()
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dmx/uiflow_block_module_dmx_init.svg">

```python
import module
dmx = module.get(module.DMX512)
dmx.dmx_init(tx, rx, en, mode)
```

- 初始化 DMX 引脚配置，并指定工作模式(master/slave)：
  - mode:
    - master:1
    - slave:2

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dmx/uiflow_block_module_dmx_read_data.svg">

```python
dmx.read_dmx_data(ch)
```

- slave 模式下， 接收指定 channel 数据：
  - ch:1-512

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dmx/uiflow_block_module_dmx_write_data.svg">

```python
dmx.write_dmx_data(ch, 100)
```

- master 模式下， 写入数据到指定 channel:
  - ch:1-512

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dmx/uiflow_block_module_dmx_clear_buffer.svg">

```python
dmx.clear_dmx_buffer()
```

- 清空 DMX 数据 buffer

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dmx/uiflow_block_module_dmx_deinit.svg">

```python
dmx.delete_port()
```

- 逆初始化 DMX,释放端口资源

