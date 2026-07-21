# Unit Dlight Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5Unit-KmeterISO](https://github.com/m5stack/M5Unit-KMeterISO)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit Kmeter-ISO](https://shop.m5stack.com/products/kmeter-isolation-unit-with-thermocouple-temperature-sensor-max31855)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/KMeterISO%20Unit/img-9a8a35e5-fa76-4bab-b1ac-b493fdfda2c0.webp" width="20%">

#>依赖库|以上驱动库如`M5Unified.h`，`M5Unit-KmeterISO`等在安装时需要其他的依赖库(如[M5HAL](https://github.com/m5stack/M5HAL), [M5Utility](https://github.com/m5stack/M5Utility)等), 如果通过Arduino库管理进行安装时, 请根据提示, 安装全部依赖。

<img src="./kmeterimg/unit_kmeteriso_arduino_lib_install_01.jpg" width="70%">

## 2.案例程序

#>案例说明 | 本案例以 Unit KMeter-ISO 为例，采集温度。

```cpp line-num
#include <M5Unified.h>
#include "M5UnitKmeterISO.h"

M5UnitKmeterISO kmeter;
auto& lcd = M5.Display;
uint8_t error_status = 0;
long delay_time = 0;

void setup()
{
    M5.begin();
    M5.Display.setFont(&fonts::lgfxJapanMinchoP_20);
    M5.Display.setTextColor(YELLOW); 
    M5.Display.setTextSize(1);
    auto pin_num_sda = M5.getPin(m5::pin_name_t::port_a_sda);
    auto pin_num_scl = M5.getPin(m5::pin_name_t::port_a_scl);
    M5_LOGI("getPin: SDA:%u SCL:%u", pin_num_sda, pin_num_scl);
    Wire.begin(pin_num_sda, pin_num_scl, 400000U);
    
    M5.Display.setCursor(0, 0);
    M5.Display.clear();
    
    Serial.begin(115200);
    while (!kmeter.begin(&Wire, KMETER_DEFAULT_ADDR, pin_num_sda, pin_num_scl, 100000L)) {
        Serial.println("Unit KmeterISO not found");
    }
}

void loop()
{
    M5.update();
    
    M5.Display.clear();
    // Serial.println("ok");
    if (millis() > delay_time) {
      M5.Display.setCursor(0, 0);
        error_status = kmeter.getReadyStatus();
        
        if (error_status == 0) {
            
            M5.Display.printf("Celsius Temp:  %.2fC\r\n",
                          ((float)(kmeter.getCelsiusTempValue())) / 100);
            M5.Display.printf("Fahrenheit Temp:  %.2fF\r\n",
                          ((float)(kmeter.getFahrenheitTempValue())) / 100);
            M5.Display.printf(
                "Chip Celsius Temp:  %.2fC\r\n",
                ((float)(kmeter.getInternalCelsiusTempValue())) / 100);
            M5.Display.printf(
                "Chip Fahrenheit Temp:  %.2fF\r\n",
                ((float)(kmeter.getInternalFahrenheitTempValue())) / 100); 
        } else {
            M5.Display.print(kmeter.getReadyStatus());
        }
        
    }
    delay(1000);
}
```

## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。
 
<img src="./kmeterimg/unit_kmeteriso_arduino_lib_install_03.jpg">

## 4.温度采集

<img src="./kmeterimg/unit_kmeteriso_arduino_lib_install_04.jpg" width="50%">


