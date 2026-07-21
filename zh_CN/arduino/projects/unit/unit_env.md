# Unit ENV Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5UnitUnified](https://github.com/m5stack/M5UnitUnified)
  - [M5Unit-ENV](https://github.com/m5stack/M5Unit-ENV)

#>驱动库|Unit ENV/II/III/IV/PRO 虽然主要的传感器IC方案有些差异，但在 M5Unit-ENV 库中都有相应的驱动与案例，能够非常方便的实现传感器数据读取。

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit ENV-IV](https://shop.m5stack.com/products/env-iv-unit-with-temperature-humidity-air-pressure-sensor-sht40-bmp280)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENV%E2%85%A3%20Unit/img-d658b7f3-ab10-463b-acfd-a182a6b05e59.webp" width="20%">

#>依赖库|以上驱动库如`M5UnitUnified`，`M5Unit-ENV`等在安装时需要其他的依赖库(如[M5HAL](https://github.com/m5stack/M5HAL), [M5Utility](https://github.com/m5stack/M5Utility)等), 如果通过Arduino库管理进行安装时, 请根据提示, 安装全部依赖。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/723/unit_env_arduino_lib_install_01.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/723/unit_env_arduino_lib_install_02.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/723/unit_env_arduino_lib_install_03.jpg" width="70%">


## 2.案例程序

#>案例说明 | 本案例以 Unit ENV-IV 为例，实现温湿度数据读取。如果使用的是 Unit ENV-III 可通过切换`USING_ENV3`注释来启用不同的实例。使用其他型号的 Unit ENV 可参考下方链接查看更多案例程序。

- [M5Unit-ENV - Examples](https://github.com/m5stack/M5Unit-ENV/tree/master/examples)

```cpp line-num
#include <M5Unified.h>
#include <M5UnitUnified.h>
#include <M5UnitUnifiedENV.h>

M5Canvas canvas(&M5.Display);

m5::unit::UnitUnified Units;

// #define USING_ENV3
#define USING_ENV4

#if defined(USING_ENV3)

m5::unit::UnitENV3 unitENV3;
auto& sht30   = unitENV3.sht30;
auto& qmp6988 = unitENV3.qmp6988;

#elif defined(USING_ENV4)

m5::unit::UnitENV4 unitENV4;
auto& sht40  = unitENV4.sht40;
auto& bmp280 = unitENV4.bmp280;

#endif

float calculate_altitude(const float pressure, const float seaLvhPa = 1013.25f)
{
    return 44330.f * (1.0f - pow((pressure / 100.f) / seaLvhPa, 0.1903f));
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    M5.Display.setFont(&fonts::lgfxJapanMinchoP_20);
    M5.Display.setTextSize(1);
    auto pin_num_sda = M5.getPin(m5::pin_name_t::port_a_sda);
    auto pin_num_scl = M5.getPin(m5::pin_name_t::port_a_scl);
    M5_LOGI("getPin: SDA:%u SCL:%u", pin_num_sda, pin_num_scl);

    Wire.begin(pin_num_sda, pin_num_scl, 400000U);

#if defined(USING_ENV3)
    if (!Units.add(unitENV3, Wire) || !Units.begin()) {
        M5_LOGE("Failed to begin Unit ENV3");
        M5.Display.clear(TFT_RED);
        while (true) {
            m5::utility::delay(10000);
        }
    }

#elif defined(USING_ENV4)
    if (!Units.add(unitENV4, Wire) || !Units.begin()) {
        M5_LOGE("Failed to begin Unit ENV4");
        M5.Display.clear(TFT_RED);
        while (true) {
            m5::utility::delay(10000);
        }
    }

#endif
}

void loop()
{
    M5.update();
    Units.update();
#if defined(USING_ENV3)

    if (sht30.updated()) {
        M5.Display.setCursor(0, 0);
        M5.Display.fillRect(0, 0, 320, 80, TFT_BLACK);
        M5.Display.printf(
            "\n>SHT30Temp:%.4f\n"
            ">Humidity:%.4f",
            sht30.temperature(), sht30.humidity());
    }
    if (qmp6988.updated()) {
        M5.Display.setCursor(0, 80);
        M5.Display.fillRect(0, 80, 320, 80, TFT_BLACK);
        auto p = qmp6988.pressure();
        M5.Display.printf(
            "\n>QMP6988Temp:%.4f\n"
            ">Pressure:%.4f\n"
            ">Altitude:%.4f",
            qmp6988.temperature(), p * 0.01f /* To hPa */, calculate_altitude(p));
    }

#elif defined(USING_ENV4)
    if (sht40.updated()) {
        M5.Display.setCursor(0, 0);
        M5.Display.fillRect(0, 0, 320, 80, TFT_BLACK);
        M5.Display.printf(
            "\n>SHT40Temp:%.4f\n"
            ">Humidity:%.4f",
            sht40.temperature(), sht40.humidity());
    }
    if (bmp280.updated()) {
        M5.Display.setCursor(0, 80);
        M5.Display.fillRect(0, 80, 320, 80, TFT_BLACK);
        auto p = bmp280.pressure();
        M5.Display.printf(
            "\n>BMP280Temp:%.4f\n"
            ">Pressure:%.4f\n"
            ">Altitude:%.4f",
            bmp280.temperature(), p * 0.01f /* To hPa */, calculate_altitude(p));
    }
#endif
    delay(1000);
}
```


## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/723/unit_env_arduino_example_01.jpg" width="70%">


## 4.温湿度数据读取

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/723/unit_env_arduino_example_02.jpg" width="50%">


