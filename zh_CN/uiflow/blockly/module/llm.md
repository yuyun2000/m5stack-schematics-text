# [Module LLM](/zh_CN/module/Module-LLM)

## 案例程序

通过 TTS 单元实现文本转换语音播放

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x222222)

adding_number = None
tts_text = None

llm_1 = module.get(module.LLM)
llm_1.init(2, tx=17, rx=16)

label0 = M5TextBox(34, 12, "State:", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label1 = M5TextBox(28, 85, "TTS text:", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label2 = M5TextBox(34, 45, "~", lcd.FONT_DejaVu24, 0x16db23, rotate=0)
label3 = M5TextBox(34, 116, "~", lcd.FONT_DejaVu24, 0xfe0101, rotate=0)

# Describe this function...
def make_tts_text():
  global adding_number, tts_text
  adding_number = adding_number + 1
  tts_text = 'x plus x equals to y.'.replace('x', str(adding_number))
  tts_text = tts_text.replace('y', str((adding_number + adding_number)))
  label3.setText(str(tts_text))
  llm_1.tts_inference(llm_1.get_latest_tts_work_id(), tts_text, 10000, 'tts_inference')

label1.setText('Wait ModuleLLM connection..')
while not (llm_1.check_connection()):
  wait(1)
label1.setText('Reset ModuleLLM..')
llm_1.sys_reset(True)
label1.setText('Setup Audio module..')
llm_1.audio_setup(cap_volume=0.5, play_volume=0.15, request_id='audio_setup')
label1.setText('Setup TTS module..')
llm_1.tts_setup(model='single_speaker_english_fast', input='tts.utf-8.stream', enoutput=True, enkws=True, request_id='tts_setup')
adding_number = 0
label1.setText('OK')
while True:
  make_tts_text()
  wait(0.5)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_init.svg">

```python
llm_1 = module.get(module.LLM)
llm_1.init(2, tx=17, rx=16)
```

- 初始化 Llm 模块并根据板型设置 UART 通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_asr_data_input_callback.svg">

```python
def llm_1_asr_data_input_event(data, finish, index):
  global asr_data, asr_is_finish, asr_index
  asr_data = data
  asr_is_finish = finish
  asr_index = index
  print('data input')
```

- 设置 ASR 数据输入 时的回调

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_asr_setup.svg">

```python
llm_1.asr_setup(model='2', enoutput=False, enkws=False, rule1=2.4, rule2=1.2, rule3=30, request_id='asr_setup')
```

- 设置 ASR 模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_tts_inference.svg">

```python
llm_1.tts_inference(llm_1.get_latest_tts_work_id(), '', 0, 'tts_inference')
```

- 使用 TTS 模块执行推理

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_tts_setup.svg">

```python
llm_1.tts_setup(model='single_speaker_english_fast', input='tts.utf-8.stream', enoutput=True, enkws=True, request_id='tts_setup')
```

- 设置 TTS 模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_audio_setup.svg">

```python
llm_1.audio_setup(cap_volume=0.5, play_volume=0.15, request_id='audio_setup')
```

- 设置 audio 模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_begin_voice_assistant.svg">

```python
print((str('begin voice assistant:') + str((llm_1.begin_voice_assistant('HI JIMMY', 'You are a helpful assistant.')))))
```

- 启动语音助手

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_data_input_callback.svg">

```python
def llm_1_llm_data_input_event(data, finish, index):
  global llm_data, llm_is_finish, llm_index
  llm_data = data
  llm_is_finish = finish
  llm_index = index
  print('llm data')
```

- 设置输入 LLM 数据时的回调

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_inference.svg">

```python
llm_1.llm_inference(llm_1.get_latest_llm_work_id(), 'Can I ask you a question?', 'llm_inference')
```

- 使用 LLM 模块执行推理

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_keyword_detected_callback.svg">

```python
llm_1.update()
print((str('begin voice assistant:') + str((llm_1.begin_voice_assistant('HI JIMMY', 'You are a helpful assistant.')))))
```

- 设置检测到 wake-up 关键字时的回调

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_kws_setup.svg">

```python
llm_1.kws_setup(kws='HI JIMMY', model='', enoutput=True, request_id='kws_setup')
```

- 设置 KWS 模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_setup.svg">

```python
llm_1.llm_setup(prompt='You are a helpful assistant.', model='2', enoutput=True, enkws=True, max_token_len=127, request_id='llm_setup')
```

- 设置 LLM 模块
  - prompt (str):提示文本
  - model (str):模型名称
  - response_format (str):响应格式
  - input (str):输入格式
  - enoutput (bool):启用输出
  - enkws (bool):启用关键字识别
  - max_token_len (int):最大令牌长度
  - request_id (str):请求 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_check_connection.svg">

```python
print((str('connection:') + str((llm_1.check_connection()))))
```

- 检查模块连接是否正常工作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_get_latest_asr_work_id.svg">

```python
print((str('latest asr work id:') + str((llm_1.get_latest_asr_work_id()))))
```

- 获取最新的 ASR 模块工作 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_get_latest_audio_work_id.svg">

```python
print((str('latest audio work id:') + str((llm_1.get_latest_audio_work_id()))))
```

- 获取最新的音频模块工作 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_get_latest_error_code.svg">

```python
print((str('err code:') + str((llm_1.get_latest_error_code()))))
```

- 获取最新的模块 LLM 响应错误代码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_get_latest_kws_work_id.svg">

```python
print((str('latest kws work id:') + str((llm_1.get_latest_kws_work_id()))))
```

- 获取最新的 KWS 模块工作 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_get_latest_llm_work_id.svg">

```python
print((str('latest llm work id:') + str((llm_1.get_latest_llm_work_id()))))
```

- 获取最新的 LLM 模块工作 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_get_latest_tts_work_id.svg">

```python
print((str('latest tts work id:') + str((llm_1.get_latest_tts_work_id()))))
```

- 获取最新的 TTS 模块工作 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_get_response_msg_list02.svg">

```python
llm_1.clear_response_msg_list()
```

- 获取相应数据列表

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_sys_ping.svg">

```python
llm_1.sys_ping()
```

- 向系统发送 ping 并获取响应代码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_tick.svg">

```python
llm_1.update()
```

- 更新模块 LLM 接收响应消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_sys_reboot.svg">

```python
llm_1.sys_reboot()
```

- 重新启动系统

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_sys_reset.svg">

```python
llm_1.sys_reset(True)
```

- 重置系统

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/llm/uiflow_block_module_llm_clear_response_msg_list.svg">

```python
print((str('response:') + str((llm_1.get_response_msg_list()))))
```

- 获取模块的响应消息列表
