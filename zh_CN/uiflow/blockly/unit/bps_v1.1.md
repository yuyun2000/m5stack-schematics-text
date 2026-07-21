# [Unit Mini BPS v1.1](/zh_CN/unit/ENV%20Pro%20Unit)

## Example

获取设备测量到的大气温度、湿度和压力

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bps_v1.1/uiflow_block_example.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
bpsv11_0 = unit.get(unit.BPS_QMP, unit.PORTA)

while True:
  print((str('temperature:') + str((bpsv11_0.temperature))))
  print((str('pressure:') + str((bpsv11_0.pressure))))
  wait_ms(2)
```

## API

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bps_v1.1/uiflow_block_bpsqmp_get_pressure.svg">

```python
print((str('pressure:') + str((bpsv11_0.pressure))))
```

- 获取压力值（Pa）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/bps_v1.1/uiflow_block_bpsqmp_get_temperature.svg">

```python
print((str('temperature:') + str((bpsv11_0.temperature))))
```

- 获取设备感应到的温度（℃）

