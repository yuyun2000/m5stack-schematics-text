# Functions

## 案例程序

定义两个函数，传入参数进行简单运算

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Functions/uiflow_block_example.svg"> 

```python
from m5stack import *
from m5ui import *
from uiflow import *

x = None
y = None
result = None

# Describe this function...
def func(x, y):
  global result
  if x < y:
    print(x + y)
  else:
    print(x - y)

# Describe this function...
def mathfuc(y, x):
  global result
  if x < 0:
    return y - x
  return x + y

func(2, 3)
result = mathfuc(10, 5)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Functions/uiflow_block_procedures_defnoreturn.svg"> 

```python
def func(x, y):
  global result
  if x < y:
    print(x + y)
  else:
    print(x - y)
```

- 创建一个函数，可设置参数，函数`没有`返回值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Functions/uiflow_block_procedures_defreturn.svg"> 

```python
def mathfuc(y, x):
  global result
  return x + y
```

- 创建一个函数，可设置参数，函数`有`返回值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/Functions/uiflow_block_procedures_ifreturn.svg"> 

```python
if x < 0:
    return y - x
```

- 在函数中运行简单的 if 逻辑运算，结束该函数运算并返回一个值
