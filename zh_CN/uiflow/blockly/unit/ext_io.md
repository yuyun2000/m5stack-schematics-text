# [Unit EXT.IO](/zh_CN/unit/extio)

## 案例程序

> 每过 0.2 秒，改变引脚状态，使得 LED 灯亮灭

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
ext_io_0 = unit.get(unit.EXT_IO, unit.PORTA)

ext_io_0.setPortMode(ext_io_0.ALL_OUTPUT)
while True:
  ext_io_0.digitWrite(1,0)
  wait(0.2)
  ext_io_0.digitWrite(2,0)
  wait(0.2)
  ext_io_0.digitWrite(3,0)
  wait(0.2)
  ext_io_0.digitWrite(4,0)
  wait(0.2)
  ext_io_0.digitWrite(1,1)
  wait(0.2)
  ext_io_0.digitWrite(2,1)
  wait(0.2)
  ext_io_0.digitWrite(3,1)
  wait(0.2)
  ext_io_0.digitWrite(4,1)
  wait(0.2)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io/uiflow_block_extio_get_digiReadPort.svg">

```python
print(ext_io_0.digitReadPort())
```

- 读取全部引脚状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io/uiflow_block_extio_set_digiRead.svg">

```python
print(ext_io_0.digitRead(0))
```

- 读取指定引脚状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io/uiflow_block_extio_set_digiWrite.svg">

```python
ext_io_0.digitWrite(0,0)
```

- 单独控制引脚状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io/uiflow_block_extio_set_digiWritePort.svg">

```python
ext_io_0.digitWritePort(0x68)
```

- 控制引脚状态，每个引脚对应1位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io/uiflow_block_extio_set_pin.svg">

```python
ext_io_0.setPinMode(0, ext_io_0.INPUT)
```

- 单独设置输入或输出

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ext_io/uiflow_block_extio_set_port.svg">

```python
ext_io_0.setPortMode(ext_io_0.ALL_INPUT)
```

- 全部引脚设置为输入或输出模式

