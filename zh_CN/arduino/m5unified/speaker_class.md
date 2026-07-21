# M5Unified Speaker Class

- [Speaker Class](#m5unified-speaker-class)
  - [config](#config)
  - [begin](#begin)
  - [end](#end)
  - [isRunning](#isrunning)
  - [isEnabled](#isenabled)
  - [isPlaying](#isplaying)
  - [getPlayingChannels](#getplayingchannels)
  - [setVolume](#setvolume)
  - [getVolume](#getvolume)
  - [setAllChannelVolume](#setallchannelvolume)
  - [setChannelVolume](#setchannelvolume)
  - [getChannelVolume](#getchannelvolume)
  - [stop](#stop)
  - [tone](#tone)
  - [playRaw](#playraw)
  - [playWav](#playwav)

## config

**函数原型:**

```cpp
speaker_config_t config(void);
```

**功能说明:**

- 获取当前 Speaker 配置信息

**传入参数:**

- null

**返回值:**

- speaker_config_t: Speaker 配置信息

```cpp line-num
  struct speaker_config_t
  {
    /// i2s_data_out (for spk)
    int pin_data_out = I2S_PIN_NO_CHANGE;
    /// i2s_bck
    int pin_bck = I2S_PIN_NO_CHANGE;
    /// i2s_ws (lrck)
    int pin_ws = I2S_PIN_NO_CHANGE;
    /// output sampling rate (Hz)
    uint32_t sample_rate = 48000;
    /// use stereo output
    bool stereo = false;
    /// use single gpio buzzer, ( need only pin_data_out )
    bool buzzer = false;
    /// use DAC speaker, ( need only pin_data_out ) ( for ESP32, only GPIO_NUM_25 or GPIO_NUM_26 )
    /// ※ for ESP32, need `i2s_port = I2S_NUM_0`. ( DAC+I2S_NUM_1 is not available )
    bool use_dac = false;
    /// Zero level reference value when using DAC ( 0=Dynamic change )
    uint8_t dac_zero_level = 0;
    /// multiplier for output value
    uint8_t magnification = 16;
    /// for I2S dma_buf_len (max 1024)
    size_t dma_buf_len = 256;
    /// for I2S dma_buf_count
    size_t dma_buf_count = 8;
    /// background task priority
    uint8_t task_priority = 2;
    /// background task pinned core
    uint8_t task_pinned_core = ~0;
    /// I2S port
    i2s_port_t i2s_port = i2s_port_t::I2S_NUM_0;
  };
```

**函数原型:**

```cpp
void config(const speaker_config_t& cfg);
```

**功能说明:**

- 配置 Speaker 配置信息

**传入参数:**

- speaker_config_t& cfg:
  - 配置信息引用

**返回值:**

- null

## begin

**函数原型:**

```cpp
bool begin(void);
```

**功能说明:**

- 初始化 Speaker

**传入参数:**

- null

**返回值:**

- bool:
  - true:初始化成功
  - false:初始化失败

## end

**函数原型:**

```cpp
void end(void);
```

**功能说明:**

- 逆初始化

**传入参数:**

- null

**返回值:**

- null

## isRunning

**函数原型:**

```cpp
bool isRunning(void);
```

**功能说明:**

- 判断当前 Speaker 后台任务程序是否处于运行状态

**传入参数:**

- null

**返回值:**

- bool:
  - true:运行中
  - false:未运行

## isEnabled

**函数原型:**

```cpp
bool isEnabled(void);
```

**功能说明:**

- 判断当前 Speaker 是否初始化

**传入参数:**

- null

**返回值:**

- bool:
  - true:已初始化
  - false:未初始化

## isPlaying

**函数原型:**

```cpp
bool isPlaying(void);
```

**功能说明:**

- 判断当前 Speaker 是否处于播放状态

**传入参数:**

- null

**返回值:**

- bool:
  - true:处于播放状态
  - false:未处于播放状态

**函数原型:**

```cpp
size_t isPlaying(uint8_t channel);
```

**功能说明:**

- 判断当前 Speaker 某个虚拟 channel 是否处于播放状态

**传入参数:**

- uint8_t channel:
  - 虚拟 channel: 0-7

**返回值:**

- size_t:
  - not playing 未处于播放状态: 0
  - playing (There's room in the queue) 处于播放状态, 队列中还有空间: 1
  - playing (There's no room in the queue.) 处于播放状态，队列已满: 2

## getPlayingChannels

**函数原型:**

```cpp
size_t getPlayingChannels(void);
```

**功能说明:**

- 获取当前处于播放状态的虚拟 channel 数量

**传入参数:**

- null

**返回值:**

- size_t: 虚拟 channel 数量

## setVolume

**函数原型:**

```cpp
void setVolume(uint8_t master_volume);
```

**功能说明:**

- 设置播放音量

**传入参数:**

- uint8_t master_volume:
  - 0-255

**返回值:**

- null

## getVolume

**函数原型:**

```cpp
uint8_t getVolume(void);
```

**功能说明:**

- 获取播放音量

**传入参数:**

- null

**返回值:**

- uint8_t volume:
  - 播放音量

## setAllChannelVolume

**函数原型:**

```cpp
void setAllChannelVolume(uint8_t volume);
```

**功能说明:**

- 设置所有虚拟 channel 播放音量

**传入参数:**

- uint8_t volume:
  - 0-255

**返回值:**

- null

## setChannelVolume

**函数原型:**

```cpp
void setChannelVolume(uint8_t channel, uint8_t volume);
```

**功能说明:**

- 设置指定虚拟 channel 播放音量

**传入参数:**

- uint8_t channel:
  - 虚拟 channel: 0-7
- uint8_t volume:
  - 0-255

**返回值:**

- null

## getChannelVolume

**函数原型:**

```cpp
uint8_t getChannelVolume(uint8_t channel);
```

**功能说明:**

- 获取指定虚拟 channel 播放音量

**传入参数:**

- uint8_t channel:
  - 虚拟 channel: 0-7

**返回值:**

- uint8_t volume:
  - 播放音量

## stop

**函数原型:**

```cpp
void stop(void);
```

**功能说明:**

- 停止播放

**传入参数:**

- null

**返回值:**

- null

**函数原型:**

```cpp
void stop(uint8_t channel);
```

**功能说明:**

- 停止指定虚拟 channel 播放

**传入参数:**

- uint8_t channel:
  - 虚拟 channel: 0-7

**返回值:**

- null

## tone

**函数原型:**

```cpp
bool tone(float frequency, uint32_t duration, int channel, bool stop_current_sound, const uint8_t* raw_data, size_t array_len, bool stereo = false);
```

**功能说明:**

- 播放指定频率 tone

**传入参数:**

- float frequency:
  - tone 频率(Hz)
- uint32_t duration:
  - tone 播放持续时间 ms
- int channel:
  - 虚拟 channel: 0-7
- bool stop_current_sound:
  - true:停止当前的播放, 执行新的播放
  - false:不停止当前的播放
- const uint8_t* raw_data:。
  - 单振幅音频, 8bit unsigned wav 数据.
- size_t array_len:
  - raw_data 大小
- bool stereo:
  - true: stereo 立体声
  - false: mono 单声道

**返回值:**

- bool:
  - true:执行成功
  - false:执行失败

**函数原型:**

```cpp
bool tone(float frequency, uint32_t duration = UINT32_MAX, int channel = -1, bool stop_current_sound = true);
```

**功能说明:**

- 播放指定频率 tone

**传入参数:**

- float frequency:
  - tone 频率(Hz)
- uint32_t duration:
  - tone 播放持续时间 ms
- int channel:
  - 虚拟 channel: 0-7
- bool stop_current_sound:
  - true:停止当前的播放, 执行新的播放
  - false:不停止当前的播放

**返回值:**

- bool:
  - true:执行成功
  - false:执行失败

## playRaw

**函数原型:**

```cpp
bool playRaw(const int8_t* raw_data, size_t array_len, uint32_t sample_rate = 44100, bool stereo = false, uint32_t repeat = 1, int channel = -1, bool stop_current_sound = false);
```

```cpp
bool playRaw(const uint8_t* raw_data, size_t array_len, uint32_t sample_rate = 44100, bool stereo = false, uint32_t repeat = 1, int channel = -1, bool stop_current_sound = false);
```

```cpp
bool playRaw(const int16_t* raw_data, size_t array_len, uint32_t sample_rate = 44100, bool stereo = false, uint32_t repeat = 1, int channel = -1, bool stop_current_sound = false);
```

**功能说明:**

- 播放 unsigned 8bit, signed 8bit, signed 16bit wav 原始音频数据

**传入参数:**

- const uint8_t* raw_data / int8_t / int16_t:
  - 原始音频数据指针
- size_t array_len:
  - 原始音频数据长度
- uint32_t sample_rate:
  - 原始音频数据采样率
- bool stereo:
  - true:立体声
  - false:单声道
- uint32_t repeat:
  - 重复播放次数. (默认 = 1)
- int channel:
  - 虚拟 channel: 0-7
- bool stop_current_sound:
  - true:停止当前的播放, 执行新的播放
  - false:不停止当前的播放

**返回值:**

- bool:
  - true:执行成功
  - false:执行失败

## playWav

**函数原型:**

```cpp
bool playWav(const uint8_t* wav_data, size_t data_len = ~0u, uint32_t repeat = 1, int channel = -1, bool stop_current_sound = false);
```

**功能说明:**

- 播放 WAV 格式音频文件数据

**传入参数:**

- const uint8_t* wav_data:
  - wav 数据. (包含 WAV 格式头)
- size_t data_len:
  - 数据长度
- uint32_t repeat:
  - 重复播放次数. (默认 = 1)
- int channel:
  - 虚拟 channel: 0-7
- bool stop_current_sound:
  - true:停止当前的播放, 执行新的播放
  - false:不停止当前的播放

**返回值:**

- bool:
  - true:执行成功
  - false:执行失败
