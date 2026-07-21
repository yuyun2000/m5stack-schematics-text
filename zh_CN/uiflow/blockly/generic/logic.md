# Logic

## 案例程序

逻辑处理函数使用

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *

date = None
boolean = None
oldData1 = None

date = 5
if date < 10:
  date = date + 1

if date != 10:
  date = date + 1
else:
  date = date - 1

boolean = date <= 6
date = 0 if date <= 6 else 2

try :
  boolean = True and False
  pass
except:
  boolean = not date == 0

if date==6:
  date = date + 1
elif date==7:
  date = date + 2
else:
  date = date - 1

if date != oldData1:
  oldData1 = date
  date = date + 1
else:
  date = date - 1
  pass

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_controls_if.svg">

```python
if date < 10:
  date = date + 1
```

- 判断条件是否成立，当成立时执行 Do 右侧程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_controls_ifelse.svg">

```python
if date != 10:
  date = date + 1
else:
  date = date - 1
```

- 判断条件是否成立，当成立时执行 Do 右侧程序，不成立时执行 else 右侧程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_logic_boolean.svg">

- 布尔值可以代替判断条件的式子，设置为 true 为成立，设置 false 为不成立

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_logic_ternary.svg">

```python
date = 0 if date <= 6 else 2
```

- 三元运算符，表达式可以看作是一个简短的 if-else 语句的替代

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_logic_compare.svg">

```python
boolean = date <= 6
```

- 逻辑关系式在 if 判断中经常用作判断条件(等于，不等于，大于，小于，大于等于，小于等于),运算两侧的数据关系是否正确，最后得出 true 或 false 两个值，用作 if 判断

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_logic_negate.svg">

```python
boolean = not date == 0
```

- 将一个式子的逻辑结果取反，即 notTrue=False,notFalse=True

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_logic_null.svg">

- 布尔值运算赋值为 `null`

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_logic_switch.svg">

```python
if date==6:
  date = date + 1
elif date==7:
  date = date + 2
else:
  date = date - 1
```

- switch-case 逻辑语法

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_logic_try_except.svg">

```python
try :
  boolean = True and False
  pass
except:
  boolean = not date == 0
```

- try-except 异常处理。当 try 块中的代码引发异常时，程序的控制流会立即跳转到与该异常类型匹配的 except 块(如果有的话)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_logic_operation.svg">

```python
boolean = True and False
```

- `and` 当左右两个逻辑关系式 `有一个成立` 时，逻辑运算的结果为 True,否则为 False
- `or` 当左右两个逻辑关系式 都成立 时，逻辑运算的结果才为 True,否则为 False

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Logic/uiflow_block_logic_when.svg">

```python
if date != oldData1:
  oldData1 = date
  date = date + 1
else:
  date = date - 1
  pass
```

- 指定数据发生变化时，触发的函数
