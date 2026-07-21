# OpenAI API

我们提供一套兼容 OpenAI API 的使用方式，只需要安装 StackFlow 包即可。

## 准备工作

1. 参考[RaspberryPi & LLM8850 软件包获取教程](/zh_CN/stackflow/raspberrypi/software)，完成以下模型包和软件包的安装。

```bash
sudo apt install lib-llm llm-sys llm-llm llm-openai-api
```

```bash
sudo apt install llm-model-qwen3-1.7b-int8-ctx-axcl
```

\#> 注意 |每次安装新模型后，需要手动执行 **sudo systemctl restart llm-openai-api** 更新模型列表。

## Curl 调用

```bash
curl http://127.0.0.1:8000/v1/models \
  -H "Content-Type: application/json"
```

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxxxxxxx" \
  -d '{
    "model": "qwen3-1.7B-Int8-ctx-axcl",
    "messages": [
      {"role": "developer", "content": "You are a helpful home assistant."},
      {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
  }'
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/openai000.png" width="100%" />

## Python 调用

```python
from openai import OpenAI
client = OpenAI(
    api_key="sk-",
    base_url="http://127.0.0.1:8000/v1"
)

client.models.list()
print(client.models.list())
```

```bash
from openai import OpenAI
client = OpenAI(
    api_key="sk-",
    base_url="http://127.0.0.1:8000/v1"
)

completion = client.chat.completions.create(
  model="qwen3-1.7B-Int8-ctx-axcl",
  messages=[
    {"role": "developer", "content": "You are a helpful home assistant."},
    {"role": "user", "content": "Turn on the light!"}
  ]
)

print(completion.choices[0].message)
```

## ChatBox 调用

获取 [ChatBox](https://chatboxai.app/en)

点击设置，添加模型提供方

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/chatbox001.png" width="100%" />

在API Host 填入 RaspberryPi 的 IP 和 API 路径，获取并添加已安装的模型

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/chatbox000.png" width="100%" />

创建新聊天，选择 **LLM8850** 提供的 **qwen3-1.7B-Int8-ctx-axcl** 模型

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/chatbox002.png" width="100%" />

修改最大上下文消息长度为 0

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/chatbox003.png" width="100%" />

支持设置 System Prompt

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/chatbox004.png" width="100%" />
