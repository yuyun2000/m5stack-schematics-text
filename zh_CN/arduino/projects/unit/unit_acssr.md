# Unit ACSSR/DCSSR Arduino 使用教程

## 1. 准备工作

- 1\. 环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 2\. 使用到的驱动库:

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-ACSSR](https://github.com/m5stack/M5Unit-ACSSR)

- 3\. 使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit ACSSR](https://shop.m5stack.com/products/single-phase-ac-ssr-unit-cdg1-1da-10a) / [Unit DCSSR](https://shop.m5stack.com/products/single-phase-dc-ssr-unit-cdg1-1dd-10a?variant=43848091599105)
  - [Unit RS485-ISO](https://shop.m5stack.com/products/isolated-rs485-unit)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/acssr/acssr_cover_01.webp" width="20%">

## 2. 工作模式

\#> 工作模式配置 | 使用前请参考以下说明流程图配置工作模式模式

- 1\. 设备断电状态下，保持长按中间按键。
- 2\. 设备供电，当设备 RGB LED 灯快速闪烁时，表示进入模式配置状态。
- 3\. 单击按键进行模式切换:
  - 绿灯：按键手动模式，工作时通过中间按键，控制开关。
  - 红灯：I2C 通信模式，工作时通过设备 HY2.0-4P Grove 接口接入 I2C 总线进行控制。
  - 黄灯: Modbus 通信模式，工作时通过设备两端 HT3.96-4P 接口接入 Modbus 总线进行控制。
- 4\. 长按按键，选中当前模式进行保存。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/814/unit_dcssr_mode_change_guide_01.mp4"></video>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/814/AC-AND-DCSSR-UNIT-note.png" width="50%">

- 负载接线示例图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/acssr/connect_example.png" width="70%">

## 3. I2C 模式控制

设备配置进入 I2C 工作模式后，通过设备 HY2.0-4P Grove 接口接入 I2C 总线进行控制。本案例使用 CoreS3 PORT.A 接口进行通信，搭配其他主控时，请根据实际的连接的引脚修改程序。

```cpp line-num
#include "M5Unified.h"
#include "M5_ACSSR.h"

M5_ACSSR SSR;
void printStatus();

void setup()
{
    M5.begin();
    Serial.begin(115200);
    while (!SSR.begin(&Wire, 2, 1, ACSSR_DEFAULT_ADDR)) {
        M5.Display.println("ACSSR I2C INIT ERROR");
        Serial.println("ACSSR I2C INIT ERROR");
        delay(1000);
    }
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
}

void loop()
{
    SSR.on();
    SSR.setLEDColor(0xff0000);
    printStatus();

    delay(1000);

    SSR.off();
    SSR.setLEDColor(0x00ff00);
    printStatus();

    delay(1000);
}

void printStatus()
{
    int relay   = SSR.status();
    int color   = SSR.getLEDColor();
    int version = SSR.getVersion();

    M5.Display.clear();
    M5.Display.setCursor(0, 0);
    M5.Display.println("I2C Mode Control");
    if (relay != -1) {
        Serial.printf("Relay: %s\n", relay ? "ON" : "OFF");
        M5.Display.printf("Relay: %s\n", relay ? "ON" : "OFF");
    }

    if (color != -1) {
        Serial.printf("LED Color: 0x%04X\n", color);
        M5.Display.printf("LED Color: 0x%04X\n", color);
    }

    if (version != -1) {
        Serial.printf("FW Version: 0x%04X\n", version);
        M5.Display.printf("FW Version: 0x%04X\n", version);
    }
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/814/unit_dcssr_arduino_i2c_demo_01.jpg" width="70%">

## 4. Modbus 模式控制

设备配置进入 Modbus 工作模式后，通过设备两端 HT3.96-4P 接口接入 Modbus 总线进行控制。本案例使用 CoreS3 PORT.A + 搭配 Unit RS485-ISO 进行 RS485 通信。

```cpp line-num
 #include "M5Unified.h"
#include "M5_ACSSR.h"
#include <ArduinoModbus.h>
#include <ArduinoRS485.h>

RS485Class RS485(Serial2, 1, 2, -1, -1);
uint8_t slave_id = 0;

void relayOn();
void relayOff();
void setLedColor(uint16_t color);
int getRelayStatus();
int getLedColor();
int getFirmwareVersion();
void printStatus();

void setup()
{
    M5.begin();
    Serial.begin(115200);
    delay(2000);

    Wire.end();
    ModbusRTUClient.begin(115200, SERIAL_8N1);

    slave_id = ACSSR_DEFAULT_SLAVE_ID;
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
}

void loop()
{
    relayOn();
    setLedColor(0xF800);  // RED
    printStatus();

    delay(1000);

    relayOff();
    setLedColor(0x07E0);  // GREEN
    printStatus();

    delay(1000);
}

void relayOn()
{
    ModbusRTUClient.coilWrite(slave_id, ACSSR_RELAY_COIL_ADDR, 0xFF);
}

void relayOff()
{
    ModbusRTUClient.coilWrite(slave_id, ACSSR_RELAY_COIL_ADDR, 0x00);
}

void setLedColor(uint16_t color)
{
    ModbusRTUClient.holdingRegisterWrite(slave_id, ACSSR_LED_HOLDING_ADDR, color);
}

int getRelayStatus()
{
    if (ModbusRTUClient.requestFrom(slave_id, COILS, ACSSR_RELAY_COIL_ADDR, 1)) {
        while (ModbusRTUClient.available()) {
            return ModbusRTUClient.read();
        }
    }
    return -1;
}

int getLedColor()
{
    if (ModbusRTUClient.requestFrom(slave_id, HOLDING_REGISTERS, ACSSR_LED_HOLDING_ADDR, 1)) {
        while (ModbusRTUClient.available()) {
            return ModbusRTUClient.read();
        }
    }
    return -1;
}

int getFirmwareVersion()
{
    if (ModbusRTUClient.requestFrom(slave_id, HOLDING_REGISTERS, ACSSR_VERSION_HOLDING_ADDR, 1)) {
        while (ModbusRTUClient.available()) {
            return ModbusRTUClient.read();
        }
    }
    return -1;
}

void printStatus()
{
    int relay   = getRelayStatus();
    int color   = getLedColor();
    int version = getFirmwareVersion();

    M5.Display.clear();
    M5.Display.setCursor(0, 0);
    M5.Display.println("Modbus Mode Control");
    if (relay != -1) {
        Serial.printf("Relay: %s\n", relay ? "ON" : "OFF");
        M5.Display.printf("Relay: %s\n", relay ? "ON" : "OFF");
    }

    if (color != -1) {
        Serial.printf("LED Color: 0x%04X\n", color);
        M5.Display.printf("LED Color: 0x%04X\n", color);
    }

    if (version != -1) {
        Serial.printf("FW Version: 0x%04X\n", version);
        M5.Display.printf("FW Version: 0x%04X\n", version);
    }
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/814/unit_dcssr_arduino_modbus_demo_01.jpg" width="70%">
