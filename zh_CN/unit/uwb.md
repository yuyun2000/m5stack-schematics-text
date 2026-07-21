# Unit UWB

<span class="product-sku">SKU:U100</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_09.webp">
</PictureViewer>

## 描述

**Unit UWB** 是一款具备室内定位技术的无线通信 Unit。该设计采用 Ai-Thinker BU01 模组方案 (基于 Decawave 的 DW1000 设计的超宽带 (UWB) 收发器模组 )。内置 STM32 并集成测距算法，定位精度可达 10 cm，支持 AT 指令控制。应用于室内无线测距时，以基站和标签方式进行工作 ( 基站把位置信息解算输出到标签 )。

## 产品特性

- 定位精度：10cm
- 内置 STM32 集成测距算法
- AT 指令控制
- 串口通信 (波特率：115200)
- 集成简单，无需 RF 设计
- 符合 IEEE 802.15.4-2011 UWB 标准
- 支持双向测距和 TDOA
- 开发平台: Arduino，UiFlow (Blockly，Python)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit UWB
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 室内定位 / 无线测距

## 规格参数

| 规格           | 参数                                    |
| -------------- | --------------------------------------- |
| MCU            | STM32F103C8T6                           |
| 数据传输速率   | 110 kbit/s，850 kbit/s 和 6.8 Mbit/s    |
| 频段           | 6 频段：从 3.5 GHz 至 6.5 GHz           |
| 发射功率       | -14 dBm/-10 dBm                         |
| 发射功率密度   | <-41.3dBm / MHz                         |
| 支持数据包大小 | 1023 字节                               |
| 发射功率密度   | <-41.3dBm / MHz                         |
| 调制方式       | BPM (二相调制) 与 BPSK (二进制相位调制) |
| FDMA           | 6 通道                                  |
| 产品尺寸       | 48.0 x 24.0 x 8.0mm                     |
| 产品重量       | 8.2g                                    |
| 包装尺寸       | 138.0 x 93.0 x 9.0mm                    |
| 毛重           | 13.5g                                   |

## 操作说明

\#> 注意事项 | 该 Unit 目前所搭载的固件仅支持测距信息的传输，暂不支持自定义信息传输。使用时，支持配置 4 个基站设备 (使用不同 ID)，同一时刻仅允许单个标签设备接入运行。

## 原理图

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_sch_01.webp" width="80%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_sch_02.webp" width="80%">
</SchViewer>

## 管脚映射

### Unit UWB

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 数据手册

- [AT Command](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/uwb/uwb_unit_at_command_cn.pdf)
- [BU01-specification](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/uwb/nodemcu-bu01-specification_1_14.pdf)
- [DW1000 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/uwb/dwm1000-datasheet-1.pdf)

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/uwb/model%20size.png" width="100%">

## 软件开发

### Arduino

- [Unit UWB Example](https://github.com/m5stack/M5Stack/blob/master/examples/Unit/UWB_DW1000/UWB_DW1000.ino)

### UiFlow1

- [Unit UWB UiFlow1 文档](/zh_CN/uiflow/blockly/unit/uwb)

### UiFlow2

- [Unit UWB UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/uwb.html)

### 通信协议

\#> 注意：发送每一条命令的结尾需添加回车换行 \*\*\r\n\*\*

- 设置类 AT 指令

`AT+switchdis=`value

- 命令说明：控制是否测距的开关，仅标签模式下有效
- 响应:
  - 当 value 等于 0 时，关闭测距，返回 ok.
  - 当 value 等于 1 时，开启测距，返回 ok.

`AT+interval=`value

- 命令说明：设置测距间隔
- 响应: OK

\#>**注意:**<br/>范围是 5-50 米，设置的是获取多少次数据后开始输出距离，值越大刷新速度越慢；

**AT+version?**

- 命令说明：获取厂商，模组系列和版本号
- 响应: "AIT-BU01-DB V000 T2020-4-17 OK"

**AT+RST**

- 命令说明：复位模组
- 响应: OK

`AT+anchor_tag=`model,ID

- 命令说明：设置设备的模式和 ID
- 参数:
  - Model 1 是选择 anchor 模式，0 是选择 tag 模式
  - ID 设置基站和标签的 ID
- 响应: OK

```cpp
//基站模式
AT+anchor_tag=1,0
+anchor_tag=OK

AT+RST
+RST=OK
```

```cpp
//标签模式
AT+RST
+RST=OK

AT+anchor_tag=0
+anchor_tag=OK

AT+interval=5
+interval=OK

AT+switchdis=1
+switchdis=OK

//返回测距结果
//....
```

### EasyLoader

| Easyloader                   | 下载链接                                                                                                                          | 备注 |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit UWB Example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_UWB_UNIT_With_M5Core.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UWB_VIDEO.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113620188922537&bvid=BV1BDqwYTEGh&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/YdZY9ud8ttg?si=NQh-ly2siuRvtiXl" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
