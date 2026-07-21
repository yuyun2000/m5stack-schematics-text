# Stamp C6LoRa EXT IO

Stamp C6LoRa 内部集成 PI4IOE5V6408 IO 扩展芯片，除用于 LoRa 模组收发电路控制及信号放大器使能控制外，还对外引出 `EXT_P0 ~ P4 `接口，可提供更多 IO 资源。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5StampC6LoRa
- M5Unified 库版本 >= 0.2.13
- M5GFX 库版本 >= 0.2.19

### Ouput

```cpp line-num
#include <Arduino.h>
#include <M5Unified.h>
#include "utility/PI4IOE5V6408_Class.hpp"

m5::I2C_Class i2c_bus_0;
m5::PI4IOE5V6408_Class ioe(0x43, 400000, &i2c_bus_0);

void setup()
{
    Serial.begin(115200);
    delay(300);
    Serial.println("PI4IOE5V6408 Output Example");

    if (!i2c_bus_0.begin(I2C_NUM_0, 10, 8)) {
        Serial.println("I2C init failed");
        while (true) delay(1000);
    }
    if (!ioe.begin()) {
        Serial.println("IOE init failed");
        while (true) delay(1000);
    }

    for (int i = 0; i < 5; i++) {
        ioe.setDirection(i, true);      // output
        ioe.setHighImpedance(i, false); // disable high-impedance so pin can actually drive
        ioe.digitalWrite(i, false);     // default low
    }
}

void loop()
{
    static bool state = false;
    state = !state;

    for (int i = 0; i < 5; i++) {
        ioe.digitalWrite(i, state);
        Serial.printf("[EXT_P%d] %d  ", i, (int)state);
    }
    Serial.println();
    delay(1000);
}

```

### Input

```cpp line-num
#include <Arduino.h>
#include <M5Unified.h>
#include "utility/PI4IOE5V6408_Class.hpp"

m5::I2C_Class i2c_bus_0;
m5::PI4IOE5V6408_Class ioe(0x43, 400000, &i2c_bus_0);

void setup()
{
    Serial.begin(115200);
    delay(300);
    Serial.println("PI4IOE5V6408 Input Example");

    if (!i2c_bus_0.begin(I2C_NUM_0, 10, 8)) {
        Serial.println("I2C init failed");
        while (true) delay(1000);
    }
    if (!ioe.begin()) {
        Serial.println("IOE init failed");
        while (true) delay(1000);
    }

    for (int i = 0; i < 5; i++) {
        ioe.setDirection(i, false);   // input
        ioe.enablePull(i, true);      // enable internal pull resistor
        ioe.setPullMode(i, true);     // pull-up (true=up, false=down)
    }
}

void loop()
{
    for (int i = 0; i < 5; i++) {
        Serial.printf("[EXT_P%d] %d  ", i, (int)ioe.digitalRead(i));
    }
    Serial.println();

    delay(1000);
}
```


