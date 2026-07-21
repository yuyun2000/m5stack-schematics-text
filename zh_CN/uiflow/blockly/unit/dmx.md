# [Unit DMX](/zh_CN/unit/Unit-DMX)

## 案例程序

> 通过 DMX 协议控制设备的多个通道(最多 512 个通道)，发送指定的数值(如通道 0 至 255 分别为灯光颜色的 RGB 值)，从而调整设备的状态，通常用于舞台灯光控制或其他数字化设备的调节。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dmx/uiflow_block_unit_dmx_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
dmx_0 = unit.get(unit.DMX, unit.PORTA)

dmx_0.init_dmx(1, 1)
while True:
  dmx_0.write_dmx_value(1, 136)
  wait(1)
  dmx_0.write_dmx_value(512, 255)
  wait(1)
  dmx_0.clear_dmx_buffer()
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dmx/1_uiflow_block_unit_dmx_init.svg">

```python
dmx_0.init_dmx(1, 1)
```

- 初始化 DMX 模块 dmx_0，设置为 MASTER 模式，并指定使用 UART 1 进行通信。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dmx/2_uiflow_block_unit_dmx_deinit.svg">

```python
dmx_0.deinit()
```

- 释放 DMX 模块 dmx_0，即停止模块运行并释放相关资源。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dmx/3_uiflow_block_unit_dmx_write_value.svg">

```python
dmx_0.write_dmx_value(1, 0)
```

- 设置 DMX 通道 1 的输出值为 0，值的范围是 0 ~ 255。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dmx/4_uiflow_block_unit_dmx_clear_buffer.svg">

```python
dmx_0.clear_dmx_buffer()
```

- 清除所有 DMX 通道的值，将它们重置为默认值(通常为 0)。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dmx/5_uiflow_block_unit_dmx_read_value.svg">

```python
dmx_0.read_dmx_value(1)
```
- 获取 DMX 通道 1 的当前值，并通过 print 显示该值(以整数形式返回)。
