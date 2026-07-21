# Module LoRaWAN

<span class="product-sku">SKU:M018</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lorawan/lorawan_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lorawan/lorawan_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lorawan/lorawan_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lorawan/lorawan_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lorawan/lorawan_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lorawan/lorawan_06.webp">
</PictureViewer>

## 描述

**Module LoRaWAN** 是 M5Stack 堆叠模块系列中的一款，节点通信模块。该模块集成了由 Ai-Thinker 设计的 RHF76-052 模组，它是 LoRaWAN™UART 调制解调器&兼容设备，支持 LoRaWAN 通信。你可以使用M5Core 作为主机 MCU ，然后通过简单的 AT 指令或 UART 去控制这个调制解调器。
Module LoRaWAN 基于 LoRa 远距离通信网络设计的一套通讯协议和系统架构。如果按协议分层来说 LoRaWAN 是媒体访问控制 (MAC) 层，LoRa 是物理层。它是由 LoRa 联盟维护的路由协议，主要用作管理 LPWAN 网关和端节点设备之间的通信的网络协议。 

## 产品特性

-  内置PCB天线
-  外部天线接口
-  模组: RHF76-052
-  支持双频段 433/470MHz和868/915MHz
-  Radio IC: Semtech SX1276
-  微处理器: STM32L052C8T6
-  接口: UART
-  协议:AT命令
-  嵌入式LoRaWAN协议栈
-  链路估算: 160dB
-  协议:LoRaWAN
-  UART配置: 
   - 波特率为9600
   - 8位数据位
   - 无校验位
   - 1位停止位

## 包装内容

-  1x Module LoRaWAN

## 应用场景

-  自动远程抄表
-  智能交通智能停车场
-  远程灌溉及环境监测

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 产品重量     | 16g                  |
| 毛重     | 28g                  |
| 产品尺寸 | 54.2 x 54.2 x 12.8mm |
| 包装尺寸 | 60 x 57 x 17mm       |
| 工作温度 | -40~ + 85℃           |
| 储存温度 | -40~ + 90℃，< 90％RH |


## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lorawan/lorawan_sch_01.webp" width="80%">


## 管脚映射

| RHF76-052_UART | ESP32 Chip |
| -------------- | ---------- |
| RXD            | U2TXD(G17) |
| TXD            | U2RXD(G16) |



## 数据手册

- [Module LoRaWAN 数据手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/LoRa_rhf76-052datasheet_v0.2_cn.pdf)
- [Module LoRaWAN 使用手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/lorawan_modem_-_cn.pdf)
- [Module LoRaWAN 区域参数](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/lorawantm_regional_parameters_v1.1rb_-_final.pdf)

## 软件开发

### Arduino

- [Module LoRaWAN Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/LoRaWAN_RHF76_052)

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lorawan/lorawan_07.webp">

### 通信协议

- [Module LoRaWAN AT 指令集](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/lorawan_class_ac_at_command_specification_-_v4.4.pdf)


### Easyloader


| Easyloader                                    | 下载链接                                                                                                   | 备注 |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---- |
| Module LoRaWAN Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_lorawan_receiver.exe) | /    |

