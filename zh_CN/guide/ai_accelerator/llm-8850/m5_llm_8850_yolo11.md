# YOLO11

基于 Ultralytics YOLO11 系列模型详细的模型导出、量化、编译的流程请参考[《基于 AX650N 部署 YOLO11》](https://zhuanlan.zhihu.com/p/772269394)。

[获取整合包](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/axcl_demo.zip)并上传树莓派，或在树莓派终端执行以下命令。

1. 下载

```bash
wget https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/axcl_demo.zip
```

2. 解压

```bash
unzip axcl_demo.zip
```

## YOLO11x

**运行：**

```bash
./axcl_demo/axcl_yolo11 -i axcl_demo/ssd_horse.jpg -m axcl_demo/yolo11x.axmodel
```

运行结果如下：

```bash
m5stack@raspberrypi:~/rsp $ ./axcl_demo/axcl_yolo11 -i axcl_demo/ssd_horse.jpg -m axcl_demo/yolo11x.axmodel
--------------------------------------
model file : axcl_demo/yolo11x.axmodel
image file : axcl_demo/ssd_horse.jpg
img_h, img_w : 640 640
--------------------------------------
axclrtEngineCreateContextt is done.
axclrtEngineGetIOInfo is done.

grpid: 0

input size: 1
    name:   images
        1 x 640 x 640 x 3


output size: 3
    name: /model.23/Concat_output_0
        1 x 80 x 80 x 144

    name: /model.23/Concat_1_output_0
        1 x 40 x 40 x 144

    name: /model.23/Concat_2_output_0
        1 x 20 x 20 x 144

==================================================

Engine push input is done.
--------------------------------------
post process cost time:0.88 ms
--------------------------------------
Repeat 1 times, avg time 24.69 ms, max_time 24.69 ms, min_time 24.69 ms
--------------------------------------
detection num: 6
17:  96%, [ 216,   71,  423,  370], horse
16:  93%, [ 144,  203,  196,  345], dog
 0:  89%, [ 273,   14,  349,  231], person
 2:  88%, [   1,  105,  132,  197], car
 0:  82%, [ 431,  124,  451,  178], person
19:  46%, [ 171,  137,  202,  169], cow
--------------------------------------
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/yolo11_out.jpg" width="50%" />

## YOLO11x-Seg

**运行：**

```bash
./axcl_demo/axcl_yolo11_seg -i axcl_demo/ssd_horse.jpg -m axcl_demo/yolo11x-seg.axmodel
```

运行结果如下：

```bash
m5stack@raspberrypi:~/rsp $ ./axcl_demo/axcl_yolo11_seg -i axcl_demo/ssd_horse.jpg -m axcl_demo/yolo11x-seg.axmodel
--------------------------------------
model file : axcl_demo/yolo11x-seg.axmodel
image file : axcl_demo/ssd_horse.jpg
img_h, img_w : 640 640
--------------------------------------
axclrtEngineCreateContextt is done.
axclrtEngineGetIOInfo is done.

grpid: 0

input size: 1
    name:   images
        1 x 640 x 640 x 3


output size: 7
    name: /model.23/Concat_1_output_0
        1 x 80 x 80 x 144

    name: /model.23/Concat_2_output_0
        1 x 40 x 40 x 144

    name: /model.23/Concat_3_output_0
        1 x 20 x 20 x 144

    name: /model.23/cv4.0/cv4.0.2/Conv_output_0
        1 x 80 x 80 x 32

    name: /model.23/cv4.1/cv4.1.2/Conv_output_0
        1 x 40 x 40 x 32

    name: /model.23/cv4.2/cv4.2.2/Conv_output_0
        1 x 20 x 20 x 32

    name:  output1
        1 x 32 x 160 x 160

==================================================

Engine push input is done.
--------------------------------------
post process cost time:5.62 ms
--------------------------------------
Repeat 1 times, avg time 34.72 ms, max_time 34.72 ms, min_time 34.72 ms
--------------------------------------
detection num: 6
17:  96%, [ 216,   71,  423,  370], horse
16:  93%, [ 144,  203,  196,  345], dog
 0:  89%, [ 273,   14,  349,  231], person
 2:  88%, [   1,  105,  132,  197], car
 0:  82%, [ 431,  124,  451,  178], person
19:  46%, [ 171,  137,  202,  169], cow
--------------------------------------
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/yolo11_seg_out.jpg" width="50%" />

## YOLO11x-Pose

**运行：**

```bash
./axcl_demo/axcl_yolo11_pose -i axcl_demo/football.jpg -m axcl_demo/yolo11x-pose.axmodel
```

运行结果如下：

```bash
m5stack@raspberrypi:~/rsp $ ./axcl_demo/axcl_yolo11_pose -i axcl_demo/football.jpg -m axcl_demo/yolo11x-pose.axmodel
--------------------------------------
model file : axcl_demo/yolo11x-pose.axmodel
image file : axcl_demo/football.jpg
img_h, img_w : 640 640
--------------------------------------
axclrtEngineCreateContextt is done.
axclrtEngineGetIOInfo is done.

grpid: 0

input size: 1
    name:   images
        1 x 640 x 640 x 3


output size: 6
    name: /model.23/Concat_1_output_0
        1 x 80 x 80 x 65

    name: /model.23/Concat_2_output_0
        1 x 40 x 40 x 65

    name: /model.23/Concat_3_output_0
        1 x 20 x 20 x 65

    name: /model.23/cv4.0/cv4.0.2/Conv_output_0
        1 x 80 x 80 x 51

    name: /model.23/cv4.1/cv4.1.2/Conv_output_0
        1 x 40 x 40 x 51

    name: /model.23/cv4.2/cv4.2.2/Conv_output_0
        1 x 20 x 20 x 51

==================================================

Engine push input is done.
--------------------------------------
post process cost time:0.36 ms
--------------------------------------
Repeat 1 times, avg time 25.09 ms, max_time 25.09 ms, min_time 25.09 ms
--------------------------------------
detection num: 6
 0:  94%, [1350,  337, 1632, 1036], person
 0:  93%, [ 492,  477,  658, 1000], person
 0:  92%, [ 756,  219, 1126, 1154], person
 0:  91%, [   0,  354,  314, 1108], person
 0:  73%, [   0,  530,   81, 1017], person
 0:  54%, [ 142,  589,  239, 1013], person
--------------------------------------
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/yolo11_pose_out.jpg" width="80%" />
