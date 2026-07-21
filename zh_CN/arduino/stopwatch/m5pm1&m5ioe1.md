# StopWatch M5PM1 & M5IOE1 电源管理

## 1. 多级电源开关设计

StopWatch 内部集成 M5PM1 + M5IOE1，结合硬件电路实现了多级电源开关，不同的级别的电源开关对应控制了相关的外设与接口供电。用户可根据运行需求，切换不同级别的电源使能，关闭未使用的外设部分，实现整机低功耗。

### M5PM1 / M5IOE1 驱动库

使用 M5PM1 / M5IOE1 驱动库能够非常便捷地配置 M5PM1 / M5IOE1 的引脚功能，用于低功耗唤醒以及外设供电开关。

- [M5PM1 Arduino Library](https://github.com/m5stack/M5PM1)
- [M5IOE1 Arduino Library](https://github.com/m5stack/M5IOE1)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/stopwatch_m5pm1_level_01.png" width="70%" />

#> 注意事项 | StopWatch 的多级电源开关设计并非串联结构。L1 ~ L3B 开关的电源输入均来自于 L0 (SYS_VBUS) 级源头，而非上一级电源，因此支持独立控制不同级别的电源开关，以上分级根据外设供电与功耗进行区分。M5PM1 启动上电后 L1, L2，L3A 将自动开启 (默认打开 `DCDC3V3_EN_PP`, `LDO3V3_EN_PP`, `CHG_EN_PP`)，在 M5Unified 初始化流程中，将进一步控制 M5IOE1 打开 L3B，使能其他的外设供电或使能引脚。

### L0

此级电源条件下，电池保持对 M5PM1 的供电。电池电量未耗尽的情况下，该层电源将一直保持，M5PM1 支持基础的按键开关机操作。

### L1

启用 IMU, 以及 RTC 外设供电。该层级的电源开关使用 M5PM1 的 `LDO3V3_EN_PP` (PM_3V3_L1_EN)，可通过以下 API 实现开关控制。

```cpp
pm1.setLdoEnable(true); // L1 ON
pm1.setLdoEnable(false); // L1 OFF
```

同时，IMU 的 INT1 中断及 RTC 的定时中断引脚连接至 M5PM1 的 PYG4，可通过配置相关的寄存器实现保持 IMU、RTC 供电，M5PM1 进入休眠状态，通过翻转设备，触发 IMU 中断（高电平有效）或 RTC 设置定时中断（低电平有效）唤醒 M5PM1。可通过以下 API 实现 IMU、RTC (L1) 供电保持。

```cpp
pm1.setLdoEnable(true);
pm1.ldoSetPowerHold(true);
pm1.setLedEnLevel(true);
pm1.shutdown();
```

### L2 / L3A

此级电源条件下，将启用 ESP32-S3、Grove 接口、M5IOE1 拓展芯片、用户按键上拉供电、EXT.PORT 接口 3V3_L2 输出，以及 CH442E 开关芯片供电 (该开关芯片用于切换 EXT.PORT 接口的 MUX_IO_1/2 功能切换 UART0 / USB )。 其中 Grove 拓展接口的输入 / 输出供电，需通过 M5PM1 的 `EXT_5V_EN` (BOOST5V_EN_PP) 引脚进行开关控制。

当 ESP32-S3 处于休眠状态时，电源处于 L2 级。当 ESP32-S3 处于工作状态时，电源处于 L3A 级。 ESP32-S3 可通过控制 M5PM1 进入休眠的方式，关断自身的供电 (L2 -> L1/L0)。

关闭 Grove EXT_5V 接口时为输入模式，此时需要外部 5V 输入供电。无外接供电的使用场景，则可以通过以下 API 重新打开 EXT_5V 输出模式。

```cpp
M5.Power.setExtOutput(true); // EXT_5V OUTPUT
// M5.Power.setExtOutput(false); // EXT_5V INPUT
```

### L3B

L3B 层级控制屏幕、扬声器、振动电机等功耗较高的外设的供电或相关配置。该层级基于 M5IOE1 IO 拓展芯片实现控制，允许独立的控制该层级的一些外设。

| M5IOE1              | PYG1        | PYG3      | PYG9       | PYG8       | PYG10      | PYG4       | PYG5         |
| ------------------- | ----------- | --------- | ---------- | ---------- | ---------- | ---------- | ------------ |
| Ext.Port Select     | PYB_MUX_CTR |           |            |            |            |            |              |
| Audio L3B           |             | PYB_AU_EN |            |            |            |            |              |
| Vibration Motor     |             |           | PYB_MT_PWM |            |            |            |              |
| 3V3_L3B             |             |           |            | PYB_L3B_EN |            |            |              |
| Speaker AMP AW8737A |             |           |            |            | PYB_SPK_EN |            |              |
| Touch               |             |           |            |            |            | PYB_TP_RST |              |
| AMOLED              |             |           |            |            |            |            | PYB_OLED_RST |

- PYG1(PYB_MUX_CTR): 背部拓展接口 MUX_IO_1/2 切换 `USB / UART` 功能
- PYG3(PYB_AU_EN): ES8311 供电 + MIC 供电
- PYG9(PYB_MT_PWM): 振动电机 PWM 信号
- PYG8(PYB_L3B_EN): AMOLED 屏幕供电
- PYG10(PYB_SPK_EN): AW8737A 扬声器功放使能
- PYG4(PYB_TP_RST): 屏幕触摸复位
- PYG5(PYB_OLED_RST): 屏幕显示复位

具体的外设供电控制，通过下方 M5IOE1 的 API 进行独立控制：

```cpp
ioe1.pinMode(M5IOE1_PIN_1, OUTPUT);
ioe1.digitalWrite(M5IOE1_PIN_1, LOW);
```

## 2. M5PM1 休眠

### 手动休眠

M5PM1 可通过程序手动控制进入休眠状态，来降低整机功耗。默认状态下，直接设置休眠将回退至 L0 级电源，此时仅 M5PM1 保持供电。

```cpp
pm1.shutdown();
```

在一些特殊的使用场景 (例如 IMU 唤醒，或是 ESP32-S3 SoC 休眠)，允许 M5PM1 进入休眠降低的同时，保持一些层级的外设供电，用于唤醒源或是状态保持。

该类应用需要在 M5PM1 进入休眠模式前，配置对应层级的电源开关引脚状态，并激活状态保持。

### I2C 空闲休眠

M5PM1 支持配置 I2C 空闲通信自动休眠状态，来降低整机功耗。进入休眠状态后，ESP32-S3 与 M5PM1 的首次通信将用于 M5PM1 唤醒，因此将通信失败，有效的通信将在唤醒后的下一次通信中完成。

```cpp
m5pm1_err_t setI2cSleepTime(uint8_t seconds);
```

## 3. M5PM1 Timer 定时器

M5PM1 支持配置定时器功能，当计时结束后，执行相应的操作，如开机，关机，复位等。

```cpp
m5pm1_err_t timerSet(uint32_t seconds, m5pm1_tim_action_t action);
```

```cpp
typedef enum {
    M5PM1_TIM_ACTION_STOP = 0b000,     // 停止，无动作
                                       // Stop, no action
    M5PM1_TIM_ACTION_FLAG = 0b001,     // 仅设置标志
                                       // Set flag only
    M5PM1_TIM_ACTION_REBOOT = 0b010,   // 系统复位
                                       // System reboot
    M5PM1_TIM_ACTION_POWERON = 0b011,  // 开机
                                       // Power on
    M5PM1_TIM_ACTION_POWEROFF = 0b100  // 关机
                                       // Power off
} m5pm1_tim_action_t;
```

### 定时开机 / 关机案例

案例说明：设备开机后，单击按键 A 配置 10s 定时器触发重新开机，单击按键 B 配置 10s 后定时器触发 M5PM1 关机 (可通过单击电源按键重新开机)。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>

M5PM1 pm1;

void setup(void)
{
    M5.begin();
    Serial.begin(115200);

    // Initialize PM1
    m5pm1_err_t err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);

    if (err == M5PM1_OK) {
        Serial.println("PM1 initialization successful");
    } else {
        Serial.printf("PM1 initialization failed, error code: %d\n", err);
    }
    pm1.setSingleResetDisable(false);
    M5.Display.fillScreen(BLACK);
    M5.Display.setTextColor(WHITE);
    M5.Display.setTextFont(&fonts::FreeMonoBold12pt7b);
    M5.Display.setCursor(80, 150);
    M5.Display.println("Timer Power Test");
    M5.Display.println("    BtnA: After 10s ON");
    M5.Display.println("    BtnB: After 10s OFF");
}

void loop(void)
{
    M5.update();
    if (M5.BtnA.wasPressed()) {
        M5.Display.fillScreen(BLACK);
        M5.Display.setCursor(40, 80);
        M5.Display.println("Shutdown");
        M5.Display.println("  After 10s");
        M5.Display.println("     Power ON");
        delay(500);
        pm1.timerSet(10, M5PM1_TIM_ACTION_POWERON);
        pm1.shutdown();
    }
    if (M5.BtnB.wasPressed()) {
        M5.Display.fillScreen(BLACK);
        M5.Display.setCursor(40, 80);
        M5.Display.println("  After 10s");
        M5.Display.println("     Power OFF");
        delay(500);
        pm1.timerSet(10, M5PM1_TIM_ACTION_POWEROFF);
    }
} 
```

## 4. IMU 唤醒

### BMI270 驱动库

- [SparkFun_BMI270_Arduino_Library](https://github.com/sparkfun/SparkFun_BMI270_Arduino_Library)

### IMU M5PM1 唤醒

电源切换至 L1 Mode, 整机仅 IMU、RTC 和 M5PM1 处于供电状态。在配置 IMU 唤醒功能后，M5PM1 也进入休眠状态，同时保持 L1 的输出供电 (3V3_L1_EN)，用于维持 IMU 工作。

此时可通过翻转或移动设备，触发 IMU 唤醒信号，唤醒 M5PM1 重新启动。

M5PM1 唤醒后将重新运行 L0、L1 和 L2 上电流程。ESP32-S3 重新执行初始化。

案例说明：设备开机后，单击按键 A 配置 IMU 中断模式与 M5PM1 L1 电源保持，M5PM1 进入休眠。 此时翻转或移动设备即可触发 M5PM1 唤醒，ESP32-S3 重新上电。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include <Wire.h>
#include "SparkFun_BMI270_Arduino_Library.h"

BMI270 imu;
M5PM1 pm1;

void setup(void)
{
    M5.begin();
    Serial.begin(115200);

    Wire1.setPins(M5.getPin(m5::pin_name_t::in_i2c_sda), M5.getPin(m5::pin_name_t::in_i2c_scl));

    // Initialize PM1
    m5pm1_err_t err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);

    if (err == M5PM1_OK) {
        Serial.println("PM1 initialization successful");
        pm1.gpioSetWakeEnable(M5PM1_GPIO_NUM_0, true);
        pm1.gpioSetWakeEdge(M5PM1_GPIO_NUM_0, M5PM1_GPIO_WAKE_FALLING);  // Falling edge
    } else {
        Serial.printf("PM1 initialization failed, error code: %d\n", err);
    }
    pm1.setSingleResetDisable(false);

    // Check if sensor is connected and initialize
    // Address defaults to 0x68)
    while(imu.beginI2C(BMI2_I2C_PRIM_ADDR, Wire1) != BMI2_OK)
    {
        Serial.println("Error: BMI270 not connected, check wiring and I2C address!");
        delay(1000);
    }
    imu.disableFeature(BMI2_ANY_MOTION);
    Serial.println("BMI270 initialization successful");

    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    M5.Display.clear();
    M5.Display.setCursor(40, 100);
    M5.Display.printf("IMU Wakeup Test\n\n");
    M5.Display.println("     Press BtnA to Sleep");
    M5.Display.println("     Shake to wake up");
}

void loop(void)
{
    M5.update();
    if (M5.BtnA.wasPressed()) {
        int8_t ret = imu.enableFeature(BMI2_ANY_MOTION);
        // Optional
        // bmi2_sens_config config;
        // config.type = BMI2_ANY_MOTION;
        // config.cfg.any_motion.threshold = 0xA0;// 1LSB equals to 0.48mg. Default is 83mg. Lower is more sensitive
        // config.cfg.any_motion.duration = 0x0A; // 1LSB equals 20ms. Default is 100ms.
        // ret |= imu.setConfig(config);
        //
        bmi2_int_pin_config intPinConfig;
        intPinConfig.pin_type = BMI2_INT1;
        intPinConfig.int_latch = BMI2_INT_NON_LATCH;
        intPinConfig.pin_cfg[0].lvl = BMI2_INT_ACTIVE_LOW;
        intPinConfig.pin_cfg[0].od = BMI2_INT_PUSH_PULL;
        intPinConfig.pin_cfg[0].output_en = BMI2_INT_OUTPUT_ENABLE;
        intPinConfig.pin_cfg[0].input_en = BMI2_INT_INPUT_DISABLE;
        ret |= imu.setInterruptPinConfig(intPinConfig);
        ret |= imu.mapInterruptToPin(BMI2_ANY_MOTION_INT, BMI2_INT1);
        if (!ret){
            Serial.println("BMI270 AnyMotionInterrupt enabled successfully");
        } else {
            Serial.println("Failed to enable BMI270 AnyMotionInterrupt");
        }

        M5.Display.clear();
        M5.Display.setCursor(40, 100);
        M5.Display.println("Power OFF");
        delay(1000);
        // Shutdown
        pm1.setLdoEnable(true);
        pm1.ldoSetPowerHold(true);
        pm1.setLedEnLevel(true);
        pm1.shutdown();
    }
}
```

例程效果演示：

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/StopWatch_Arduino_imu_m5pm1.mp4" type="video/mp4"></video>

### IMU ESP32-S3 唤醒

M5PM1 的 PYG1_IRQ 引脚在电路上连接到了 ESP32-S3 的 G12 上，可以通过链式的唤醒信号实现 ESP32-S3 唤醒，实现步骤如下:

1. 配置 M5PM1 PYG0 为输入模式，该引脚连接 IMU 的 INT1 输出信号。
2. 配置 M5PM1 PYG1_IRQ 为 IRQ 输出信号引脚。当 PYG0 (IMU 产生中断信号) 引脚状态变化时， PYG1_IRQ 引脚将输出中断信号
3. 配置 ESP32-S3 进入休眠，配置唤醒引脚为 G12
4. 翻转或移动设备：触发 IMU 唤醒信号 -> 触发 M5PM1 PYG1_IRQ -> 唤醒 ESP32-S3

案例说明：设备开机后，单击按键 A 配置 IMU 中断模式。翻转或移动设备即可触发 GPIO 中断处理函数。再次单击按键 A 可清除 M5PM1 IRQ 标志位，再次进行测试。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include <Wire.h>
#include "SparkFun_BMI270_Arduino_Library.h"
#include "driver/rtc_io.h"

BMI270 imu;
M5PM1 pm1;

void setup(void)
{
    M5.begin();
    Serial.begin(115200);

    Wire1.setPins(M5.getPin(m5::pin_name_t::in_i2c_sda), M5.getPin(m5::pin_name_t::in_i2c_scl));

    // Initialize PM1
    m5pm1_err_t err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);

    if (err == M5PM1_OK) {
        Serial.println("PM1 initialization successful");
        pm1.irqClearGpioAll();
        pm1.irqClearSysAll();
        pm1.irqClearBtnAll();

        pm1.irqSetGpioMaskAll(M5PM1_IRQ_MASK_ENABLE);
        pm1.irqSetSysMaskAll(M5PM1_IRQ_MASK_ENABLE);
        pm1.irqSetBtnMaskAll(M5PM1_IRQ_MASK_ENABLE);

        pm1.irqSetGpioMask(M5PM1_IRQ_GPIO0, M5PM1_IRQ_MASK_DISABLE);
        pm1.gpioSetMode(M5PM1_GPIO_NUM_0, M5PM1_GPIO_MODE_INPUT);
        pm1.gpioSetPull(M5PM1_GPIO_NUM_0, M5PM1_GPIO_PULL_UP);

        pm1.gpioSetMode(M5PM1_GPIO_NUM_1, M5PM1_GPIO_MODE_OUTPUT);
        pm1.gpioSetDrive(M5PM1_GPIO_NUM_1, M5PM1_GPIO_DRIVE_PUSHPULL);
        pm1.gpioSetFunc(M5PM1_GPIO_NUM_1, M5PM1_GPIO_FUNC_IRQ);
    } else {
        Serial.printf("PM1 initialization failed, error code: %d\n", err);
    }
    pm1.setSingleResetDisable(false);

    // Check if sensor is connected and initialize
    // Address defaults to 0x68)
    while(imu.beginI2C(BMI2_I2C_PRIM_ADDR, Wire1) != BMI2_OK)
    {
        Serial.println("Error: BMI270 not connected, check wiring and I2C address!");
        delay(1000);
    }
    imu.disableFeature(BMI2_ANY_MOTION);
    Serial.println("BMI270 initialization successful");

    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    M5.Display.clear();
    M5.Display.setCursor(40, 100);
    M5.Display.printf("IMU IRQ Test\n\n");
    M5.Display.println("     Press BtnA to Sleep");
    M5.Display.println("     Shake to wake up");
}

