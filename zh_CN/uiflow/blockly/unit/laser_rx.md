# [Unit Laser RX](/zh_CN/unit/laser-rx)

## 案例程序

> 获取设备接收的激光数据

<img class="blockly_svg" src="example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
laser_rx_0 = unit.get(unit.LASERRX, unit.PORTB)
laser_tx_0 = unit.get(unit.LASERTX, unit.PORTB)

while True:
  print(laser_rx_0.value())
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/laser_rx/uiflow_block_laserrx_get_value.svg">

```python
print((str('value：') + str((laser_rx_0.value()))))
```

- 获取 Unit Laser RX 接收的数据

