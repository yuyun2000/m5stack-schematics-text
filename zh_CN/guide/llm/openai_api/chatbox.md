# Chatbox

## 安装 Chatbox

访问[Chatbox 官网](https://chatboxai.app/en)下载对应操作系统的安装包并进行安装。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/chatbox_01.jpg" width="70%" />

## 配置 Chatbox

1. 安装完成后，启动Chatbox。点击设置（Settings）选项，点击 Model Provider 下拉选项，选择 Add Custom Provider。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/chatbox_02.jpg" width="70%" />

2. 在MODEL选项卡中填写服务配置信息。

- **API Mode**：选择 `OpenAI API Compatible`  
- **API Host**：填入当前本地部署的设备IP地址，格式为`http://IP:8000/v1`
- **API Path**：设置为 `/chat/completions`  
- **API Key**：目前暂不要求填写
- **Model**：模型名称（eg: qwen2.5-0.5B-p256-ax630c）

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/chatbox_03.jpg" width="70%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/chatbox_04.jpg" width="70%" />


3. 点击CHAT选项卡，关闭以下配置选项。

- 关闭 `Auto Generate Chat Titles（自动生成聊天标题）`
- 关闭 `Inject default metadata under the CHAT tab（在 CHAT 标签下注入默认元数据）`

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/chatbox_05.jpg" width="70%" />


## 开始对话

点击 `New Chat` 创建新会话，输入信息并发送，即可收到模型回复。

?>文本长度注意事项|输入的文本长度不能超过对应模型所支持的最大长度。模型包名称包含`p256`的单次最大token输入为256，其他无特殊标记的模型单次最大token输入为128.


<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/chatbox_06.jpg" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/chatbox_07.jpg" width="70%" />









