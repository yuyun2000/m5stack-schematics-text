# PWM

## 案例程序

初始化引脚的方向，并获取引脚的值打印在屏幕上

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pwm/uiflow_block_pwm_demo.svg"> 


```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import machine
import time


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

i = None

label0 = M5Label('label0', x=137, y=88, color=0x000, font=FONT_MONT_14, parent=None)

PWM0 = machine.PWM(26, freq=50, duty=3, timer=0)
while True:
  for i in range(13):
    PWM0.duty(i)
    wait_ms(1000)
    label0.set_text(str(i))
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pwm/uiflow_block_pwm.svg"> 

```python
machine.PWM(26, freq=10000, duty=50, timer=0)
```

- 设置产生 PWM 信号的引脚、频率、占空比、和计时器选择
  

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pwm/uiflow_block_pwm_freq.svg"> 

```python
PWM0.freq(1)
```
 
- 设置 PWM 产生频率

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pwm/uiflow_block_pwm_duty.svg"> 

```python
PWM0.duty(0)
```

- 设置 PWM 占空比

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pwm/uiflow_block_pwm_pause.svg"> 

```python
PWM0.pause()
```

- 暂停 PWM 信号产生


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pwm/uiflow_block_pwm_resume.svg"> 

```python
PWM0.resume() 
```

- 继续 pwm 信号的产生


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/pwm/uiflow_block_pwm_hold_us.svg"> 

```python
PWM0.hold_us(0)
```

- 保持住 PWM 信号几 us(毫秒)