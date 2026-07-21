# Unit Tube Pressure

<span class="product-sku">SKU:U130</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_08.webp">
</PictureViewer>

## 描述

**Unit Tube Pressure** 是一款 **正负压力计**，支持 **-100 ~ 200Kpa** 宽测量范围。使用时通过导管连接，另一侧接入气体测量环境。传感器将比例映射 **-100 ~ 200Kpa** 输出 **0.1 ~ 3.1V** 电压。自带全覆盖保护外壳，有效保障传感器工作稳定性，非常适合应用于工业设备 **气体压力检测** 等场景。

## 产品特性

- 内部集成和补偿压力传感器
- 线性输出，使用简单
- 测量介质：气体
- 正负量程:-100 ~ 200Kpa
- 比例输出：0.1 ~ 3.1V
- 精度正负：1.5Kpa
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit Tube Pressure
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 设备气压测量

## 规格参数

| 规格       | 参数                  |
| ---------- | --------------------- |
| 传感器型号 | MCP-H10-B200KPPN      |
| 测量介质   | 气体                  |
| 正负量程   | -100 ~ 200Kpa         |
| 比例输出   | 0.1 ~ 3.1V            |
| 精度正负   | 1.5Kpa (0 ~ 85°C)     |
| 供电电压   | 5V                    |
| 产品尺寸   | 32.0 x 24.0 x 12.5mm  |
| 产品重量   | 4.6g                  |
| 包装尺寸   | 138.0 x 93.0 x 13.5mm |
| 毛重       | 10.0g                 |

## 操作说明

### 输出电压与压力值转换

- P: 实际测试压力值，单位 (Kpa)
- Vout: 传感器电压输出值
  \= K, B: 传感器型号 MCP-H10-B200KPPN 对应的系数值，和偏移值。 (K = 100, B = -110)
- 计算公式： P = K x Vout + B

```cpp
float K = 100.0;
float B = 110.0;
float P = analogVolts * K - B;
```

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_linear_01.webp">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_sch_01.webp" width="100%">

## 管脚映射

### Unit Tube Pressure

::grove-table
| HY2.0-4P | Black | Red | Yellow | White         |
| -------- | ----- | --- | ------ | ------------- |
| PORT.B   | GND   | 5V  | NC     | Analog Output |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/tube_pressure/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%">

## 软件开发

### Arduino

```cpp line-num
#include <Arduino.h>

int sensorPin = 36;

void setup()
{
    Serial.begin(115200);
    pinMode(sensorPin, INPUT);
    analogReadResolution(12);
    analogSetAttenuation(ADC_11db);
}

void loop()
{
    // read the analog / millivolts value:
    int analogValue = analogRead(sensorPin);
    int analogVolts = analogReadMilliVolts(sensorPin);

    // print out the values you read:
    Serial.printf("ADC analog value = %d\n", analogValue);
    Serial.printf("ADC millivolts value = %d\n", analogVolts);

    float K = 100.0;
    float B = 110.0;
    float P = analogVolts / 1000.0 * K - B;
    Serial.printf("Pressure: %f.2 Kpa \n", P);
    delay(100);  // delay in between reads for clear read from serial
}
```

### UiFlow1

- [Unit Tube Pressure UiFlow1 文档](/zh_CN/uiflow/blockly/unit/tube_pressure)

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_tube_pressure_sensor)

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/tube_pressure_video.mp4" type="video/mp4">
</video>
