# [Unit MIC](/zh_CN/unit/mic)

## Example

读取音频数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/microphone/uiflow_mic_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
mic_0 = unit.get(unit.MICROPHONE_AD, unit.PORTB)

while True:
  print((str('analog value:') + str((mic_0.analogValue()))))
  print((str('digital value:') + str((mic_0.digitalValue()))))
  wait_ms(2)
```

## API

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/microphone/uiflow_block_unit_mic_get_analog.svg">

```python
print((str('analog value:') + str((mic_0.analogValue()))))
```

- 获取模拟信号输出数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/microphone/uiflow_block_unit_mic_get_digital.svg">

```python
print((str('digital value:') + str((mic_0.digitalValue()))))
```

- 获取数字信号输出数据

