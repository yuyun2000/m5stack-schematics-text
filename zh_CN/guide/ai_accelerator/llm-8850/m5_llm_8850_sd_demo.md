# SD1.5-LLM8850

1. [手动下载模型](https://huggingface.co/M5Stack/SD1.5-LLM8850) 并上传到 raspberrypi5，或者通过以下命令拉取模型仓库。

?> 提示 | 如果没有安装 **git lfs**，先参考[git lfs 安装说明](./m5_llm_8850_git_lfs)进行安装。

```bash
git clone https://huggingface.co/M5Stack/SD1.5-LLM8850
```

**文件说明：**


```bash
m5stack@raspberrypi5:~/rsp/SD1.5-LLM8850 $ ls -lh
total 92K
-rw-rw-r-- 1 m5stack m5stack  12K Sep 26 11:07 api_10steps.py
-rw-rw-r-- 1 m5stack m5stack  12K Sep 26 11:07 api_server.py
-rw-rw-r-- 1 m5stack m5stack  19K Sep 26 11:07 axengine-0.1.3-py3-none-any.whl
drwxrwxr-x 2 m5stack m5stack 4.0K Sep 26 11:11 client
drwxrwxr-x 2 m5stack m5stack 4.0K Sep 26 11:11 client_jp
-rw-rw-r-- 1 m5stack m5stack  13K Sep 26 11:07 dpm20_infer.py
-rw-rw-r-- 1 m5stack m5stack 1.3K Sep 26 11:07 gen_img.py
drwxrwxr-x 4 m5stack m5stack 4.0K Sep 26 11:08 models
-rw-rw-r-- 1 m5stack m5stack 2.5K Sep 26 11:10 README.md
-rw-rw-r-- 1 m5stack m5stack  112 Sep 26 11:07 requirements.txt
-rw-rw-r-- 1 m5stack m5stack  165 Sep 26 11:07 sd-launch.desktop
-rw-rw-r-- 1 m5stack m5stack 2.4K Sep 26 11:07 sd-launch.sh
```

2. 创建虚拟环境

```bash
python -m venv sd
```

3. 激活虚拟环境

```bash
source sd/bin/activate
```

4. 安装依赖包

```bash
sudo apt install cmake -y
pip install -r requirements.txt
pip install https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc2/axengine-0.1.3-py3-none-any.whl
```

启动后端

```bash
uvicorn api_10steps:app --host 0.0.0.0 --port 7888
```

新建一个终端，启动 Web 界面

```bash
source sd/bin/activate
cd client && python app.py
```

 浏览器访问 http://127.0.0.1:5000

 <img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/sd_llm8850_001.png" width="100%" />

选择想要生成的参数或选择随机描述，点击立即生成

  <img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax8850_card/images/sd_llm8850_002.png" width="100%" />