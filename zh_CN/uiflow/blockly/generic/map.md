# Map

## 案例程序

map 函数是一种在多种编程语言中普遍存在的内置函数或方法，它主要用于对可迭代对象，以下是如何使用 map 函数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Map/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *

date = None

date = {'a':1,'b':2,'c':'3'}
print('a' in date.keys())
print(date['b'])
date['d'] = '4'
date['a'] = '11'
date.pop('b')
date.clear()
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Map/uiflow_block_set_map_key.svg">

```python
date['a'] = '11'
```

- 在字典中设置键值对

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Map/uiflow_block_get_map_in.svg">

```python
print('a' in date.keys())
```

- 返回是否存在键

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Map/uiflow_block_add_map_key.svg">

```python
date['d'] = '4'
```

- 在字典中添加键值对

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Map/uiflow_block_delete_map_key.svg">

```python
date.pop('b')
```

- 删除指定的键

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Map/uiflow_block_get_map_key.svg">

```python
print(date['b'])
```

- 返回键的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Map/uiflow_block_map_clear.svg">

```python
date.clear()
```

- 清空字典

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Map/uiflow_block_map_on_loop.svg">

```python
date = {'a':1,'b':2,'c':'3'}
```

- 建立键值对
