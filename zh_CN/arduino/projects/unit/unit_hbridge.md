# Unit HBridge Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-Hbridge](https://github.com/m5stack/M5Unit-Hbridge)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit HBridge v1.1](https://shop.m5stack.com/products/h-bridge-unit-v1-1-stm32f030)


<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/HBridge%20v1.1%20Unit/img-454f24a1-a8c3-4d1f-87af-5a0eca4eabb7.webp" width="20%">


## 2.案例程序

#>案例说明|Unit HBridge 是一款直流电机驱动模块，支持配置电机速度，方向，电压等。`Unit HBridge v1.1`版本还支持读取当前电流值。


### 电源开关

?> 电机电源选择 | Unit HBridge 内部集成DC/DC降压电路，可以将外部3.96端子输入的 6 ~ 12V 降低至 5V 用于适配不同电机的电源需求。同时提供了一个电源切换开关，可用于选择电机电源使用外部输入的 6 ~ 12V 或 DC/DC 降压后的5V。开关切至 HPWR 表示使用外部输入电压，切至5V表示使用DC/DC降压后的5V电压。 实际使用时，请根据电机的规格选择适合的驱动电压。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/769/unit_hbridge_power_switch_01.jpg" width="50%">


### 电机接线


<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/769/unit_hbridge_connect_01.jpg" width="50%">


### 完整程序

```cpp line-num
#include "M5Unified.h"
#include "Wire.h"
#include "M5UnitHbridge.h"

M5UnitHbridge driver;
uint8_t fw_version = 0;
bool motor_run     = false;

void get_current_voltage()
{
    // getMotorCurrent() function only support in Hbridge V1.1 version
    if (fw_version >= 2) {
        Serial.printf("%.2fA\r\n", driver.getMotorCurrent());
    }
    Serial.printf("%.2fV\r\n", driver.getAnalogInput(_12bit) / 4095.0f * 3.3f / 0.09f);
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setFont(&fonts::lgfxJapanMinchoP_24);

    while (!driver.begin(&Wire, HBRIDGE_I2C_ADDR, 2, 1, 100000L)) {
        M5.Display.drawString("Unit HBridge init Fail!", M5.Display.width() / 2, M5.Display.height() / 2);
        delay(1000);
    }

    fw_version = driver.getFirmwareVersion();
    Serial.printf("Hbridge Firmware Version: %d\r\n", fw_version);

    M5.Display.clear();
    M5.Display.drawString("Unit HBridge init OK", M5.Display.width() / 2, M5.Display.height() / 2 - 20);
    M5.Display.drawString("Touch to Start/Stop Motor", M5.Display.width() / 2, M5.Display.height() / 2 + 20);
}

void loop()
{
    M5.update();
    auto t = M5.Touch.getDetail();
    if (t.wasClicked() || M5.BtnA.wasClicked()) {
        motor_run = !motor_run;
        M5.Display.clear();
        if (motor_run) {
            driver.setDriverDirection(HBRIDGE_FORWARD);
            // driver.setDriverDirection(HBRIDGE_BACKWARD);
            driver.setDriverSpeed8Bits(127);
            M5.Display.drawString("Motor Running", M5.Display.width() / 2, M5.Display.height() / 2);
        } else {
            driver.setDriverDirection(HBRIDGE_STOP);
            driver.setDriverSpeed8Bits(127);
            M5.Display.drawString("Motor Stop", M5.Display.width() / 2, M5.Display.height() / 2);
        }
    }
    get_current_voltage();
    delay(10);
}
```

## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">


- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/769/unit_hbridge_example_01.jpg" width="70%">


## 4.电机控制

使用 Unit HBridge 控制电机旋转与停止。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/769/unit_hbridge_example_02.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/769/unit_hbridge_example_03.jpg" width="50%">
 