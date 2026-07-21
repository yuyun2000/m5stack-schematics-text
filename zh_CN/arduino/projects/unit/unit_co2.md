# Unit CO2 / CO2L Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5UnitUnified](https://github.com/m5stack/M5UnitUnified)
  - [M5Unit-ENV](https://github.com/m5stack/M5Unit-ENV)

#>驱动库| 在 M5Unit-ENV 库中包含了对 Unit CO2 / Unit CO2L 传感器的驱动与案例，能够非常方便的实现传感器数据读取。

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit CO2L](https://shop.m5stack.com/products/co2l-unit-with-temperature-and-humidity-sensor-scd41)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-38780333-42e3-42bc-818f-75c2ca9b26ce.webp" width="20%">

#>依赖库|以上驱动库如`M5UnitUnified`，`M5Unit-ENV`等在安装时需要其他的依赖库(如[M5HAL](https://github.com/m5stack/M5HAL), [M5Utility](https://github.com/m5stack/M5Utility)等), 如果通过Arduino库管理进行安装时, 请根据提示, 安装全部依赖。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/741/unit_co2l_arduino_lib_install_01.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/741/unit_co2l_arduino_lib_install_02.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/741/unit_co2l_arduino_lib_install_03.jpg" width="70%">


## 2.案例程序

#>案例说明 | 本案例以 Unit CO2L 为例，实现空气 CO2 浓度数据读取。该程序适用于 Unit CO2L / Unit CO2， 其二者区别在于 Unit CO2L 支持低功耗单次测量，可在程序中根据实际使用的硬件选择是否启用该选项。

```cpp line-num
#include <M5Unified.h>
#include <M5UnitUnified.h>
#include <M5UnitUnifiedENV.h>

auto& lcd = M5.Display;
m5::unit::UnitUnified Units;
m5::unit::UnitCO2 unit;

void setup()
{
    M5.begin();

    M5.Display.setFont(&fonts::lgfxJapanMinchoP_20);
    M5.Display.setTextSize(1);
    auto pin_num_sda = M5.getPin(m5::pin_name_t::port_a_sda);
    auto pin_num_scl = M5.getPin(m5::pin_name_t::port_a_scl);
    M5_LOGI("getPin: SDA:%u SCL:%u", pin_num_sda, pin_num_scl);

    Wire.begin(pin_num_sda, pin_num_scl, 400000U);
    if (!Units.add(unit, Wire) || !Units.begin()) {
        M5_LOGE("Failed to begin");
        M5.Display.clear(TFT_RED);
        while (true) {
            m5::utility::delay(10000);
        }
    }

    M5_LOGI("M5UnitUnified has been begun");
    M5_LOGI("%s", Units.debugInfo().c_str());
    M5.Display.setCursor(0, 0);
    M5.Display.clear();
    M5.Display.println("Init...");
}

void loop()
{
    M5.update();
    Units.update();
    if (unit.updated()) {
        M5.Display.setCursor(0, 0);
        M5.Display.clear();
        M5.Display.printf("\n>CO2:%u\n>Temperature:%2.2f\n>Humidity:%2.2f", unit.co2(), unit.temperature(),
                          unit.humidity());
    }
}
```


## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/741/unit_co2l_arduino_example_01.jpg" width="70%">


## 4. CO2 / CO2L浓度读取

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/741/unit_co2l_arduino_example_02.jpg" width="50%">


