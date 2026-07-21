# Hat CardKB

<span class="product-sku">SKU:U077</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/hat-cardkb_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/hat-cardkb_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/hat-cardkb_03.webp">
</PictureViewer>

## 描述

**Hat CardKB**是一款功能齐全的 QWERTY 键盘。如果你想要实现一些复杂的键盘输入交互，单纯依靠 M5StickC 上的按键实现起来很有难度，为了解决这一问题我们推出了**Hat CardKB**。

使用**Hat CardKB**不仅能够实现全键盘输入，还支持多种按键组合（Shift + Key，Fn + Key）输出更丰富的键值，一颗板载彩色 LED 能根据按键的输入模式会发出不同颜色的灯光提示，**Hat CardKB**的 I2C 地址为 0x5F。

## 产品特性

- 全键盘输入，多种按键组合.
- 小巧便携

## 包装内容

- 1 x Hat CardKB

## 应用场景

- M5StickC 键盘输入外设

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 通信接口 | I2C 通信 @ 0x5F       |
| 产品尺寸 | 84.6 x 54.2 x 6.5mm   |
| 产品重量 | 17.0g                 |
| 包装尺寸 | 115.0 x 96.0 x 40.0mm |
| 毛重     | 21.0g                 |

**按钮组合说明:**

- **按下单个按键**(蓝灯亮一次), 键盘将输出第一键值 (字母键值则输出小写形式). 例如，按下 "Q", 键盘将输出 "q"(小写形式).

- **双击 Shift 或 fn**, 锁定 Shift (红灯常亮) 或 Fn (绿灯常亮), 方便多次输出第二或第三键值

- **Shift+key**(红灯闪烁), 键盘将输出字母的大写形式，复用按键将输出第二键值。例如，单击 "Shift" 后，按下 "Q", 键盘将输出 "Q"(大写形式). 双击 "Shift" 锁定功能，之后按下的任意字母按键都将输出大写形式，按下的数字和符号按键输出第二键值，再次单击 "Shift" 进行解锁.

- **Fn+key (自定义功能键组合)**(绿灯闪烁), 键盘将输出第三键值。你可以自定义按下的按键其对应的功能.

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/hat-cardkb_04.webp">

## 管脚映射

**Mega328 ISP**下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

## 软件开发

### Arduino

- [Hat CardKB Example](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/CardKB)

### UiFlow1

- [Hat CardKB UiFlow1 文档](/zh_CN/uiflow/blockly/hat/cardkb)

### UiFlow2

- [Hat CardKB UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/cardkb.html)

### 内置固件

- [Hat CardKB 内置固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Hat/CardKB_HAT/firmware_328p/cardKB_HAT)

### 通信协议

- 协议类型 I2C
- I2C Address: **0x5F**

```cpp
/*--------------------------------------------------------------------------------------------------*/
| KEYBOARD REG       | 0x5F
| ------------------------------------------------------------------------------------------------
| keyboard_value_reg[0]        |  R |  KEYBOARD VALUE
/*----------------------------------------------------------------------------------------------------
```

### EasyLoader

| Easyloader            | 下载链接                                                                                                 | 备注 |
| --------------------- | -------------------------------------------------------------------------------------------------------- | ---- |
| Hat CardKB Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/CardKB/EasyLoader_CardKB_HAT.exe) | /    |

## 相关视频

**Hat CardKB 的使用演示**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/CardKB_HAT.mp4" type="video/mp4">
</video>
