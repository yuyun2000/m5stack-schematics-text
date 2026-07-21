# StopWatch 出厂固件使用教程

## 简介

StopWatch 是一款面向便携与交互场景的 AMOLED 圆形触控开发板，出厂固件集成电子徽章、电子秒表、闹钟等功能，可满足便携智能操控、穿戴人机交互、轻量化物联网终端等多元化开发应用需求。本教程介绍 StopWatch 设备出厂固件的使用方法。

## 按键操作

- 开机后同时长按按键 A 和按键 B，进入主菜单。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_27.jpg" width="50%">

- 按下按键 A / 按键 B，或点击屏幕左右按键，均可左右滑动切换功能菜单。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_01_s0_fast1_5.gif" width="50%">

- 点击屏幕功能图标可以进入功能详情页。同时长按按键 A 和按键 B 返回主菜单；从设备上边缘向中间滑动，会**显示电量**。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_02.gif" width="50%">

## Badge（电子徽章）功能使用

StopWatch 的电子徽章功能，可以连接设备 AP ，上传本地图片并显示。

1. 点击`Badge`菜单进入电子徽章功能。
2. 长按屏幕，弹出对话框，询问是否进入电子徽章编辑界面，点击`Edit`。设备将自动开启 AP 热点`M5StopWatch-xxxx`，使用手机/电脑连接热点后，在浏览器中访问 `192.168.4.1` 即可打开 电子徽章的管理界面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_28.jpg" width="40%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/152-factory-doc_12.jpg" width="40%">

3. 单击选中要上传图片的`Slot`后，单击`Choose File`，选中要上传的图片，可以通过`Zoom`功能调整图片的显示尺寸，`Background`功能可以调整图片的背景颜色。
4. 设置完成后，单击`Upload To Selected Slot`，即可上传图片。重复上述操作，可为多个 Slot 上传图片。
5. 图片上传完成后，单击界面底部的`Done`，图片上传成功。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/152-factory-doc_13.jpg" width="50%">

图片上传完成：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_14.jpg" width="50%">

效果展示：

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_15.mp4" type="video/mp4"></video>

## 功能菜单介绍

- **AlarmClock**：闹钟功能，单击 Add 键可以添加多个闹钟。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_16.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_03.jpg" width="50%">

- **WatchFace**：时钟功能，单击按键 A/按键 B 可以切换时间的显示样式，单击屏幕可以切换时钟的背景颜色/风格。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_25.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_05.jpg" width="50%">

- **Stopwatch**：电子秒表。
  - **START**：开始计时
  - **RESET**：数据重置
  - **LAP**：分段键
  - **STOP**：停止计时

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_22.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_04.jpg" width="50%">

- **Badge**：电子徽章，可上传图片并显示，手机端上传时图片大小需要小于 3MB。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_26.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_31.jpg" width="50%">

- **IMU**：IMU 姿态显示界面，实时展示三轴加速度数据，直观反映设备当前的倾斜状态与空间姿态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_19.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_11.jpg" width="50%">

- **Audio.FFT**：测量声音音调频率。单击界面中心区域可以显示/取消显示频率的数值。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_20.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_08.jpg" width="50%">

- **LuckyWheel**：幸运转盘。自定义转盘分区数量后，点击中心转盘图标即可启动转动。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_23.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_09.jpg" width="50%">

- **Settings**：设备的相关设置，包括屏幕亮度，设备音量，时间/日期，查询固件版本等。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_24.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-factory-doc_10.jpg" width="50%">
