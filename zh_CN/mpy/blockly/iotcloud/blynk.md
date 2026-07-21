## Blynk

>连接Blynk服务,实现通过手机App进行控制,与数据采集。

```python
from IoTcloud import blynk

# 断开连接
blynk1.disconnect()

# 发送邮件
blynk1.email('', '', '')

# 发送通知
blynk1.tweet('')

# 发送通知
blynk1.notify('')

# 配置组件属性参数
blynk1.set_property(0, '', '')

# 同步虚拟引脚状态
blynk1.virtual_sync(0)

# 初始化连接
blynk1 = blynk.Blynk(token='xxxxxxxxxxxxxxxxxxxxxxxxxx')

# 响应callback
def blynk_read_v3(v_pin,value):
  print(value)
  # 响应数据到指定VPIN
  blynk1.virtual_write(v_pin, "Hello!")

# 绑定虚拟引脚响应callback
blynk1.handle_event('read v3', blynk_read_v3)

while True:
  blynk1.run()

```