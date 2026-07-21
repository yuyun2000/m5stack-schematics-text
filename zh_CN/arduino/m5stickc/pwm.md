# StickC PWM 脉冲宽度调制

**PWM用于产生模拟信号驱动舵机或蜂鸣器**

## ledcSetup()

**功能说明:**

设置PWM通道,频率和分辨率

**函数原型:**

`void ledcSetup(uint8_t channel, double freq, uint8_t resolution_bits)`

## ledcAttachPin()

**功能说明:**

将 LEDC 通道绑定到指定 IO 口上以实现输出

**函数原型:**

`void ledcAttachPin(uint8_t pin, uint8_t channel)`

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  ledcSetup(8, 1,10);  
          // Set the frequency of LEDC channel 8 to 1 and the resolution to
          // 10 bits, that is, the duty cycle can be selected from 0 to
          // 1023. 设置LEDC通道8频率为1，分辨率为10位，即占空比可选0~1023
  ledcAttachPin(32,8);
          // Set LEDC channel 8 to output on IO32.  设置LEDC通道8在IO32上输出
}

void loop() {}
```

## ledWrite()

**功能说明:**

向channel通道写入duty%占空比

**函数原型:**

`void ledcWrite(uint8_t channel, uint32_t duty)`


**案例程序:**

```cpp line-num
#include <M5StickC.h>
int freq = 1800;
int channel = 0;
int resolution_bits = 8;
int buzzer = 2;

void setup() {
  M5.begin();
  ledcSetup(channel, freq, resolution_bits);
  ledcAttachPin(buzzer, channel);
}
void loop() {
    ledcWrite(channel, 128);
    delay(1000);
    ledcWrite(channel, 0);
    delay(1000);
}
```