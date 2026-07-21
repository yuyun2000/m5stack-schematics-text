# Module LLM UiFlow2 快速上手

## 概述

`Module LLM` 模块能够搭配不同的 M5 主控使用，本教程将以 `Basic` 主控举例如何在 `UiFlow2` 中编程控制 Module LLM。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_module_device_01.jpg" width="70%" />

## 准备工作

- 参考[UiFlow Web IDE 教程](/zh_CN/uiflow2/uiflow_web)，了解使用 UiFlow2 的基本流程，并参考[M5Core 固件烧录与程序推送教程](/zh_CN/uiflow2/m5core/program) 完成设备 UiFlow 固件烧录和 UiFlow2 连接。

## 案例程序

以下提供了一些基础使用案例程序，你可以根据自己的需求，导入到 UiFlow2 中进行使用。

- examples:
  - [get_model_list](https://uiflow2.m5stack.com/?pkey=57b3b457cf2247ce827a09d3cc245e5d): 获取 Module LLM 的模型列表
  - [kws_asr](https://uiflow2.m5stack.com/?pkey=0328459639b345a1a08a2a73806a76fc): 通过 KWS 实现唤醒 -> 触发 ASR 实现语音转换文本。 (KWS+ASR)
  - [text_assistant](https://uiflow2.m5stack.com/?pkey=167c2996558d421eb8826f92d79239e6): 通过文本方式输入内容至 LLM 模型，完成推理后以文本形式输出。 (LLM)
  - [tts](https://uiflow2.m5stack.com/?pkey=f1845bb08b24461580130d55d4d95524): 通过 TTS 单元实现文本转换语音播放。 (TTS)
  - [melotts](https://uiflow2.m5stack.com/?pkey=cddb9b394e204e4f909a75da88b96888): 通过 MeloTTS 单元实现文本转语音播放。
  - [voice_assistant](https://uiflow2.m5stack.com/?pkey=66093b875a12421eacb6f4b9af6daf57): 通过 KWS 实现唤醒 -> 触发 ASR 实现语音转换文本 -> 将其转换内容作为 LLM 输入用作推理 -> 最后将推理输出结果通过 TTS 输出语音。 (KWS+ASR+LLM+TTS)
  - [yolo11n with UVC](https://uiflow2.m5stack.com/?pkey=94183b4a55924e61888cbf80a2c2b4aa): 通过 USB 摄像头读取视频流，将视频流送入 yolo11, 推理输出识别结果。
  - [vlm](https://uiflow2.m5stack.com/?pkey=28a4aad4b72c46539f591c4466b1a842): 通过 CoreS3 摄像头读取画面，将图片送入 vlm，推理输出结果。

## 相关链接

- [Module LLM UiFlow2 API](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/llm.html)

## 教程视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113461845560481&bvid=BV1dhmyYjEfZ&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/s4E1ua7V9GM?si=AcHq9I5ttKktMklr" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
