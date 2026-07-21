## 大模型

| 模型 | 上下文长度 | 量化方式 | 首次生成延迟(ms) | 生成速度(Token/s) | 运行设备 |
|------|------|------|------|------|------|
| DeepSeek-R1-Distill-Qwen-1.5B | 128 | W8A16 | 1075.04 | 3.57 | Module LLM Kit / LLM630 Compute Kit |
| DeepSeek-R1-Distill-Qwen-1.5B | 256 | W8A16 | 3056.86 | 3.57 | Module LLM Kit / LLM630 Compute Kit |
| DeepSeek-R1-Distill-Qwen-1.5B | 256 | W4A16 | - | 13.29 | LLM8850 |
| DeepSeek-R1-Distill-Qwen-1.5B | - | W4A8 | 660 | 7.05 | Hailo-10H |
| Llama-3.2-1B-Instruct | 128 | W8A16 | 891 | 4.48 | Module LLM Kit / LLM630 Compute Kit |
| Llama-3.2-1B-Instruct | 256 | W8A16 | 2601.11 | 4.49 | Module LLM Kit / LLM630 Compute Kit |
| MiniCPM4-0.5B | 512 | W8A16 | 212.91 | 21.05 | LLM8850 |
| MiniCPM4-0.5B | - | - | ✗ | ✗ | Hailo-10H |
| openbuddy-llama3.2-1b-v23.1-131k | 128 | W8A16 | 891.02 | 4.52 | Module LLM Kit / LLM630 Compute Kit |
| Qwen2.5-0.5B-Instruct | 128 | W8A16 | 359.8 | 10.32 | Module LLM Kit / LLM630 Compute Kit |
| Qwen2.5-0.5B-Instruct | 256 | W8A16 | 1126.19 | 10.3 | Module LLM Kit / LLM630 Compute Kit |
| Qwen2.5-0.5B-Instruct | 128 | W4A16 | 442.95 | 12.52 | Module LLM Kit / LLM630 Compute Kit |
| Qwen2.5-0.5B-Instruct | 128 | W4A16 | 140.17 | 37.11 | AI Pyramid |
| Qwen2.5-0.5B-Instruct | 128 | W4A16 | - | 27.05 | LLM8850 |
| Qwen2.5-0.5B-Instruct | - | - | ✗ | ✗ | Hailo-10H |
| Qwen2.5-1.5B-Instruct | 128 | W8A16 | 3056.54 | 3.57 | Module LLM Kit / LLM630 Compute Kit |
| Qwen2.5-1.5B-Instruct | 128 | W4A16 | 1219.54 | 4.63| Module LLM Kit / LLM630 Compute Kit |
| Qwen2.5-1.5B-Instruct | 128 | W4A16 | 289.06 | 16.77 | AI Pyramid |
| Qwen2.5-1.5B-Instruct | 128 | W4A16 | - | 15.06 | LLM8850 |
| Qwen2.5-1.5B-Instruct | - | W4A8 | 370 | 6.82 | Hailo-10H |
| Qwen2.5-3B-Instruct | 128 | W4A16 | 550.3 | 9.46 | AI Pyramid |
| Qwen2.5-0.5B-Instruct | 1024 | W8A16 | 533.19 | 9.76 | Module LLM Kit / LLM630 Compute Kit |
| Qwen2.5-0.5B-Instruct | 1024 | W8A16 | 143.02 | 25.5 | AI Pyramid |
| Qwen2.5-0.5B-Instruct | - | - | 8210 | 1.54 | RaspberryPi5 CPU (ollama) |
| Qwen3-0.6B | 128 | W8A16 | 361.81 | 10.28 | Module LLM Kit / LLM630 Compute Kit |
| Qwen3-0.6B | 2048 | W8A16 | 670.51 | 12.88 | LLM8850 |
| Qwen3-0.6B | - | - | ✗ | ✗ | Hailo-10H |
| Qwen3-1.7B | 2048 | W8A16 | 796.38 | 7.38 | LLM8850 |
| Qwen3-1.7B | - | - | ✗ | ✗ | Hailo-10H |

## 多模态大模型

| 模型 | 上下文长度 | 量化方式 | 首次生成延迟(ms) | 图片尺寸 | 图片编码耗时(ms) | 生成速度(Token/s) | 运行设备 |
|------|------|------|------|------|------|------|------|
| InternVL2_5-1B-MPO | 256 | W8A16 | 1117.27 | 364 | 1164.61 | 10.56 | Module LLM Kit / LLM630 Compute Kit |
| InternVL2_5-1B-MPO | 256 | W8A16 | 433.87 | 448 | 362.22 | 29.48 | AI Pyramid |
| InternVL3-1B | 1024 | W8A16 | 534.95 | 448 | 2267.89 | 9.78 | Module LLM Kit / LLM630 Compute Kit |
| InternVL3-1B | 2048 | W8A16 | 142.32 | 448 | 393.08 | 26.67 | AI Pyramid |
| InternVL3-1B | 1024 | W8A16 | - | 448 | - | - | LLM8850 |
| Qwen2-VL-2B-Instruct | - | W4A8 | 931 | 336 | 323 | 8.16 | LLM8850 |
| Qwen2.5-VL-3B-Instruct | 512 | W8A16 | 558.68 | 308 | 773.95 | 4.81 | LLM8850 |
| Qwen2.5-VL-3B-Instruct | - | - | ✗ | - | ✗ | ✗ | Hailo-10H |
| Qwen3-VL-2B-Instruct | 1152 | W8A16 | 159.79 | 384 | 190.73 | 11.93 | AI Pyramid |
| Qwen3-VL-2B-Instruct | 1152 | W8A16 | - | 384 | 191.65 | 7.8 | LLM8850 |
| Qwen3-VL-2B-Instruct | - | - | ✗ | - | ✗ | ✗ | Hailo-10H |
| Qwen3-VL-2B-Instruct | - | - | 24909 | - | - | 0.42 | RaspberryPi5 CPU (ollama) |

## 语音模型

| 模型 | 输入语音长度(S)  | 实时系数 | 运行设备 |
|------|------|------|------|
| SenseVoiceSmall | 10 | 0.061 | AI Pyramid |
| SenseVoiceSmall | 10 | 0.015 | LLM8850 |
| SenseVoiceSmall | - | ✗ | Hailo-10H |

| 模型  | 实时系数 | 运行设备 |
|------|------|------|
| CosyVoice2-0.5B | 1.36 | AI Pyramid |
| CosyVoice2-0.5B | 1.73 | LLM8850 |
| CosyVoice2-0.5B | ✗ | Hailo-10H |

## 视觉模型

| 模型  | 尺寸 | 模型每秒推理帧数 | 运行设备 |
|------|------|------|------|
| YOLO26n | 640 | 118 | Module LLM Kit / LLM630 Compute Kit |
| YOLO26n | 640 | 649 | AI Pyramid |
| YOLO26n | 640 | 645 | LLM8850 |
| YOLO26n | 640 | 3.47 | RaspberryPi5 CPU (torch) |
| YOLO26n | 640 | 7.4 | RaspberryPi5 CPU (onnx) |
| YOLO26n | 640 | 15.8 | RaspberryPi5 CPU (ncnn) |