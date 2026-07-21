# Bytearray

bytearray 是 Python 中一个内置的可变序列类型，用于处理字节数据。它类似于 bytes 类型，但不同之处在于 bytearray 是可变的，而 bytes 是不可变的。bytearray 在处理二进制数据时非常有用，尤其是在需要对数据进行修改的情况下。它结合了列表的可变性和字节字符串的高效存储，是一个灵活且强大的工具。

## 案例程序

创建 bytearray, 并对其内部的元素增加，删除， 字符串 decode 操作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/bytearray/uiflow_block_bytearray_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

bytes2 = None

bytes2 = bytearray(5)
bytes2[0] = 104
bytes2[1] = 101
bytes2[2] = 108
bytes2[3] = 108
bytes2[4] = 111
bytes2.append(33)
print(bytes2.decode(bytes2))
print(bytes2[5])

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/bytearray/uiflow_block_variables_set.svg">

```python
bytes2 = bytearray(5)
```

- 创建指定长度 bytearray

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/bytearray/uiflow_block_bytearray_setIndex.svg">

```python
bytes2[0] = 104
```

- bytearray 指定索引赋值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/bytearray/uiflow_block_bytearray_append.svg">

```python
bytes2.append(33)
```

- 添加一个字节到 bytearray 的末尾。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/bytearray/uiflow_block_bytearray_decode.svg">

```python
print(bytes2.decode('utf-8'))
```

- bytearray 字符串解码
