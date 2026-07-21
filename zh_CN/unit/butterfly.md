# Butterfly Launcher

<span class="product-sku">SKU:A041-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/butterfly/butterfly_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/butterfly/butterfly_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/butterfly/butterfly_03.webp">
</PictureViewer>

## 描述

**Butterfly Launcher** 是一个酷炫的蝴蝶模型发射器。相比旧版本的发射器，新版配备了 MEGA328 微处理器、锂电池组件、18 个彩色 LED 灯，以及提供了两个拓展端口 (分别用于电源、串口通信)。实际使用时能够同时串联多个设备，并独立控制它们。

## 产品特性

- 可串接拓展
- RGB LED
- 支持 [UiFlow](http://flow.m5stack.com) (Blockly / 图形化语言)

## 包装内容

- Butterfly Launcher
- 纸蝴蝶模型
- CONNEXT 连接线
- 橡皮筋

## 应用场景

- 时尚科技
- STEM 教育

## 规格参数

| 规格     | 参数             |
| -------- | ---------------- |
| 电池容量 | 120mA            |
| RGB LED  | x 18             |
| 通讯方式 | UART             |
| 产品重量 | 68g              |
| 毛重     | 68g              |
| 产品尺寸 | 45 x 35 x 32mm   |
| 包装尺寸 | 110 x 110 x 30mm |

## 操作说明

串行通信机制：将多个设备进行串联，为了准确的向某个设备发送指令，我们在代码中附加 "id" 变量，当指令通过控制器串行传输到设备时，每经过一个设备，变量都将进行减一操作，读取到变量为 0 的设备则执行命令. <br/>
因此，1，我们能够独立控制串行设备中的任意一个，并单独设置它们的 LED 颜色，闪烁模式，亮度和伺服状态.
2，如同下方视频所示，在 LED 灯演示时，存在着一定的延迟，假设每个设备有 100ms 的延迟，并且我们总共有 10 个，则最后一个设备将有 1s 的延迟时间。为了优化这种延迟，我们可以对第一个设备进行编程以等待最后一个设备 (由于协议的特性，延迟的产生是无法避免的)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/butterfly/butterfly_04.webp" width="30%">

### 按钮功能 (正面)

- 右：单击打开电源，双击打开电源。
- 左：长按直到 led cricle 变为另一种颜色，松开按钮。然后短按它将调整伺服臂。重复上述过程以获得正确的位置。

### 装配蝴蝶模型

<video width="500" height="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/App/Butterfly/butterfly_assembly_steps.mp4" type="video/mp4" >
</video>

### 外接电源 (在设备连接超过 10 个的情况下，会需要外接电源使其稳定)

<br/><br/> <img src="https://static-cdn.m5stack.com/resource/docs/products/unit/butterfly/butterfly_uiflow_06.webp"  width="30%">

注意:

- 1\. 在线路末端添加电源，或者使用 (HY2.0-4P-usbA 连接线 + 充电宝) 或 (HY2.0-4P-usbA 连接线 + 5V 充电头)
- 2.HY2.0-4P 2 usbA 连接线
- 3\. 带 HY2.0-4P 公端口的墙上插头

## 推荐步骤

- 1\. 使用 m5go 连接设备，在末端连接额外的电源。
- 2\. 使用 uiflow 测试代码测试线路，确保每个设备正常工作。
- 3\. 使用设备上的按钮加载蝴蝶.
- 4\. 编程 M5GO 上的按钮启动发射蝴蝶

## 管脚映射

**Mega328 ISP**下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%">

## 软件开发

### UiFlow1

- [Butterfly Launcher UiFlow1 Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Application/butterfly)

关于控制程序，我们在 UIFLow 上封装了一个特别的程序块，这使得您能够简单地编写控制程序。下面将向您展示如何在 UiFlow 上添加程序块。

- 1\. 导航到 "自定义"，单击 "打开"\* m5d
- 2\. 选择 butterfly.m5d
- 3\. 展开 Custom 选项，选择蝴蝶程序块.

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/butterfly/butterfly_uiflow_01.webp" width="30%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/butterfly/butterfly_uiflow_02.webp" width="30%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/butterfly/butterfly_uiflow_03.webp" width="30%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/butterfly/butterfly_uiflow_04.webp" width="30%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/butterfly/butterfly_uiflow_05.webp" width="30%">

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/App/Butterfly/butterfly.mp4" type="video/mp4" >
</video>
