# [Unit Mini CAN](/zh_CN/unit/Unit-Mini%20CAN)

## 案例程序

发送并发送 CAN 数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_minican_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
mini_can_0 = unit.get(unit.MINI_CAN, unit.PORTC)

mini_can_0.can_init(0, extframe=True, mode=mini_can_0.NORMAL, baudrate=mini_can_0.BAUDRATE_250K, tx_io=17, rx_io=16, auto_restart=False)
while True:
  mini_can_0.send('Hello', 0)
  if mini_can_0.any():
    print((str('message:') + str(mini_can_0.recv())))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_deinit.svg">

```python
mini_can_0.deinit()
```

- 释放资源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_init.svg">

```python
mini_can_0.can_init(0, extframe=True, mode=mini_can_0.NORMAL, baudrate=mini_can_0.BAUDRATE_250K, tx_io=17, rx_io=16, auto_restart=False)
```

- 初始设备配置
   - bus
   - extframe
   - mode
   - baudrate 
   - TX
   - RX

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_any.svg">

```python
print((str('Boolean:') + str(mini_can_0.any())))
```

- 检查是否有数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_clearfilter.svg">

```python
mini_can_0.clear_filter()
```
- 清除过滤器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_clear_rx_queue.svg">

```python
mini_can_0.clear_rx_queue()
```

- 清空接收队列

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_clear_tx_queue.svg">

```python
mini_can_0.clear_tx_queue()
```

- 清空发送队列

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_get_remoteid.svg">

```python
print((str('id:') + str(mini_can_0.remote_id())))
```

- 获取远程ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_recv.svg">

```python
print((str('message:') + str(mini_can_0.recv())))
```

- 从总线读取报文

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_restart.svg">

```python
mini_can_0.restart()
```

- 重新初始化设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_send.svg">

```python
mini_can_0.send([], 0)
```

- 向总线写入报文

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_set_filter.svg">

```python
mini_can_0.set_filter(0, mini_can_0.FILTER_RAW_SINGLE, [])
```

- 配置报文过滤规则

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mini_can/uiflow_block_unit_minican_state.svg">

```python
print((str('state:') + str(mini_can_0.state())))
```

- 获取设备当前状态

