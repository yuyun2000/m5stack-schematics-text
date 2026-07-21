# AI Pyramid 快速上手

## 1. 设备开关机

- 设备供电后将自动启动
- 可通过软件指令关机，关机后可通过顶部按键重新开机。
- 顶部按键长按 15s 强制关机

?> 供电要求 | 设备要求电源适配器的 PD 供电能力需在 DC 9V@3A (27W) 或以上。若使用 DC 5V 供电，设备将无法启动。

设备连接以太网，开机启动后，将通过 OLED 屏幕显示当前 IP 地址。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_eth_ip_01.jpg" width="50%">

## 2. SSH

默认登录用户为`root`，密码为`123456`，同一局域网下可使用下方 SSH 指令访问设备。(指令需替换为实际设备 IP)

```bash
ssh root@192.168.20.173
```

## 3. 桌面 GUI

预装的 Ubuntu 镜像带有桌面 GUI, 可使用 Display Output 连接显示器输出。

- AI Pyramid 使用左侧的 Display Output #1 连接显示器输出。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_display_output_01.jpg" width="70%">

- AI Pyramid-Pro 使用右侧的 Display Output 连接显示器输出。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_pro_display_output_01.jpg" width="70%">

## 4. OLED 显示屏

设备上的 OLED 屏用于设备以太网 IP 显示，自定义字符显示功能，接口电源状态监控。长按 OLED 屏左侧的按键，可切换当前显示的页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_oled_button_01.jpg" width="100%">

## 5. 语音助手

设备启动后，将默认启用内置语音助手。 `单击顶部按键` 或 通过唤醒词 `Hi M Five` 即可唤醒，进行对话。当前版本，唤醒后将执行单次对话，暂时不支持连续对话。固定使用语言为英文。

- 对话演示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_voice_assistant_01.mp4" type="video/mp4"></video>
