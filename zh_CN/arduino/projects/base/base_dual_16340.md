# Base Dual 16340 Arduino 使用教程

## 1. 准备工作

- 1\. 环境配置：参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 2\. 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

\#> 库说明 | M5GFX 已作为 M5Unified 的依赖包含在内，通常情况下只需安装 M5Unified 即可。若编译时提示缺少 M5GFX，再单独安装。

- 3\. 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Base Dual 16340](https://shop.m5stack.com/products/base-dual-16340-1400-mah)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1251/A179_Base_Dual_16340_main_pictures_02.webp" width="20%"/>

## 2. 注意事项

\#> 电池安装与供电 | 请先确认两节 16340 电池的正负极安装正确，再将底座拨动开关切换到 `ON`。虽然底座带有保护电路，但不建议在通电状态下频繁插拔电池。

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/base/Base_Dual_16340)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="A179" type="BASE"></ProductCompatible>

## 3. 案例程序

- 本教程中使用的主控设备为 CoreS3，搭配 Base Dual 16340。底座板载 INA226 通过内部 I2C 总线与主控通信，参考 CoreS3 与底座的堆叠引脚定义，示例中使用的 I2C 引脚为 `G12 (SDA)`、`G11 (SCL)`。

```cpp line-num
#include "M5Unified.h"

// INA226 current/voltage monitor on internal I2C bus(M5.In_I2C)
// INA226 I2C address: 0x45
m5::INA226_Class Ina226(0x45);
bool ina226Ready = false;

void setup()
{
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);

    // Initialize INA226 at I2C address 0x45
    if (Ina226.begin()) {
        ina226Ready = true;
        M5.Display.setCursor(10, 10);
        M5.Display.print("INA226 found!");

        // Configure INA226 measurement parameters
        m5::INA226_Class::config_t ina_cfg;

        // Shunt resistor value: 20mΩ (Fixed value for Base Dual 16340)
        ina_cfg.shunt_res = 0.02f;
        // Maximum expected current: 3A — used by the chip to set the calibration register
        ina_cfg.max_expected_current = 3.0f;
        // Operating mode: continuous measurement of both bus voltage and shunt voltage
        ina_cfg.mode = m5::INA226_Class::Mode::ShuntAndBus;
        // ADC sampling rate: average 16 samples per reading for noise reduction
        ina_cfg.sampling_rate = m5::INA226_Class::Sampling::Rate16;
        // Bus voltage conversion time: 1.1 ms per sample
        ina_cfg.bus_conversion_time = m5::INA226_Class::ConversionTime::US_1100;
        // Shunt voltage conversion time: 1.1 ms per sample
        ina_cfg.shunt_conversion_time = m5::INA226_Class::ConversionTime::US_1100;
        // Apply all configuration settings to the INA226
        Ina226.config(ina_cfg);
    } else {
        M5.Display.setCursor(10, 10);
        M5.Display.print("INA226 not found!");
    }
}

void loop()
{
    M5.update();
    M5.Display.clear();

    if (!ina226Ready) {
        M5.Display.setCursor(10, 10);
        M5.Display.print("INA226 not found!");
        delay(1000);
        return;
    }

    // VBUS is wired to BUS_BAT, so this is the battery output bus voltage.
    float batteryVoltage_V = Ina226.getBusVoltage();
    float batteryVoltage_mV = batteryVoltage_V * 1000.0f;
    M5.Display.setCursor(10, 10);
    M5.Display.printf("Battery Voltage: %.0fmV", batteryVoltage_mV);

    // Current through the shunt resistor is the battery current if no bypass path exists.
    float batteryCurrent_A = Ina226.getShuntCurrent();
    float batteryCurrent_mA = batteryCurrent_A * 1000.0f;
    M5.Display.setCursor(10, 40);
    M5.Display.printf("Battery Current: %.1fmA", batteryCurrent_mA);

    // Voltage drop across the 20mΩ shunt resistor.
    float shuntVoltage_mV = Ina226.getShuntVoltage() * 1000.0f;
    M5.Display.setCursor(10, 70);
    M5.Display.printf("Shunt Voltage: %.3fmV", shuntVoltage_mV);

    float shuntCurrent_mA = batteryCurrent_mA;
    M5.Display.setCursor(10, 100);
    M5.Display.printf("Shunt Current: %.1fmA", shuntCurrent_mA);

    // INA226 calculates power from bus voltage and calibrated shunt current.
    float batteryPower_mW = Ina226.getPower() * 1000.0f;
    M5.Display.setCursor(10, 130);
    M5.Display.printf("Battery Power: %.1fmW", batteryPower_mW);

    delay(1000);
}
```

## 4. 编译上传

- 1\. 进入下载模式：CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

#> 说明| 不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1251/A179_Base_Dual_16340_Arduino_pictures_01.png" width="70%">

## 5. 电池监测效果

程序成功上传后，主控屏幕将实时循环显示电池的电压、电流、功率等信息，方便用户对电池的使用状态进行监测。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1251/A179_Base_Dual_16340_Arduino_pictures_02.jpg" width="30%">


