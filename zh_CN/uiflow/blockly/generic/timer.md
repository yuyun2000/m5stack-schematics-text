# Timer

## 案例程序

程序延时与打印运行时间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/timer/uiflow_block_timer_wait_example.svg"> 

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time

setScreenColor(0x222222)

print(time.ticks_ms())
wait_ms(100)
print(time.ticks_ms())
wait(1)
print(time.ticks_ms())
```

## 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/timer/uiflow_block_timer_wait_ms.svg"> 

```python
wait_ms(100)
```

- 程序延时/ms


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/timer/uiflow_block_timer_wait_sec.svg"> 

```python
wait(1)
```

- 程序延时/s


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/timer/uiflow_block_timer_get_ticks_ms.svg"> 

```python
print(time.ticks_ms())
```

- 获取当前运行时间/ms

