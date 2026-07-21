# [Unit DDS](/zh_CN/unit/dds)

## 案例程序

DDS 功能测试

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dds/uiflow_dds_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
dds_0 = unit.get(unit.DDS, unit.PORTA)

mode = None
freq = None
phase = None

label0 = M5TextBox(39, 41, "MODE:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label1 = M5TextBox(97, 41, "Text", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
title0 = M5Title(title="UNIT DDS", x=120, fgcolor=0xFFFFFF, bgcolor=0x830269)
label2 = M5TextBox(39, 93, "FREQ:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label3 = M5TextBox(97, 93, "Text", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label4 = M5TextBox(39, 142, "PHASE:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label5 = M5TextBox(104, 142, "Text", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label6 = M5TextBox(44, 219, "MODE", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label7 = M5TextBox(139, 219, "FREQ", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label8 = M5TextBox(224, 219, "PHASE", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)

from numbers import Number

def buttonA_wasPressed():
  global mode, freq, phase
  mode = (mode if isinstance(mode, Number) else 0) + 1
  if mode >= 5:
    mode = 1
  if mode == 1:
    label1.setText('SINE')
    dds_0.set_mode(dds_0.SINE)
  elif mode == 2:
    dds_0.set_mode(dds_0.TRIANGLE)
    label1.setText('TRIANGLE')
  elif mode == 3:
    dds_0.set_mode(dds_0.SQUARE)
    label1.setText('SQUARE')
  elif mode == 4:
    dds_0.set_mode(dds_0.SAWTOOTH)
    label1.setText('SAWTOOTH')
  dds_0.set_freq_phase(0, freq, 0, phase)
  dds_0.output(0, 0)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global mode, freq, phase
  freq = (freq if isinstance(freq, Number) else 0) + 100
  label3.setText(str(freq))
  dds_0.set_freq_phase(0, freq, 0, phase)
  dds_0.output(0, 0)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global mode, freq, phase
  phase = (phase if isinstance(phase, Number) else 0) + 5
  if phase >= 360:
    phase = 0
  label5.setText(str(phase))
  dds_0.set_freq_phase(0, freq, 0, phase)
  dds_0.output(0, 0)
  pass
btnC.wasPressed(buttonC_wasPressed)

mode = 0
freq = 100
phase = 0
dds_0.set_mode(dds_0.DC)
dds_0.set_freq_phase(0, freq, 0, phase)
dds_0.output(0, 0)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dds/uiflow_block_dds_quick_output.svg">

```python
dds_0.quick_output(dds_0.SINE, 0, 0)
```

- 设备快速输出模式
  - SINE
    - sine:正弦波
    - freq:频率
    - phase:相位
  - TRIANGLE
  - SQUARE
  - SAWTOOTH
  - DC


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dds/uiflow_block_dds_reset.svg">

```python
dds_0.reset()
```

- 复位/重置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dds/uiflow_block_dds_set_control_sleep.svg">

```python
dds_0.set_sleep(1)
```

- 设置控制休眠
  - Disable MCLK
  - Disable DAC
  - Enable ALL

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dds/uiflow_block_dds_set_freq_phase.svg">

```python
dds_0.set_freq_phase(0, 0, 0, 0)
```

- 设置频率/相位

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dds/uiflow_block_dds_set_mode.svg">

```python
dds_0.set_mode(dds_0.SINE)
```

- 设置工作模式
  - SINE
  - TRIANGLE
  - SQUARE
  - SAWTOOTH
  - DC

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dds/uiflow_block_dds_set_output_freq_phase.svg">

```python
dds_0.output(0, 0)
```

- 设置输出频率/相位

