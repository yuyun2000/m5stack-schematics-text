# [Unit VMeter](/zh_CN/unit/vmeter)

## 案例程序

测量电压

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/vmeter/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
VMeter_0 = unit.get(unit.VMETER, unit.PORTA)

while True:
  print((str('Voltage: ') + str(((str((VMeter_0.voltage())) + str(' mV'))))))
  wait(0.3)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/vmeter/uiflow_block_vmeter_raw.svg">

```python
print((str('raw:') + str((VMeter_0.raw()))))
```

- 获取测量电压数据原始值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/vmeter/uiflow_block_vmeter_set_gain2.svg">

```python
VMeter_0.setGain(VMeter_0.PGA_256)
```

- 设置最大输出电压

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/vmeter/uiflow_block_vmeter_set_mode.svg">

```python
VMeter_0.setMode(VMeter_0.MODE_CONTINUOUS)
```

- 设置输出模式
  - continuous
  - singleshot

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/vmeter/uiflow_block_vmeter_set_rate.svg">

```python
VMeter_0.setRate(VMeter_0.RATE_8)
```

- 设置每秒获取 8 个样本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/vmeter/uiflow_block_vmeter_voltage.svg">

```python
print((str('V:') + str((VMeter_0.voltage()))))
```

- 获取电压（V）

