# NPU 示例

## NPU 工具链

经常在 AI 芯片上部署算法模型的同学都知道，想要把模型部署到芯片上的 NPU 中运行，都需要使用芯片原厂提供的 NPU 工具链，这里我们使用的是 Pulsar2。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/pulsar2.png" width="95%" />

- [Pulsar2 在线文档](https://pulsar2-docs.readthedocs.io/zh-cn/latest/index.html)

  - [安装指导](https://pulsar2-docs.readthedocs.io/zh-cn/latest/user_guides_quick/quick_start_prepare.html)
  - [快速上手](https://pulsar2-docs.readthedocs.io/zh-cn/latest/user_guides_quick/quick_start_ax650.html)
  - [NPU 算子支持列表](https://pulsar2-docs.readthedocs.io/zh-cn/latest/appendix/op_support_list_ax650.html)
  - [大模型转换](https://pulsar2-docs.readthedocs.io/zh-cn/latest/appendix/build_llm.html)

## AXCL-Samples

AXCL-Samples 由 爱芯元智 主导开发。该项目实现了常见的深度学习开源算法在基于**爱芯元智**的 SoC 实现的**PCIE 算力卡**产品上运行的示例代码，方便社区开发者进行快速评估和适配。

- [axcl-samples](https://github.com/AXERA-TECH/axcl-samples)
- 该仓库采用最简单的方式展示常用的开源模型，例如 Ultralytics 的 YOLO 系列，DepthAnything，YOLO-Worldv2 等等。

### 获取示例

- AXCL-Samples 的预编译 ModelZoo 请参考：
  - [百度网盘](https://pan.baidu.com/s/1cnMeqsD-hErlRZlBDDvuoA?pwd=oey4)
  - [Hugging Face](https://huggingface.co/collections/AXERA-TECH/vision-models-67b0bce92ddc61229e8e94ed)
  - [模型和程序 OSS 下载](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/axcl_demo.zip)
  - [模型和程序 Hugging Face 下载](https://huggingface.co/M5Stack/axcl_demo)

## LLM 示例

- 模型转换请参考[大模型编译文档](https://pulsar2-docs.readthedocs.io/zh-cn/latest/appendix/build_llm.html)
- 预编译 ModelZoo-LLM 请参考[百度网盘](https://pan.baidu.com/s/1grJNjcpUln-fDBisJxuvCA?pwd=mys8) [Hugging Face](https://huggingface.co/AXERA-TECH/models)
