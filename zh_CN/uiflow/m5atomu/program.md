# AtomU 固件烧录与程序推送

## 1. 准备工作

- 参考[UIFlow Web IDE 教程](/zh_CN/uiflow/uiflow_web)，了解使用 UiFlow 的基本流程， 并完成 M5Burner 固件烧录工具的安装。
- 在 M5Burner 中下载适配`AtomU`的固件， 如下图所示。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/atomu/burner_atomu_01.jpg" width="70%">

## 2.USB 驱动安装

?> 波特率限制 | 在进行设备程序下载操作时，推荐选用以下串口波特率选项。若采用其他速度，可能导致程序无法正常下载。<br/>**1500000 bps** / **750000 bps** / **500000 bps** / **250000 bps** / **115200 bps**

\#> 将设备连接至 PC，打开设备管理器为设备安装[FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件， 并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`, Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载 FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

\#> 对于 MacOS 用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的 App` - > `App Store 和认可的开发者选项`。

## 3. 端口选择

1\. 将设备通过 USB 线连接至电脑，在 M5Burner 中选择对应固件的 Burn 按钮，填写 WiFi 信息，选择对应设备端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/atomu/burner_atomu_02.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/atomu/burner_atomu_03.jpg" width="70%">

## 4. 固件烧录

1\. 点击 Start 按键开始烧录。 注：若中途出现烧录失败或连接超时等情况，请检查是否存在端口占用，或尝试更新 USB 线，降低波特率。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/atomu/burner_atomu_04.jpg" width="70%">

## 5.API KEY

1\. 完成固件烧录后，设备将重新启动，保持连接 USB 连接。使用 M5Burner 点击`Configure`选项，选择对应端口，点击`Load`加载当前设备配置。获取成功后将弹窗显示当前设备的`API KEY`, `Start Mode`等信息， 此时我们可以复制保存设备的 API KEY 信息用于后续步骤使用。 注：在本示例中，我们将使用 UIFlow Web IDE (网络版) 进行编程，因此`Start Mode`需要确保配置为`Internet Mode`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/atomu/burner_atomu_05.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/atomu/burner_atomu_06.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/atomu/burner_atomu_07.jpg" width="70%">

2\. 将设备配置为在线编程模式后， 我们需要通过 API KEY 让设备与 UiFlow 建立起连接， 使其能够为指定的设备推送程序。用户需在电脑端浏览器访问[flow.m5stack.com](http://flow.m5stack.com/)进入 UiFlow 编程页面

3\. 点击页面右上角的菜单栏中的设置按钮， 输入我们在上一步骤获取的 API KEY, 点击 OK 保存， 等待提示连接成功。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/atomu/burner_atomu_08.jpg" width="70%">

## 6.RUN

1\. 完成上述配置后， 我们尝试编程点亮 LED 灯。首先， 从左侧程序块菜单中，选中`Hardware`->`RGB`->`Set RGB Bar color`. 将其拖拽到工作区并连接到 setup。 点击右上角的三角形运行按钮，执行程序。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/atomu/uiflow_atomu_emample.gif" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/atomu/burner_atomu_11.jpg" width="70%">
