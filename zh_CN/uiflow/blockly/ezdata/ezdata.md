# EzData 1.0

## 功能说明

EzData 1.0 是 M5Stack 提供的一个 IoT 云端数据储存服务，不同的设备之间可以通过`唯一 token`，向储存队列中插入或提取数据，实现数据共享。

<img src="https://static-cdn.m5stack.com/resource/docs/static/image/iotservice/ezdata/ezdata_01.webp" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_example.svg" width="70%">

## 案例程序

```python
from m5stack import *
from m5ui import *
from uiflow import *
from flow import ezdata
import wifiCfg

i = None

wifiCfg.autoConnect(lcdShow=False)

while True:
  ezdata.setData('6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_topic', 'Hello EzData')
  print(ezdata.getData('6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_topic'))
  for i in range(11):
    ezdata.addToList('6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_list', i)
  print(ezdata.getData('6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_list', 0, 50))
  ezdata.removeData('6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_topic')
  print(ezdata.getCurrentISODateTime())
  wait_ms(2)
```

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_set_key_with_token.svg" width="70%">

```python
ezdata.setData('6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_topic', 'Hello EzData')
```

- 保存数据至指定 topic 队列首位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_get_key_with_token.svg" width="70%">

```python
print(ezdata.getData('6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_topic'))
```

- 从指定的 topic 队列首位获取一个数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_add_value_with_token.svg" width="70%">

```python
ezdata.addToList('6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_list', i)
```

- 保存数据至指定数据列表首位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_get_list_with_token.svg" width="70%">

```python
print(ezdata.getData('6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_list', 0, 50))
```

- 从指定的数据列表中获取一组数据，使用列表储存的优点是，支持指定数据索引偏移且可一次获取多个数据，返回值为一个 list
- list: 列表名称字符串
- offset: 相对于数据列表首位的偏移
- count: 读取数据个数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_remove_key_with_token.svg" width="70%">

```python
ezdata.removeData('6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_topic')
```

- 删除 topic 或 list，并清空队列数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_get_iso_date.svg" width="70%">

```python
print(ezdata.getCurrentISODateTime())
```

- 获取当前 ISO Data 时间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_async_set_value.svg" width="70%">

```python
ezdata.setDataAsync(ezdata_set_NdmNNcb, ezdata_set_fail_NdmNNcb, '6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_topic', 'Hello EzData')
```

- 异步操作。保存数据至指定 topic 队列首位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_async_set_list_value.svg" width="70%">

```python
ezdata.addToListAsync(ezdata_set_iQCwDcb, ezdata_set_fail_iQCwDcb, '6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_list', i)
```

- 异步操作。保存数据至指定数据列表首位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_async_get_value.svg" width="70%">

```python
ezdata.getDataAsync(ezdata_get_iRBYXcb, ezdata_get_fail_iRBYXcb, '6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_topic')
```

- 异步操作。从指定的 topic 队列首位获取一个数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_async_get_list_value.svg" width="70%">

```python
ezdata.getDataAsync(ezdata_get_rfWJMcb, ezdata_get_fail_rfWJMcb, '6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', 'my_list', 0, 50)
```

- 异步操作
- 从指定的数据列表中获取一组数据，使用列表储存的优点是，支持指定数据索引偏移且可一次获取多个数据，返回值为一个 list
- list: 列表名称字符串
- offset: 相对于数据列表首位的偏移
- count: 读取数据个数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_async_remove.svg" width="70%">

```python
ezdata.removeDataAsync(ezdata_remove_KcMAbcb, ezdata_remove_fail_KcMAbcb, '6ijRMmiFRdO2tVfFIbNpy6PN1sRvFmsy', '')
```

- 异步操作。删除 topic 或 list，并清空队列数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/ezdate/uiflow_block_ezdata_async_get_iso_date.svg" width="70%">

```python
ezdata.getCurrentISODateTimeAsync(ezdata_get_ESdHGcb, ezdata_get_fail_ESdHGcb)
```

- 异步操作。获取当前 ISO Data 时间

#>注意事项：<br/>1. 以上所有操作都依赖于`唯一 token`，该 token 在同一浏览器环境下是固定的， 使用前请复制 token。<br/>2. 半年时间内没有进行数据操作，则清空该 token 对应的数据队列。<br/>3. 数据将按照插入时间，降序排序(最后插入的数据，在列表的首位)，数据会累积保存。