volatile bool pm1IrqTriggered = false;

void ARDUINO_ISR_ATTR pm1_irq_handler()
{
    pm1IrqTriggered = true;
}

void loop(void)
{
    M5.update();

    if (pm1IrqTriggered) {
        pm1IrqTriggered = false;

        Serial.println("PM1 IRQ triggered");

        uint16_t status = 0;
        imu.getInterruptStatus(&status);
        Serial.printf("BMI270 interrupt status: 0x%04X\n", status);

        M5.Display.setCursor(40, 130);
        M5.Display.println("PM1 IRQ triggered");
    }
    
    if (M5.BtnA.wasPressed()) {
        pm1.irqClearGpioAll();
        pm1.irqClearSysAll();
        pm1.irqClearBtnAll();
        int8_t ret = imu.enableFeature(BMI2_ANY_MOTION);
        // Optional
        // bmi2_sens_config config;
        // config.type = BMI2_ANY_MOTION;
        // ret |= imu.getConfig(&config);
        // config.cfg.any_motion.threshold = 0xE0;// 1LSB equals to 0.48mg. Default is 83mg. Lower is more sensitive
        // config.cfg.any_motion.duration = 0x0A; // 1LSB equals 20ms. Default is 100ms.
        // ret |= imu.setConfig(config);
        
        bmi2_int_pin_config intPinConfig;
        intPinConfig.pin_type = BMI2_INT1;
        intPinConfig.int_latch = BMI2_INT_NON_LATCH;
        intPinConfig.pin_cfg[0].lvl = BMI2_INT_ACTIVE_HIGH;// active - high
        intPinConfig.pin_cfg[0].od = BMI2_INT_PUSH_PULL;
        intPinConfig.pin_cfg[0].output_en = BMI2_INT_OUTPUT_ENABLE;
        intPinConfig.pin_cfg[0].input_en = BMI2_INT_INPUT_DISABLE;
        ret |= imu.setInterruptPinConfig(intPinConfig);
        ret |= imu.mapInterruptToPin(BMI2_ANY_MOTION_INT, BMI2_INT1);
        if (!ret){
            Serial.println("BMI270 AnyMotionInterrupt enabled successfully");
        } else {
            Serial.println("Failed to enable BMI270 AnyMotionInterrupt");
        }

        M5.Display.clear();
        M5.Display.setCursor(40, 100);
        M5.Display.println("Now Shake!");
        
        // Choose either of the two pieces of code below.
        pinMode(GPIO_NUM_12, INPUT_PULLUP);
        attachInterrupt(GPIO_NUM_12, pm1_irq_handler, FALLING);

        // esp_sleep_enable_ext0_wakeup(GPIO_NUM_12, 0);  // 0 = Low
        // rtc_gpio_pullup_en(GPIO_NUM_12);
        // Serial.println("Going to sleep now");
        // esp_deep_sleep_start();
    }
}
```

例程效果演示：

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/StopWatch_Arduino_imu_esp32s3.mp4" type="video/mp4"></video>

## 5. RTC 唤醒

### RTC M5PM1 唤醒

电源切换至 L1 Mode, 整机仅 IMU、RTC 和 M5PM1 处于供电状态。当配置 RTC 定时唤醒功能后，M5PM1 进入休眠状态，同时保持 L1 的输出供电 (3V3_L1_EN)，用于维持 RTC 工作。

此时可通过配置 RTC 定时器唤醒，触发 M5PM1 唤醒，ESP32-S3 重新上电。

M5PM1 唤醒后将重新运行 L0、L1 和 L2 上电流程。ESP32-S3 重新执行初始化。

案例说明：设备开机后，单击按键 A 配置 RTC 定时器唤醒，M5PM1 进入休眠。 5s 后触发 RTC 唤醒，ESP32-S3 重新上电。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>

M5PM1 pm1;

void setup(void)
{
    M5.begin();
    Serial.begin(115200);

    // Initialize PM1
    m5pm1_err_t err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);

    if (err == M5PM1_OK) {
        Serial.println("PM1 initialization successful");
        pm1.gpioSetWakeEnable(M5PM1_GPIO_NUM_0, true);
        pm1.gpioSetWakeEdge(M5PM1_GPIO_NUM_0, M5PM1_GPIO_WAKE_FALLING);  // Falling edge
    } else {
        Serial.printf("PM1 initialization failed, error code: %d\n", err);
    }
    pm1.setSingleResetDisable(false);

    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    M5.Display.clear();
    M5.Display.setCursor(40, 100);
    M5.Display.printf("RTC Wakeup Test\n\n");
    M5.Display.println("     Press BtnA to Sleep");
}

void loop(void)
{
    M5.update();
    if (M5.BtnA.wasPressed()) {
        M5.Rtc.clearIRQ();

        if (M5.Rtc.setTimerIRQ(5000)){// 5s later wakeup
            Serial.println("RTC IRQ enabled successfully");
            M5.Display.clear();
            M5.Display.setCursor(40, 100);
            M5.Display.printf("Power OFF");
            M5.Display.setCursor(40, 130);
            M5.Display.printf("5s later wakeup");
            delay(500);
            // Shutdown
            pm1.setLdoEnable(true);
            pm1.ldoSetPowerHold(true);
            pm1.setLedEnLevel(true);
            pm1.shutdown();
        } else {
            Serial.println("Failed to enable RTC IRQ");
        }
    }
}
```

