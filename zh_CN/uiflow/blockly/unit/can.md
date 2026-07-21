# [Unit CAN](/zh_CN/unit/can)

## 案例程序

> 点击按钮发送 CAN 通信网络数据，并实时接收 CAN 通信网络数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x5c0000)
can_0 = unit.get(unit.CAN, unit.PORTC)

def buttonB_wasPressed():
  # global params
  can_0.send([10, 20, 30], 0X710)
  pass
btnB.wasPressed(buttonB_wasPressed)

can_0.can_init(0, extframe=True, mode=can_0.NORMAL, baudrate=can_0.BAUDRATE_250K, tx_io=17, rx_io=16, auto_restart=False)
label3.setText(str(can_0.state()))
while True:
  if can_0.any():
    print((str('message:') + str(can_0.recv())))
    print((str('ID:') + str(can_0.remote_id())))
  wait_ms(25)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_deinit.svg">

```python
can_0.deinit()
```

- 关闭 CAN 总线

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_init.svg">

```python
can_0.can_init(0, extframe=True, mode=can_0.NORMAL, baudrate=can_0.BAUDRATE_250K, tx_io=17, rx_io=16, auto_restart=False)
```

- 在给定的总线上构造一个 CAN 对象
  - mode：NORMAL、NO_ACKNOWLEDGE LISTEN_ONLY
  - tx: 用于传输数据的 pin
  - rx: 用于接收数据的 pin
  - baudrate:波特率
  - extframe:扩展帧

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_any.svg">

```python
print(can_0.any())
```

- 是否有消息在 FIFQ 上等待

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_clearfilter.svg">

```python
can_0.clear_filter()
```

- 清除数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_clear_rx_queue.svg">

```python
can_0.clear_rx_queue()
```

- 重置接收队列(RX Queue)中的所有待发送消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_clear_tx_queue.svg">

```python
can_0.clear_tx_queue()
```

- 重置发送队列(TX Queue)中的所有待发送消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_get_remoteid.svg">

```python
print(can_0.remote_id())
```

- 获取 Remote ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_recv.svg">

```python
print(can_0.recv())
```

- 获取接收数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_restart.svg">

```python
can_0.restart()
```

- 强制软件重启 CAN 控制器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_send.svg">

```python
can_0.send('uiflow2', 0)
```

- 发送数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_set_filter.svg">

```python
can_0.set_filter(0, can_0.FILTER_RAW_SINGLE, 'uiflow2')
```

- 发送数据
  - bank:number
  - mode:filter raw single/filter raw dual/filter address
  - Message:string

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/can/uiflow_block_unit_can_state.svg">

```python
print(can_0.state())
```

- 返回控制器的状态
