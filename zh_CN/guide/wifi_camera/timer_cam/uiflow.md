# TimerCAM/Unit CAM - UiFlow

## 功能描述

使用设备通过 GROVE 接口连接 TimerCAM/Unit CAM，实现指令控制摄像头 UART 传输图像并在 M5CORE 的屏幕上预览，或是配置定时拍摄上传云端功能 (返回固定 HTTP API)。

## 驱动安装

\#> 将设备连接至 PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`, Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

\#>MacOS 用户注意事项 | 对于 MacOS 用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## 下载烧录工具

> 请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具。解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 固件烧录

\#>TimerCAM 默认出厂的固件并不适配该应用，因此使用前需要为摄像头烧录匹配 UiFlow 的固件，注：UnitCAM 的出厂固件默认适配 UiFlow，无需重新烧录。 打开 M5Burner`-`切换至 TimerCam 选项`-->`选择合适版本点击 download`-->点击`Burn`进行烧录-->等待弹窗`successful\` 则表示烧录完成。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timer_cam/uiflow_block_unit_timercam_firmware.jpg" width="70%">

## 工作模式

UiFlow 支持配置摄像头切换`UART`与`Wi-Fi`两种工作模式，WiFi 模式支持定时拍摄并将图片自动上传至 M5 云端并返回图片调用接口 (URL)。UART 模式下支持用户`使用其他的主控设备通过UART通信获取图片帧`以及修改图片参数。下方将使用主控 CORE 作为案例，连接 UnitCAM 并获取图片数据。

## 案例程序

\#> 使用前需点击左下角添加按钮，添加对应摄像头拓展。<br/>案例操作说明:<br/>按键 A 启用 WiFi 连接模式，连接指定 WiFi, 摄像头间隔 5s 拍摄图片并上传至 M5 云端，按键 B 获取摄像头 Token, 并使用该 Token 生成的云端图像 URL 创建二维码。<br/>按键 C 启用 UART 连接模式，配置图片尺寸为 320\*240, 启动图片显示线程不断刷新图片至屏幕。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timer_cam/uiflow_block_unit_timercam_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
timercam_0 = unit.get(unit.UNITCAM, unit.PORTB)
unitcam_0 = unit.get(unit.UNITCAM, unit.PORTB)
timercam_token = None

def buttonA_wasPressed():
  global timercam_token
  timercam_0.set_wifi('xxxxx', 'xxxxx')
  timercam_0.set_upload_time(5)
  timercam_0.set_mode(timercam_0.CLOUD_MODE)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global timercam_token
  timercam_token = timercam_0.get_token()
  if timercam_token:
    lcd.qrcode(('camera.m5stack.com/timer-cam/image?tok=' + timercam_0.get_token()), x=72, y=32, width=176, version=6)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global timercam_token
  timercam_0.set_show(True)
  timercam_0.set_image_size(timercam_0.SIZE_320_240)
  timercam_0.set_mode(timercam_0.UART_MODE)
  pass
btnC.wasPressed(buttonC_wasPressed)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timer_cam/uiflow_block_unit_timercam_set_wifi.svg">

```python
timercam_0.set_wifi('ssid', 'password')
```

- 配置摄像头连接指定 WiFi

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timer_cam/uiflow_block_unit_timercam_set_upload_time.svg">

```python
timercam_0.set_upload_time(5)
```

- 配置摄像头图片上传云端间隔

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timer_cam/uiflow_block_unit_timercam_get_token.svg">

```python
timercam_0.set_upload_time(5)
```

- 获取摄像头 Token

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timer_cam/uiflow_block_unit_timercam_get_token.svg">

```python
'camera.m5stack.com/timer-cam/image?tok=' + timercam_0.get_token()
```

- 获取摄像头云端图片 URL

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timer_cam/uiflow_block_unit_timercam_set_mode.svg">

```python
timercam_0.set_mode(timercam_0.UART_MODE)
timercam_0.set_mode(timercam_0.CLOUD_MODE)
```

- 切换 UART/CLOUD 模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timer_cam/uiflow_block_unit_timercam_set_size.svg">

```python
timercam_0.set_image_size(timercam_0.SIZE_320_240)
```

- 设置摄像头返回图像尺寸

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timer_cam/uiflow_block_unit_timercam_set_position.svg">

```python
timercam_0.set_position(0, 0)
```

- 设置图像显示位置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/timer_cam/uiflow_block_unit_timercam_set_position.svg">

```python
timercam_0.set_led_brightness(1024)
```

- 设置摄像头板载 LED 的亮度:
  - 0-1024

## 操作视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/timercam_uiflow_video.mp4" type="video/mp4">
</video>
