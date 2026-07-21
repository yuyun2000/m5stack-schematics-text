# variables

## 案例程序

创建变量

```python
from m5stack import *
from m5ui import *
from uiflow import *

date = None

from numbers import Number

date = 10
date = (date if isinstance(date, Number) else 0) + (0 + 1)
print(date)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/variables/uiflow_block_variables_set.svg">

```python
date = 10
```

- 为变量赋值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/variables/uiflow_block_math_change.svg">

```python
date = (date if isinstance(date, Number) else 0) + (0 + 1)
```

- 修改当前变量， 输入参数为修改的大小(如： +10, -10), 可以是表达式。若变量值不为 number 类型， 则将输入参数的结果赋值给当前变量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/variables/uiflow_block_variables_get.svg">

- 赋值
