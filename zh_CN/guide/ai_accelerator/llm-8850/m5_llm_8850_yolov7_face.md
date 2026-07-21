# YOLOv7-Face

\#> 提示 | 参考[YOLO11章节](./m5_llm_8850_yolo11) 获取获取并解压整合包。

**运行：**

```bash
./axcl_demo/axcl_yolov7_face -m axcl_demo/yolov7-face.axmodel -i axcl_demo/selfie.jpg
```

运行结果如下：

```bash
m5stack@raspberrypi:~/rsp $ ./axcl_demo/axcl_yolov7_face -m axcl_demo/yolov7-face.axmodel -i axcl_demo/selfie.jpg
--------------------------------------
model file : axcl_demo/yolov7-face.axmodel
image file : axcl_demo/selfie.jpg
img_h, img_w : 640 640
--------------------------------------
axclrtEngineCreateContextt is done.
axclrtEngineGetIOInfo is done.

grpid: 0

input size: 1
    name:   images
        1 x 640 x 640 x 3


output size: 3
    name:      511
        1 x 80 x 80 x 63

    name:      520
        1 x 40 x 40 x 63

    name:      529
        1 x 20 x 20 x 63

==================================================

Engine push input is done.
--------------------------------------
post process cost time:7.76 ms
--------------------------------------
Repeat 1 times, avg time 12.23 ms, max_time 12.23 ms, min_time 12.23 ms
--------------------------------------
detection num: 277
 0:  91%, [1137,  869, 1283, 1065], face
 0:  91%, [1424,  753, 1570,  949], face
 0:  89%, [1305,  764, 1403,  900], face
 0:  87%, [1738,  786, 1796,  860], face
 0:  86%, [1914,  785, 1981,  865], face
 0:  86%, [ 860,  795,  967,  906], face
 0:  85%, [ 362,  891,  429,  978], face
 0:  85%, [ 280,  790,  335,  852], face
 0:  83%, [1666,  889, 1738,  969], face
 0:  83%, [  53,  869,  131,  955], face
 0:  83%, [ 447,  828,  505,  895], face
 0:  82%, [1586,  735, 1640,  801], face
 0:  82%, [ 455,  941,  528, 1037], face
 0:  81%, [1767,  905, 1834,  978], face
 0:  81%, [ 666,  798,  721,  856], face
 0:  81%, [ 203,  739,  261,  801], face
 0:  81%, [ 274,  874,  335,  953], face
 0:  81%, [  76,  721,  129,  779], face
 0:  81%, [ 462,  729,  512,  787], face
 0:  60%, [ 309,  457,  332,  487], face
 ...
 0:  20%, [1543,  563, 1574,  604], face
--------------------------------------
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/yolov7_face_out.jpg" width="80%" />
