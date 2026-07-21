# StamPLC Modbus Slave 从机

#>StamPLC驱动库整合了Modbus Slave功能。在整机完成简易的初始化配置后，便能作为从机设备，经由PWR-485接口便捷接入Modbus总线。其他设备也能够非常方便的控制StamPLC的继电器和读取输入信号状态。

## 案例程序

### StamPLC Modbus Slave


```cpp line-num
/*
 *SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
 *
 *SPDX-License-Identifier: MIT
 */
#include <Arduino.h>
#include <M5StamPLC.h>

void setup()
{
    /* Enable Modbus */
    auto config              = M5StamPLC.config();
    config.enableModbusSlave = true;
    config.modbusBaudRate    = 115200;
    config.modbusSlaveId     = 1;
    config.enableCan         = true;
    M5StamPLC.config(config);

    /* Init M5StamPLC */
    M5StamPLC.begin();
}

void loop()
{
    /* Now you can controll StamPLC via Modbus RS485 */
    /*
     * Modbus Slave Configuration for M5StamPLC
     * =======================================
     *
     * Register Map:
     * -------------
     * 1. Coils (Read/Write)
     *    - Address 0: Relay 1 output (true/false)
     *    - Address 1: Relay 2 output (true/false)
     *    - Address 2: Relay 3 output (true/false)
     *    - Address 3: Relay 4 output (true/false)
     *
     * 2. Input Registers (Read-only)
     *    - Address 0-7:   Inputs (true/false) - 8 registers
     *    - Address 8-9:   Temperature (FLOAT32) - 2 registers
     *    - Address 10-11: Bus Voltage (FLOAT32) - 2 registers
     *    - Address 12-13: Shunt Current (FLOAT32) - 2 registers
     *
     * Note: FLOAT32 values use 2 consecutive registers (32 bits total)
     */
    delay(1000);
}
```


### Modbus Master

#> 使用任意 ESP32 主控设备，搭配 [Unit RS485](https://shop.m5stack.com/products/rs485-module), 实现Modbus Master。然后通过PWR-485接口对 StamPLC 进行控制。

