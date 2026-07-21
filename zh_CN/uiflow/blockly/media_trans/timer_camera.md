# Timer Camera

\#> 功能说明 | Timer Camera 在烧录了定时拍摄固件的后将按指定间隔拍摄图像并上传至服务器。其他设备在 UiFlow 中可以通过使用 Timer Camera 功能获取最新一帧图像并显示到屏幕上， 通过配置与设备一致的 token, 来获取对应设备的图像内容。

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/timer_camera/uiflow_block_timercam_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
from MediaTrans.TimerCam import TimerCam

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

cam = TimerCam('08d1f96ae2f0bc54b4998407c937e99d', 0, 0, 320, 240)
cam.show()
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/timer_camera/uiflow_block_timercam_init.svg">

```python
from MediaTrans.TimerCam import TimerCam
cam = TimerCam('08d1f96ae2f0bc54b4998407c937e99d', 0, 0, 320, 240)
```

- 初始化 TimerCAM 图像显示服务， 并传入设备 Token

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/timer_camera/uiflow_block_timercam_show.svg">

```python
cam.show()
```

- 启用图像显示

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/timer_camera/uiflow_block_timercam_hide.svg">

```python
cam.hide()
```

- 图像隐藏

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/media_trans/timer_camera/uiflow_block_timercam_delete.svg">

```python
cam.delete()
```

- 释放 TimerCAM 图像显示服务
