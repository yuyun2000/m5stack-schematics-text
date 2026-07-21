# Math

## 案例程序

简单的逻辑运算与变量赋值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_example.svg" >


## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_number.svg" >

```python
date = 10
```

- 添加常量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_arithmetic.svg" >

```python
date = 11 + 12
```

- 在式子的两边添加数据进行`加`/`减`/`乘`/`除`/`求余`/`幂运算`

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_arithmetic_arr.svg" >

```python
date = 13 + 4 - 8 % 2 - 7
```

- 对两个或多个数据进行`加`/`减`/`乘`/`除`/`求余`/`幂运算`

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_bit_operation.svg" >

```python
date = 5 & 6
```

- 位运算

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_constant.svg" >

```python
date = math.pi
```

- 赋值常量 π

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_modulo.svg" >

```python
date = 9 % 2
```

- 取模运算函数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_number_property.svg" >

```python
date = 8 % 2 == 0
```

- 检测数据。 `even`/`old`/`prime`/`whole`/`positive`/`negative`/`divisible by`

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_on_list.svg" >

```python
date = sum(list1)
```

- 数组运算函数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_random_float.svg" >

```python
date = random.random()
```

- 输出一个 0 ~ 1 之间的随机浮点数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_random_int.svg" >

```python
date = random.randint(0, 10)
```

- 输出一个一定范围内的随机数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_constrain.svg" >

```python
date = min(max(50, 1), 100)
```

- 限制数据范围

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_remap.svg" >

```python
date = math.remap(0, 0, 1023, 0, 255)
```

- 数值映射

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_round.svg" >

```python
date = round(2.4)
```

- 数据取整。round()

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_single.svg" >

```python
date = math.sqrt(0)
```

- 对数值进行数学函数处理。`sqrt()`/`log()`/`log10()`/`exp()`/`pow()`

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_trig.svg" >

```python
date = math.sin(10 / 180.0 * math.pi)
```

- 三角函数。`sin()`/`cos()`/`tan()`/`asin()`/`acos()`/`atan()`

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_convent_int.svg" >

```python
date = int('8')
```

- 将数据类型转换为`int`类型

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_convent_float.svg" >

```python
date = float('0.8')
```

- 将右边的数据类型转换为`float`类型

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_clear_bit.svg" >

```python
date = ((10 >> 0) & 0x01)
```

- 清除数据中的某一位数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_get_bit.svg" >

```python
date = (10 | (0x01 << 0))
```

- 获取数据中的某一位数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_set_bit.svg" >

```python
date = (10 & (~ (0x01 << 0)))
```

- 修改数据中的某一位数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_int_from_bytes.svg" >

```python
date = int.from_bytes(10, 'big')
```

- 翻转给定数值的最低位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/generic/math/uiflow_block_math_reverse_bit.svg" >

```python
date = (10 ^ (0x01 << 0))
```

- 将字节序列转换为整数
