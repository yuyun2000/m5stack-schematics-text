# Unit CardKB

<span class="product-sku">SKU:U035</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb/cardkb_01.webp">
</PictureViewer>

## 描述

**Unit CardKB**是一款功能齐全的 QWERTY 键盘。如果你想要实现一些复杂的键盘输入交互，仅仅依靠 M5Core 上的 3 个按键恐怕有些难度。面对这一难题，**Unit CardKB**横空出世。

使用 **Unit CardKB**不仅能够实现全键盘输入，还支持多种按键组合 (Sym + Key，Shift + Key，Fn + Key) 输出更丰富的键值。该 **Unit** 通过 PORT A 端口 (I2C 接口) 与 M5Core 通信。I2C 地址为 0x5F。

## 产品特性

- 全键盘输入，多种按键组合.
- HY2.0-4P 接口，支持 [UiFlow](http://flow.m5stack.com) 、 [Arduino](http://www.arduino.cc)

## 包装内容

- 1 x Unit CardKB
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- M5Stack Core 的键盘外设

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 键位数量 | 50                   |
| RGB LED  | x 1                  |
| 通信接口 | I2C 通信 @ 0x5F      |
| 产品尺寸 | 88.0 x 54.0 x 5.0mm  |
| 产品重量 | 17.0g                |
| 包装尺寸 | 136.0 x 92.0 x 5.0mm |
| 毛重     | 18.0g                |

## 操作说明

**1. 按钮组合说明:**

- **按下单个按键**，键盘将输出第一键值 (字母键值则输出小写形式) . 例如，按下 "Q"，键盘将输出 "q" (小写形式) .

- **Sym+key**，键盘将输出第二键值。例如，单击 "Sym" 后，按下 "Q"，键盘将输出 "{". 双击 "Sym" 锁定功能，之后按下的任意按键都将输出第二键值。再次双击 "Sym" 进行解锁.

- **Shift+key**，键盘将输出字母的大写形式。例如，单击 "Shift" 后，按下 "Q"，键盘将输出 "Q" (大写形式) . 双击 "Shift" 锁定功能，之后按下的任意按键都将输出大写形式，再次双击 "Shift" 进行解锁.

- **Fn+key (自定义功能键组合)** ，键盘将输出第三键值。你可以自定义按下的按键其对应的功能.

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb/cardkb_02.webp">

## 管脚映射

### Unit CardKB v1.1

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### ATMega8A ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

## 软件开发

### Arduino

- [Unit CardKB Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/CardKB)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb/cardkb_arduino_01.webp">

### UiFlow1

- [Unit CardKB UiFlow1 文档](/zh_CN/uiflow/blockly/unit/cardkb)

### UiFlow2

- [Unit CardKB UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/cardkb.html)

### 内置固件

- [Unit CardKB 内置固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/CARDKB/firmware_328p/CardKeyBoard)

### 通信协议

- 协议类型 I2C
- I2C Address: **0x5F**

```cpp
/*--------------------------------------------------------------------------------------------------*/
| KEYBOARD REG       | 0x5F
| ------------------------------------------------------------------------------------------------
| keyboard_value_reg[0] 0x5F        |  R |  KEYBOARD VALUE
/*----------------------------------------------------------------------------------------------------
```

### EasyLoader

| Easyloader                      | 下载链接                                                                                       | 备注 |
| ------------------------------- | ---------------------------------------------------------------------------------------------- | ---- |
| Unit CardKB example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_CardKB.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201901/M5stack%20Cardkb.mp4" type="video/mp4">
</video>
