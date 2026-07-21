# LidarBot

<span class="product-sku">SKU:K017-C</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/lidarbot/lidarbot_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/lidarbot/lidarbot_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/lidarbot/lidarbot_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/lidarbot/lidarbot_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/lidarbot/lidarbot_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/lidarbot/lidarbot_06.webp">
</PictureViewer>

## 描述

**LidarBot** 是一款激光雷达车。配备 360° 激光雷达传感器、M5Core 主控、4 个麦克纳姆轮、车轮控制底板 (集成 MEGA328)、RGB 灯条、操纵杆控制器等硬件，此外额外附送一个 TRACE 寻迹模块套件用于黑白轨迹的识别。基于麦克纳姆轮技术的全方位运动小车可以实现前行、横移、斜行、旋转及其组合等运动方式。装配大容量锂电池为雷达小车提供长时间续航。

控制器与 LidarBot 之间通过 ESP-NOW 进行实时通信，运行时你可以在控制器屏幕上查看由激光雷达传感器扫描的地图数据。我们在 Github 上提供了开源代码，基于官方源代码进行修改，你能够将雷达扫描等采集的数据通过 Wi-Fi 或其他方式传输至其他节点。LidarBot 能够应用在 STEM 教育领域用作编程学习、竞赛等活动。不仅如此，功能强大的它，同样适用于 AGV 开发领域的开发者进行项目开发。

## 产品特性

- EAI YDLIDAR X2 雷达测距与转速: 8m @ 7Hz
- ESP-NOW 遥控
- 具备寻迹功能
- 开发平台
  - Arduino
  - UiFlow
- 兼容 LEGO

## 包装内容

- 1 x LidarBot
- 1 x 远程控制手柄
- 1 x 寻迹模块套件
- 2 x 电池 (1300mAh @ 11.1V)
- 1 x 电池充电器
- 1 x Type-C USB 数据线

## 应用场景

- 室内导航
- 自主走迷宫
- 路径规划
- 自动驾驶

## 规格参数

| 规格     | 参数                    |
| -------- | ----------------------- |
| MCU      | STM32F030F4P6           |
| 产品尺寸 | 142.0 x 117.0 x 120.0mm |
| 产品重量 | 1980.0g                 |
| 包装尺寸 | 208.0 x 208.0 x 167.0mm |
| 毛重     | 2140.0g                 |

## 操作说明

### 连接与匹配

在未连接状态或连接断开的情况下，显示或者控制都有可能出现问题，这时候我们都需要做一个重新的连接。

- 雷达车按住 C 键不放按一下 M5Core 的电源键，等待屏幕重启完松开 C 键即可进入广播模式，所有从机都会收到主机发来的信号。
- 在雷达车进入广播模式的情况下，我们按住手柄 C 键不放再按一下手柄的电源键，等待手柄重启完成再松开 C 键即可在屏幕上查看到当前广播的主机。我们通过 A/C 键向上向下选择，然后按 B 键确定想要连接的主机的 Mac 地址，主机的 Mac 地址可以通过手机或者电脑查看附近的 Wi-Fi, 以 lidar 开头后面紧接着的就是主机的 Mac 地址。
- 确认完主机之后，主机即雷达车屏幕将收到从机的确认信号，同样通过 ABC 键选择和确定从机即手柄的地址。当按下 B 键确定之后，雷达车和手柄就完成了通信的配置，双方可以互发消息，实现雷达图显示和手柄控制。

#### 控制和显示

在雷达车和手柄已经匹配的情况下，雷达车和手柄可以通过 ESP-NOW 互发消息，雷达车的雷达信息可以显示到手柄上，手柄也可以通过 ESP-NOW 控制小车的移动。

- 普通控制模式：移动手柄摇杆，小车将实现前进后退和转向。
- 全向控制模式：按住手柄 A 键即手柄屏幕三个按钮中最左边的按钮，再移动摇杆可以实现左右的横移，但是前后的方向是反过来的。

### 网页显示雷达图像

