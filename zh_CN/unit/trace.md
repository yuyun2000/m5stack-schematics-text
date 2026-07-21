# Unit Trace

<span class="product-sku">SKU:A048</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/trace/trace_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/trace/trace_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/trace/trace_03.webp">
</PictureViewer>

## 描述

**Unit Trace** 是一款红外巡线 Unit。内置 4 组红外发光 LED 和红外敏感光电晶体管，机器人在进行移动的同时，能够实时检测地面背景颜色，并将其转化为数字信号输出到微控制器。通过程序进行路线矫正，实现巡线功能。该 Unit 与 M5Core 通过 PORT A 接口通信，I2C 地址为**0x5A**。

## 产品特性

- 工作范围：反射面距光电面小于 11mm
- HY2.0-4P 接口，支持 [UiFlow](http://flow.m5stack.com) 、 [Arduino](http://www.arduino.cc)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit Trace

## 应用场景

- 巡线机器人

## 规格参数

| 规格     | 参数             |
| -------- | ---------------- |
| 产品重量 | 32g              |
| 毛重     | 34g              |
| 产品尺寸 | 70 x 16 x 18mm   |
| 包装尺寸 | 200 x 100 x 10mm |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/trace/trace_sch_01.webp" width="80%">

## 管脚映射

### Unit Trace

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### Mega328 ISP\*\* 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

## 软件开发

### Arduino

- [Trace 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/TRACE)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/trace/trace_04.webp">

### UiFlow1

- [Trace 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/TRACE/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/trace/trace_uiflow_01.webp" width="65%">

### 内置固件

- [MEGA328 内部固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/TRACE/firmware_328p)

### Easyloader

| Easyloader            | 下载链接                                                                                      | 备注 |
| --------------------- | --------------------------------------------------------------------------------------------- | ---- |
| Trace Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_TRACE.exe) | /    |
