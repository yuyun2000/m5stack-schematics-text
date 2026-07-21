# Text

## 案例程序

字符串函数使用方法


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import binascii

string = None
date = None

string = 'hello world'
print(string.upper())
print('hello')
print(string[0])
print(string.count('o'))
print(not len(string))
print(len(string))
print(string.replace('e', 'w'))
print('   m5stack   '.strip())
print('hello world'.strip('h'))
print(str(2500))
print((str('Hi! ') + str(string)))
date = binascii.hexlify('hello').decode()
print(date.encode())
print((binascii.unhexlify(date)).decode())
print("%.0f"%float(date))

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text.svg">

```python
string = 'hello workd'
```

- 建立文本内容

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_add.svg">

```python
print(string.upper())
```

- 文本合并

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_changeCase.svg">

```python
print(string.upper())
```

- 将文本内容进行大写或小写转换

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_charAt.svg">

```python
print(string[0])
```

- 截取指定的文本内容

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_count.svg">

```python
print(string.count('o'))
```

- 返回文本中指定字符出现的次数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_isEmpty.svg">

```python
print(not len(string))
```

- 返回文本是否为空

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_length.svg">

```python
print(len(string))
```

- 返回文本长度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_convent_str.svg">

```python
print(str(2500))
```

- 将其他格式转为字符串

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_decode_str.svg">

```python
print((binascii.unhexlify(date)).decode())
```

- 将字符串解码为指定格式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_encode_str.svg">

```python
print(date.encode())
```

- 将字符串转换回 bytes 对象

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_m5_text_bytestr_to_hexstr.svg">

```python
date = binascii.hexlify('hello').decode()
```

- 将字符串转码为 byte

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_m5_text_hexstr_to_bytestr.svg">

```python
print((binascii.unhexlify(date)).decode())
```

- 将字符串转码为 String

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_math_split.svg">

```python
print("%.0f"%float(date))
```

- 字符串格式化操作，用于将浮点数(float)格式化为一个不包含小数部分的字符串

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_print.svg">

```python
print('')
```

- 打印文本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_replace.svg">

```python
print(string.replace('e', 'w'))
```

- 将文本内容进行替换

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_trim.svg">

```python
print('   m5stack   '.strip())
```

- 删除字符串两边空格

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_trim_string.svg">

```python
print('hello world'.strip('h'))
```

- 指定删除字符串两边的字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_unescaped.svg">

```python
print('hello')
```

- 字符串没有被转义，包含了所有原始字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_prompt.svg">

- 终端提示符。提示输入带有消息的文本

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Text/uiflow_block_text_prompt_ext.svg">

- 终端提示符。自定义提示输入带有消息的文本
