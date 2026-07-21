# Atom Voice 蓝牙音箱使用教程

Atom Voice 出厂默认预设音频播放固件，可与手机、平板、电脑等设备建立无线连接，实现音频外放。本文档介绍通过 M5Burner 工具烧录对应专用固件的操作步骤。

## 固件烧录

1. 按照[M5Burner 使用教程](/zh_CN/uiflow/m5burner/intro)完成烧录工具安装，并参照下图下载对应蓝牙音箱固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_01.jpg" width="80%" />

2. 使用 USB-TypeC 数据线将 Atom Voice 设备连接至电脑，在 M5Burner 内点击对应固件的 **Burn** 按钮，选中设备对应串口端口后，点击 **Start** 开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_03.jpg" width="80%" />

页面显示 `Burn successfully, click here to return` 即代表固件烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_04.jpg" width="80%" />

## 无线音箱使用方法

1. 给 Atom Voice 接通电源，设备红灯常亮，进入待配对状态。
2. 开启手机、电脑等终端设备的无线音频连接功能，搜索周边可用设备，找到名为`M5_SPEAKER_T1`的设备即为 Atom Voice。
3. 点击设备名称完成配对建立连接，连接成功后指示灯转为绿色，即可正常外放播放音频（注意：当前固件版本暂不支持通话免提功能）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_08-EN.jpg" width="70%" />

<video id="example_video" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_video_01.mp4" type="video/mp4">
</video>