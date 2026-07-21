# List

## 案例程序

数组处理与数组函数使用

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *

list01 = None
list02 = None

def first_index(my_list, elem):
  try: index = my_list.index(elem) + 1
  except: index = 0
  return index

list01 = []
list02 = [1, 2, 3, [4, 5, 6]]
print(len(list02))
print(not len(list01))
print(list02[1])
print(first_index(list02, 1))
print(list02[2 : 4])
print(list(reversed(list02)))

list02[-1] = 9
print(list02)

list01 = [2] * 2
print(list01)

print('1,2,3,4'.split(','))
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_create_empty.svg">

```python
list01 = []
```

- 自定义一个空数组

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_create_with.svg">

```python
list02 = [1, 2, 3, [4, 5, 6]]
```

- 建立一个数组，使用元素重复一定次数进行填充

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_getIndex.svg">

```python
print(list02[1])
```

- 获取数组某个索引元素值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_getSublist.svg">

```python
print(list02[2 : 4])
```

- 从数组中截获元素作为新数组

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_indexOf.svg">

```python
print(first_index(list02, 1))
```

- 数组索引，索引正序或倒序的某个指定元素

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_isEmpty.svg">

```python
print(not len(list01))
```

- 判断一个数组是否为空，成立时式子为 True,否则为 False

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_length.svg">

```python
print(len(list02))
```

- 测量数组的长度(即数组中元素的个数)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_repeat.svg">

```python
list01 = [2] * 2
print(list01)
```

- 建立一个数组，使用元素重复一定次数进行填充

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_reverse.svg">

```python
print(list(reversed(list02)))
```

- 数组倒序排列

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_setIndex.svg">

```python
list02[-1] = 9
print(list02)
```

- 在数组中设置某个索引为指定值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Lists/uiflow_block_lists_split.svg">

```python
print('1,2,3,4'.split(','))
```

- 从文本建立数组，使用分隔符
