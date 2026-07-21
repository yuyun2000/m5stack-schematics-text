# YOLO World

## YOLO World v2

YOLO-Worldv2 该模型的详细模型导出、量化、编译的流程请参考[《再谈 YOLO World 部署》](https://zhuanlan.zhihu.com/p/721856217)。

- 模型：yoloworldv2_4cls_50_npu3.axmodel
- 输入图片：ssd_horse.jpg
- 输入文本：dog.bin, 对应的 4 分类 'dog' 'horse' 'sheep' 'cow'

\#> 提示 | 参考[YOLO11章节](./m5_llm_8850_yolo11) 获取获取并解压整合包。

**运行**

```bash
./axcl_demo/axcl_yolo_world_open_vocabulary -m axcl_demo/yoloworldv2_4cls_50_npu3.axmodel -t axcl_demo/dog.bin -i axcl_demo/ssd_horse.jpg
```

运行结果如下：

```bash
m5stack@raspberrypi:~/rsp $ ./axcl_demo/axcl_yolo_world_open_vocabulary -m axcl_demo/yoloworldv2_4cls_50_npu3.axmodel -t axcl_demo/dog.bin -i axcl_demo/ssd_horse.jpg
--------------------------------------
model file : axcl_demo/yoloworldv2_4cls_50_npu3.axmodel
image file : axcl_demo/ssd_horse.jpg
text_feature file : axcl_demo/dog.bin
img_h, img_w : 640 640
--------------------------------------
axclrtEngineCreateContextt is done.
axclrtEngineGetIOInfo is done.

grpid: 0

input size: 2
    name:   images
        1 x 640 x 640 x 3

    name: txt_feats
        1 x 4 x 512


output size: 3
    name:  stride8
        1 x 80 x 80 x 68

    name: stride16
        1 x 40 x 40 x 68

    name: stride32
        1 x 20 x 20 x 68

==================================================

Engine push input is done.
--------------------------------------
post process cost time:0.25 ms
--------------------------------------
Repeat 1 times, avg time 4.52 ms, max_time 4.52 ms, min_time 4.52 ms
--------------------------------------
detection num: 2
 1:  91%, [ 215,   71,  421,  374], class2
 0:  67%, [ 144,  204,  197,  346], class1
--------------------------------------
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/yolo_world_out.jpg" width="50%" />

## YOLO World v2 CLI

[获取源码](https://github.com/AXERA-TECH/yoloworld.axera) 并上传到 raspberrypi5 或使用 git 命令拉取。

1. 拉取代码

```bash
git clone https://github.com/AXERA-TECH/yoloworld.axera.git
```

2. 进入项目目录

```bash
cd yoloworld.axera
```

?> 提示 | 后续操作在此目录执行。

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/yoloworld.axera $ ls -lh
total 36K
-rwxrwxr-x 1 m5stack m5stack 2.1K Aug 12 11:26 build_aarch64.sh
-rwxrwxr-x 1 m5stack m5stack  775 Aug 12 11:26 build.sh
-rw-rw-r-- 1 m5stack m5stack 1.5K Aug 12 11:26 CMakeLists.txt
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 11:26 include
drwxrwxr-x 3 m5stack m5stack 4.0K Aug 12 14:46 pyyoloworld
-rw-rw-r-- 1 m5stack m5stack 1.9K Aug 12 11:26 README.md
drwxrwxr-x 4 m5stack m5stack 4.0K Aug 12 11:26 src
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 11:26 tests
drwxrwxr-x 2 m5stack m5stack 4.0K Aug 12 11:26 toolchains

```

3. 安装依赖

```bash
sudo apt update
sudo apt install cmake libopencv-dev -y
```

4. 编译代码

```bash
mkdir build && cd build
cmake .. && make -j4 install
cd ..
```

5. 获取模型和词表

```bash
wget https://github.com/AXERA-TECH/yoloworld.axera/releases/download/v0.1/clip_b1_u16_ax650.axmodel
wget https://github.com/AXERA-TECH/yoloworld.axera/releases/download/v0.1/yolo_u16_ax650.axmodel
wget https://github.com/AXERA-TECH/yoloworld.axera/releases/download/v0.1/vocab.txt
```

6. 运行

```bash
./build/test_detect_by_text --yoloworld yolo_u16_ax650.axmodel --tenc clip_b1_u16_ax650.axmodel -v vocab.txt -i ssd_horse.jpg --classes person,car,dog,horse
```

运行结果如下：

```bash
m5stack@raspberrypi:~/rsp/yoloworld.axera $ ./build/test_detect_by_text --yoloworld yolo_u16_ax650.axmodel --tenc clip_b1_u16_ax650.axmodel -v vocab.txt -i ssd_horse.jpg --classes person,car,dog,horse
open libax_sys.so failed
open libax_engine.so failed
[I][                             run][  31]: AXCLWorker start with devid 0
label-0 class_names: person
label-1 class_names: car
label-2 class_names: dog
label-3 class_names: horse
yoloworld_path: yolo_u16_ax650.axmodel
text_encoder_path: clip_b1_u16_ax650.axmodel
tokenizer_path: vocab.txt

input size: 2
    name:   images [unknown] [unknown]
        1 x 640 x 640 x 3   size: 1228800

    name: txt_feats [unknown] [unknown]
        1 x 4 x 512   size: 8192


output size: 3
    name:  stride8
        1 x 80 x 80 x 68   size: 1740800

    name: stride16
        1 x 40 x 40 x 68   size: 435200

    name: stride32
        1 x 20 x 20 x 68   size: 108800

[I][                       yw_create][ 408]: num_classes: 4, num_features: 512, input w: 640, h: 640
is_output_nhwc: 1

input size: 1
    name: text_token [unknown] [unknown]
        1 x 77   size: 308


output size: 1
    name:     2202
        1 x 1 x 512   size: 2048

[I][               load_text_encoder][  44]: text feature len 512
[I][                  load_tokenizer][  60]: text token len 77
[I][                  yw_set_classes][ 463]: label-0 class_names: person
[I][                  yw_set_classes][ 463]: label-1 class_names: car
[I][                  yw_set_classes][ 463]: label-2 class_names: dog
[I][                  yw_set_classes][ 463]: label-3 class_names: horse
yw_set_classes time: 12.76 ms
preprocess 1.04
inference 19.06
postprocess 0.27
yw_detect time: 20.45 ms
object-0 class_id: 3 score: 0.88 box: 215 69 206 304
object-1 class_id: 0 score: 0.88 box: 271 13 76 220
object-2 class_id: 0 score: 0.77 box: 430 123 20 54
object-3 class_id: 2 score: 0.75 box: 144 203 52 143
object-4 class_id: 1 score: 0.65 box: 0 105 131 91
object-5 class_id: 0 score: 0.37 box: 402 130 7 16
object-6 class_id: 0 score: 0.16 box: 413 134 13 16
[I][                             run][  81]: AXCLWorker exit with devid 0
[2025-08-12 16:00:53.491][55020][C][device][print][18]: allocated device memories: 7
[2025-08-12 16:00:53.491][55020][C][device][print][20]: [0x1497ae000] : 0x134 bytes
[2025-08-12 16:00:53.491][55020][C][device][print][20]: [0x1495de000] : 0x1a900 bytes
[2025-08-12 16:00:53.491][55020][C][device][print][20]: [0x1497af000] : 0x800 bytes
[2025-08-12 16:00:53.491][55020][C][device][print][20]: [0x149573000] : 0x6a400 bytes
[2025-08-12 16:00:53.491][55020][C][device][print][20]: [0x1493ca000] : 0x1a9000 bytes
[2025-08-12 16:00:53.491][55020][C][device][print][20]: [0x1493c8000] : 0x2000 bytes
[2025-08-12 16:00:53.491][55020][C][device][print][20]: [0x14929c000] : 0x12c000 bytes
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/yoloworldv2.jpg" width="50%" />

## YOLO World v2 Web

1. 创建虚拟环境

```bash
python -m venv yolo
```

2. 激活虚拟环境

```bash
source yolo/bin/activate
```

3. 安装依赖包

```bash
pip install -r pyyoloworld/requirements.txt
```

4. 复制动态库

```bash
cp build/libyoloworld.so pyyoloworld/
```

5. 启动服务

```bash
python pyyoloworld/gradio_example.py --yoloworld yolo_u16_ax650.axmodel --tenc clip_b1_u16_ax650.axmodel --vocab vocab.txt
```

正在运行后信息如下：

```bash
(yolo) m5stack@raspberrypi:~/rsp/yoloworld.axera $ python pyyoloworld/gradio_example.py --yoloworld yolo_u16_ax650.axmodel --tenc clip_b1_u16_ax650.axmodel --vocab vocab.txt
Trying to load: /home/m5stack/rsp/yoloworld.axera/pyyoloworld/aarch64/libyoloworld.so

❌ Failed to load: /home/m5stack/rsp/yoloworld.axera/pyyoloworld/aarch64/libyoloworld.so
   /home/m5stack/rsp/yoloworld.axera/pyyoloworld/aarch64/libyoloworld.so: cannot open shared object file: No such file or directory
🔍 File not found. Please verify that libclip.so exists and the path is correct.

Trying to load: /home/m5stack/rsp/yoloworld.axera/pyyoloworld/libyoloworld.so
open libax_sys.so failed
open libax_engine.so failed
✅ Successfully loaded: /home/m5stack/rsp/yoloworld.axera/pyyoloworld/libyoloworld.so
[I][                             run][  31]: AXCLWorker start with devid 0

input size: 2
    name:   images [unknown] [unknown]
        1 x 640 x 640 x 3   size: 1228800

    name: txt_feats [unknown] [unknown]
        1 x 4 x 512   size: 8192


output size: 3
    name:  stride8
        1 x 80 x 80 x 68   size: 1740800

    name: stride16
        1 x 40 x 40 x 68   size: 435200

    name: stride32
        1 x 20 x 20 x 68   size: 108800

[I][                       yw_create][ 408]: num_classes: 4, num_features: 512, input w: 640, h: 640
is_output_nhwc: 1

input size: 1
    name: text_token [unknown] [unknown]
        1 x 77   size: 308


output size: 1
    name:     2202
        1 x 1 x 512   size: 2048

[I][               load_text_encoder][  44]: text feature len 512
[I][                  load_tokenizer][  60]: text token len 77
* Running on local URL:  http://0.0.0.0:7860
* To create a public link, set `share=True` in `launch()`.
```

6. 在浏览器中打开 127.0.0.1:7860，添加图片，输入要检测的类别，点击**检测**

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/yoloworld_web.png" width="90%" />
