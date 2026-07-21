# DEIMv2

1. [手动下载模型](https://huggingface.co/AXERA-TECH/DEIMv2) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/DEIMv2
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/DEIMv2 $ ls -lh
total 19M
-rw-rw-r-- 1 m5stack m5stack 8.9K Nov 10 10:11 axmodel_inf.py
-rw-rw-r-- 1 m5stack m5stack    0 Nov 10 10:11 config.json
-rw-rw-r-- 1 m5stack m5stack  18M Nov 10 10:11 deimv2_dinov3_s_coco.axmodel
-rw-rw-r-- 1 m5stack m5stack  87K Nov 10 10:11 onboard_result.jpg
-rw-rw-r-- 1 m5stack m5stack 261K Nov 10 10:11 people.jpg
-rw-rw-r-- 1 m5stack m5stack  888 Nov 10 10:11 README.md
```

2. 创建虚拟环境

```bash
python -m venv deim
```

3. 激活虚拟环境

```bash
source deim/bin/activate
```

4. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install opencv-python torch torchvision
```

5. 运行

```bash
python3 axmodel_inf.py --axmodel deimv2_dinov3_s_coco.axmodel --input people.jpg -ms n
```

运行结果：

```bash
(deim) m5stack@raspberrypi:~/rsp/DEIMv2 $ python3 axmodel_inf.py --axmodel deimv2_dinov3_s_coco.axmodel --input people.jpg -ms n
[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.2 8a28aa57
Image processing complete. Result saved as 'result.jpg'.
```

原图：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/deimv2_people.jpg" width="60%" />

输出：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/deimv2_result.jpg" width="60%" />