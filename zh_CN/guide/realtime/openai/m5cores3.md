# CoreS3 OpenAI 语音助手

\#> 案例说明 | 本教程将使用[CoreS3](/zh_CN/core/CoreS3)主控，通过 M5Burner 烧录 OpenAI Voice Assistant 固件，构建个人语音助手应用。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/realtime/openai/m5cores3/cores3_openai_assistant_01.jpg" width="50%" />

## 1. 准备工作

1\. 请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具。解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

2\. 访问[OpenAI](https://openai.com/)完成注册与登录，了解开通 OpenAI Realtime API 相关资费内容，并在控制台中创建并获取`API keys`,

## 2. 固件烧录

- 1\. 双击打开 Burner 烧录工具，在左侧菜单中选择对应的设备类型`CoreS3`, 点击下载`OpenAI Voice Assistant For CoreS3`固件。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/realtime/openai/m5cores3/cores3_openai_assistant_firmware_01.jpg" width="80%" />

- 2\. 点击`Burn`, 并根据提示填写 Wi-Fi 连接信息与 OpenAI API keys.

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/realtime/openai/m5cores3/cores3_openai_assistant_firmware_02.jpg" width="80%" />

- 3\. 设备连接 USB 后，长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="40%">

- 4\. 选择设备对应的端口。点击`Burn`, 等待烧录完成。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/realtime/openai/m5cores3/cores3_openai_assistant_firmware_03.jpg" width="80%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/realtime/openai/m5cores3/cores3_openai_assistant_firmware_04.jpg" width="80%" />

?> 常见问题:| 中国大陆区域网络可能无法正常访问 OpenAI Realtime API 接口，如遇设备无法正常连接服务，请通过代理或更换网络环境重试。

## 3. 开始使用

设备启动后，当屏幕开始显示声音采样曲线则表示已连接服务，可开始语音交互。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/realtime/openai/m5cores3/cores3_openai_assistant_02.jpg" width="50%" />
