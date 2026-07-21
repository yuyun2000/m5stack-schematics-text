# Frigate 

Frigate 是一个开源的 NVR，基于实时 AI 物体检测构建。所有处理均在您自己的硬件上本地执行，您的摄像头视频流从不会离开您的家。

1. [手动下载程序](https://huggingface.co/AXERA-TECH/frigate-resource/tree/rpi-axcl) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone -b rpi-axcl https://huggingface.co/AXERA-TECH/frigate-resource
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/frigate-resource $ ls -lh
total 2.8G
-rw-rw-r-- 1 m5stack m5stack  48M Oct  9 16:46 axcl_host_aarch64_V3.6.5_20250908154509_NO4973.deb
-rw-rw-r-- 1 m5stack m5stack  648 Oct  9 16:41 docker-compose.yml
-rw-rw-r-- 1 m5stack m5stack 2.8G Oct  9 16:46 frigate-rpi-axcl-f8f387a.tar
-rw-rw-r-- 1 m5stack m5stack 3.7K Oct  9 16:41 README.md
```

2. 导入 docker 镜像

?> 提示 | 如果没有安装 **docker**，先参考[RaspberryPi docker 安装说明](./m5_llm_8850_docker)进行安装。

```bash
docker load -i frigate-resource/frigate-rpi-axcl-f8f387a.tar # 镜像文件可能升级，以实际文件名为准。
```

3. 准备工作目录

```bash
mkdir -p ~/frigate-runtime/{config,storage}
cp frigate-resource/docker-compose.yml ~/frigate-runtime/
```

4. 启动容器

```bash
cd ~/frigate-runtime/
docker compose up -d
```

5. 通过 https://server_ip:8971 访问 Frigate 管理 Web

#>提示|默认用户名 **admin**  默认密码 **axera123456**

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/frigate1.png" width="90%" />

6. 点击设置，配置参数，填入以下内容。go2rtc:部分修改为自己的 IP Camera 地址，保存并重启。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/frigate2.png" width="90%" />

配置示例
```yml
#ffmpeg全局变量，必须
ffmpeg:
  global_args: ["-hide_banner", "-loglevel", "warning", "-threads", "1"]
  output_args:
    detect: ["-threads", "1", "-f", "rawvideo",  "-pix_fmt", "yuv420p"]

mqtt:
  enabled: false

go2rtc:
  streams:
    #主码流
    road1:
      - rtsp://192.168.20.57:8554/road1.264
    #子码流
    road1_sub:
      - rtsp://192.168.20.57:8554/road1_sub.264
cameras:
  road1:
    enabled: true
    ffmpeg:
      inputs:
        #录制流的路径，这里使用go2rtc中设置的主码流
        #调试阶段这里可以使用本地码流文件
        - path: rtsp://127.0.0.1:8554/road1
          roles:
            - record
        #检测流的路径，这里使用go2rtc中设置的辅码流
        #调试阶段这里可以使用本地码流文件
        - path: rtsp://127.0.0.1:8554/road1_sub
          roles:
            - detect
      #preset-rpi-64-h264用于解码h264码流
      #preset-rpi-64-h265用于解码h265码流
      hwaccel_args: preset-rpi-64-h264

record:
  enabled: true
 
#打开检测功能
#若不设置检测宽高，则默认使用检测码流的原生分辨率
detect:
  enabled: true
  width: 1280
  height: 720
  fps: 5
 
#配置检测引擎使用axengine
detectors:
  axengine:
    type: axengine
 
#配置axengine的目标检测模型
model:
  path: yolov5s_320
  width: 320
  height: 320
  input_pixel_format: bgr
  labelmap_path: /labelmap/coco-80.txt
 
#要跟踪的目标类型
objects:
  track:
    - person
    - car
    - bicycle
    - motorcycle
 
version: 0.16-0
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/frigate3.png" width="90%" />

可以在设置中预览配置

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/frigate4.png" width="90%" />