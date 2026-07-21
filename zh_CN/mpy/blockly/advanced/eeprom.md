## EEPROM

>通过EEPROM持久化保存数据。

```python

import nvs

# 写入数据
nvs.write_str(KEY, VALUE)

# 读取数据
nvs.read_str(KEY)

```