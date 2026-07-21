# [Unit ASR](/zh_CN/unit/Unit%20ASR)

## 案例程序

发送 Hello 语音指令，执行打印程序（Print）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_example.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
asr_0 = unit.get(unit.ASR, unit.PORTC)

def asr_0_hello_event(args):
  # global params
  print('I am Fine')

asr_0.init(2)
asr_0.add_command_word(0x32, 'hello', asr_0_hello_event)
print((str('raw message:') + str((asr_0.get_current_raw_message()))))
while True:
  asr_0.handler()
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_init.svg">

```python
asr_0.init(2)
```

- 初始化 Unit

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_event.svg">

```python
def asr_0_hello_event(args):
  # global params
  pass
```

- 当 Unit ASR 识别命令字时触发的回调函数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_get_command_handler.svg">

```python
print((str('current command handler state:') + str((asr_0.get_command_handler()))))
```

- 检查当前命令是否有关联的处理程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_get_command_list.svg">

```python
print((str('current command list:') + str((asr_0.get_command_list()))))
```

- 获取所有命令及其关联处理程序的列表

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_get_current_command_num.svg">

```python
print((str('current command num:') + str((asr_0.get_current_command_num()))))
```

- 获取当前命令编号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_get_current_command_word.svg">

```python
print((str('current command word:') + str((asr_0.get_current_command_word()))))
```

- 获取当前命令编号对应的命令字

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_add_command_word.svg">

```python
asr_0.add_command_word(0x32, 'hello', _)
```

- 注册自定义命令和处理程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_get_current_raw_message.svg">

```python
print((str('current raw message:') + str((asr_0.get_current_raw_message()))))
```

- 获取以十六进制格式接收的原始消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_get_received_status.svg">

```python
print((str('receive message:') + str((asr_0.get_received_status()))))
```

- 获取消息接收状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_remove_command_word.svg">

```python
asr_0.remove_command_word('hello')
```

- 按单词从命令列表中删除命令单词

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_search_command_num.svg">

```python
print((str('command word:') + str((asr_0.search_command_num('')))))
```

- 搜索与命令字关联的命令编号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_search_command_word.svg">

```python
print((str('command word(hex):') + str((asr_0.search_command_word(0x32)))))
```

- 搜索与命令编号关联的命令字

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_send_message.svg">

```python
asr_0.send_message(0xFE)
```

- 通过 UART 发送命令

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/asr/uiflow_block_unit_asr_update_in_loop.svg">

```python
asr_0.handler()
```

- 更新函数