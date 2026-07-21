# StickC-Plus Buzzer 蜂鸣器

## 案例程序

```cpp line-num
#include <M5StickCPlus.h>

void setup() {
    M5.begin();
    M5.Beep.tone(4000, 300);
}

void loop() {
    M5.update();
}
```

## begin

**函数原型:**

```cpp
void begin();
```

**功能说明:**

- 初始化Buzzer, 通过M5.begin();的同时将会自动调用该功能进行初始化。

**传入参数:**

- null

**返回值:**

- null

## update

**函数原型:**

```cpp
void update();
```

**功能说明:**

- 更新Buzzer播放状态, 对于设置了播放时长的功能, 需持续调用该函数进行状态更新。通过M5.update();的同时将会自动调用该功能进行更新。

**传入参数:**

- null

**返回值:**

- null

## end

**函数原型:**

```cpp
void end();
```

**功能说明:**

- 逆初始化, 释放Buzzer IO资源

**传入参数:**

- null

**返回值:**

- null

## mute

**函数原型:**

```cpp
void mute();
```


**功能说明:**

- 播放静音

**传入参数:**

- null

**返回值:**

- null


## tone

**函数原型:**

```cpp
void tone(uint16_t frequency);
```

```cpp
void tone(uint16_t frequency, uint32_t duration);
```


**功能说明:**

- 控制发声频率

**传入参数:**

- uint16_t frequency:
  - 发声频率
- uint32_t duration:
  - 持续时间

**返回值:**

- null


## beep

**函数原型:**

```cpp
void beep();
```


**功能说明:**

- 控制发声Beep提示音, 默认发声频率4000Hz, 持续时间100ms

**传入参数:**

- null

**返回值:**

- null


## setBeep

**函数原型:**

```cpp
void setBeep(uint16_t frequency, uint16_t duration);
```


**功能说明:**

- 配置Beep提示音的参数

**传入参数:**

- uint16_t frequency:
  - 发声频率
- uint32_t duration:
  - 持续时间


**返回值:**

- null


## write

**函数原型:**

```cpp
void write(uint8_t value);
```


**功能说明:**

- 写入Buzzer驱动DAC模拟值

**传入参数:**

- uint8_t value:
  - DAC模拟值


**返回值:**

- null


## setVolume

**函数原型:**

```cpp
void setVolume(uint8_t volume);
```

**功能说明:**

- 设置播放音量, 仅对playMusic函数有效。

**传入参数:**

- uint8_t volume:
  - 音量

**返回值:**

- null

## playMusic

**函数原型:**

```cpp
void playMusic(const uint8_t *music_data, uint16_t sample_rate);
```

**功能说明:**

- 播放原始PCM音频数据

**传入参数:**

- const uint8_t *music_data:
  - 播放数据指针
- uint16_t sample_rate:
  - 播放数据采样率

**返回值:**

- null