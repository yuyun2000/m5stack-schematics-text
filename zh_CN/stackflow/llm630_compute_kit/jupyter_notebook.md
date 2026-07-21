# Jupyter Notebook

#>Jupyter Notebook|LLM630 Compute Kit默认集成了[Jupyter Notebook](https://jupyter.org/), 便于用户学习和开发。本教程将提供一个简易的案例工程, 带你体验使用pyaxengine推理Yolo11n模型实现目标检测的过程。

## 1.准备工作

- 参考[LLM630 Compute Kit - Config](/zh_CN/guide/llm/llm630_compute_kit/config)教程, 学习如何为LLM630 Compute Kit配置网络与文件传输, 并获取设备IP地址。

- 下载下方LLM630 Compute Kit Jupyter Notebook 案例工程压缩包, 将其解压。

| 软件版本                                            | 下载链接                                                                                                                                                                               |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| llm630_compute_kit_jupyter_project_for_yolo11s_v1.0 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/resource/llm630_compute_kit_jupyter_project_for_yolo11s_v1.0.zip) |


## 2.访问Jupyter Notebook

同一网段下的PC可通过设备IP访问Jupyter Notebook Web页面(默认端口:8888)。

```bash
http://{IP}:8888
```

点击`Upload`将案例工程文件导入到工作区, 双击打开工程文件。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/jupyter/llm630_compute_kit_jupyter_01.jpg" width="70%" />


## 3.测试运行

?>网络|本案例在执行的过程中需要通过网络进行一些依赖包安装包, 因此要求设备具备正常网络通信条件。

根据工程文件提示，逐步执行代码块，体验使用pyaxengine推理Yolo11n模型实现目标检测。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/jupyter/llm630_compute_kit_jupyter_02.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/jupyter/llm630_compute_kit_jupyter_03.jpg" width="70%" />