- 使用到的驱动库:
  - [Arduino485 Library](https://github.com/m5stack/ArduinoRS485)
  - [ArduinoModbus Library](https://github.com/m5stack/ArduinoModbus)


```cpp line-num
#include <ArduinoModbus.h>
#include <ArduinoRS485.h>

RS485Class RS485(Serial2, 39, 0, 46, -1);
uint8_t slave_id = 1;

// 将两个 16 位寄存器解析为 FLOAT32
float parseFloat(uint16_t high, uint16_t low)
{
    union {
        uint32_t i;
        float f;
    } value;
    value.i = ((uint32_t)high << 16) | low;
    return value.f;
}

void setup()
{
    Serial.begin(115200);
    delay(2000);
    if (!ModbusRTUClient.begin(115200, SERIAL_8N1)) {
        Serial.println("Failed to start Modbus RTU Client");
        while (1);
    }
}

void loop()
{
    /* Now you can controll StamPLC via Modbus RS485 */
    /*
     * Modbus Slave Configuration for M5StamPLC
     * =======================================
     *
     * Register Map:
     * -------------
     * 1. Coils (Read/Write)
     *    - Address 0: Relay 1 output (true/false)
     *    - Address 1: Relay 2 output (true/false)
     *    - Address 2: Relay 3 output (true/false)
     *    - Address 3: Relay 4 output (true/false)
     *
     * 2. Input Registers (Read-only)
     *    - Address 0-7:   Inputs (true/false) - 8 registers
     *    - Address 8-9:   Temperature (FLOAT32) - 2 registers
     *    - Address 10-11: Bus Voltage (FLOAT32) - 2 registers
     *    - Address 12-13: Shunt Current (FLOAT32) - 2 registers
     *
     * Note: FLOAT32 values use 2 consecutive registers (32 bits total)
     */
    Serial.println("\n--- Reading Modbus Registers ---");

    // 1. 控制 Coils（0x01）
    Serial.println("Turning Relays ON:");
    for (uint8_t addr = 0; addr < 4; addr++) {
        if (ModbusRTUClient.coilWrite(slave_id, addr, 0xFF)) {
            Serial.printf("Relay %d ON\n", addr);
        } else {
            Serial.printf("Failed to turn on Relay %d\n", addr);
        }
        delay(500);
    }

    Serial.println("Reading Coils Status:");
    for (uint8_t addr = 0; addr < 4; addr++) {
        if (ModbusRTUClient.requestFrom(slave_id, COILS, addr, 1)) {
            Serial.printf("Relay %d: ", addr);
            while (ModbusRTUClient.available()) {
                Serial.print(ModbusRTUClient.read(), HEX);
                Serial.print(' ');
            }
            Serial.println();
        } else {
            Serial.printf("Failed to read Relay %d\n", addr);
        }
    }

    Serial.println("Turning Relays OFF:");
    for (uint8_t addr = 0; addr < 4; addr++) {
        if (ModbusRTUClient.coilWrite(slave_id, addr, 0x00)) {
            Serial.printf("Relay %d OFF\n", addr);
        } else {
            Serial.printf("Failed to turn off Relay %d\n", addr);
        }
        delay(500);
    }

    Serial.println("Reading Coils Status Again:");
    for (uint8_t addr = 0; addr < 4; addr++) {
        if (ModbusRTUClient.requestFrom(slave_id, COILS, addr, 1)) {
            Serial.printf("Relay %d: ", addr);
            while (ModbusRTUClient.available()) {
                Serial.print(ModbusRTUClient.read(), HEX);
                Serial.print(' ');
            }
            Serial.println();
        } else {
            Serial.printf("Failed to read Relay %d\n", addr);
        }
    }

    delay(500);

    // 分开读取各个 Input Register 区间
    Serial.println("Reading Input Registers:");

    uint16_t tempRegisters[2], voltageRegisters[2], currentRegisters[2];
    float temperature, busVoltage, shuntCurrent;

    if (ModbusRTUClient.requestFrom(slave_id, INPUT_REGISTERS, 8, 2)) {
        for (uint8_t i = 0; i < 2; i++) {
            tempRegisters[i] = ModbusRTUClient.read();
        }
        temperature = parseFloat(tempRegisters[0], tempRegisters[1]);
        Serial.printf("Temperature: %.2f°C\n", temperature);
    } else {
        Serial.println("Failed to read Temperature Registers");
    }

    if (ModbusRTUClient.requestFrom(slave_id, INPUT_REGISTERS, 10, 2)) {
        for (uint8_t i = 0; i < 2; i++) {
            voltageRegisters[i] = ModbusRTUClient.read();
        }
        busVoltage = parseFloat(voltageRegisters[0], voltageRegisters[1]);
        Serial.printf("Bus Voltage: %.2fV\n", busVoltage);
    } else {
        Serial.println("Failed to read Bus Voltage Registers");
    }

    if (ModbusRTUClient.requestFrom(slave_id, INPUT_REGISTERS, 12, 2)) {
        for (uint8_t i = 0; i < 2; i++) {
            currentRegisters[i] = ModbusRTUClient.read();
        }
        shuntCurrent = parseFloat(currentRegisters[0], currentRegisters[1]);
        Serial.printf("Shunt Current: %.2fA\n", shuntCurrent);
    } else {
        Serial.println("Failed to read Shunt Current Registers");
    }

    Serial.printf(">>>>>> Temperature: %.2f°C, Bus Voltage: %.2fV, Shunt Current: %.2fA\n", temperature, busVoltage,
                  shuntCurrent);

    delay(5000);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_arduino_modbus_example_01.jpg" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_arduino_modbus_example_02.jpg" width="50%">