例程效果演示：

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/StopWatch_Arduino_rtc_m5pm1.mp4" type="video/mp4"></video>

### RTC ESP32-S3 唤醒

RTC 唤醒配置步骤与 IMU ESP32-S3 唤醒类似，区别在于 RTC 唤醒不需要像 IMU 那样配置 BMI270 中断，但仍依赖 RTC IRQ → M5PM1 GPIO → PYG1_IRQ → ESP32-S3 G12 这条链路。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include "driver/rtc_io.h"

M5PM1 pm1;

void setup(void) {
  M5.begin();
  Serial.begin(115200);
  M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
  M5.Display.clear();
  M5.Display.setCursor(40, 100);
  M5.Display.printf("RTC IRQ Test\n\n");
  M5.Display.println("     Press BtnA to Sleep");

  // Initialize PM1
  m5pm1_err_t err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);

  if (err == M5PM1_OK) {
    Serial.println("PM1 initialization successful");
    pm1.irqClearGpioAll();
    pm1.irqClearSysAll();
    pm1.irqClearBtnAll();

    pm1.irqSetGpioMaskAll(M5PM1_IRQ_MASK_ENABLE);
    pm1.irqSetSysMaskAll(M5PM1_IRQ_MASK_ENABLE);
    pm1.irqSetBtnMaskAll(M5PM1_IRQ_MASK_ENABLE);

    pm1.irqSetGpioMask(M5PM1_IRQ_GPIO0, M5PM1_IRQ_MASK_DISABLE);
    pm1.gpioSetMode(M5PM1_GPIO_NUM_0, M5PM1_GPIO_MODE_INPUT);
    pm1.gpioSetPull(M5PM1_GPIO_NUM_0, M5PM1_GPIO_PULL_UP);

    pm1.gpioSetMode(M5PM1_GPIO_NUM_1, M5PM1_GPIO_MODE_OUTPUT);
    pm1.gpioSetDrive(M5PM1_GPIO_NUM_1, M5PM1_GPIO_DRIVE_PUSHPULL);
    pm1.gpioSetFunc(M5PM1_GPIO_NUM_1, M5PM1_GPIO_FUNC_IRQ);
  } else {
    Serial.printf("PM1 initialization failed, error code: %d\n", err);
  }
  pm1.setSingleResetDisable(false);
  delay(200);
  M5.Rtc.clearIRQ();
  delay(200);
}

