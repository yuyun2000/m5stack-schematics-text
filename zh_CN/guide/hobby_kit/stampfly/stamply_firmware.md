# StampFly & Atom Joystick 固件烧录与使用教程

#>说明:|StampFly & Atom Joystick 是 M5Stack 推出的开源四轴飞行器套件, 本教程将演示如何为其烧录固件, 并实现配对和基本飞行操作。

## 1.烧录工具

请根据您所使用的操作系统,点击下方按钮下载相应的 M5Burner 固件烧录工具.解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

双击打开 Burner 烧录工具, 在左侧菜单中选择对应的设备类型`STAMPS3`, 点击下载`StampFly Firmware`固件和`StampFly Controller Firmware`固件,。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/stampfly/stampfly_fw_01.jpg" width="70%">

## 2.固件烧录

### StampFly 固件烧录

断电状态下长按 StampS3 中心按键, 然后接入 USB 线, 即可进入下载模式, 此时将成功识别到设备端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/stampfly/stampfly_download_mode_01.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/stampfly/stampfly_download_mode_02.jpg" width="70%">

点击`Burn`后, 选择对应的端口开始烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/stampfly/stampfly_fw_02.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/stampfly/stampfly_fw_03.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/stampfly/stampfly_fw_04.jpg" width="70%">

### Atom Joystick 固件烧录

AtomS3 连接 USB 后长按机身侧边复位按键, 待绿灯亮起则进入下载模式, 此时将成功识别到设备端口。参考 StampFly 固件烧录操作, 进行`StampFly Controller Firmware`固件烧录即可。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/stampfly/atoms3_download_mode_01.jpg" width="70%">

## 3.设备配对

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/StampFly%E3%80%81AtomJoyStick%20video.mp4" type="video/mp4"></video>

## 4.操作说明

### 设备配对

- 1.长按 AtomS3 中间按钮, 开机后根据屏幕提示, 再次单击进入配对模式。
- 2.单击 StampFly 的 Reset 按钮发送配对广播。
- 3.等待配对完成。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/stampfly/stampfly_pair_01.jpg" width="70%">

### 起飞降落

- 1.单击 AtomS3 中间按钮, 可控制起飞或降落

### 功能模式

- Atom Joystick 左前方按钮(操控模式切换)
  - `稳定模式`: 提供稳定的控制交互, 适用于常规的飞行和巡航动作。
  - `运动模式`: 提供最大控制自由度, 可以实现复杂动作, 但需要极高的操作技巧。
- Atom Joystick 右前方按钮(高度模式切换)
  - `自动高度`: 高度稳定在设定值, 上下推动左摇杆会改变设定的高度。
  - `手动高度`: 高度全油门控制, 需要较高的操作技巧。
- Atom Joystick 右侧摇杆中心按钮(空中翻转动作)

## 5.状态灯说明

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/f89b0db443ee16c6fd11996bbf2cd41.jpg" width="100%" />

- 1.开机
  - 白色: 设备自检开始。
  - 紫色：传感器偏移校准中。(此状态请保持 StampFly 水平，请勿触碰影响校准)
  - 红绿蓝交替: 待机状态。(可以起飞)
- 2.运行
  - 浅蓝色：低电量提醒
  - 黄色：手动高度模式
  - 紫色：自动高度模式
  - 绿色：自动高度模式下自动降落
