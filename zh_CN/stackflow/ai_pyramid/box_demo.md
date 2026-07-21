# AI Pyramid - Box Demo

BoxDemo 是 AXERA 官方提供的高性能多路视频检测演示程序，支持同时处理 16 路视频流的编解码与目标检测。该程序可检测机动车、非机动车、行人及车牌等对象，并通过 Display #0 接口输出实时检测结果。AI Pyramid 可作为高效的多路视频处理算力盒子应用。

## 1. 获取测试视频

您可以选择以下方式之一获取测试视频：

**方式一：手动下载上传**

访问 [BoxDemo 测试视频集合](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/boxvideos.zip) 进行下载，随后上传到 AI Pyramid 设备。

**方式二：命令行获取**

```bash
wget https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/boxvideos.zip
```

?> 依赖检查 | 若系统未安装 **zip** 工具，请先执行 `apt install zip` 进行安装。

## 2. 部署文件

解压视频文件包并替换相应的配置文件：

```bash
unzip boxvideos.zip
rm boxvideos.zip
cp boxvideos/run.sh /opt/bin/BoxDemo/
cp boxvideos/box.conf /opt/bin/BoxDemo/
```

## 3. 运行 BoxDemo

执行启动脚本运行程序：

```bash
/opt/bin/BoxDemo/run.sh
```

?> 资源冲突提示 | 若其他程序已加载并占用 AI 模型资源，将导致 BoxDemo 初始化失败。请确保系统资源充足且没有其他 AI 应用同时运行。

程序启动后，请耐心等待完整加载。加载完成后，Display #0 接口将输出实时的多路检测视频及检测结果。

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/videos/boxdemo.mp4" type="video/mp4"></video>