volatile bool pm1IrqTriggered = false;

void ARDUINO_ISR_ATTR pm1_irq_handler() {
    pm1IrqTriggered = true;
}

void loop(void) {
    M5.update();

    if (pm1IrqTriggered) {
        pm1IrqTriggered = false;
        M5.Rtc.setTimerIRQ(0);
        M5.Rtc.clearIRQ();
        pm1.irqClearGpioAll();
        pm1.irqClearSysAll();
        pm1.irqClearBtnAll();

        Serial.println("PM1 IRQ triggered");
        M5.Display.setCursor(40, 130);
        M5.Display.println("PM1 IRQ triggered");
    }

    if (M5.BtnA.wasPressed()) {
        if (M5.Rtc.setTimerIRQ(5000)){// Set Timer IRQ
            Serial.println("RTC IRQ enabled successfully");
            M5.Display.clear();
            M5.Display.setCursor(40, 100);
            M5.Display.printf("Wait for IRQ to wake up...");

            // Choose either of the two pieces of code below.
            pinMode(GPIO_NUM_12, INPUT_PULLUP);
            attachInterrupt(GPIO_NUM_12, pm1_irq_handler, FALLING);

            // esp_sleep_enable_ext0_wakeup(GPIO_NUM_12, 0);  // 0 = Low
            // rtc_gpio_pullup_en(GPIO_NUM_12);
            // Serial.println("Going to sleep now");
            // esp_deep_sleep_start();
        } else {
            Serial.println("Failed to enable RTC IRQ");
        }
    }
}
```

例程效果演示：

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/StopWatch_Arduino_rtc_esp32s3.mp4" type="video/mp4"></video>

## 6. M5IOE1 外设控制

M5IOE1 作为一个独立的 IO 拓展芯片，控制着 L3B 级电源的部分外设供电及相关配置，如屏幕、扬声器、振动电机等。通过 M5IOE1 的 API，可以独立控制这些外设，实现更灵活的电源管理。

#> 说明 | 由于目前 M5Unified 库暂时不支持单独初始化屏幕，因此下方程序中未对涉及到屏幕的 `IOE_TP_EN`、`IOE_OLED_RST` 以及 `IOE_L3B_EN` 引脚进行控制，这些引脚拉低再次上电后屏幕需要再次初始化才能正常显示和触摸，请待后续 M5Unified 库更新后支持。控制 API 同理，例如可以通过 `ioe1.digitalWrite(IOE_L3B_EN, LOW)` 来控制 L3B 电源开关。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include <M5IOE1.h>

M5PM1 pm1;
M5IOE1 ioe1;

#define IOE_MUX_EN   M5IOE1_PIN_1
#define IOE_AU_EN    M5IOE1_PIN_3
#define IOE_MT_PWM   M5IOE1_PIN_9
#define IOE_L3B_EN   M5IOE1_PIN_8
#define IOE_SPK_EN   M5IOE1_PIN_10
#define IOE_TP_EN    M5IOE1_PIN_4
#define IOE_OLED_RST M5IOE1_PIN_5

void setup(void)
{
    M5.begin();
    Serial.begin(115200);

    // Initialize PM1
    m5pm1_err_t pm1_err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);

    if (pm1_err == M5PM1_OK) {
        Serial.println("PM1 initialization successful");
    } else {
        Serial.printf("PM1 initialization failed, error code: %d\n", pm1_err);
    }
    pm1.setSingleResetDisable(false);

    // Initialize IOE1
    m5ioe1_err_t ioe1_err = ioe1.begin(&M5.In_I2C, M5IOE1_DEFAULT_ADDR, M5IOE1_I2C_FREQ_100K);

    if (ioe1_err == M5IOE1_OK) {
        Serial.println("IOE1 initialization successful");
    } else {
        Serial.printf("IOE1 initialization failed, error code: %d\n", ioe1_err);
    }
    ioe1.pinMode(IOE_MUX_EN, OUTPUT);
    ioe1.pinMode(IOE_AU_EN, OUTPUT);
    ioe1.pinMode(IOE_MT_PWM, OUTPUT);
    ioe1.pinMode(IOE_L3B_EN, OUTPUT);
    ioe1.pinMode(IOE_SPK_EN, OUTPUT);
    ioe1.pinMode(IOE_TP_EN, OUTPUT);
    ioe1.pinMode(IOE_OLED_RST, OUTPUT);
    
    ioe1.setPwmFrequency(2000);
    ioe1.setPwmDuty(M5IOE1_PWM_CH1, 0);   

    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    M5.Display.clear();
    M5.Display.setCursor(40, 100);
    M5.Display.printf("IOE1 Power Test Begin\n\n");
    delay(1000);
}

void loop(void)
{
    M5.update();
    // MUX IO
    M5.Display.clear();
    M5.Display.setCursor(40, 100);
    M5.Display.printf("MUX IO set to UART0");
    ioe1.digitalWrite(IOE_MUX_EN, LOW);
    delay(1000);
    M5.Display.setCursor(40, 130);
    M5.Display.printf("MUX IO set to USB");
    ioe1.digitalWrite(IOE_MUX_EN, HIGH);
    delay(1000);

    // Speaker
    M5.Display.clear();
    M5.Display.setCursor(40, 100);
    M5.Display.printf("Speaker off");
    ioe1.digitalWrite(IOE_SPK_EN, LOW);
    M5.Speaker.tone(10000, 100);
    M5.Display.setCursor(40, 130);
    M5.Display.printf("No sound");
    delay(1000);
    M5.Display.setCursor(40, 160);
    M5.Display.printf("1s later hear sound");
    ioe1.digitalWrite(IOE_SPK_EN, HIGH);
    delay(1000);
    M5.Speaker.tone(4000, 200);
    delay(1000);

    // Vibration Motor
    M5.Display.clear();
    M5.Display.setCursor(40, 100);
    M5.Display.printf("Motor off");
    ioe1.setPwmDuty(M5IOE1_PWM_CH1, 0);
    M5.Display.setCursor(40, 130);
    M5.Display.printf("No vibration");
    delay(1000);
    M5.Display.setCursor(40, 160);
    M5.Display.printf("1s vibrate");
    ioe1.digitalWrite(IOE_MT_PWM, HIGH);
    ioe1.setPwmDuty(M5IOE1_PWM_CH1, 50);
    delay(1000);
    ioe1.setPwmDuty(M5IOE1_PWM_CH1, 0);
    delay(200);

    // Audio
    M5.Display.clear();
    M5.Display.setCursor(40, 100);
    M5.Display.printf("Audio off");
    ioe1.digitalWrite(IOE_AU_EN, LOW);
    M5.Speaker.end();
    M5.Speaker.begin();
    M5.Speaker.setVolume(128);
    M5.Speaker.tone(10000, 100);
    M5.Display.setCursor(40, 130);
    M5.Display.printf("No sound");
    delay(1000);
    M5.Display.setCursor(40, 160);
    M5.Display.printf("1s later hear sound");
    ioe1.digitalWrite(IOE_AU_EN, HIGH);
    M5.Speaker.end();
    M5.Speaker.begin();
    M5.Speaker.setVolume(128);
    delay(1000);
    M5.Speaker.tone(6000, 200);
    delay(1000);    
}
```

成功烧录后，程序将依次演示背部拓展接口切换、扬声器、振动电机以及音频放大器的控制效果。

