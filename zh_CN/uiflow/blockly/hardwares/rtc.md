# RTC

## 案例程序

设置不同时区，并显示实时时钟到串口(年月日时分秒星期)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_demo1.svg"> 


```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time

rtc.settime('ntp', host='cn.pool.ntp.org', tzone=8)
while True:
  print(rtc.datetime()[0])
  print(rtc.datetime()[1])
  print(rtc.datetime()[2])
  print(rtc.datetime()[3])
  print(rtc.datetime()[4])
  print(rtc.datetime()[5])
  print(rtc.datetime()[6])
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_set_time_ntp_host_and_timezone.svg"> 

```python
rtc.settime('ntp', host='cn.pool.ntp.org', tzone=8)
```

- 通过 NTP(网络时间协议)主机服务器来设置时间，并根据时区进行调整。你可以选择以下 NTP 服务器：

- **cn.pool.ntp.org**：中国区 NTP 服务器
- **jp.pool.ntp.org**：日本区 NTP 服务器
- **sg.pool.ntp.org**：新加坡区 NTP 服务器
- **tw.pool.ntp.org**：台湾区 NTP 服务器
- **hk.pool.ntp.org**：香港区 NTP 服务器
- **us.pool.ntp.org**：美国区 NTP 服务器
- **de.pool.ntp.org**：德国区 NTP 服务器

#> 通过与 NTP 服务器 cn.pool.ntp.org 同步来设置时间，并根据时区偏移+8小时进行调整
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_year.svg"> 

```python
str(rtc.datetime()[0])
```
 
- 获取当前日期时间，并使用索引 [0] 提取年份，然后将其转换为字符串格式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_month.svg"> 

```python
str(rtc.datetime()[1])
```

- 获取当前日期时间，并使用索引 [1] 提取月份，然后将其转换为字符串格式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_date.svg"> 

```python
str(rtc.datetime()[2])
```

- 获取当前日期时间，并使用索引 [2] 提取日期，然后将其转换为字符串格式


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_week.svg"> 

```python
str(rtc.datetime()[3])
```

- 获取当前日期时间，并使用索引 [3] 提取星期几，然后将其转换为字符串格式


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_hour.svg"> 

```python
str(rtc.datetime()[4)
```

- 获取当前日期时间，并使用索引 [4] 提取小时，然后将其转换为字符串格式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_minute.svg"> 

```python
str(rtc.datetime()[5)
```

- 获取当前日期时间，并使用索引 [5] 提取分钟，然后将其转换为字符串格式


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_second.svg"> 

```python
str(rtc.datetime()[6)
```

- 获取当前日期时间，并使用索引 [6] 提取秒钟，然后将其转换为字符串格式


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_set_time.svg"> 

```python
rtc.datetime((0, 1, 1, 0, 0, 0, 0, 0))
```

- 设置日期和时间，其中参数为 (年， 月， 日， 星期， 时， 分， 秒， 秒)。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_get_real_time.svg"> 

```python
str(rtc.datetime())
```

- 获取当前 RTC(实时时钟)时间，并将其转换为字符串格式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/rtc/uiflow_block_rtc_print_real_time.svg"> 

```python
str(rtc.printRTCtime())
```

- 返回当前 RTC 时间，然后将其转换为字符串格式