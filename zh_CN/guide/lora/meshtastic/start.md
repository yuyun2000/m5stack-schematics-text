# 通过 M5Stack 产品使用 Meshtastic

## 1.Meshtastic 介绍

[Meshtastic](https://meshtastic.org/) 是一个开源的、基于 LoRa 无线通信技术的离网通信项目，旨在在没有蜂窝网络或互联网的环境下，实现点对点（P2P）或网状（Mesh）通信。通过超低功耗的硬件和免费频段，它支持远距离消息传输。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/meshtastic-topology.webp" width="60%">

### 核心特性

- 远距离通信：数公里范围内稳定通信
- 低功耗：适合长时间户外使用
- 端到端加密：采用 AES-256
- 网状中继：每个节点都是转发节点
- 手机支持：可通过蓝牙与手机 app 配对发送消息
- GPS 支持：部分设备带定位功能

### 工作原理

Meshtastic 使用 LoRa 无线电在免许可频段（如 433 / 470 / 868 / 915 MHz）中通信。设备之间通过广播消息建立多跳中继网络，并可通过蓝牙与手机 app 通信。每台设备既是发射器也是中继器，形成网状网络，无需依赖基站或路由器。

### 应用场景

- 户外探险：在无信号区域团队成员之间通信
- 紧急救援：灾害中快速搭建本地通信网络
- 社区互联：构建本地共享消息网络
- 物联网应用：农业传感器间数据收集

## 2. 产品配置与使用

learn>| ![Unit C6L](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/U202-Unit-C6L_10.webp) | [Unit C6L](/zh_CN/guide/lora/meshtastic/unit_c6l) | 本教程介绍如何通过 Unit C6L 使用 Meshtastic。|

## 3. 相关链接

- [Meshtastic 官网](https://meshtastic.org/)
- [Meshtastic 下载页](https://meshtastic.org/downloads/)
- [Meshtastic 文档](https://meshtastic.org/docs/introduction/)
- [iOS App 使用](https://meshtastic.org/docs/software/apple/usage/)
- [Android App 使用](https://meshtastic.org/docs/software/android/usage/)
