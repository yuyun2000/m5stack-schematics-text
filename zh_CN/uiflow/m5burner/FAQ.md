# M5Burner 常见问题及处理方法

## 兼容性问题

### 问题描述

在 Intel 芯片的 Mac 设备上使用 M5Burner 烧录固件时，如果出现错误提示`Error:spawn Unknown system error -86`，如下图所示，可参考以下解决方案进行处理。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/Burner-trouble-01.png" width="70%" />

### 处理步骤

1. 下载 [esptool-v5.0.1工具](https://github.com/espressif/esptool/releases/download/v5.0.1/esptool-v5.0.1-macos-amd64.tar.gz) 并解压缩，获取到`esptool`工具。

2. 在 Mac 设备上打开`Finder`，单击顶部的`Go`页签，找到`Applications`并单击打开。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/Burner-trouble-02.png" width="30%" />

3. 在`Applications`页签中找到`m5burner.app`，单击右键选择`Show Package Contents`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/Burner-trouble-03.png" width="30%" />

4. 进入`Contents/Resources/packages/tool`目录下，用步骤 1 下载的**esptool**工具替换该目录下的**esptool**工具即可。

## 启动问题

### 问题描述

启动 M5Burner 时出现没反应 / 白屏 / 无法启动 / 不显示任何固件信息的现象。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/Burner-trouble-09.png" width="70%" />

### 处理步骤

尝试更换网络、关闭代理、禁用系统防火墙。

## 登录问题

### 问题描述

登录 M5Burner 时弹出登录失败的提示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/Burner-trouble-05.png" width="40%" />

### 处理步骤

1. 检查邮箱与密码是否输入正确，若确认输入无误，可查看验证邮件。若未收到验证邮件，可联系淘宝客服，或发送邮件至 M5Stack 官方邮箱 support@m5stack.com 咨询。
2. 确保已经关闭了任何网络代理、防火墙以及广告拦截软件。

## 烧录问题

### 烧录固件时显示`Invalid Chip`。

#### 问题描述

烧录固件时显示`Invalid Chip`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/Burner-trouble-06.png" width="40%" />

#### 处理步骤

请先获取设备的 MAC 地址，随后将该地址提供给淘宝客服，或发送至 M5Stack 官方邮箱 support@m5stack.com，并同步说明相关原因。具体获取方法可参考[教程](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/How_to_provide_MAC_address-ZH.pdf)。

### 烧录固件时显示`Get mac failed`

#### 问题描述

烧录 UiFlow2 固件时出现 Get mac failed 错误提示

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/Burner-trouble-07.png" width="40%" />

#### 处理步骤

该提示通常出现在烧录 UiFlow2 固件的场景中，原因主要是设备未进入下载模式；请参照设备文档的说明操作，使设备进入下载模式即可解决。
