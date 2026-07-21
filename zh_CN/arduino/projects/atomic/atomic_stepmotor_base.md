# Atomic Stepmotor Base Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库：          

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 使用到的硬件产品：
  - [AtomS3R](https://shop.m5stack.com/products/atoms3r-ai-chatbot-kit-8mb-psram)
  - [Atomic Stepmotor Base](https://shop.m5stack.com/products/atomic-stepmotor-base-drv8825)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3R/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20Stepmotor%20Base/img-8395110d-7df8-4c8d-b613-9e52d7216eeb.webp" width="20%">

## 2. 步进电机控制知识介绍

- 步进电机是一种将电脉冲转换为角位移的电机。每接收到一个脉冲，电机轴就会按固定的角度旋转。这种特性使得步进电机非常适合需要精确位置控制的应用场景，如打印机、数控机床和机器人等。

- 1\. 结构组成：
  - 定子（Stator）：由多个绕组组成，通电后产生磁场。
  - 转子（Rotor）：通常为带有齿槽的铁芯，受定子磁场作用而旋转。

- 2\. 工作原理：
  - 通过按特定顺序给 A、B 相绕组通电，产生旋转磁场，吸引转子磁极随之转动。
  - 1 个控制脉冲对应 1 次绕组通电状态切换，转子完成 1 步角位移；脉冲频率决定转速，脉冲数量决定总位移。

- 3\. 主要参数：
  - 相数（Phases）：步进电机的绕组数量，常见的有两相、三相、四相、五相步进电机。
  - 全步数量（Number of Full Steps）：电机旋转一圈所需的基础脉冲数，由硬件结构决定。两相步进电机常见为 200 步 / 圈，即每接收 200 个全步脉冲，转子旋转 360°。
  - 步距角（Step Angle）：指电机每接收一个脉冲时轴旋转的角度，公式为 `步距角 = 360°/ 全步数量`，两相 200 步电机的全步步距角 = 360° ÷ 200 = 1.8°。
  - 微步细分（Microstepping）：通过控制电流大小将 1 个全步拆分为多个更小的 “微步”，可以提升定位精度和平滑度。常见细分有 1/2、1/4、1/8、1/16 等。
  - 转速（Speed）：步进电机的转速通常以每分钟转圈数（RPM）表示，受脉冲频率和负载影响，与脉冲频率正相关，公式为 `转速 = 脉冲频率 / 全步数量 × 60`。
  - 保持力矩（Holding Torque）：当电机静止时，能够抵抗外力使其转动的最大力矩，两相电机常见范围为 0.1 ~ 5N・m。

## 3. 案例程序

- 本教程中使用的主控设备为 AtomS3R ，搭配 Atomic Stepmotor Base。本模块采用串口方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的串口引脚为`G5 (EN)`、`G6 (STEP)`、`G7 (DIR)`。

### 3.1 引脚拨码开关

Atomic Stepmotor Base 可以通过调节拨码开关设置步进电机的细分模式，拨码开关共有 4 个开关位，M2、M1、M0、DECAY 分别对应芯片 DRV8825 的 `MODE2`、`MODE1`、`MODE0` 、 `DECAY` 引脚。其中，M2、M1、M0 用于设置步进电机的细分模式，具体设置如下表所示；
DECAY 用于设置电流衰减模式，更多详细信息请参考 DRV8825 [数据手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/DRV8825_en.pdf)。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/925/microstep.png" width="60%">

下方例程中通过变量 `step_division` 设置了步进电机的细分模式，请根据拨码开关的实际设置修改该变量的值；本次实际设置中，引脚拨码开关切换到了 1/32 微步模式，详见下图。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/925/Atomic_Stepmotor_Base_DIP.png" width="40%">

### 3.2 示例代码

```cpp line-num
#include "M5Unified.h"
#include "M5GFX.h"

// Stepper motor configuration parameters
int step_division = 32;           // Motor microstepping division factor
int number_of_steps = 200;       // Number of steps per full revolution of the motor
int en_pin = 5;                  // Motor driver enable pin
int step_pin = 6;                // Motor step control pin
int dir_pin = 7;                 // Motor direction control pin

// Timing variables for step control
unsigned long step_interval = 10000;  // Microsecond interval between step pulses
unsigned long last_step_time = 0;     // Timestamp of the last step pulse
unsigned long target_step_time1 = 0;  // Target time for step pin HIGH state
unsigned long target_step_time2 = 0;  // Target time for step pin LOW state

void motor_setSpeed(float rpm);               // Set motor rotation speed (revolutions per minute)
void motor_powerEnable(bool ena);             // Enable/disable motor driver
void motor_setDirection(long steps_to_move);  // Set rotation direction based on step count
void motor_move();                            // Generate a single step pulse
void motor_moveInterval(unsigned long target_delay);  // Control step pulse timing
void motor_dynamicMove(int s1, int s2);       // Step with dynamic acceleration/deceleration
void motor_step(long steps_to_move);          // Move specified steps without acceleration
void motor_step_accdec(long steps_to_move, long steps_acc, long steps_dec);  // Move with acceleration/deceleration

void setup() {
  M5.begin(); 
  M5.Lcd.setFont(&fonts::FreeMonoBoldOblique9pt7b);  // Set display font
  M5.Lcd.drawCenterString("Motor", 64, 64);          // Display title at center

  pinMode(en_pin, OUTPUT);
  pinMode(dir_pin, OUTPUT);
  pinMode(step_pin, OUTPUT);

  motor_setSpeed(0);       // Set initial speed to 0
  motor_powerEnable(true); // Enable motor driver
  delay(1600);             // Short delay for initialization
}

void loop() {
  M5.update();  

  if (M5.BtnA.wasPressed()) {
    motor_setSpeed(300);   // Set motor speed to 300 RPM
    motor_step(1200);      // Rotate 1200 steps clockwise
    motor_step(-1200);     // Rotate 1200 steps counter-clockwise
  }
}

// ---- Function Definitions ----

/**
 * Set motor rotation speed in revolutions per minute (RPM)
 * Calculates step interval based on RPM, steps per revolution, and microstepping
 * @param rpm Target rotation speed in revolutions per minute
 */
void motor_setSpeed(float rpm) {
  // Calculate microsecond interval between steps: 
  // 60,000,000 microseconds/minute ÷ (steps/rev × RPM × microsteps)
  step_interval = 60000000L / (number_of_steps * rpm * step_division);
}

/**
 * Enable or disable the motor driver
 * @param ena True to enable motor (driver active), false to disable
 */
void motor_powerEnable(bool ena) {
  digitalWrite(en_pin, ena ? LOW : HIGH);  // Typically, LOW enables most drivers
}

/**
 * Set motor rotation direction based on step count sign
 * @param steps_to_move Positive for clockwise, negative for counter-clockwise
 */
void motor_setDirection(long steps_to_move) {
  if (steps_to_move < 0) {
    digitalWrite(dir_pin, HIGH);  // Set direction pin for counter-clockwise
  } else {
    digitalWrite(dir_pin, LOW);   // Set direction pin for clockwise
  }
}

/**
 * Generate a single step pulse (HIGH then LOW) with proper timing
 */
void motor_move() {
  digitalWrite(step_pin, HIGH);    // Set step pin HIGH to trigger step
  motor_moveInterval(step_interval);  // Maintain HIGH state and then transition to LOW
}

/**
 * Control timing for step pin state transitions
 * Ensures proper duration for HIGH and LOW states of the step pulse
 * @param target_delay Total duration of one step cycle (HIGH + LOW) in microseconds
 */
void motor_moveInterval(unsigned long target_delay) {
  // Calculate target times for state transitions
  target_step_time1 = last_step_time + (target_delay / 2);  // Midpoint (HIGH to LOW)
  target_step_time2 = last_step_time + target_delay;        // End of cycle (LOW to next step)

  // Wait for HIGH state duration
  if (target_step_time1 >= last_step_time) {
    while (micros() < target_step_time1) {}  // Handle normal time progression
  } else {
    while ((long)(micros()) < (long)target_step_time1) {}  // Handle micros() rollover
  }
  
  digitalWrite(step_pin, LOW);  // Set step pin LOW after half the interval

  // Wait for remaining LOW state duration
  if (target_step_time2 >= last_step_time) {
    while (micros() < target_step_time2) {}  // Handle normal time progression
  } else {
    while ((long)(micros()) < (long)target_step_time2) {}  // Handle micros() rollover
  }
  
  last_step_time = micros();  // Update last step timestamp
}

/**
 * Generate a step with dynamic speed adjustment for acceleration/deceleration
 * @param s1 Current step in acceleration/deceleration phase
 * @param s2 Total steps in acceleration/deceleration phase
 */
void motor_dynamicMove(int s1, int s2) {
  digitalWrite(step_pin, HIGH);  // Start step pulse
  
  // Calculate speed ratio using polynomial for smooth acceleration/deceleration
  double r1 = (double)s1 / (double)s2;
  double r2 = 0.1 + 0.2*r1 + 2.2*r1*r1 - 1.5*r1*r1*r1;
  
  // Adjust step interval based on calculated ratio
  motor_moveInterval((unsigned long)(step_interval / r2));
}

/**
 * Move motor specified number of steps without acceleration
 * Converts input steps to microstepped steps using step_division
 * @param steps_to_move Number of steps to move (positive = clockwise, negative = counter-clockwise)
 */
void motor_step(long steps_to_move) {
  steps_to_move *= step_division;  // Convert to microstepped steps
  motor_setDirection(steps_to_move);  // Set rotation direction
  last_step_time = micros();        // Initialize step timestamp
  
  // Generate each step pulse
  for (long i = abs(steps_to_move); i > 0; i--) {
    motor_move();
  }
}

/**
 * Move motor with acceleration, constant speed, and deceleration phases
 * @param steps_to_move Total steps to move (signed for direction)
 * @param steps_acc Number of steps used for acceleration phase
 * @param steps_dec Number of steps used for deceleration phase
 */
void motor_step_accdec(long steps_to_move, long steps_acc, long steps_dec) {
  // Convert all step counts to microstepped values
  steps_to_move *= step_division;
  steps_acc *= step_division;
  steps_dec *= step_division;
  
  motor_setDirection(steps_to_move);  // Set rotation direction
  last_step_time = micros();          // Initialize step timestamp

  // Acceleration phase: gradually increase speed
  if (steps_acc > 0) {
    for (long i = 1; i <= steps_acc; i++) {
      motor_dynamicMove(i, steps_acc);
    }
  }

  // Constant speed phase: maintain steady speed
  long constant_steps = abs(steps_to_move) - abs(steps_acc) - abs(steps_dec);
  for (long i = constant_steps; i > 0; i--) {
    motor_move();
  }

  // Deceleration phase: gradually decrease speed
  if (steps_dec > 0) {
    for (long i = (steps_dec - 1); i >= 0; i--) {
      motor_dynamicMove(i, steps_dec);
    }
  }
}
```

## 4. 编译上传

- 1\. 下载模式：不同设备进行程序烧录前需要下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- AtomS3R 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/download%20mode.gif" width="30%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/925/Atomic_Stepmotor_Base_arduino_example.png" width="70%">

## 5. 步进电机控制

- 设备上电后按压一次屏幕，步进电机先正转 6 圈/ 1200 步，再反转 6 圈 / 1200 步，具体效果如下所示。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/925/Atomic_Stepmotor_Base_example.mp4" type="video/mp4"></video>

