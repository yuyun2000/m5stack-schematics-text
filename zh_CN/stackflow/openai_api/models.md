# 模型列表

该接口用于获取当前设备已安装的模型列表。

## 模型安装与查看

1. 使用前请参考对应设备的软件更新教程，完成 M5Stack apt 软件源信息的添加与模型列表更新。

- [Module LLM 软件升级教程](/zh_CN/stackflow/module_llm/software)
- [LLM630 Compute Kit 软件升级教程](/zh_CN/stackflow/llm630_compute_kit/software)
- [AI Pyramid 软件升级教程](/zh_CN/stackflow/ai_pyramid/software_update)

2. 查看可用 llm deb 包列表。其中以 `llm-model-name` 格式命名的为模型包。

```bash
apt list | grep llm-model-
```

3. 根据需求使用 `apt` 指令安装软件包， 如安装 `llm-model-qwen2.5-0.5b-p256-ax630c` 包。这个需要根据平台选择对应的模型。ModuleLLM/LLM630 Compute Kit 平台模型后缀为 **-ax630c**，AI Pyramid 平台后缀为 **-ax650**，LLM8850 平台后缀为 **-axcl**，具体参考[模型介绍](/zh_CN/stackflow/models/list)章节

```bash
apt install llm-model-qwen2.5-0.5b-p256-ax630c
```

## 查看可用模型

安装好的模型可直接通过 OpenAI API 查询当前设备可用的模型列表。程序执行前需将下方 `base_url` 的IP部分修改为设备实际IP地址。

\#> 注意 |每次安装新模型后，需要手动执行 **systemctl restart llm-openai-api** 更新模型列表。

## Curl 调用

```bash
curl http://127.0.0.1:8000/v1/models \
  -H "Content-Type: application/json"
```

## Python 调用

```python
from openai import OpenAI
client = OpenAI(
    api_key="sk-",
    base_url="http://192.168.20.186:8000/v1"
)

client.models.list()
print(client.models.list())
```


## 返回示例

```
SyncPage[Model](data=[
Model(id='melotts_zh-cn', created=0, object='model', owned_by='user', permission=[], root=''), 
Model(id='qwen2.5-0.5B-prefill-20e', created=0, object='model', owned_by='user', permission=[], root=''), 
Model(id='sherpa-ncnn-streaming-zipformer-20M-2023-02-17', created=0, object='model', owned_by='user', permission=[], root=''), 
Model(id='sherpa-ncnn-streaming-zipformer-zh-14M-2023-02-23', created=0, object='model', owned_by='user', permission=[], root=''), 
Model(id='single_speaker_english_fast', created=0, object='model', owned_by='user', permission=[], root=''), 
Model(id='single_speaker_fast', created=0, object='model', owned_by='user', permission=[], root=''), 
Model(id='qwen2.5-0.5B-p256-ax630c', created=0, object='model', owned_by='user', permission=[], root='')
], 
object='list')
```
