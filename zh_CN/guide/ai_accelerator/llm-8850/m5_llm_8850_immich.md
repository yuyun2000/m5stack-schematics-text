# Immich

Immich 是一个开源的自托管照片和视频管理平台，支持自动备份、智能搜索和跨设备访问。

1. [手动下载程序](https://huggingface.co/AXERA-TECH/immich) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/AXERA-TECH/immich
```

**文件说明：**

```bash
m5stack@raspberrypi:~/rsp/immich $ ls -lh
total 421M
drwxrwxr-x 2 m5stack m5stack 4.0K Oct 10 09:12 asset
-rw-rw-r-- 1 m5stack m5stack 421M Oct 10 09:20 ax-immich-server-aarch64.tar.gz
-rw-rw-r-- 1 m5stack m5stack    0 Oct 10 09:12 config.json
-rw-rw-r-- 1 m5stack m5stack 7.6K Oct 10 09:12 docker-deploy.zip
-rw-rw-r-- 1 m5stack m5stack 104K Oct 10 09:12 immich_ml-1.129.0-py3-none-any.whl
-rw-rw-r-- 1 m5stack m5stack 9.4K Oct 10 09:12 README.md
-rw-rw-r-- 1 m5stack m5stack  177 Oct 10 09:12 requirements.txt
```

2. 导入 docker 镜像

?> 提示 | 如果没有安装 **docker**，先参考[RaspberryPi docker 安装说明](./m5_llm_8850_docker)进行安装。

```bash
cd immich
docker load -i ax-immich-server-aarch64.tar.gz
```

3. 准备工作目录

```bash
unzip docker-deploy.zip
cp example.env .env
```

4. 启动容器

```bash
docker compose -f docker-compose.yml -f docker-compose.override.yml up -d
```

启动成功后信息如下：

```bash
m5stack@raspberrypi:~/rsp/immich $ docker compose -f docker-compose.yml -f docker-compose.override.yml up -d
WARN[0000] /home/m5stack/rsp/immich/docker-compose.override.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 3/3
 ✔ Container immich_postgres  Started                                      1.0s 
 ✔ Container immich_redis     Started                                      0.9s 
 ✔ Container immich_server    Started                                      0.9s 
```

5. 创建虚拟环境

```bash
python -m venv mich
```

6. 激活虚拟环境

```bash
source mich/bin/activate
```

7. 安装依赖包

```bash
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
pip install -r requirements.txt
pip install immich_ml-1.129.0-py3-none-any.whl # 预编译包可能升级，以实际文件名为准。
```

8. 启动 immich_ml 服务

```bash
python -m immich_ml
```

运行后信息如下：

```bash
(mich) m5stack@raspberrypi:~/rsp/immich $ python -m immich_ml
[10/10/25 09:50:12] INFO     Starting gunicorn 23.0.0                           
[10/10/25 09:50:12] INFO     Listening at: http://[::]:3003 (8698)              
[10/10/25 09:50:12] INFO     Using worker: immich_ml.config.CustomUvicornWorker 
[10/10/25 09:50:12] INFO     Booting worker with pid: 8699                      
2025-10-10 09:50:13.589360675 [W:onnxruntime:Default, device_discovery.cc:164 DiscoverDevicesForPlatform] GPU device discovery failed: device_discovery.cc:89 ReadFileContents Failed to open file: "/sys/class/drm/card1/device/vendor"
[INFO] Available providers:  ['AXCLRTExecutionProvider']
/home/m5stack/rsp/immich/mich/lib/python3.11/site-packages/immich_ml/models/clip/cn_vocab.txt
[10/10/25 09:50:16] INFO     Started server process [8699]                      
[10/10/25 09:50:16] INFO     Waiting for application startup.                   
[10/10/25 09:50:16] INFO     Created in-memory cache with unloading after 300s  
                             of inactivity.                                     
[10/10/25 09:50:16] INFO     Initialized request thread pool with 4 threads.    
[10/10/25 09:50:16] INFO     Application startup complete.  
```

在浏览器中输入 Raspberry Pi 的 IP地址和 3003 端口，例如 192.168.20.27:3003

注意，第一次访问需要注册管理员账户，帐号密码保存在本地

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/immich1.png" width="95%" />

配置完成，即可上传图片

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/immich2.png" width="95%" />

第一次需要配置机器学习服务器，参考下图进入配置

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/immich3.png" width="95%" />

URL 填写为 Raspberry Pi 的 IP地址和 3003 端口，例如 192.168.20.27:3003

CLIP 模型如果使用中文搜索，填写为 **ViT-L-14-336-CN__axera** 如果使用英文搜索填写为 **ViT-L-14-336__axera**

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/immich4.png" width="95%" />

设置完成后，保存

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/immich5.png" width="95%" />

第一次需要手动进入 Jobs 选项，在 SMART SEARCH 中手动触发

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/immich6.png" width="95%" />

在搜索栏输入图片的描述，即可检索相关的图片

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/immich7.png" width="95%" />