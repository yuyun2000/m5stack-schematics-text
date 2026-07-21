# DIP Switch 引脚切换说明

## 什么是 M5-Bus

M5-Bus 是 M5Stack 堆叠系列产品（Module、Base）采用的一种堆叠拓展总线设计，接口为 2x15P@2.54mm 排针 / 排母。Core 系列主控可通过 M5-Bus 快速堆叠不同模块实现功能扩展。其固定位置定义了 GND、5V、3V3、BAT 等电源引脚，方便兼容不同设备；其他引脚则根据主控型号有所调整，使用时需根据实际引脚配置程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/M5-Bus.png" width="70%">

## 固定功能引脚

M5-Bus 的引脚序号固定由左上角的 GND 引脚开始，从 1 ~ 30 进行排序，该顺序在每个主控上都一样。其中标红框的是固定功能引脚（电源和 GND 等），其他引脚位在不同主控上的功能与 GPIO 可能不一样。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/dip_switch_m5_bus_fixed_part_01.jpg" width="100%">

## 什么是 DIP Switch

DIP Switch 是拨码开关。它用来灵活切换模块关键引脚的连接方式，以适配不同型号的主控。以 Module GPS v2.0 为例，Module GPS v2.0 有三个可切换的引脚，分别是 TXD、RXD、PPS。通过板载的两个拨码开关能够控制具体连接到的引脚。

其中，DIP Switch1 的 1-4 号开关用来控制 TXD，5-8 号开关用来控制 RXD；DIP Switch2 用来控制 PPS。

为了避免引脚冲突，通常每一个功能引脚，仅需根据实际使用需求，切换一个引脚进行连接即可。例如以下示例，将 DIP Switch1 的 1 号和 5 号开关拨到**ON**， DIP Switch2 的 2 号开关拨到**ON**，其余开关全部设置为**OFF**。

参考 PCB 板上的丝印能够得知:

- 对应主控 Basic 的 G17，Core2 的 G14，CoreS3 的 G17 引脚就会连接至 TXD。
- 对应主控 Basic 的 G16，Core2 的 G13，CoreS3 的 G18 引脚就会连接至 RXD。
- 对应主控 Basic / Core2 的 G35，CoreS3 的 G10 引脚就会连接至 PPS。

为设备编辑程序时，需要根据实际的引脚连接情况，去修改对应的引脚配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/dip_switch_m5_bus_gps_tx_connect_01.jpg" width="70%">

拨码开关对应连接到 M5-Bus 上 的位置和序号是固定的（蓝色框标注）。

若 PCB 丝印的 I/O 连接参考表中未包含您当前使用的主控型号，可参考已有设备的丝印 PinMap，确定拨码开关所连接的 M5-Bus 序号，再将其对应至当前主控的对应引脚即可。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/dip_switch_m5_bus_gps_tx_connect_02.jpg" width="100%">
