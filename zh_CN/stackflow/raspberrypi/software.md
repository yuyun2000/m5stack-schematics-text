# Raspberry 软件包获取

#>软件包更新 | 用于应用程序安装和升级，使用apt软件包管理工具下载和更新功能单元, 具体请参考以下操作。

## 1.准备工作

- 通过 SSH 等方式连接 RaspberryPi 设备终端。
 
## 2.更新软件源

1. 使用 **lsb_release -a** 命令获取 Raspberry 系统版本。

```bash
lsb_release -a
```

命令执行结果如下：

bookworm：

```bash
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux 12 (bookworm)
Release:	12
Codename:	bookworm
```

trixie：

```bash
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux 13 (trixie)
Release:	13
Codename:	trixie
```

2.复制以下指令，添加GPG密钥并将 M5Stack 的软件源信息添加到系统的软件源列表中。

bookworm：

```bash
sudo wget -qO /etc/apt/keyrings/StackFlow.gpg https://repo.llm.m5stack.com/m5stack-apt-repo/key/StackFlow.gpg
echo 'deb [arch=arm64 signed-by=/etc/apt/keyrings/StackFlow.gpg] https://repo.llm.m5stack.com/m5stack-apt-repo bookworm llm8850' \
| sudo tee /etc/apt/sources.list.d/StackFlow.list > /dev/null
```

trixie：

```bash
sudo wget -qO /etc/apt/keyrings/StackFlow.gpg https://repo.llm.m5stack.com/m5stack-apt-repo/key/StackFlow.gpg
echo 'deb [arch=arm64 signed-by=/etc/apt/keyrings/StackFlow.gpg] https://repo.llm.m5stack.com/m5stack-apt-repo trixie llm8850' \
| sudo tee /etc/apt/sources.list.d/StackFlow.list > /dev/null
```

3.执行apt update命令来更新软件包索引。

```bash
sudo apt update
```

## 3.安装软件包

1.查看可用llm deb包列表。其中以`llm-model-name`格式命名的为模型包，以`llm-name`命名的为功能单元包。

```bash
apt list | grep llm
```

2.根据需求使用apt指令安装软件包， 如安装llm-whisper包。注意：模型将占用较大空间，建议按需安装。

```bash
sudo apt install llm-whisper
```

有关软件包详细信息可访问[StackFlow Github](https://github.com/m5stack/StackFlow/tree/axcl/projects/llm_framework)软件包列表查看。其中包含模型配置json文件，将展示该模型来源(homepage)，功能与数据格式。

## 4. 依赖包介绍

### lib-llm

- 提供软件运行所需的环境。

```shell
sudo apt install lib-llm
```

### llm-sys

- 提供 StackFlow 的基础功能。

```shell
sudo apt install llm-sys
```

## 5. 功能模块介绍

### llm-whisper

- 提供语音转文本功能。

```shell
sudo apt install llm-whisper
```

### llm-llm

- 提供文本生成能力。

```shell
sudo apt install llm-llm
```

### llm-vlm

- 提供多模态文本生成能力。

```shell
sudo apt install llm-vlm
```

### llm-melotts

- 提供文本转语音功能。

```shell
sudo apt install llm-melotts
```

### llm-openai-api

- 提供 OpenAI API 接口。

```shell
sudo apt install llm-openai-api
```