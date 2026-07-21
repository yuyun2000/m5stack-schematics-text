# Atom Voice STT 快速上手

## 驱动安装

\#> 将设备连接至 PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`, Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

\#>MacOS 用户注意事项 | 对于 MacOS 用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## EchoSTT 服务的 Arduino 案例程序

**指示灯说明**

1\. 开机后红色状态灯表示网络未连接

2\. 开机后绿色状态灯表示已连接网络

3\. 按下按键状态灯变为黄色

4\. 识别结果识别状态灯为红色

5\. 识别结果成功状态灯为绿色

使用该案例时您需要通过 M5Burner 点击获取 Token, 在示例中填入 SSID 和 WIFI 密码，找到 rest.settoken ("your_token"); 在其中填入获取的 Token

- [EchoSTT服务](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Core/Atom/AtomEcho/Arduino/EchoSTT)

### Arduino 示例程序

1. 这个示例用于测试 LED、麦克风和扬声器是否正常工作，如果在通电同时按下按键，则扬声器会一直播放音乐，否则只播放一次然后进入测试麦克风环节，您可以通过串口监视器查看。

   - [FactoryTest](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Core/Atom/AtomEcho/Arduino/Factory_Test)

2. 这是一个录音与回放的示例，当您按住按键时开始录音，录音时间不多于 6 秒，松开按键后将播放您录制的内容。

   - [Recoder\&Replay](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Core/Atom/AtomEcho/Arduino/Repeater)

3. 这个示例可以通过 url 播放音乐，由于缓冲区内存较小，因此网络状况不好的情况下会出现持续性的噪声，请合理选择 url 链接与您的 wifi 网络。

   - [StreamHttpMP3](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Core/Atom/AtomEcho/Arduino/StreamHttpClient_ECHO)
