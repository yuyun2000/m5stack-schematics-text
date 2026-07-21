# IDE 布局介绍

UiFlow1 Web IDE 是一款 图形化编程工具，具有免安装、可视化、模块化编程等特点。界面总体分为 6 个区块，分别为菜单栏、UI 编辑器、资源拓展模块、Blockly 列表、工作区和运行与调试区。用户可以在 UiFlow1 上进行产品开发、项目管理等多种个性化体验。本文介绍 UiFlow1 Web IDE 的布局，帮助用户更好地理解和使用 UiFlow1。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_34.jpg" width="70%">

1. 菜单栏
2. UI 编辑器
3. 资源拓展模块
4. Blockly 列表
5. 工作区
6. 运行与调试区

## 菜单栏

菜单栏位于 UiFlow1 Web IDE 界面的上方位置，主要包含以下模块：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_01.jpg" width="70%">

1. 进入技术社区、选择 UiFlow 版本、UiFlow1 升级日志，以及设置菜单。
2. UiFlow1 使用指导，适合新手快速入门。
3. 查找官方文档和产品文档，链接至 M5Stack 官方文档中心，可查阅 UiFlow1 开发文档、硬件产品手册等。
4. 产品使用样例，内置丰富的项目案例库，支持一键导入项目至工作区。
5. 链接到 EzData 管理器页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_28.jpg" width="70%">

6. 将当前项目以新名称、新路径保存为本地文件（.m5f 格式）。
7. 保存修改，保存工作区代码与设计变更。
8. 打开本地存储的 .m5f 项目文件。
9. 创建一个新的.m5f 项目文件。
10. 项目管理，查看最近的 100 个项目文件及其创建时间，也可进行下载 / 删除操作。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_29.jpg" width="70%">

11. 撤销上一步操作（如删除 Block、修改代码、移动 UI 组件）。
12. 恢复已撤销的操作，当有可恢复操作时激活。
13. 设备文件管理，管理连接设备的文件系统。
14. 显示快捷键列表。
15. 登录 M5Stack 账号。
16. 图形化 Blokly / Python 代码切换。
17. 修改当前工程文件名称。

\#> 说明 |**图形化 Blokly / Python 代码切换**功能，可以查看 Blokly 对应的 Python 代码逻辑，如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_31.jpg" width="70%">

## UI 编辑器

如果您的设备自带显示屏，可以通过 UI 编辑器为设备设计个性化的 UI。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_23.jpg" width="70%">

将组件拖动到模拟显示屏，可以对组件进行配置基础属性，如字体大小，组件大小，颜色，样式等。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_11.jpg" width="70%">

## 资源拓展模块

资源拓展模块支持接入传感器、控制器等拓展单元，可以通过 M5 主机上的接口，来对这些模块进行控制和信息采集。这个区域可以为设备提供更多样的功能开发，满足用户的多种开发需求。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_12.jpg" width="70%">

单击 + 以添加更多拓展单元：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_24.jpg" width="70%">

添加成功的拓展单元会显示在该区域内：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_26.jpg" width="70%">

## Blockly 列表

Blockly 列表是 UiFlow1 的核心功能区，也是图形化编程的主要区域，该区域集中了基础硬件功能，UI 编程，逻辑函数，以及 Module 扩展和 Unit 传感器控制等功能，通过拖拽拼接 Blockly 块进行编程。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_13.jpg" width="70%" >

如果在**资源拓展模块**添加了功能单元，对应的拓展 Block 会加载到 Blockly 列表中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_25.jpg" width="70%" >

- **Event**：事件函数
- **UI**：通过程序代码自由更改字体，屏幕颜色，图形等
- **Hardware**：M5 主机上自带的一些外部设备，如喇叭、RGB 灯等
- **Unit**：外接传感器扩展单元驱动库，如 Unit ENV，用于扩展硬件功能，采集温度、湿度和气压等数据
- **Module**：包含 M5 不同功能底座的相关 Block
- **Advanced**：从 M5 内核的 ESP32 拓展出来的外设接口，包括普通 IO 口，串口，和 I2C 等
- **Remote**：远程控制，可通过手机终端对 M5 设备实现远程控制
- **System**：配置系统基本功能，如程序延时，连接 WLAN 网络，控制电池等
- **Custom**：自定义硬件驱动 API 导入接口

## 工作区

工作是拖拽式积木实现业务逻辑构建的场地，可实时生成可编辑的 Python 代码。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_22.jpg" width="70%" >

## 运行与调试

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_32.jpg" width="70%" >

1. **Download**：把编辑好的程序直接下载到设备中，并配置为开机自动运行。
2. **Run**：运行程序。
3. **Terminal(Beta)**: 浏览器内串口调试工具，设备连接 USB 并运行程序后，您可以观察程序的运行状态以及错误提示，在调试工具中还可以对设备中的文件进行简单操作。
4. 设置：进入设置菜单后，可以查看 / 输入设备的 API key，设置系统语言，选择设备类型等，如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/uiflow1_33.jpg" width="70%" >
