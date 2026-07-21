# CAN

## 案例程序

使用 ESP32内部 CAN 控制器资源，实现 CAN 总线数据收发，注：使用前需要为设备接入[CAN UNIT](https://shop.m5stack.com/products/canbus-unitca-is3050g).

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from machine import CAN
import time

setScreenColor(0x222222)

frame = None

label0 = M5TextBox(16, 53, "Device State: ", lcd.FONT_Default, 0x00ff7c, rotate=0)
label1 = M5TextBox(126, 53, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label2 = M5TextBox(16, 97, "message: ", lcd.FONT_Default, 0x00ff7c, rotate=0)
label3 = M5TextBox(16, 132, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label4 = M5TextBox(16, 162, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label5 = M5TextBox(16, 192, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)

def buttonA_wasPressed():
  global frame
  can.send([0, 1, 2, 3, 4, 5, 6, 7], 0)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global frame
  can.clear_tx_queue()
  can.clear_rx_queue()
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global frame
  can.restart()
  pass
btnC.wasPressed(buttonC_wasPressed)


can = CAN(0, extframe=True, mode=CAN.NORMAL, baudrate=CAN.BAUDRATE_25K, tx_io=17, rx_io=16, auto_restart=False)
while True:
  label1.setText(str(can.state()))
  if can.any():
    frame = can.recv()
    label3.setText(str(frame[0]))
    label4.setText(str(frame[1]))
    label5.setText(str(frame[3]))
  wait_ms(30)
  wait_ms(2)

```

## 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_init.svg">

```python
from machine import CAN
can = CAN(0, extframe=True, mode=CAN.NORMAL, baudrate=CAN.BAUDRATE_25K, tx_io=17, rx_io=16, auto_restart=False)
```

- 初始化 CAN 总线， 配置是否为拓展帧模式，工作模式(常规模式， 回环模式等)以及波特率设置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_any.svg">

```python
can.any()
```

- 检查 FIFO 中是否有未读的数据


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_recv.svg">

```python
frame = can.recv()
```

- 接收数据


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_send.svg">

```python
can.send([0, 1, 2, 3, 4, 5, 6, 7], id)
```

- 发送一条数据，并指定数据帧的 ID, ID 长度为1个 byte, 传入的数据类型要求为`list`或是`tuple`, 数据帧的数据长度要求是`8个 byte`。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_set_filter.svg">

```python
can.setfilter(0, CAN.FILTER_RAW_SINGLE, [])
```

- 设置过滤组

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_state.svg">

```python
can.state()
```

- 获取 CAN 控制器状态


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_clear_rx_queue.svg">

```python
can.clear_rx_queue()
```

- 清除接收队列

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_clear_tx_queue.svg">

```python
can.clear_tx_queue()
```

- 清除发送队列


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_clearfilter.svg">

```python
can.clearfilter()
```

- 清除过滤组


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_restart.svg">

```python
can.restart()
```

- 重启 CAN 总线

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/can/uiflow_block_can_deinit.svg">

```python
can.deinit()
```

- 停止 CAN 总线