在雷达车启动完成之后，不需要雷达车和手柄完成匹配，便可以通过连接雷达车 Wi-Fi 热点 (SSID:X2Lidar:xx:xx:xx, PWD:12345678), 然后通过手机或者电脑浏览器访问 192.168.4.1/map 看到雷达图像信息。

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/lidarbot/lidarbot_map_01.webp" width="70%">

## 数据手册

- [EAI YDLIDAR X2 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/lidarbot/YDLIDAR%20X2%20%E6%95%B0%E6%8D%AE%E6%89%8B%E5%86%8C.pdf)

## 软件开发

### Arduino

- [LidarBot 测试程序](https://github.com/m5stack/Applications-LidarBot/tree/master/LidarBot-X2)

### 通信协议

#### 主控与底板之间的协议

协议格式：帧头 (命令类型) + 数据帧 + 帧尾

| 协议对象      | 协议格式                                        | 案例                                                  | 调用函数                     |
| ------------- | :----------------------------------------------- | ----------------------------------------------------- | ---------------------------- |
| Wheels        | 0xAA,SpeedX (-7 ~ 7),SpeedY,SpeedZ,SpeedA,0x55  | 0xAA, 5, 5, 5, 5, 0x55 (前进，速度: 5)                | ControlWheel (5, 5, 5)       |
| One RGB       | 0xAB,LedIndex,R (0 ~ 254),G,B,0x55              | 0xAB, 3, 20, 50, 100, 0x55 (3 号灯点亮，显示指定颜色) | setLedColor (3, 20, 50, 100) |
| Front RGB Bar | 0xAC,R (0 ~ 254),G,B,0x55                       | 0xAC, 20, 50, 100, 0x55 (前向灯带点亮，显示指定颜色)  | setFrontLedBar (20, 50, 100) |
| Back RGB Bar  | 0xAD,R (0 ~ 254),G,B,0x55                       | 0xAD, 20, 50, 100, 0x55 (后向灯带点亮，显示指定颜色)  | setBackLedBar (20, 50, 100)  |
| All RGB       | 0xAE,R (0 ~ 254),G,B,0x55                       | 0xAE, 20, 50, 100, 0x55 (全部灯带点亮，显示指定颜色)  | setLedAll (20, 50, 100)      |
| ServoMotor0   | 0xAF,Angle (0 ~ 180),0x55                       | 0xAF, 100, 0x55 (舵机 0 转动 100 °)                   | setServo0Angle (100)         |
| ServoMotor1   | 0xB0,Angle (0 ~ 180),0x55                       | 0xB0, 100, 0x55 (舵机 1 转动 100 °)                   | setServo1Angle (100)         |

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/lidarbot/lidarbot_07.webp" width="50%">

#### 参数

- 通信参数
  - M5Core (车体主控) <-> 激光雷达 U1RXD (GPIO16) <-> 激光雷达
    串口配置参数: "115200bps, 8, n, 1"(8 位数据，无奇偶校验，1 位停止位)
  - M5Core (车体主控) <-> 控制底板 U2TXD (GPIO17) <-> 控制底板
    串口配置参数: "115200bps, 8, n, 1"(8 位数据，无奇偶校验，1 位停止位)
- 接口
  - 舵机 0 <-> A0 (MEGA328)
  - 舵机 1 <-> A1 (MEGA328)
  - RGB LED <-> 11(MEGA328)

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/lidarbot/lidarbot_08.webp" width="50%">

### Easyloader

| Easyloader                          | 下载链接                                                                                                                                         | 备注 |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| LidarBot Master Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Application/LidarBOT/LidarBot_CarMain/EasyLoader_LidarBot_CarMain.exe)        | /    |
| LidarBot Remote Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Application/LidarBOT/LidarBot_RemoteController/LidarBot_RemoteController.exe) | /    |

## 相关视频

- LidarBot 案例

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201904/LidarBot.mp4" type="video/mp4">
</video>

## 版本变更

| 上市日期 | 产品变动                                                          | 备注                             |
| -------- | ----------------------------------------------------------------- | -------------------------------- |
| 2019.7   | 采用雷达型号为 EAI YDLIDAR X2, 添加钣金结构件 SKU: K017 -> K017-C | 雷达测距转速 8m @ 6Hz ->8m @ 7Hz |
| 2018.12  | 首次发售                                                          | /                                |
