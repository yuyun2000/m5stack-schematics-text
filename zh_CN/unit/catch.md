# Unit Catch

<span class="product-sku">SKU:U102</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/catch/catch_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/catch/catch_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/catch/catch_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/catch/catch_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/catch/catch_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/catch/catch_06.webp">
</PictureViewer>

## 描述

**Unit Catch** 是一款由使用 SG92R 舵机作为动力源的夹爪。该舵机使用 PWM 信号驱动夹爪齿轮旋转，控制夹爪进行夹持和释放操作。结构上采用了兼容乐高 8 mm 圆孔的设计。你可以将它结合到其他的乐高组件中，搭建出创意十足的控制结构，如机械臂 、夹爪车等。

## 注意事项

!> 旋转角度 | 由于夹爪的开合角为**90°**，驱动舵机旋转角度请控制在**0-45°** (PWM: 频率 50Hz，0°-45°(pulse:0.5ms-1ms) )，防止阻转导致舵机烧毁。

## 产品特性

- SG92R 舵机
- PWM 信号驱动
- 乐高孔兼容
- 夹爪开合角度 90°
- 兼容 RoverC
- 支持输入电压: 4.2-6V
- 开发平台 [UiFlow](http://flow.m5stack.com)，[MicroPython](http://micropython.org/)，[Arduino](http://www.arduino.cc)

## 包装内容

- 1 x Unit Catch
- 1 x HY2.0-4 转接头
- 1 x RoverC.Pro 连接件

## 应用场景

- 夹爪机器人
- 舵机机械臂夹爪

## 规格参数

| 主控资源            | 参数                                       |
| ------------------- | ------------------------------------------ |
| 舵机型号            | SG92R                                      |
| 驱动信号            | PWM: 频率 50Hz，0°-45° (pulse:0.5ms-1ms) ° |
| 工作频率            | 50Hz                                       |
| 夹爪开合角度        | 90°                                        |
| 输入电压范围        | 4.2-6V                                     |
| 工作死区            | 10us                                       |
| 输出扭力            | 2.5kg/cm at 4.8V                           |
| 输出速度            | 0.1sec/60° at 4.8V                         |
| 工作温度            | 0 ~ 55°C                                   |
| 产品重量            | 21.5g                                      |
| 毛重                | 50g                                        |
| 产品尺寸 (夹爪展开) | 72 x 56 x 37mm                             |
| 包装尺寸            | 147 x 90 x 40mm                            |
| 外壳材质            | Plastic (PC)                               |

## 管脚映射

**当将 Unit Catch 连接至 PortB 时，管脚映射如下**

| M5Core (PORT B) | G26    | 5V  | GND |
| --------------- | ------ | --- | --- |
| Unit Catch      | SIGNAL | 5V  | GND |

## 尺寸图

- [Unit Catch 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1063/K121-sacle-kit.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1063/K121-sacle-kit_page_01.png" width="100%">

## 软件开发

### Arduino

- [Unit Catch Test Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/CATCH)

```cpp

/*
    Description: Control Unit Catch through PWM.
*/

#include <M5Stack.h>

//设置控制引脚
const int servoPin = 26;
//设置频率
int freq = 50;
//设置PWM通道
int ledChannel = 0;
//设置脉冲分辨率
int resolution = 10;
void setup() {
  // put your setup code here, to run once:
  M5.begin();
  M5.Power.begin();
  M5.Lcd.setCursor(100, 50, 4);
  M5.Lcd.println("Unit Catch");
  M5.Lcd.setCursor(40, 120, 4);
  ledcSetup(ledChannel, freq, resolution);
  ledcAttachPin(servoPin, ledChannel);
}

void loop() {
  // High level 0.5ms is angle 0°
  // duty = 0.5/20ms = 0.025, 0.025 x 1023≈25
    ledcWrite(ledChannel, 25);
    delay(2000);
  // High level 1ms is angle 45°
  // duty = 1/20ms = 0.05, 0.05 x 1023≈50
    ledcWrite(ledChannel, 50);
    delay(2000);
}

```

### UiFlow2

- [Unit Catch UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/catch.html)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/CATCH.mp4" type="video/mp4">
</video>
