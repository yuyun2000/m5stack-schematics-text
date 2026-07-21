# [Unit IR](/zh_CN/unit/ir)

## 案例程序

接收 IR 数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ir/uiflow_block_example.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
ir_0 = unit.get(unit.IR_NEC, unit.PORTB)

addr = None
data = None

def ir_nec_rx_cb(_data, _addr, _ctrl):
  global addr, data
  data = _data
  addr = _addr
  print((str('addr:') + str(addr)))
  print((str('data:') + str(data)))

ir_0.rx_cb(ir_nec_rx_cb)

ir_0.txOn()
addr = 0
addr = 27
while True:
  print((str('state:') + str((ir_0.rxStatus()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ir/uiflow_block_unit_ir_nec_cb.svg">

```python
def ir_nec_rx_cb(_data, _addr, _ctrl):
  # global params
  data = _data
  addr = _addr

ir_0.rx_cb(ir_nec_rx_cb)
```

- 接收指定地址发送 IR 的数据，并触发函数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ir/uiflow_block_unit_ir_nec_tx.svg">

```python
ir_0.tx(0, 0)
```

- 将 IR 信号值发送到地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ir/uiflow_block_unit_ir_off.svg">

```python
ir_0.txOff()
```

- 开启数据发送

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ir/uiflow_block_unit_ir_on.svg">

```python
ir_0.txOn()
```

- 关闭数据发送

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/ir/uiflow_block_unit_ir_state.svg">

```python
print((str('state:') + str((ir_0.rxStatus()))))
```

- 获取当前设备状态

