# IDE 布局介绍

UiFlow2 Web IDE 是一款 图形化编程工具，界面总体分为 6 个区块，分别为菜单栏、UI 编辑器、功能拓展模块、Blockly 列表、工作区和运行&调试。用户可以在 UiFlow2 上进行产品开发、项目管理等多种个性化体验。本文介绍 UiFlow2 Web IDE 的布局，帮助用户更好地理解和使用 UiFlow2。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow2_01.jpg" width="70%">

1. 菜单栏 
2. UI 编辑器 
3. 功能拓展模块
4. Blockly 列表
5. 工作区
6. 运行与调试

## 菜单栏

菜单栏位于 UiFlow2 Web IDE 界面的上方位置，主要包含以下模块：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow2_21.jpg" width="70%">

1. 登录：保存的项目文件可实现云端工程同步。

2. 项目管理：对云端同步的工程文件进行引用或修改操作。

3. 保存项目：手动存储工程文件至本地和云端。

4. 项目命名：修改当前工程文件名称。

5. 代码预览：点击这里可以切换图形化编程模式与代码编辑模式，方便调试。

6. Project Zone：官方社区精选项目库，您可以下载运行其他用户分享的项目，也可以把有趣的项目分享到社区。

7. 文件操作：工程文件导入、导出、版本管理功能等。

8. 帮助：如果您需要查找官方文档 产品文档以及到技术社区，可以通过帮助列表进入。

9. 设置：您可根据自己的需求配置界面主题、语言等系统。

## UI 编辑器

如果您的设备自带显示屏，可以通过 UI 编辑器为设备设计个性化的 UI。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow2_23.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow2_11.jpg" width="70%">

1. 排版工具：对文字、图片等进行对齐或居中排列。
2. 屏幕显示区：您可以拖动 UI，1:1 对屏幕中 UI 进行细节布局。
3. 界面样式：调节 UI 字体、圆角、阴影等视觉参数。

## 功能拓展模块

功能拓展区可以为设备提供更多样的功能开发，满足用户的多种开发需求。主要包含如下模块：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow2_12.jpg" width="70%">

- **SoC**：芯片类型
- **Software**：通信协议与文件管理模块，选用模块后，可使用对应的 Blockly 进行编程。
- **Hardware**：选用对应模块后，您可以直接使用设备自带的硬件功能，如 IMU 陀螺仪，RGB 指示灯，Speaker 扬声器等。
- **Module**：使用这些功能，需要外接可堆叠扩展模块，如 2Relay，4Encoder，GPS，用于增强硬件功能，如增加继电器控制、电机驱动、通信能力等。
- **Unit**：外接传感器扩展单元驱动库，如 Unit ENV，Unt CO2 等，用于扩展硬件功能，采集温度，CO2 浓度等数据。
- **Custom**：自定义硬件驱动 API 导入接口。
- **Project Files**：工程依赖的图片、音频、字体资源管理器，可以小容量存储一些图片和音频

## Blockly 列表

Blockly 列表是 UiFlow2 的核心功能区，也是图形化编程的主要区域，该区域集中了设备基础配置，UI 编程，逻辑函数，以及 Module 扩展和 Unit 传感器控制等等功能，通过拖拽拼接 Blockly 块进行编程。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow2_13.jpg" width="70%" >

- **System**：配置系统基本功能，如程序延时，连接 WLAN 网络，控制电池等。
- **UI**：UI 功能可以使您通过程序代码自由更改字体，屏幕颜色，图形等。
- **Math**：三角函数 逻辑判断数学工具箱。
- **Hardware**：您可以控制设备自带的硬件，如对 Button IMU Touch 进行精准控制并进行逻辑编程。
- **Advanced**：高级功能扩展区，如鼠标功能，AI 功能等。

## 工作区

工作是拖拽式积木实现业务逻辑构建的场地，可实时生成可编辑的 MicroPython 源代码。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow2_14.jpg" width="70%" >

## 运行&调试

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow2_22.jpg" width="70%" >

1. **WebTerminal**：浏览器内串口调试工具。设备连接 USB 并运行程序后，您可以观察程序的运行状态以及错误提示，在调试工具中还可以对设备中的文件进行简单操作。

2. **WebBurner**：无线固件烧录工具。

3. **Device File Manager**：设备存储空间文件管理器。如果您需要把图片或者音频等文件导入到设备中，可以通过存储空间文件管理器进行导入。

4. **Select Device**：M5Stack 设备型号切换。点击设备型号切换，可以观察到绑定账户的设备状态，如果设备开启并连接 WLAN 后，可以通过无线模式进行编程，方便快捷。

5. **Run**：运行程序。

6. **Download**：点击 Download，把编辑好的程序直接下载到设备中，并配置为开机自动运行。
