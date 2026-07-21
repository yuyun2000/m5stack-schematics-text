# 模型列表

该接口用于获取当前设备已安装的模型服务列表。

## 模型安装与查看

1.使用前请参考对应设备的软件更新教程，完成M5Stack apt软件源信息的添加与索引更新。

- [Module LLM 镜像 & 软件升级教程](/zh_CN/guide/llm/llm/image)
- [LLM630 Compute Kit 镜像 & 软件升级教程](/zh_CN/guide/llm/llm630_compute_kit/image)


2.查看可用llm deb包列表。其中以`llm-model-name`格式命名的为模型包。

```bash
apt list | grep llm-model-
```

3.根据需求使用`apt`指令安装软件包， 如安装`llm-model-qwen2.5-0.5b-p256-ax630c`包。注意：模型将占用较大空间，建议按需安装。

```bash
apt install llm-model-qwen2.5-0.5b-p256-ax630c
```

## 查看可用模型

可在 PC 端通过 OpenAI API 查询设备当前可用的模型列表。程序执行前需将下方`base_url`的IP部分修改为设备实际IP地址。

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
