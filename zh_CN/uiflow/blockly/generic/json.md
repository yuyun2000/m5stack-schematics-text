# Json

## 案例程序

JSON 是一种轻量级的数据交换格式，以下是 JSON 函数使用方法

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_example.svg"> 

```python
from m5stack import *
from m5ui import *
from uiflow import *
from libs.json_py import *
import json

date = None

date = py_2_json({'author':'M5Stack','people':100,'device':'CoreS3','number':5})
print(json.dumps(date))
print(get_json_keys(date))
print(get_json_key(date, 'number'))
print(get_json_values(date))
print(get_json_keys_len(date))
set_json_elements(date, 'people', 101)
set_json_elements(date, 'devicetow', 'core2')
delete_json_elements(date, 'number')
print(json.dumps(date))
print(json.loads('{"string":"stack","number":100}'))
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_dumps_json.svg"> 

```python
print(json.dumps(date))
```

- 将 Python 对象(如列表或字典)转换(序列化)为 JSON 格式的字符串。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_json_add_key_value.svg"> 

```python
set_json_elements(date, 'devicetow', 'core2')
```

- 添加 JSON 对象键值对

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_json_create.svg"> 

```python
date = py_2_json({'author':'M5Stack','people':100,'device':'CoreS3','number':5})
```

- 创建一个 JSON 对象，通过 Key Value 的方式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_json_del_key.svg"> 

```python
delete_json_elements(date, 'number')
```

- 通过 key 值删除对应的 JSON 对象的键值对

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_json_get_key_value.svg"> 

```python
print(get_json_key(date, 'number'))
```

- 获取 JSON 对象的指定 key 的 valus 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_json_get_keys.svg"> 

```python
print(get_json_keys(date))
```

- 获取 JSON 对象的所有 key，返回一个 list

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_json_get_keys_len.svg"> 

```python
print(get_json_keys_len(date))
```

- 获取 JSON 对象的 length

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_json_get_values.svg"> 

```python
print(get_json_values(date))
```

- 获取 JSON 对象的所有 valie，返回一个 list

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_json_set_key_value.svg"> 

```python
set_json_elements(date, 'people', 101)
```

- 设置 JSON 对象的对应 key 的 valie

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/JSON/uiflow_block_variables_set.svg"> 

```python
print(json.loads('{"string":"stack","number":100}'))
```

- 解析字符串中有效的 JSON 对象
