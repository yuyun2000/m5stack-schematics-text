# DAC

## 案例程序

使用 dac0通道在25引脚输出波形

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/dac/uiflow_block_dac_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *
import machine
import time

setScreenColor(0x222222)

dac0 = machine.DAC(26)
while True:
  dac0.write(0)
  wait(1)
  dac0.write(255)
  wait(1)
  wait_ms(2)

```


#### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/dac/uiflow_block_dac_init.svg"> 

```python
dac0 = machine.DAC([pin])
```

- 设置转换通道

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/dac/uiflow_block_dac_write_value.svg"> 

```python
dac0.write(255)
```

- 写入 DAC 转换值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/dac/uiflow_block_dac_write_beep.svg"> 

```python
dac0.beep(1800, 200, 0)
```

- 配置输出驱动蜂鸣器频率，时间和振幅


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/dac/uiflow_block_dac_write_waveform.svg"> 

```python
dac0.waveform(1800, dac0.SINE, duration=200, scale=0, offset=0, invert=0)
```

- 设置输出波形频率振幅偏移量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/dac/uiflow_block_dac_write_waveform_stop.svg"> 

```python
dac0.stopwave()
```

- 停止输出

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/dac/uiflow_block_dac_set_freq.svg"> 

```python
dac0.freq(1800)
```

- 设置输出频率

