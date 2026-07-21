# StamPLC Input & Output 输入输出

StamPLC 输入信号和继电器控制相关API与案例程序。

## Relay 案例程序

```cpp line-num
/*
 *SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
 *
 *SPDX-License-Identifier: MIT
 */
#include <Arduino.h>
#include <M5StamPLC.h>

void setup()
{
    /* Init M5StamPLC */
    M5StamPLC.begin();
}

void loop()
{
    static bool relay_state = false;

    /* Toggle relay state */
    relay_state = !relay_state;
    for (int i = 0; i < 4; i++) {
        M5StamPLC.writePlcRelay(i, relay_state);
        printf("Write Relay %d to %s\n", i, relay_state ? "ON" : "OFF");
        delay(500);
    }

    delay(1000);
}
```


## Relay API

### writePlcRelay

**函数原型:**

```cpp
void writePlcRelay(const uint8_t& channel, const bool& state);
```

**功能说明:**

- 控制写入指定编号继电器状态

**传入参数:**

- const uint8_t& channel：
  - 0-3

- const bool& state
  - true: ON
  - false: OFF

**返回值:**

- null


### writePlcAllRelay

**函数原型:**

```cpp
void writePlcAllRelay(const uint8_t& relayState);
```

**功能说明:**

- 控制写入指定编号继电器状态

**传入参数:**

- const uint8_t& relayState
  - bit[0:3] -> channel[0:3]
  - bit == 1: ON
  - bit == 0: OFF

**返回值:**

- null


### readPlcRelay

**函数原型:**

```cpp
bool readPlcRelay(const uint8_t& channel);
```

**功能说明:**

- 读取指定编号继电器状态

**传入参数:**

- const uint8_t& channel：
  - 0-3

**返回值:**

- bool:
  - true: ON
  - false: OFF


## Input 案例程序

```cpp line-num
/*
 *SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
 *
 *SPDX-License-Identifier: MIT
 */
#include <Arduino.h>
#include <M5StamPLC.h>

void setup()
{
    /* Init M5StamPLC */
    M5StamPLC.begin();
}

void loop()
{
    static std::array<bool, 8> input_list;

    // Read inputs
    for (int i = 0; i < 8; i++) {
        input_list[i] = M5StamPLC.readPlcInput(i);
    }

    // Print input reading result
    printf("Input: %d, %d, %d, %d, %d, %d, %d, %d\n", input_list[0], input_list[1], input_list[2], input_list[3],
           input_list[4], input_list[5], input_list[6], input_list[7]);

    delay(1000);
}
```


## Input API


### readPlcInput

**函数原型:**

```cpp
bool readPlcInput(const uint8_t& channel);
```

**功能说明:**

- 读取指定编号输入信号状态

**传入参数:**

- const uint8_t& channel：
  - channel 0-7

**返回值:**

- bool:
  - true: HIGH
  - false: LOW

