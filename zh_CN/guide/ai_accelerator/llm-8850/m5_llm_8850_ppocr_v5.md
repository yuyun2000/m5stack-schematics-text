# PP-OCRv5

PP-OCRv5 是PP-OCR新一代文字识别解决方案，该方案聚焦于多场景、多文字类型的文字识别。在文字类型方面，PP-OCRv5支持简体中文、中文拼音、繁体中文、英文、日文5大主流文字类型，在场景方面，PP-OCRv5升级了中英复杂手写体、竖排文本、生僻字等多种挑战性场景的识别能力。

1. [手动下载模型](https://huggingface.co/AXERA-TECH/PPOCR_v5) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/PPOCR_v5
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/PPOCR_v5 $ ls -lh
total 32M
-rw-rw-r-- 1 m5stack m5stack  48K Oct 20 10:40 11.jpg
drwxrwxr-x 2 m5stack m5stack 4.0K Oct 20 10:40 ax620e
drwxrwxr-x 2 m5stack m5stack 4.0K Oct 20 10:40 ax650
-rw-rw-r-- 1 m5stack m5stack 1.3K Oct 20 10:35 cls.json
-rw-rw-r-- 1 m5stack m5stack 958K Oct 20 10:38 cls_mobile_sim_static.onnx
-rw-rw-r-- 1 m5stack m5stack    0 Oct 20 10:35 config.json
-rw-rw-r-- 1 m5stack m5stack 1.2K Oct 20 10:35 det.json
-rw-rw-r-- 1 m5stack m5stack 4.6M Oct 20 10:38 det_mobile_sim_static.onnx
-rw-rw-r-- 1 m5stack m5stack  21K Oct 20 10:35 infer_axmodel.py
-rw-rw-r-- 1 m5stack m5stack  21K Oct 20 10:35 infer_onnx.py
-rw-rw-r-- 1 m5stack m5stack  73K Oct 20 10:35 ppocrv5_dict.txt
-rw-rw-r-- 1 m5stack m5stack 4.4K Oct 20 10:35 README.md
-rw-rw-r-- 1 m5stack m5stack 1.3K Oct 20 10:35 rec.json
-rw-rw-r-- 1 m5stack m5stack  16M Oct 20 10:38 rec_mobile_sim_static.onnx
-rw-rw-r-- 1 m5stack m5stack 121K Oct 20 10:40 res_ax.jpg
-rw-rw-r-- 1 m5stack m5stack 121K Oct 20 10:40 res_onnx.jpg
-rw-rw-r-- 1 m5stack m5stack  11M Oct 20 10:36 simfang.ttf
```

2. 创建虚拟环境

```bash
python -m venv ppocr
```

3. 激活虚拟环境

```bash
source ppocr/bin/activate
```

4. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install -r requirements.txt
```

**运行：**

```bash
python infer_axmodel.py --det_model_dir ./ax650/det_npu3.axmodel --rec_model_dir ./ax650/rec_npu3.axmodel --cls_model_dir ./ax650/cls_npu3.axmodel
```

运行结果：

```bash
(ppocr) m5stack@raspberrypi:~/rsp/PPOCR_v5 $ python infer_axmodel.py \
  --det_model_dir ./ax650/det_npu3.axmodel \
  --rec_model_dir ./ax650/rec_npu3.axmodel \
  --cls_model_dir ./ax650/cls_npu3.axmodel
[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Available providers: ['AXCLRTExecutionProvider']
[INFO] 使用 provider: AXCLRTExecutionProvider
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.2 b98901c3
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.2 b98901c3
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.2 b98901c3
[[[22.0, 32.0], [307.0, 32.0], [307.0, 77.0], [22.0, 77.0]], ('纯臻营养护发素', 0.9881175756454468)]
[[[24.0, 80.0], [174.0, 80.0], [174.0, 105.0], [24.0, 105.0]], ('产品信息/参数', 0.9941993951797485)]
[[[25.0, 110.0], [333.0, 110.0], [333.0, 135.0], [25.0, 135.0]], ('(45元/每公斤，100公斤起订）', 0.9549185633659363)]
[[[24.0, 140.0], [283.0, 142.0], [283.0, 167.0], [24.0, 165.0]], ('每瓶22元，1000瓶起订）', 0.9522098898887634)]
[[[23.0, 175.0], [302.0, 174.0], [302.0, 197.0], [23.0, 198.0]], ('【品牌】：代加工方式/OEMODM', 0.98729008436203)]
[[[24.0, 206.0], [235.0, 208.0], [235.0, 229.0], [24.0, 228.0]], ('【品名】：纯臻营养护发素', 0.9895920753479004)]
[[[26.0, 238.0], [242.0, 238.0], [242.0, 259.0], [26.0, 259.0]], ('【产品编号】：YM-X-3011', 0.9853904843330383)]
[[[412.0, 233.0], [430.0, 233.0], [430.0, 303.0], [412.0, 303.0]], ('ODMOEM', 0.8154547810554504)]
[[[24.0, 269.0], [181.0, 268.0], [181.0, 289.0], [25.0, 290.0]], ('【净含量】：220ml', 0.9779437780380249)]
[[[24.0, 300.0], [253.0, 301.0], [253.0, 322.0], [24.0, 321.0]], ('【适用人群】：适合所有肤质', 0.9893492460250854)]
[[[24.0, 331.0], [345.0, 332.0], [345.0, 354.0], [24.0, 352.0]], ('【主要成分】：鲸蜡硬脂醇、燕麦β-葡聚', 0.9715114235877991)]
[[[26.0, 364.0], [283.0, 364.0], [283.0, 384.0], [26.0, 384.0]], ('糖、椰油酰胺丙基甜菜碱、泛醌', 0.9863923192024231)]
[[[367.0, 366.0], [476.0, 366.0], [476.0, 388.0], [367.0, 388.0]], ('(成品包材)', 0.8738409876823425)]
[[[25.0, 394.0], [362.0, 394.0], [362.0, 416.0], [25.0, 416.0]], ('【主要功能】：可紧致头发磷层，从而达到', 0.9911136627197266)]
[[[27.0, 426.0], [373.0, 426.0], [373.0, 447.0], [27.0, 447.0]], ('即时持久改善头发光泽的效果，给干燥的头', 0.9935663342475891)]
[[[26.0, 457.0], [137.0, 457.0], [137.0, 478.0], [26.0, 478.0]], ('发足够的滋养', 0.9879047274589539)]
```