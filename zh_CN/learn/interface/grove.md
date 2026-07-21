# Grove Port

## 1.接口颜色定义

M5Stack多数产品都采用了统一的Grove拓展接口(HY2.0-4P)规格, 并为不同的通信协议类型定义了接口的颜色。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/start/interface/grove_01.jpg" alt="" width="70%">

在不同的Unit或拓展设备上, 一般存在以下几种接口定义。

- 红色: 定义为I2C接口。
- 蓝色：定义为UART接口。
- 黑色：定义为GPIO接口, 部分引脚可能用于ADC/DAC, 或是一些特殊单总线协议。
- 白色：未定义接口, 一般为分线器或自定义接口。

#>主控设备上的Grove接口|在主控设备上的Grove拓展接口也会使用不同的颜色进行标记, 但根据主控芯片方案的不同, 其接口上的GPIO通常也支持映射成其他的功能。

## 2.管脚映射

Grove接口端子, 一般从左到右边依次定义为GND,5V与两个通信使用的IO。

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | GPIO   | GPIO  |
::

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/start/interface/grove_connect_01.png" width="70%" >



