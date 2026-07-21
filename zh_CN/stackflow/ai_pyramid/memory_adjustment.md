# AI Pyramid 内存分配调整

## 1. 简介

**AI Pyramid** 默认出厂内存分配为 2GB RAM + 2GB CMM（AI 专用连续内存）。**AI Pyramid-Pro** 默认出厂内存分配为 2GB RAM + 6GB CMM（AI 专用连续内存）。可以在系统中，通过以下命令调整分配的大小。

1. 在终端输入以下命令：

```bash
core-config
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_pro_core_config_mem_01.png" width="70%">

2. 选择 `3 Advanced Options`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_pro_core_config_mem_02.png" width="70%">

3. 选择`A4 MEM`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_pro_core_config_mem_03.png" width="70%">

4. 输入要分配的大小。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_pro_core_config_mem_04.png" width="70%">

5. 保存并重启。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_pro_core_config_mem_05.png" width="70%">
