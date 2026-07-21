## M5mqtt

>使用M5mqtt模块中的API, 连接mqtt服务器与订阅发布消息内容。

- 连接mqtt服务器

```python

from m5mqtt import M5mqtt

# 创建连接实例
m5mqtt = M5mqtt(
    client_id,
    server, 
    port=0, 
    user=None, 
    password=None, 
    keepalive=0,
    ssl=False, 
    ssl_params=None
)

# 开始连接
m5mqtt.start()

while True:


```

- 订阅与发布消息

```python

# 订阅消息
def callback(topic_data):
    print(topic_data)

m5mqtt.subscribe(topic, callback)


# 发布消息
m5mqtt.publish(topic, data)

```

- 其他配置

```python

# 配置客户端遗嘱消息
m5mqtt.set_last_will(topic, msg)

# 断开连接
m5mqtt.deinit()

```