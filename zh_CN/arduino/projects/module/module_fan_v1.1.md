# Module Fan v1.1 Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Module-Fan](https://github.com/m5stack/M5Module-Fan)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Module Fan v1.1](https://shop.m5stack.com/products/m5stack-fan-module-v1-1-stm32f030)


<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_04.webp" width="20%">

## 2.案例程序

#>案例说明| Module Fan v1.1 是风扇散热模块，采用I2C通信接口，支持配置PWM频率，占空比等电机参数，用于实现电机调速，有效帮助设备散热。本案例将使用 Module Fan v1.1 搭配 CoreS3 主控实现散热风扇电机控制，同时读取状态信息进行显示。


```cpp line-num
#include <M5Unified.h>
#include <m5_module_fan.hpp>

M5ModuleFan moduleFan;
uint8_t deviceAddr = MODULE_FAN_BASE_ADDR;
uint8_t dutyCycle  = 80;
bool fan_status    = true;
M5Canvas canvas(&M5.Display);

void setup()
{
    M5.begin();
    Serial.begin(115200);
    canvas.createSprite(320, 240);
    canvas.setFont(&fonts::FreeSerifBold12pt7b);
    canvas.setTextDatum(top_center);
    canvas.setTextColor(WHITE);

    while (!moduleFan.begin(&Wire1, deviceAddr, 12, 11, 400000)) {
        Serial.printf("Module FAN Init faile\r\n");
        canvas.drawString("Module FAN Init faile", 160, 120);
        canvas.pushSprite(0, 0);
        delay(1000);
    }

    // Set the fan to rotate at 80% duty cycle
    moduleFan.setPWMDutyCycle(dutyCycle);
    moduleFan.setPWMFrequency(PWM_48KHZ);
    moduleFan.setStatus(MODULE_FAN_ENABLE);
}

void loop()
{
    int pwm_config_index  = moduleFan.getPWMFrequency();
    String pwm_config_str = "";

    switch (pwm_config_index) {
        case PWM_1KHZ:
            pwm_config_str = "1KHz";
            break;
        case PWM_12KHZ:
            pwm_config_str = "12KHz";
            break;
        case PWM_24KHZ:
            pwm_config_str = "24KHz";
            break;
        case PWM_48KHZ:
            pwm_config_str = "48KHz";
            break;
    }
    canvas.setCursor(0, 10);
    canvas.clear();
    canvas.printf("Work Status      : %s\r\n", moduleFan.getStatus() == MODULE_FAN_ENABLE ? "RUNING" : "STOP");
    canvas.printf("PWM  Frequency   : %s\r\n", pwm_config_str.c_str());
    canvas.printf("PWM  Duty Cycle  : %d\r\n", moduleFan.getPWMDutyCycle());
    canvas.printf("RPM              : %d\r\n", moduleFan.getRPM());
    canvas.pushSprite(0, 0);

    M5.update();
    auto t = M5.Touch.getDetail();
    if (t.wasClicked() || M5.BtnA.wasClicked()) {
        fan_status = !fan_status;
        if (fan_status) {
            moduleFan.setStatus(MODULE_FAN_ENABLE);
        } else {
            moduleFan.setStatus(MODULE_FAN_DISABLE);
        }
    }
}
```


## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">


- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_01.jpg" width="70%">


## 4.风扇启动

触摸屏幕控制风扇启动与停止，同时屏幕查看看当前风扇转速与配置信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_02.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_03.jpg" width="50%">

#>散热模块安装|Module Fan v1.1 设计的进风口在模块底部，为了取得较为有效的散热效果，推荐将其堆叠在需要散热的模块的顶部，如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_04.jpg" width="50%">


