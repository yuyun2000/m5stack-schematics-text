# [Unit Mini TVOC/eCO2](/zh_CN/unit/tvoc)

## 案例程序

测量空气质量参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tvoc_eco2/uiflow_tvoc_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
tvoc_0 = unit.get(unit.TVOC, unit.PORTA)

while True:
  print((str('IAP baseline: ') + str((tvoc_0.get_iaq_baseline()))))
  print((str('TVOC now') + str((tvoc_0.TVOC))))
  print((str('eCO2 now') + str((tvoc_0.eCO2))))
  print((str('H2 now') + str((tvoc_0.H2))))
  print((str('Ethanol now') + str((tvoc_0.Ethanol))))
  wait(0.5)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tvoc_eco2/uiflow_block_tvoc_baseline_tvoc.svg">

```python
print(tvoc_0.baseline_TVOC)
```

- 获取 TVOC 基准值功能块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tvoc_eco2/uiflow_block_tvoc_get_baseline_eco2.svg">

```python
print((str('line eco2:') + str((tvoc_0.baseline_eCO2))))
```

- 获取 eCO₂ 基准值功能块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tvoc_eco2/uiflow_block_tvoc_get_eco2.svg">

```python
print((str('eco2:') + str((tvoc_0.eCO2))))
```

- 获取 eCO₂ 值功能块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tvoc_eco2/uiflow_block_tvoc_get_ethanol.svg">

```python
print(tvoc_0.Ethanol)
```

- 获取乙醇（浓度）值功能块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tvoc_eco2/uiflow_block_tvoc_get_h2.svg">

```python
print((str('H2:') + str((tvoc_0.H2))))
```

- 获取氢气（H₂ 浓度）值功能块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tvoc_eco2/uiflow_block_tvoc_get_iaq_baseline.svg">

```python
print((str('line:') + str((tvoc_0.get_iaq_baseline()))))
```

- 获取室内空气质量（IAQ）基准值功能块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/tvoc_eco2/uiflow_block_tvoc_get_tvoc.svg">

```python
print(tvoc_0.TVOC)
```

- 获取 TVOC 值功能块

