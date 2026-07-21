# 快速体验

## 模型 benchmark

前两步做完后，模型跑分的工具 `axcl_run_model` 就可以使用了。该工具参数较多，可以用 `axcl_run_model --help` 查看可用的参数；如果对其实现机制感兴趣，还可以检查对应的 `sample` 目录中的源码。该工具和其他 `cv & llm sample` 都是以源码形式提供的，以便用户理解 `API` 的用法。

以测试一个模型的运行速度为例，使用 `axcl_run_model -m your_model.axmodel -r 10` 这样的形式，通过 `-m` 指定要跑的模型，`-r` 指定重复次数，即可简单的跑测模型的速度。

获取模型：

```bash
wget https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/yolo11s.axmodel
```

测试：

```bash
axcl_run_model -m yolo11s.axmodel -r 10
```

执行结果如下：

```bash
m5stack@raspberrypi5:~ $ axcl_run_model -m yolo11s.axmodel -r 10
   Run AxModel:
         model: yolo11s.axmodel
          type: 3 Core
          vnpu: Disable
        warmup: 1
        repeat: 10
         batch: { auto: 1 }
    axclrt ver: 1.0.0
   pulsar2 ver: 3.2 99cf147d
      tool ver: 0.0.1
      cmm size: 10488066 Bytes
  ------------------------------------------------------
  min =   3.391 ms   max =   3.414 ms   avg =   3.402 ms
  ------------------------------------------------------
```

从以上运行示例的运行结果来看，除了能指示模型运行时间外，还能指示工具链版本、模型类型等信息。

## CV 示例

?> 注意 | 如果没有安装解压工具，请先使用以下命令安装：

```bash
sudo apt install zip
```

1. 获取 Demo：

```bash
wget https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/cv_demo.zip
```

2. 解压 Demo：

```bash
unzip cv_demo.zip
```

3. 进入目录

```bash
cd cv_demo
```

### 分类模型

以 [`imagenet`](https://image-net.org/) 数据集的 `imagenet_cat.jpg` 作为分类对象，`sample` 执行完成后会有如下输出（注意，模型和输入图像要根据实际情况微调）：

![](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/imagenet_cat.jpg)

执行命令：

```bash
./axcl_sample_classification -m mobilenetv2.axmodel -i cat.jpg
```

结果如下：

```bash
m5stack@raspberrypi5:~/cv_demo $ ./axcl_sample_classification -m mobilenetv2.axmodel -i cat.jpg
axcl initializing...
axcl inited.
Select axcl device{index: 0} as {1}.
axclrt Engine inited.
--------------------------------------
model file : mobilenetv2.axmodel
image file : cat.jpg
img height : 224
img width  : 224
--------------------------------------
282:  9.8%,  tiger cat
285:  9.8%,  Egyptian cat
283:  9.5%,  Persian cat
281:  9.4%,  tabby, tabby cat
463:  7.5%,  bucket, pail
--------------------------------------
```

### 检测模型

以 [`PASCAL VOC`](http://host.robots.ox.ac.uk/pascal/VOC/) 数据集的 voc_dog.jpg 作为检测对象，sample 执行完成后，会有如下输出（注意，模型和输入图像要根据实际情况微调）：

![](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/voc_dog.jpg)

执行命令：

```bash
./axcl_sample_yolov5s -m yolov5s.axmodel -i dog.jpg
```

结果如下：

```bash
m5stack@raspberrypi5:~/cv_demo $ ./axcl_sample_yolov5s -m yolov5s.axmodel -i dog.jpg
axcl initializing...
axcl inited.
Select axcl device{index: 0} as {1}.
axclrt Engine inited.
--------------------------------------
model file : yolov5s.axmodel
image file : dog.jpg
img height : 640
img width  : 640
--------------------------------------
post process cost time:0.61 ms
--------------------------------------
Repeat 1 times, avg time 8.10 ms, max_time 8.10 ms, min_time 8.10 ms
--------------------------------------
16:  91%, [ 138,  218,  310,  541], dog
 2:  69%, [ 470,   76,  690,  173], car
 1:  56%, [ 158,  120,  569,  420], bicycle
```

可见检测到了 3 个目标，并且给出了类别 `ID`、置信度和坐标。在 `sample` 执行的目录下，会保存一个名为 `yolov5s_out.jpg` 的检测结果，可以使用图片浏览器打开，预览输出结果。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/voc_dog_yolov5s_out.jpg" width="50%" />
