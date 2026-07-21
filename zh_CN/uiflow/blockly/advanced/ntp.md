# NTP

## 案例程序

通过网络服务器读取当前时间， 注： 当程序 download 离线运行时，需要在 NTP 初始化程序前，添加 WiFi 连接程序，使得设备连接网络。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_example.svg">


```python
from m5stack import *
from m5ui import *
from uiflow import *
import ntptime
import time

setScreenColor(0x222222)

ntp = ntptime.client(host='cn.pool.ntp.org', timezone=8)
while True:
  print(ntp.formatDatetime('-', ':'))
  print(ntp.getTimestamp())
  wait(1)
  wait_ms(2)
```


## 功能说明 


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_init_timezone.svg">

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_init_timezone_dropdown.svg">

```python
import ntptime
ntp = ntptime.client(host='cn.pool.ntp.org', timezone=8)
```

- 设置 NTP 服务器和时区， 并进行连接。
  - host:
    - `cn.pool.ntp.org`
    - `jp.pool.ntp.org`
    - `sg.pool.ntp.org`
    - `tw.pool.ntp.org`
    - `hk.pool.ntp.org`
    - `us.pool.ntp.org`
    - `de.pool.ntp.org`

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_date_format.svg">

```python
ntp.formatDate('-')
```

- 读取当前日期，并设置分隔符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_time_format.svg">

```python
ntp.formatTime(':')
```

- 读取当前时间，并设置分隔符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_date_time_format.svg">

```python
ntp.formatDatetime('-', ':')
```

- 读取当前日期和时间，并设置日期格式分隔符和时间格式分隔符。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_timestamp.svg">

```python
ntp.getTimestamp()
```

- 读取当前 Unix 时间戳

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_year.svg">

```python
ntp.year()
```

- 读取当前年

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_month.svg">

```python
ntp.month()
```

- 读取当前月

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_weekday.svg">

```python
ntp.weekday()
```

- 读取当前星期
- 返回值：
  - Sunday:0 
  - Monday:1
  - Tuesday:2
  - Wednesday:3
  - Thursday:4
  - Friday:5
  - Saturday:6


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_day.svg">

```python
ntp.day()
```

- 读取当前日


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_hour.svg">

```python
ntp.hour()
```

- 读取当前小时

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_minute.svg">

```python
ntp.minute()
```

- 读取当前分钟

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/ntp/uiflow_block_ntp_get_second.svg">

```python
ntp.second()
```

- 读取当前秒

