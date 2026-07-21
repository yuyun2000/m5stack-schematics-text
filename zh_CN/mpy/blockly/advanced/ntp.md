## NTP

>通过NTP服务器获取当前时间信息。

```python

import ntptime


# 设置NTP服务器
# eg:
# ntp = ntptime.client(host='jp.pool.ntp.org', timezone=8)
# ntp = ntptime.client(host='sg.pool.ntp.org', timezone=8)
# ntp = ntptime.client(host='tw.pool.ntp.org', timezone=8)
# ntp = ntptime.client(host='hk.pool.ntp.org', timezone=8)
# ntp = ntptime.client(host='tw.pool.ntp.org', timezone=8)
# ntp = ntptime.client(host='hk.pool.ntp.org', timezone=8)
# ntp = ntptime.client(host='us.pool.ntp.org', timezone=8)
# ntp = ntptime.client(host='de.pool.ntp.org', timezone=8)

ntp = ntptime.client(host='cn.pool.ntp.org', timezone=8)

# 获取时间戳
ntp.getTimestamp()

# 格式化日期
ntp.formatDate('-')

# 格式化时间
ntp.formatTime('-')

# 格式化日期&时间
ntp.formatDatetime('-', ':')

ntp.year()
ntp.month()
ntp.day()
ntp.hour()
ntp.minute()
ntp.second()
ntp.weekday()

```
