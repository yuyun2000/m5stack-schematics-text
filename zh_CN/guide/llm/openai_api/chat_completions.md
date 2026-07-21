# 会话补全

会话补全 API 接口会根据传入的信息列表来构建对话，然后通过模型生成回复。

## 案例程序

在 PC 端通过 OpenAI API 传入信息列表来构建对话。程序执行前需将下方`base_url`的IP部分修改为设备实际IP地址，并在设备中安装对应的model模型包。模型包安装教程可参考[模型列表](/zh_CN/guide/llm/openai_api/models)章节。

```python
from openai import OpenAI
client = OpenAI(
    api_key="sk-",
    base_url="http://192.168.20.186:8000/v1"
)

completion = client.chat.completions.create(
  model="qwen2.5-0.5B-p256-ax630c",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
```


### 请求参数

| 参数名称        | 类型    | 必选 | 示例值                                | 描述                                                                                                |
| --------------- | ------- | ---- | ------------------------------------- | --------------------------------------------------------------------------------------------------- |
| messages        | array   | 是   | [{"role": "user", "content": "你好"}] | 对话历史，由若干条消息组成，支持文本、图像、音频等模态（视模型而定）                                |
| model           | string  | 是   | qwen2.5-0.5B-p256-ax630c              | 用于生成回复的模型 ID。支持多个模型，请参阅[模型列表](/zh_CN/guide/llm/openai_api/models)进行选择。 |
| audio           | -       | 否   | -                                     | 当前不支持音频输出                                                                                  |
| function_call   | -       | 否   | -                                     | 当前不支持函数调用功能                                                                              |
| max_tokens      | integer | 否   | 1024                                  | 模型允许生成的最大 token 数量，超出将被截断                                                         |
| response_format | object  | 否   | "json_object"                         | 指定模型输出的格式，目前仅支持 "json_object"                                                        |


## 返回示例


```
ChatCompletionMessage(content='Hello! How can I assist you today?', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None)
```

