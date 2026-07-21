# Unit Pahub Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5UnitUnified](https://github.com/m5stack/M5UnitUnified)
  - [M5Unit-ENV](https://github.com/m5stack/M5Unit-ENV)
  - [M5Unit-HUB](https://github.com/m5stack/M5Unit-HUB)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit Pahub v2.1](https://shop.m5stack.com/products/i2c-hub-1-to-6-expansion-unit-v2-1-with-dip-switch-pca9548a)
  - [Unit ENV-III](https://shop.m5stack.com/products/env-iii-unit-with-temperature-humidity-air-pressure-sensor-sht30-qmp6988)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-PaHub2.1/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/envIII/envIII_cover_01.webp" width="20%">

#>依赖库|以上驱动库如`M5UnitUnified`，`M5Unit-ENV`等在安装时需要其他的依赖库(如[M5HAL](https://github.com/m5stack/M5HAL), [M5Utility](https://github.com/m5stack/M5Utility)等), 如果通过Arduino库管理进行安装时, 请根据提示, 安装全部依赖。


<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/unit/unit_pahub/lib_install_01.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/unit/unit_pahub/lib_install_02.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/unit/unit_pahub/lib_install_03.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/unit/unit_pahub/lib_install_04.jpg" width="70%">


## 2.案例程序

#>案例说明|Unit Pahub提供了六个I2C拓展接口, 每个接口可以独立控制开关接入。通过分时接入的方式, Unit Pahub能够避免从机地址冲突, 接入多个相同I2C地址的设备到总线中。本教程将以接入6个相同的Unit ENV-III为例, 介绍如何通过Unit Pahub进行拓展。

?>I2C地址|拓展传感器的时候, 需要注意传感器地址是否与Unit Pahub v2.1的默认地址冲突。如本案例Unit ENV-III中的传感器`QMP6988`则有着相同的I2C地址(0x70)。我们需要将Unit Pahub v2.1的地址拨码开关切换至其他地址来解决该问题。其他版本的Unit Pahub可通过焊接A0-A2电阻来进行地址切换。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/unit/unit_pahub/pahub_change_addr_01.jpg" width="50%">


### Select Channel

该方式可搭配其他对Wire简单进行封装的传感器驱动库使用, 仅对Unit Pahub的拓展接口进行开关操作。在切换通道后, 再手动进行对应的传感器的读写操作。

- Channel I2C Scan Example

```cpp line-num
#include <M5Unified.h>
#include <M5UnitUnified.h>
#include <M5UnitUnifiedHUB.h>
#include "Wire.h"

namespace {
m5::unit::UnitUnified Units;
m5::unit::UnitPaHub2 hub0{0x77};  // 0x70 as default, but we change to 0x77
}  // namespace

void setup()
{
    M5.begin();
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    auto pin_num_sda = M5.getPin(m5::pin_name_t::port_a_sda);
    auto pin_num_scl = M5.getPin(m5::pin_name_t::port_a_scl);
    M5_LOGI("getPin: SDA:%u SCL:%u", pin_num_sda, pin_num_scl);

    Wire.begin(pin_num_sda, pin_num_scl, 400000U);

    if (!Units.add(hub0, Wire) ||  // Connect hub0 to core
        !Units.begin()) {
        M5_LOGE("Failed to begin");
        M5.Display.clear(TFT_RED);
        while (true) {
            m5::utility::delay(10000);
        }
    }
}

void scan_ch(uint8_t ch)
{
    M5.Display.clear();
    int textColor = YELLOW;
    for (size_t i = 0; i < 2; i++) {
        M5.Display.setCursor(0, 0);
        M5.Display.print("scanning Address [HEX]\r\n");
        M5.Display.printf("Pahub Channel: %d\r\n", ch);
        for (uint8_t addr = 1; addr < 127; addr++) {
            Wire.beginTransmission(addr);
            uint8_t error = Wire.endTransmission();
            if (error == 0) {
                M5.Display.print(addr, HEX);
                M5.Display.print(" ");
            } else {
                M5.Display.print(".");
            }
            delay(10);
        }

        if (textColor == YELLOW) {
            textColor = CYAN;
        } else {
            textColor = YELLOW;
        }
        M5.Display.setTextColor(textColor, BLACK);
    }
}

void loop()
{
    M5.update();
    for (uint8_t i = 0; i < 6; i++) {
        // Select & Scan Each Channel
        hub0.selectChannel(i);
        scan_ch(i);
    }
}
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/unit/unit_pahub/pahub_addr_scan_01.jpg" width="70%">


### UniUnified

如果使用是已经支持了UnitUnified驱动的传感器库, 可以通过`add`的方式直接将传感器实例注册到hub中, 在使用`Units.update();`时将自动拉取各个通道的传感器数值。

- Channel Unit ENV-III Get Data Example

```cpp line-num
#include <M5Unified.h>
#include <M5UnitUnified.h>
#include <M5UnitUnifiedHUB.h>
#include <M5UnitUnifiedENV.h>

namespace {
m5::unit::UnitUnified Units;
m5::unit::UnitPaHub2 hub0{0x77};  // 0x70 as default, but we change to 0x77
m5::unit::UnitENV3 unitENV3_0;
m5::unit::UnitENV3 unitENV3_1;
auto& sht30_0   = unitENV3_0.sht30;
auto& qmp6988_0 = unitENV3_0.qmp6988;
auto& sht30_1   = unitENV3_1.sht30;
auto& qmp6988_1 = unitENV3_1.qmp6988;
}  // namespace

void setup()
{
    M5.begin();
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    auto pin_num_sda = M5.getPin(m5::pin_name_t::port_a_sda);
    auto pin_num_scl = M5.getPin(m5::pin_name_t::port_a_scl);
    M5_LOGI("getPin: SDA:%u SCL:%u", pin_num_sda, pin_num_scl);

    Wire.begin(pin_num_sda, pin_num_scl, 400000U);

    if (!hub0.add(unitENV3_0, 0) ||  // Connect unit to hub0 ch 0
        !hub0.add(unitENV3_1, 1) ||  // Connect unit to hub0 ch 0
        !Units.add(hub0, Wire) ||    // Connect hub0 to core
        !Units.begin()) {
        M5_LOGE("Failed to begin");
        M5.Display.clear(TFT_RED);
        while (true) {
            m5::utility::delay(10000);
        }
    }
}

void loop()
{
    M5.update();
    Units.update();
    if (sht30_0.updated()) {
        M5.Display.setCursor(0, 0);
        M5.Display.fillRect(0, 0, 320, 60, BLACK);
        M5.Display.printf(">CH0 SHT30Temp:%2.2f\n>Humidity:%2.2f", sht30_0.temperature(), sht30_0.humidity());
        M5_LOGI("\n>CH0 SHT30Temp:%2.2f\n>Humidity:%2.2f", sht30_0.temperature(), sht30_0.humidity());
    }
    if (qmp6988_0.updated()) {
        M5.Display.setCursor(0, 60);
        M5.Display.fillRect(0, 60, 320, 60, BLACK);
        M5.Display.printf(">CH0 QMP6988Temp:%2.2f\n>Pressure:%.2f", qmp6988_0.temperature(), qmp6988_0.pressure());
        M5_LOGI("\n>CH0 QMP6988Temp:%2.2f\n>Pressure:%.2f", qmp6988_0.temperature(), qmp6988_0.pressure());
    }
    if (sht30_1.updated()) {
        M5.Display.setCursor(0, 120);
        M5.Display.fillRect(0, 120, 320, 60, BLACK);
        M5.Display.printf(">CH1 SHT30Temp:%2.2f\n>Humidity:%2.2f", sht30_1.temperature(), sht30_1.humidity());
        M5_LOGI("\n>CH1 SHT30Temp:%2.2f\n>Humidity:%2.2f", sht30_1.temperature(), sht30_1.humidity());
    }
    if (qmp6988_1.updated()) {
        M5.Display.setCursor(0, 180);
        M5.Display.fillRect(0, 180, 320, 60, BLACK);
        M5.Display.printf(">CH1 QMP6988Temp:%2.2f\n>Pressure:%.2f", qmp6988_1.temperature(), qmp6988_1.pressure());
        M5_LOGI("\n>CH1 QMP6988Temp:%2.2f\n>Pressure:%.2f", qmp6988_1.temperature(), qmp6988_1.pressure());
    }
}
```


## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/unit/unit_pahub/pahub_env_example_01.jpg" width="70%">

## 4.传感器数据读取

通过分时接入的方式, 读取多个Unit ENV-III的温湿度数值, 进行显示。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/unit/unit_pahub/pahub_env_example_02.jpg" width="70%">

