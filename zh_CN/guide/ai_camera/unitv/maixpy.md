# UnitV Maixpy 上手指南

## 驱动安装

\#> 将设备连接至 PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。(注：某些系统环境下，需要安装两次驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`。对于 Windows 用户，我们推荐使用驱动文件在设备管理器直接进行安装，可执行文件安装方式可能无法正常工作)。

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

\#>MacOS 用户注意事项 | MacOS 用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## 固件烧录

### Kflash_GUI

1. 下载固件和 Kflash_GUI 烧录工具。（ UnitV 和 StickV 使用的是相同的固件）

| 固件版本                       | 下载链接                                                                                              |
| ------------------------------ | ----------------------------------------------------------------------------------------------------- |
| M5StickV_Firmware_v5.1.2.kfpkg | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/M5StickV_Firmware_v5.1.2.kfpkg) |

| 软件版本           | 下载链接                                                                                                 |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| Kflash_GUI_Windows | [Download](https://github.com/sipeed/kflash_gui/releases/download/v1.5.3/kflash_gui_v1.5.3_windows.7z)   |
| Kflash_GUI_MacOS   | [Download](https://github.com/sipeed/kflash_gui/releases/download/v1.8.1/kflash_gui_v1.8.1_macOS.dmg)    |
| Kflash_GUI_Linux   | [Download](https://github.com/sipeed/kflash_gui/releases/download/v1.5.3/kflash_gui_v1.5.3_linux.tar.xz) |

2. 将设备连接至电脑，打开烧录工具**Kflash_GUI**，选择对应的设备端口、开发板类型 (M5StickV)、固件程序、波特率。点击下载，开始烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv/maixpy_01.jpg" width="50%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv/maixpy_02.jpg" width="50%">

## MaixPy IDE

MaixPy IDE 能够便捷的实现脚本程序的实时编辑、执行，以及实时监控摄像头图像，文件传输等功能。 MaixPy IDE 适合初学者以及想要快速搭建项目的开发者使用。

- [MaixPy IDE](http://dl.sipeed.com/MAIX/MaixPy/ide/)

运行 MaixPy IDE， 点击工具栏，选择开发板型号。`Tools`-> `Select Board`-> `M5StickV`

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv/maixpy_05.jpg" width="70%">

点击左下角的连接按钮，并选择正确的连接端口，点击 OK。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv/maixpy_06.jpg" width="70%">

当连接按钮变为红色时表示已经连接成功，你可以在上方的文本框编辑代码，并点击左下角的运行按钮执行。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv/maixpy_07.jpg" width="70%">

### 串口调试工具

1. 设备的 USB 将默认启用为系统 log 端口，用户可使用该接口连接至电脑，使用任何终端工具进行访问，默认波特率为`115200bps`, 以下的操作说明基于 Putty。

- [Putty - download](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

2. 运行 Putty 后，将设备连接至电脑，在 Putty 中设置相应的端口号与波特率，点击 Open。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv/maixpy_03.jpg" width="50%">

3. 连接成功后，将自动进入 MaixPy 的交互界面。此时设备正在运行默认程序，可以通过按下快捷键 "Ctrl+C" 中断其运行，并进入命令行。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv/maixpy_04.jpg" width="70%">

## 编辑与运行文件

### 编辑文件

在 MaixPy 中，内置了一款开源编辑器 [Micropython Editor(pye)](https://github.com/robert-hh/Micropython-Editor), 可以方便的修改程序文件。

使用 `os.listdir()` 可以查看当前目录下的文件，

使用 `pye("hello.py")` 可以创建文件并进入编辑模式，快捷键等使用说明可以在[这里查看](https://github.com/robert-hh/Micropython-Editor/blob/master/additional_documentation/Pyboard%20Editor.pdf)

完成编辑后，按 `Ctrl+S` > `Enter` 键进行保存，按 `Ctrl+Q` 退出编辑

**注意**: 必须使用 `Del` 键来代替 `Backspace` 键，`Backspace` 键默认会触发 `Ctrl+H`。

### 运行程序

使用 `os.chdir()` 切换工作目录，比如 `os.chdir("/flash")`

#### 方法一：直接在命令行中逐行执行 Python 代码

执行 `import hello`，即可看到输出 `hello maixpy`

需要注意的是，`import` 只能执行一次，多次 `import` 将不会执行。如果需要多次执行，建议按照如下方法运行 .py 文件

#### 方法二：运行 .py 文件

使用 `exec()` 函数来运行 `hello.py`

```python
with open("hello.py") as f:
    exec(f.read())

```

### 开机自动运行脚本

系统会在 `/flash` 或者 `/sd` 目录创建 `boot.py` 文件，系统启动时会自动执行此脚本，你可以编辑这个文件来自定义开机时要运行的程序。

## WS2812

固件内置了 WS2812 RGB LED 驱动库，以下为参考例程。注意：由于 UnitV 的拓展端口不具备驱动负载功能，因此该程序仅适用于驱动内置的 RGB LED:

```python
from modules import ws2812
from fpioa_manager import *
fm.register(8)
class_ws2812 = ws2812(8,100)
r=0
dir = True
while True:
    if dir:
        r += 5
    else:
        r -= 5
    if r>=255:
        r = 255
        dir = False
    elif r<0:
        r = 0
        dir = True
    for i in range(100):
        a = class_ws2812.set_led(i,(0,0,r))
    a=class_ws2812.display()
```
