# Watch Dog Timer

## 案例程序

设置 Watch Dog Timer, 当程序出现异常没有按照预期时间进行 feed 操作时， 将复位设备。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/wdt/uiflow_block_wdt_example.svg"> 

```python
from m5stack import *
from m5ui import *
from uiflow import *
from machine import WDT
import time


setScreenColor(0x222222)

wdt = WDT(timeout=2000)
while True:
  wait(3000)
  wdt.feed()
  wait_ms(2)
```

#### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/wdt/uiflow_block_wdt_init.svg"> 

```python
wdt = WDT(timeout=2000)
```

- 初始化 Watch Dog Timer，并设置超时时间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/wdt/uiflow_block_wdt_feed.svg"> 


```python
wdt.feed()
```

- 在超时时间内重复执行 Feed 的操作进行刷新， 若发生超时为及时 feed 情况将复位设备。

