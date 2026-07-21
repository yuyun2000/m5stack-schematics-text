# Chatbox

## 安装 Chatbox

访问[Chatbox 官网](https://chatboxai.app/en)下载对应操作系统的安装包并进行安装。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/chatbox_01.jpg" width="70%" />

## 配置 Chatbox

1. 点击 **Setup Provider**，添加模型提供方

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/pictures/chatbox001.png" width="60%" />

2. Add provider 中，Name 填写 **ModuleLLM** 或 **AI Pyramid** 即可，API Mode 选择 **OpenAI API Compatible**

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/pictures/chatbox002.png" width="60%" />

3. 在API Host 填入 ModuleLLM 或 AI Pyramid 的 IP 和 API 路径，获取并添加已安装的模型

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/pictures/chatbox003.png" width="60%" />

4. 添加 **StackFlow** 提供的 **qwen2.5-1.5B-Int4-ax650** 模型，这个需要根据平台选择对应的模型。ModuleLLM/LLM630 Compute Kit 平台模型后缀为 **-ax630c**，AI Pyramid 平台后缀为 **-ax650**，LLM8850 平台后缀为 **-axcl**，具体参考参考[模型介绍](/zh_CN/stackflow/models/list)章节

#> 提示 | Qwen3-VL, InternVL 等模型支持图片输入，只需要在模型能力中勾选视觉能力。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/pictures/chatbox004.png" width="60%" />

5. 修改最大上下文消息长度为 0，注意在设置中，关闭自动生成标题功能。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/pictures/chatbox005.png" width="60%" />

6. 模型支持流式输出，部分模型支持连续对话，发送 "reset" 即可清空上下文。多模型模型，例如 **Internvl3** 可以同时传入多张图片，但每次传入新的图片前，需要先发送 “reset” 清空上下文。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/pictures/chatbox006.png" width="60%" />
