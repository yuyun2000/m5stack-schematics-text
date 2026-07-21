# AIFlow 使用教程


## 简介

AIFlow 是一款专门适配 M5Stack 软硬件的 Vibe Coding 工具。无需复杂的环境配置，即可通过自然语言快速为 M5Stack 设备生成代码、下发程序并完成调试。

本教程以 StickS3 和 StackChan 设备为例，介绍如何接入 AIFlow，并快速完成首次使用。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_02.png" width="70%">


## 软件下载

访问 [AIFlow GitHub](https://github.com/m5stack/AIFlow) 页面下载桌面客户端。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_26.jpg" width="90%">


## 模型配置

首次启动 AIFlow 后，可按照上手指引完成模型接口配置：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_15.png" width="90%">

模型接口配置主要包括以下信息：

- 自定义名称
- 模型 ID
- API Key
- 模型服务商 Base URL

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_13.png" width="90%">

当前**支持**模型：

- Anthropic Claude
- DeepSeek、智谱 GLM、阿里 Qwen 等提供的 Anthropic 兼容 API

当前**不支持**模型：

- OpenAI
- Google Gemini

## 烧录固件

1. 在AIFlow界面配置完成模型接口信息后，点击`Flash`，进入固件烧录页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_29.png" width="90%">


2. 设备进入下载模式：

- **StickS3**：将 StickS3 连接到电脑，长按电源按键，直到绿色指示灯开始闪烁，设备将进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/stickS3_operate_01.gif" width="50%">

- **StackChan**：将 StackChan 连接到电脑，长按电源按键，直到绿色指示灯常亮，设备将进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/stackchan-download-mode-demo.gif" width="50%">

3. 选择对应的设备端口，填写 固件类型以及 Wi-Fi 等相关信息后，点击 `Start Flash` 开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_20.png" width="90%">


## 连接 AIFlow

固件烧录完成后，设备需要通过 Access Code 与 AIFlow 建立无线连接，用于程序推送与设备控制。

1. 获取设备 **Access Code**：

- StickS3：设备启动后，单击中心按键，等待服务器连接成功后，将自动生成 Access Code 显示在屏幕上。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_16.png" width="90%">

- StackChan：设备启动后，等待服务器连接成功后，将自动生成 Access Code 显示在屏幕上。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_30.png" width="90%">


2. 在 AIFlow 中输入 Access Code后，点击`Next`完成设备连接配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_17.png" width="90%">


## 界面布局

AIFlow 的界面围绕“聊天 -> 代码生成 -> 运行调试”的工作流设计，整体由左至右排布，便于快速完成从想法到运行结果的闭环。

常用区域包括：

- 项目管理
- 指引与主题切换
- 对话历史
- 模型管理
- 代码预览
- 设备资源管理器
- 设备管理
- 设备远程终端

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_11.png" width="90%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_05.png" width="90%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_07.png" width="90%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_09.png" width="90%">


## 开始使用

完成连接后，即可直接输入自然语言，描述想要实现的功能细节，等待大模型完成推理，自动生成对应的 MicroPython 代码，并将程序通过网络自动推送至设备。还可以结合代码预览与运行调试功能，快速完成验证与迭代。

#>注意|经过 AI 推理生成的程序并不固定，同样提示词也可能得到不一样的程序结果，以下仅做效果演示，可能与实际效果存在出入。

### StickS3 案例演示

```markdown
帮我创建一个番茄钟计时器应用，按下A键可将时间设置为20分钟
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_19.png" width="90%">

效果展示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_18.png" width="90%">


### StackChan 案例演示

```markdown
显示一个可爱的表情，当我触摸你的头部的触摸区域时候，切换显示为生气表情，同时控制舵机身体左右摇晃，点亮RGB LED灯，红色和蓝色切换。
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_28.png" width="90%">

效果展示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/AIFlow_use_tutorial_27.png" width="90%">

