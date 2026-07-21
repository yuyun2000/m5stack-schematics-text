# Unit Mini BPS Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5UnitUnified](https://github.com/m5stack/M5UnitUnified)
  - [M5Unit-ENV](https://github.com/m5stack/M5Unit-ENV)

#>驱动库| 在 M5Unit-ENV 库中包含了对 Unit Mini BPS / Unit Mini BPS v1.1 传感器的驱动与案例，能够非常方便的实现传感器数据读取。

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit Mini BPS v1.1](https://shop.m5stack.com/products/barometric-pressure-unitqmp6988)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/BPS(QMP6988)/img-385e5d9c-e004-4da4-9a8e-8e1ff7c3cd74.webp" width="20%">

#>依赖库|以上驱动库如`M5UnitUnified`，`M5Unit-ENV`等在安装时需要其他的依赖库(如[M5HAL](https://github.com/m5stack/M5HAL), [M5Utility](https://github.com/m5stack/M5Utility)等), 如果通过Arduino库管理进行安装时, 请根据提示, 安装全部依赖。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/740/mini_unit_bps_arduino_lib_install_01.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/740/mini_unit_bps_arduino_lib_install_02.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/740/mini_unit_bps_arduino_lib_install_03.jpg" width="70%">


## 2.案例程序

#>案例说明 | 本案例以 Unit Mini BPS v1.1 为例，实现气压数据读取。如果使用的是 Unit Mini BPS (BMP280款) 可通过切换`USING_BPS`注释来启用不同的实例。


```cpp line-num
#include <M5Unified.h>
#include "M5UnitENV.h"

M5Canvas canvas(&M5.Display);

// #define USING_BPS
#define USING_BPS_V11

#if defined(USING_BPS)

BMP280 bmp;

#elif defined(USING_BPS_V11)

QMP6988 qmp;

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

#if defined(USING_BPS)
    if (!bmp.begin(&Wire, BMP280_I2C_ADDR, pin_num_sda, pin_num_scl, 400000U)) {
        Serial.println("Couldn't find BMP280");
        M5.Display.clear(TFT_RED);
        while (1) delay(1);
    }
    /* Default settings from datasheet. */
    bmp.setSampling(BMP280::MODE_NORMAL,     /* Operating Mode. */
                    BMP280::SAMPLING_X2,     /* Temp. oversampling */
                    BMP280::SAMPLING_X16,    /* Pressure oversampling */
                    BMP280::FILTER_X16,      /* Filtering. */
                    BMP280::STANDBY_MS_500); /* Standby time. */

#elif defined(USING_BPS_V11)
    if (!qmp.begin(&Wire, QMP6988_SLAVE_ADDRESS_L, pin_num_sda, pin_num_scl, 400000U)) {
        Serial.println("Couldn't find QMP6988");
        M5.Display.clear(TFT_RED);
        while (1) delay(1);
    }

#endif
}

void loop()
{
    M5.update();

#if defined(USING_BPS)

    if (bmp.update()) {
        M5.Display.setCursor(0, 0);
        M5.Display.clear(TFT_BLACK);
        M5.Display.println("-----BMP280-----");
        M5.Display.print(F("Temperature: "));
        M5.Display.print(bmp.cTemp);
        M5.Display.println(" degrees C");
        M5.Display.print(F("Pressure: "));
        M5.Display.print(bmp.pressure);
        M5.Display.println(" Pa");
        M5.Display.print(F("Approx altitude: "));
        M5.Display.print(bmp.altitude);
        M5.Display.println(" m");
        M5.Display.println("-------------\r\n");
    }

#elif defined(USING_BPS_V11)

    if (qmp.update()) {
        M5.Display.setCursor(0, 0);
        M5.Display.clear(TFT_BLACK);
        M5.Display.println("-----QMP6988-----");
        M5.Display.print(F("Temperature: "));
        M5.Display.print(qmp.cTemp);
        M5.Display.println(" *C");
        M5.Display.print(F("Pressure: "));
        M5.Display.print(qmp.pressure);
        M5.Display.println(" Pa");
        M5.Display.print(F("Approx altitude: "));
        M5.Display.print(qmp.altitude);
        M5.Display.println(" m");
        M5.Display.println("-------------\r\n");
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

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/740/mini_unit_bps_arduino_example_01.jpg" width="70%">


## 4.气压值读取

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/740/mini_unit_bps_arduino_example_02.jpg" width="50%">


