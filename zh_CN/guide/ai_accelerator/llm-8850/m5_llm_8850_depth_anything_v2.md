# DepthAnything

DepthAnything 该模型的详细模型导出、量化、编译的流程请参考[《基于 AX650N 的 Depth Anything》](https://zhuanlan.zhihu.com/p/681378259)。

\#> 提示 | 参考[YOLO11章节](./m5_llm_8850_yolo11) 获取获取并解压整合包。

**运行：**

```bash
./axcl_demo/axcl_depth_anything -m axcl_demo/depth_anything_v2_vits_ax650.axmodel -i axcl_demo/ssd_horse.jpg
```

运行结果如下：

```bash
m5stack@raspberrypi:~/rsp $ ./axcl_demo/axcl_depth_anything -m axcl_demo/depth_anything_v2_vits_ax650.axmodel -i axcl_demo/ssd_horse.jpg
--------------------------------------
model file : axcl_demo/depth_anything_v2_vits_ax650.axmodel
image file : axcl_demo/ssd_horse.jpg
img_h, img_w : 384 640
--------------------------------------
axclrtEngineCreateContextt is done.
axclrtEngineGetIOInfo is done.

grpid: 0

input size: 1
    name:    input
        1 x 518 x 518 x 3


output size: 1
    name:   output
        1 x 1 x 518 x 518

==================================================

Engine push input is done.
--------------------------------------
post process cost time:4.18 ms
--------------------------------------
Repeat 1 times, avg time 33.24 ms, max_time 33.24 ms, min_time 33.24 ms
--------------------------------------
--------------------------------------
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/depth_anything_out.png" width="80%" />
