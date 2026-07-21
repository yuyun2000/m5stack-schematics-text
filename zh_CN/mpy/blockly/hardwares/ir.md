## IR

### IR NEC Mode

>该API仅适用于集成IR发射器的主控设备(eg: StickC/C Plus/ATOM LITE/MATRIX)。

```python
from m5stack import *

#发送数据
#ir.tx(addr, data)
ir.tx(111, 23)

```

### IR Unit

>其他主控若需要添加IR收发功能可通过拓展外设[IR Unit](/zh_CN/unit/ir)实现,并通过以下API使用。

```python

import unit

ir0 = unit.get(unit.IR_NEC, unit.PORTA)

data = None
addr = None

#接收Callback
def ir_nec_rx_cb(_data, _addr, _ctrl):
  global data, addr
  data = _data
  addr = _addr
  print(data)
  print(addr)

#设置接收Callback
ir0.rx_cb(ir_nec_rx_cb)

#发送数据
#ir.tx(addr, data)
ir.tx(111, 23)

```
