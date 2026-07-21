# LLM-8850 Card 硬件安装

在树莓派 5 上安装 LLM-8850 加速卡时，可使用 M5Stack [LLM-8850 PiHat](https://shop.m5stack.com/products/ai-8850-llm-accelerator-m-2-kit-8gb-version-ax8850) 或 [树莓派官方 M.2 HAT+ 扩展板](https://www.raspberrypi.com/news/using-m-2-hat-with-raspberry-pi-5/)

!> 安装前先断电 | 安装 LLM-8850 Card 前务必断开树莓派 5 电源。不可带电安装！

## 使用 LLM-8850 PiHat 扩展板

### 供电注意事项

搭配 LLM-8850 PiHat 扩展板使用时，请留意以下供电注意事项

- 1. 通过转接板的 PD 供电接口为整机供电
- 2. 供电能力 > 9V@3A (27W)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1215/LLM-8850_Kit_Raspberry_Pi_5_01.jpg" width="60%">

- 安装视频

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1215/AI-002-8G_LLM-8850_Kit_Installation.mp4" type="video/mp4"></video>

## 使用 M.2 HAT+ 扩展板

### 供电注意事项

搭配 M.2 HAT+ 扩展板使用时， 推荐 DC 5V@3A 供电能力的开关电源 (非 PD 协议) 适配器；若使用 PD 电源适配器，可能因协议适配问题导致无法正常输出最大功率，进而造成设备工作异常。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_14.webp" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_15.webp" width="40%">
