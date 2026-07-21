# Atom Voice 蓝牙音箱使用教程

Atom Voice 出厂默认固件为蓝牙音箱模式，用户可使用手机、平板、电脑等终端设备与其蓝牙配对连接，实现音频外放播放。本文档将介绍使用 M5Burner 工具烧录 Atom Voice 蓝牙音箱固件的操作流程。

## 固件烧录

1. 按照[M5Burner 使用教程](/zh_CN/uiflow/m5burner/intro)完成烧录工具安装，并参照下图下载对应蓝牙音箱固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_01.jpg" width="80%" />

2. 使用 USB-TypeC 数据线将 Atom Voice 设备连接至电脑，在 M5Burner 内点击对应固件的 **Burn** 按钮，选中设备对应串口端口，点击 **Start** 开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_02.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_03.jpg" width="80%" />

页面显示 `Burn successfully, click here to return` 即代表固件烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_04.jpg" width="80%" />

## 无线音箱使用方法

1. 为 Atom Voice 接通供电，设备指示灯常亮红色，进入待配对状态。
2. 开启手机、电脑等终端设备蓝牙功能，搜索周边蓝牙设备，搜索到名称为 `M5_SPEAKER_T1` 的设备即为 Atom Voice。
3. 点击设备名称发起配对，完成配对验证后即可建立蓝牙连接；连接成功后设备指示灯切换为绿色，此时可正常使用设备播放音频（注意：当前版本固件暂不支持通话免提功能）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_08.jpg" width="70%" />

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/AtomEcho.mp4" type="video/mp4">
</video>