## Tencent

>连接Tencent IoT云服务平台。

```python

from IoTcloud.Tencent import Tencent

# 初始化连接
tencent = Tencent(
	product_id='XXXXXXXXXXX', 
	device_name='XXXXXXX', 
	username='XXXXXXXXXXXXXXXXXX;12010126;B335D;1702277766',
	password='e822dc0027a1b363f9ed1a23fb77860c0b707d7d;hmacsha1',
	port=1883,
	keepalive=30
)

# 上传数据
tencent.publish_property_msg(temperature=temp,humidity=humid)


# 下行数据回调
def tencent_fun(property_data):
  print(property_data)

# 订阅平台下发消息
tencent.subscribe_property_msg(tencent_fun)


```