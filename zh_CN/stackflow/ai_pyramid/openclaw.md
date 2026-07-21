# AI Pyramid 部署 OpenClaw

## 1. 简介

OpenClaw 是一个开源 AI Agent 框架，可连接本地或云端大语言模型，实现自动化任务与智能交互。本文将介绍如何在 **AI Pyramid** 上进行 OpenClaw 的镜像烧录、初始化配置与首次访问。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/openclaw-deployment01.png" width="70%">

## 2. OpenClaw 镜像烧录

下载下方 OpenClaw 镜像文件，并参考 [AI Pyramid 镜像烧录](/zh_CN/stackflow/ai_pyramid/image) 完成烧录。

| 固件版本                                              | 下载链接                                                                                                                                                                   |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI_Pyramid_openclaw_emmc_ubuntu_rootfs_desktop_V3.6.4 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/AI_Pyramid_openclaw_emmc_ubuntu_rootfs_desktop_V3.6.4_20250822020158_20260306105829.axp) |

## 3. 登录设备

完成镜像烧录后，设备会自动启用 OpenClaw 初始化引导页面（仅在未完成初始化时显示）。

### 3.1 进入 Web Terminal

#### **局域网访问（推荐）**

1. 为 AI Pyramid 接通电源并连接以太网
2. 在同一局域网内的电脑上，通过浏览器访问 `https://pyramid-openclaw.local`
3. 滑动至 `Get Started` 并点击 `Open Web Terminal` 进入终端

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_01.png" width="80%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_02.png" width="80%">

#### **本地桌面访问**

将显示器、鼠标和键盘连接到 AI Pyramid 本机，在桌面浏览器中访问 `https://pyramid-openclaw.local`，操作方式与局域网访问相同。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/openclaw-deployment04.png" width="50%">

### 3.2 登录终端

在 Web Terminal 中输入用户名 `root` 和密码 `123456` 登录设备终端：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_03.png" width="80%">

## 4. OpenClaw 初始化

下面以 QuickStart 配置方式接入 `Qwen` API 为例，直接运行以下命令开始初始化（设备已预装 OpenClaw 服务）：

1. 执行初始化命令。

```bash
openclaw onboard
```

提示：初始化通常需要约 8 分钟，请耐心等待。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_04.png" width="80%">

2. 同意安全提示：阅读安全提示后，选择 `Yes` 继续：

```bash
◆ I understand this is personal-by-default and shared/multi-user use requires lock-down. Continue?
 ● Yes / ○ No
```

3. 选择配置模式：选择 `QuickStart`：

```bash
◆ Onboarding mode
│ ● QuickStart (Configure details later via openclaw configure.)
│ ○ Manual
```

4. 选择 AI 模型提供商。

本案例以 `Qwen (OAuth)` 作为示例，也可根据自己的订阅选择其他提供商：

```bash
◆ Model/auth provider
│ ○ OpenAI
│ ○ Anthropic
│ ● Qwen (OAuth)
│ ○ OpenRouter
│ ○ Skip for now
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_05.png" width="80%">

5. 完成 OAuth 认证：将显示的链接复制到浏览器中打开，完成 Qwen OAuth 认证（若无账号请先注册）：

```bash
◇ Qwen OAuth
│ Open https://chat.qwen.ai/authorize?user_code=1-_VFKMX&client=qwen-code to approve access.
│ If prompted, enter the code 1-_VFKMX.
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_06.png" width="80%">

6. 确认默认模型：认证成功后，选择 `Keep current` 保持默认模型：

```bash
◆ Default model
│ ● Keep current (qwen-portal/coder-model)
│ ○ Enter model manually
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_07.png" width="80%">

7. 跳过通道配置：选择 `Skip for now` 跳过通信通道配置：

```bash
◆ Select channel (QuickStart)
│ ○ Telegram (Bot API)
│ ○ Discord (Bot API)
│ ● Skip for now
```

8. 跳过 Skills 安装：选择 `No`，暂不安装 Skills：

```bash
◆ Configure skills now? (recommended)
│ ○ Yes / ● No
```

9. 跳过 Hooks 配置：按空格键选中 `Skip for now`，回车确认：

```bash
◆ Enable hooks?
│ ◼ Skip for now
│ ◻ 🚀 boot-md
│ ◻ 📝 command-logger
```

10. 保存 Token：初始化完成后，务必保存显示的 `token` 值。这是后续访问 OpenClaw 控制台的凭证：

```bash
◇  Dashboard ready
│  Dashboard link (with token):
│  http://127.0.0.1:18789/#token=0c4a936a196d3be5812e7624d5cb419b0b364c308f68b799
│  Copy/paste this URL in a browser on this machine to control OpenClaw.
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_08.png" width="80%">

11. 配置局域网访问：在终端依次执行以下命令，以启用局域网访问：

```bash
openclaw config set gateway.bind lan
openclaw config set gateway.controlUi.allowInsecureAuth true
openclaw config set gateway.controlUi.allowedOrigins '["http://127.0.0.1","http://127.0.0.1:18789","https://pyramid-openclaw.local"]'
openclaw config set gateway.controlUi.enabled true
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_09.png" width="80%">

12. 访问 OpenClaw 控制台：在电脑浏览器中打开控制台地址（将 `YOUR_TOKEN_VALUE` 替换为第 10 步保存的 token）：

在同一局域网内，通过以下域名加 token 参数访问：

```bash
https://pyramid-openclaw.local#token=YOUR_TOKEN_VALUE
```

?> 注意事项 | 目前不支持通过 IP 地址访问控制台，仅支持域名访问。若浏览器提示 “不是私密连接” 或其他安全警告，可点击高级选项并选择继续访问。

13. 设备配对：首次访问控制台时需要完成设备配对。在设备终端中执行以下命令查看待配对设备：

```bash
openclaw devices list
```

然后批准配对请求（将 `<requestId>` 替换为实际的设备 ID）：

注意：requestId 仅对当前浏览器有效，更换设备或浏览器后需重新查看 requestId 并重新发起配对。

```bash
openclaw devices approve <requestId>
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_10.png" width="80%">

配置完成后，网页端即可正常访问控制台。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_openclaw_setup_11.png" width="80%">

## 5. 效果演示

在 OpenClaw 控制台中提交如下任务，验证部署效果：

> 生成一个完整的俄罗斯方块网页小游戏，保存为 openclaw-deploy-game.html，然后在该文件所在目录启动本地 HTTP 服务器，并返回可访问的 URL 地址。

OpenClaw 完成任务后，复制返回的 URL 并在浏览器中打开，即可查看小游戏效果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/openclaw-deployment06.png" width="80%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/openclaw-deployment07.png" width="80%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/openclaw-deployment08.png" width="80%">

## 6. 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=116261291821667&bvid=BV1csAJzUEEM&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/KkRbzm5CtVA?si=kfc0hrrXWGbP6OEG" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>