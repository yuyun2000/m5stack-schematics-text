# M5-Bus

## 1. 简介

M5-Bus 是 M5Stack 堆叠系列产品 (Module, Base) 采用的一种堆叠拓展总线设计 (2x15P@2.54mm)。Core 系列主控设备能够通过 M5-Bus 快速堆叠不同的模块，实现功能拓展。

## 2. 管脚映射

M5-Bus 总线在一些固定编号位置，定义了一些电源相关的连接 (GND, 5V, 3V3, BAT 等), 方便兼容不同的模块与主控设备。其他部分的 IO 则根据实际的情况有所调整，因此不同的主控设备在堆叠拓展模块的时候，程序会需要根据实际使用的 IO 进行调整。

::m5-bus-table
| FUNC    | PIN  | LEFT | RIGHT | PIN  | FUNC    |
| ------- | ---- | ---- | ----- | ---- | ------- |
|         | GND  | 1    | 2     | G35  | ADC     |
|         | GND  | 3    | 4     | G36  | ADC     |
|         | GND  | 5    | 6     | RST  | EN      |
| MOSI    | G23  | 7    | 8     | G25  | DAC/SPK |
| MISO    | G19  | 9    | 10    | G26  | DAC     |
| SCK     | G18  | 11   | 12    | 3V3 |         |
| RXD0    | G3   | 13   | 14    | G1   | TXD0    |
| RXD2    | G16  | 15   | 16    | G17  | TXD2    |
| Int SDA | G21  | 17   | 18    | G22  | Int SCL |
| GPIO    | G2   | 19   | 20    | G5   | GPIO    |
| I2S_SK  | G12  | 21   | 22    | G13  | I2S_WS  |
| I2S_OUT | G15  | 23   | 24    | G0   | I2S_MK  |
|         | HPWR | 25   | 26    | G34  | I2S_IN  |
|         | HPWR | 27   | 28    | 5V   |         |
|         | HPWR | 29   | 30    | BAT  |         |
::