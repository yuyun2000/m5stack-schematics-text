# [Unit Synth](/zh_CN/unit/Unit-Synth)

## 案例程序

> 间隔 300ms 演奏音符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
synth_0 = unit.get(unit.SYNTH, unit.PORTB)

synth_0.set_channel_volume(0, 121)
synth_0.set_change_instrument(0, 0, 112)
while True:
  synth_0.set_note_on(0, 80, 23)
  synth_0.set_note_on(0, 57, 73)
  wait_ms(300)
  synth_0.set_note_on(0, 66, 101)
  synth_0.set_note_on(0, 60, 52)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_all_drums.svg">

```python
synth_0.set_all_drums()
```

- 发送 System Exclusive 消息，将通道上的所有鼓设置为默认值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_all_note_off.svg">

```python
synth_0.set_all_notes_off(0)
```

- 停止对指定通道发送 MIDI 消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_change_instrument.svg">

```python
synth_0.set_change_instrument(0, 0, 1)
```

- 更改指定通道上的节目(乐器)
  - bank – 程序更改的 音源选择器(bank0 GM：标准音源/bank127： MT-32音源)
  - channel – MIDI 通道 (0-15)
  - value – 程序编号 (0-127)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_channel_volume.svg">

```python
synth_0.set_channel_volume(0, 0)
```

- 设置指定通道的通道音量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_chorus.svg">

```python
synth_0.set_chorus(0, 0, 0, 0, 0)
```

- 在指定通道上配置合唱效果
  - channel – MIDI 通道 (0-15)
  - program – 合唱节目编号 (0-7)
  - level – 合唱级别 (0-127)
  - feedback – 合唱反馈量 (0-127)
  - chorusdelay – 合唱延迟量 (0-127)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_device_reset.svg">

```python
synth_0.midi_reset()
```

- 发送 MIDI 系统独占重置命令

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_envelope.svg">

```python
synth_0.set_envelope(0, 0, 0, 0)
```

- 为指定通道设置音阶调谐
  - channel – 要应用包络的 MIDI 通道 (0-15)
  - attack – 攻击时间 (0-127)
  - decay – 衰减时间 (0-127)
  - release – 发布时间 (0-127)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_eq.svg">

```python
synth_0.set_equalizer(0, 0, 0, 0, 0, 0, 0, 0, 0)
```

- 设置指定通道的均衡器电平和频率
  - channel – MIDI 通道 (0-15)
  - 低频段 – 低频段电平(-12dB 至 +12dB)
  - medlowband – 中低频段电平(-12dB 至 +12dB)
  - medhighband – 中高频段电平(-12dB 至 +12dB)
  - 高频段 – 高频段电平(-12dB 至 +12dB)
  - lowfreq – 低频段频率 (Hz)
  - medlowfreq – 中低频段频率 (Hz)
  - medhighfreq – 中高频段频率 (Hz)
  - highfreq – 高频段频率 (Hz)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_master_volume.svg">

```python
synth_0.set_master_volume(0)
```

- 使用标准系统独占消息设置主音量(0-127)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_mod_wheel.svg">

```python
synth_0.set_mod_wheel(0, 0, 0, 0, 0, 0, 0, 0)
```

- 设置影响指定通道上各种效果的调制轮参数
  - channel – 要应用调制的 MIDI 通道 (0-15)
  - pitch – 音高调制深度
  - tvtcutoff – 截止频率调制深度
  - amplitude – 幅度调制深度
  - rate – 调制率
  - pitchdepth – 音高调制的深度
  - tvfdepth – TVF 调制的深度
  - tvadepth – TVA(音压放大器)调制的深度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_note_off.svg">

```python
synth_0.set_note_off(0, 0)
```

- 向指定通道发送 MIDI Note Off 消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_note_on.svg">

```python
synth_0.set_note_on(0, 0, 0)
```

- 将 MIDI Note On 消息发送到指定通道

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_pan.svg">

```python
synth_0.set_pan(0, 0)
```

- 设置指定通道的声像位置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_pitch_bend.svg">

```python
synth_0.set_pitch_bend(0, 0)
```

- 向指定通道发送 MIDI 弯音消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_pitch_bend_range.svg">

```python
synth_0.set_pitch_bend_range(0, 0)
```

- 设置指定通道上的弯距范围
  - channel – MIDI 通道 (0-15)
  - value – 螺距弯曲值 (0-16383)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_reverb.svg">

```python
synth_0.set_reverb(0, 0, 0, 0)
```

- 在指定通道上配置混响效果
  - channel – MIDI 通道 (0-15)
  - program – 混响节目编号 (0-7)
  - level – 混响级别 (0-127)
  - delayfeedback：延迟反馈量(0-127)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_scale_tuning.svg">

```python
synth_0.set_scale_tuning(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
```

- 为指定通道设置音阶调谐
  - channel – 要应用音阶调谐的 MIDI 通道 (0-15)
  - v1~v12 – 音阶中每个音符的调音值 (0-127)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_tuning.svg">

```python
synth_0.set_tuning(0, 0, 0)
```

- 设置指定通道的调谐
  - channel – MIDI 通道 (0-15)
  - fine – 微调值(美分)
  - coarse – 粗调值(半音)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_tvf.svg">

```python
synth_0.set_tvf(0, 0, 0)
```

- 在指定通道上设置 TVF(音压滤波器)的参数
  - channel – 要应用滤波器的 MIDI 通道 (0-15)
  - cutoff – 滤波器截止频率 (0-127)
  - resonance – 滤波器谐振 (0-127)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/synth/uiflow_block_unit_synth_set_vibrate.svg">

```python
synth_0.set_vibrate(0, 0, 0, 0)
```

- 在指定通道上设置颤音效果参数
  - channel – 要对 (0-15) 应用颤音效果的 MIDI 通道
  - rate – 颤音率 (0-127)
  - depth – 颤音深度 (0-127)
  - delay – 颤音延迟 (0-127)
