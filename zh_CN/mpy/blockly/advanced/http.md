
## HTTP

>使用HTTP模块中的API, 向服务器发送HTTP请求,获取数据。

```python
import urequests

# GET请求
req = urequests.request(
    method='GET', 
    url='http://api.m5stack.com/v1',
    headers={'Content-Type':'text/html'}
    )

# POST请求
req = urequests.request(
    method='POST', 
    url='http://api.m5stack.com/v1',
    json={'KEY':'VALUE'}, 
    headers={'Content-Type':'text/html'}
    )

# 获取响应体状态码
print(req.status_code)

# 获取响应体Reason-Phrase
print(req.reason)

# 获取原生响应体
print(req.content)

# 获取响应体字符串
print(req.text)

# 获取响应体JSON
print(req.json)

```
