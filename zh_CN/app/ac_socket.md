# AC Socket

<span class="product-sku">SKU:K031</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/ac_socket/ac_socket_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/ac_socket/ac_socket_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/ac_socket/ac_socket_03.webp">
</PictureViewer>

## 描述

**AC Socket** 是一款增强型 AC 插座。支持定制 RS485 通信方式，将多个 AC 插座串联在同一 RS485 总线上，通过串行通信能够同时控制多个 AC 插座，能够应用于一般的工业应用场景。

## 产品特性

- RS485 接口
- 串行通信协议：Modbus-RTU
- 支持多个设备串行连接
- 内置 STM32F030F4P6
- 采用 BASE26 底座
- 预装 4x M3 螺母
- 输入: 100-240V
- 输出: 10A
- 电源状态指示灯

## 包装内容

- 1x AC Socket

## 应用场景

- 智能 AC 插座

## 规格参数

| 规格     | 参数            |
| -------- | --------------- |
| MCU      | STM32F030F4P6   |
| 产品重量 | 120.0g          |
| 毛重     | 158.0g          |
| 产品尺寸 | 52 x 52 x 60mm  |
| 包装尺寸 | 72 x 102 x 72mm |

## 操作说明

**AC Socket** 的整体构造由插座面板与 BASE26 底座拼接而成，底座侧面嵌入了一个 3pin 接口，这是 AC 插座的电源输入接口。

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/ac_socket/ac_socket_04.webp" width="30%">

- 顶部是 AC 插头接口，其内部的继电器控制将接通和断开电源。

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/ac_socket/ac_socket_05.webp" width="30%">

- 为了让更多的 AC 插座串联，插座的另一侧提供了 HT3.96 端子连接器（图中的橙色端子）。

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/ac_socket/ac_socket_06.webp" width="30%">

- 底部的电路板主要负责将 AC 电源 220V 转换为 DC 5V, 为微处理器 STM32F030F4 和 RS485 相关电路供电，从图中可以看出，这两部分通过 M5-Bus 插座和一对电源线连接。在插座的顶部提供了一颗红色 LED 指示灯.

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/ac_socket/ac_socket_07.webp" width="30%">

## 软件开发

### Arduino

- [AC Socket 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/AC-SOCKET)

### EasyLoader

| Easyloader                | Download                                                                                                                     | Note |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---- |
| AC Socket Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/APPLICATION/EasyLoader_AC_Socket_APPLICATION.exe) | /    |

### 通信协议

#### ACSocket Modbus RTU 协议

##### 说明:

- 1. 通信采用 RS485, 1 位起始位 + 8 位数据位 + 无校验位(NONE) + 1 位停止位
- 2. 波特率 9600
- 3.Device ID 默认为 AAH
- 4. 地址 00H 为广播地址，从机无回复

##### 指令：(十六进制)(Modbus RTU 格式)

##### 1. 写线圈

主机发送:

`AA 05 00 00 FF 00 95 E1`(闭合线圈)

`AA 05 00 00 00 00 D4 11`(断开线圈)

| 发送内容       | 字节数 | 发送报文 | 备注                                     |
| -------------- | ------ | -------- | ---------------------------------------- |
| 模块地址       | 1      | AAH      | 00H 为广播地址                           |
| 功能码         | 1      | 05H      | 写单个线圈                               |
| 起始寄存器地址 | 2      | 0000H    | 线圈 0 地址                              |
| 写入数据       | 2      | FF00H    | FF00H: 表示线圈闭合；0000H: 表示线圈断开 |
| CRC 校验       | 2      | XXXXH    | 前面所有数据的 CRC 码 (CRC16)            |

从机应答:

操作成功返回原始数据:

`AA 05 00 00 FF 00 95 E1`

操作失败返回:

`AA 85 错误码 CRC_L CRC_H`

##### 2. 读线圈

主机发送:

`AA 01 00 00 00 01 E4 11`

| 发送内容       | 字节数 | 发送报文 | 备注                          |
| -------------- | ------ | -------- | ----------------------------- |
| 模块地址       | 1      | AAH      | 00H 为广播地址                |
| 功能码         | 1      | 01H      | 读线圈                        |
| 起始寄存器地址 | 2      | 0000H    | 线圈 0 地址                   |
| 读出数量       | 2      | 0001H    | 只能为 0001H                  |
| CRC 校验       | 2      | XXXXH    | 前面所有数据的 CRC 码 (CRC16) |

从机应答:

操作成功返回:

| 地址 | 功能码 | 返回数据长度 | 线圈状态 | CRC_L | CRC_H |
| ---- | ------ | ------------ | -------- | ----- | ----- |
| AA   | 01     | 01           | 01       | B0    | 6C    |

线圈状态:`01H -> 线圈闭合` / `00H -> 线圈断开`

操作失败返回:`AA 81 错误码 CRC_L CRC_H`

##### 3. 写设备地址

主机发送:

`AA 41 00 00 00 12 A4 13`

| 发送内容       | 字节数 | 发送报文 | 备注                          |
| -------------- | ------ | -------- | ----------------------------- |
| 模块地址       | 1      | AAH      | 00H 为广播地址                |
| 功能码         | 1      | 41H      | 设置模块地址                  |
| 起始寄存器地址 | 2      | 0000H    | 地址                          |
| 模块新地址     | 1      | 12H      | 1 个字节                      |
| CRC 校验       | 2      | XXXXH    | 前面所有数据的 CRC 码 (CRC16) |

从机应答:

操作成功返回原始数据:

`AA 41 00 00 00 12 A4 13`

操作失败返回:

`AA C1 错误码 CRC_L CRC_H`

##### 4. 广播恢复设备地址

主机发送:

`00 42 00 00 A0 30`

| 发送内容       | 字节数 | 发送报文 | 备注                          |
| -------------- | ------ | -------- | ----------------------------- |
| 广播地址       | 1      | 00H      | 00H 为广播地址                |
| 功能码         | 1      | 42H      | 恢复地址为 AAH                |
| 起始寄存器地址 | 2      | 0000H    | 地址                          |
| CRC 校验       | 2      | XXXXH    | 前面所有数据的 CRC 码 (CRC16) |

从机应答:`无`

## 相关视频

<video id="example_video" controls>
   <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/App/AcSocket.mp4" type="video/mp4">
</video>
