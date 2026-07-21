# Repeat

## 案例程序

循环函数使用

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/loops/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *

date = None
list2 = None
i = None
j = None

date = 10
list2 = [5, 6, 7]
for count in range(10):
  date = date + 1
while date < 25:
  date = date * 2
for i in list2:
  date = date + i
for j in range(0, 6, 2):
  date = date + 1
  if j == 3:
    break
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/loops/uiflow_block_controls_repeat.svg">

```python
for count in range(10):
  date = date + 1
```

- 自定义循环运行 do 的内容一定次数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/loops/uiflow_block_controls_forEach.svg">

```python
list2 = [5, 6, 7]
for i in list2:
  date = date + i
```

- 将一个数组的内容顺序迭代到变量 `i` 上，并且每迭代一次，运行 do 的内容一次

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/loops/uiflow_block_controls_whileUntil.svg">

```python
while date < 25:
  date = date * 2
```

- 循环判断，执行一系列的操作，直到条件不再满足为止

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/loops/uiflow_block_controls_for.svg">

```python
for j in range(0, 6, 2):
  date = date + 1
  if j == 3:
    break
```

- 从 `a` 开始增加到 `b` ,每次增加的数为 `c` ,并将每一次增加后的结果，迭代到变量 `i` 上，每迭代一次，运行 do 的内容一次

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/loops/uiflow_block_controls_flow_statements.svg">

```python
break
```

