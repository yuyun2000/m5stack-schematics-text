
# HTTP


## 案例程序


### GET method


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/http/uiflow_block_http_request_get_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *
import urequests
setScreenColor(0x222222)

try:
  req = urequests.request(method='GET', url='https://httpbin.org/get', headers={'Accept':'application/json'})
  print((str('Status: ') + str((req.status_code))))
  print(req.text)
  gc.collect()
  req.close()
except:
  print((str('Status: ') + str((req.status_code))))
  print('Fail')
```

### POST method

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/http/uiflow_block_http_request_post_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *
import urequests
from libs.json_py import *
setScreenColor(0x222222)

try:
  req = urequests.request(method='POST', url='https://httpbin.org/post',json={'Payload':(py_2_json({'msg':'hello'}))}, headers={'Content-Type':'application/json'})
  print((str('Status: ') + str((req.status_code))))
  print(req.text)
  gc.collect()
  req.close()
except:
  print((str('Status: ') + str((req.status_code))))
  print('Fail')

```


## 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/http/uiflow_block_http_request.svg"> 

```python
try:
  req = urequests.request(method='GET', url='https://httpbin.org/get', headers={'Accept':'application/json'})
  print((str('Status: ') + str((req.status_code))))
  print(req.text)
  gc.collect()
  req.close()
except:
  print((str('Status: ') + str((req.status_code))))
  print('Fail')

```

- 创建 HTTP 请求，方法支持 GET、POST、DELET、PUT、PATCH。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/http/uiflow_block_get_status_code.svg"> 

```python
print(req.status_code)
```

- 返回状态码


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/http/uiflow_block_get_data.svg"> 

```python
print(req.text)
```

- 获取返回的请求数据
