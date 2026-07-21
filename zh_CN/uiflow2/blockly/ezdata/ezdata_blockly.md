# EzData 2.0

EzData 2.0 是 M5Stack 提供的一个 IoT 云端数据储存服务，不同的设备之间可以通过`唯一 token`，向储存队列中插入或提取数据，实现数据共享。

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/uiflow2_block_exampley.svg" width="70%">

```python
import os, sys, io
import M5
from M5 import *
from ezdata import *

ez_0 = None
ez_item = None

def setup():
  global ez_0
  M5.begin()
  Widgets.fillScreen(0x222222)
  ez_0 = EzData('b1112ac5e9644f26af381c15c4a0e1da', 'age')
  ez_0.set("res/img/default.png", is_file=True)

def loop():
  global ez_0
  M5.update()
  ez_0.set(18, is_file=False)
  print(ez_0.get())
  ez_0.set([1, 2, 3], is_file=False)
  print(ez_0.history())
  ez_0.delete()
  for ez_item in get_key_list(device_token=_).iterms():
    print(ez_item[0])
    print(ez_item[1])

if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
```

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/init.svg" width="70%">

```python
ez_0 = EzData('b1112ac5e9644f26af381c15c4a0e1da', 'age')
```

- 初始化 EzData，选填已在线设备 token 与对应需要访问的 key

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/init1.svg" width="70%">

```python
ez_1 = EzData('b1112ac5e9644f26af381c15c4a0e1da', 'hello_M5')
```

- 初始化 EzData，自定义填写设备 token 与对应需要访问的 key

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/init_data_token.svg" width="70%">

```python
ez_4 = EzData('b1112ac5e9644f26af381c15c4a0e1da', '', public=True)
```

- 初始化 EzData，自定义填写设备 token

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/init_dataset_key.svg" width="70%">

```python
ez_3 = EzData('795efd86c2a6478eb9c3bb414376bb6b', 'age')
```

- 初始化 EzData dataset 对象，选填设备 token 与对应需要访问的 key

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/set_value.svg" width="70%">

```python
ez_0.set(18, is_file=False)
```

- 修改指定 key 对应的 value

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/set_value1.svg" width="70%">

```python
ez_0.set({'hello_M5':'hello M5'}, is_file=False)
```

- 保存数据 Value 至指定 key 对应的值中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/set_value2.svg" width="70%">

```python
ez_0.set([1, 2, 3], is_file=False)
```

- 保存数组 list 至指定 key 对应的值中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/set_value3.svg" width="70%">

```python
ez_0.set({'hello_M5':'hello M5'}, is_file=False)
```

- 创建数组 map，保存数组 map 至指定 key 对应的 value 中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/set_value_file.svg" width="70%">

```python
ez_0.set("res/img/default.png", is_file=True)
```

- 自定义图片资源文件，上传至指定 key 对应的 value 中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/set_value_file1.svg" width="70%">

```python
ez_0.set("res/img/default.png", is_file=True)
```

- 选择需要保存的图片资源文件上传至指定 key 对应的 value 中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/get_file.svg" width="70%">

```python
ez_0.get_file('helloM5.png')
```

- 更新图片资源文件到指定 key 对应的值 value 中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/get_update_time.svg" width="70%">

```python
print(ez_0.get_update_time())
```

- 获取数据最近一次更新时间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/get_value.svg" width="70%">

```python
print(ez_0.get())
```

- 获取指定的 key 对应的数据 Value 值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/has_new_data.svg" width="70%">

```python
print(ez_0.has_new_data())
```

- 获取指定的 key 对应的数据的最新的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/history.svg" width="70%">

```python
print(ez_0.history())
```

- 获取指定的 key 对应的数据的历史记录

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/for_each.svg" width="70%">

```python
for ez_item in get_key_list(device_token=_).iterms():
```

- 遍历 EzData 对象所有 list

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/for_each_get_key.svg" width="70%">

```python
print(ez_item[0])
```

- 获取遍历 EzData list 对应的数据 list 的所有 key

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/for_each_get_value.svg" width="70%">

```python
print(ez_item[1])
```

- 获取指定的 key 对应的数据 list 的所有数据 value

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/blockly/ezdata2/delete.svg" width="70%">

```python
ez_0.delete()
```

- 删除当前设备 EzData 对应的 key 对象
