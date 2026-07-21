# M5Unified Mic Class

- [Mic Class](#m5unified-mic-class)
  - [config](#config)
  - [begin](#begin)
  - [end](#end)
  - [isRunning](#isrunning)
  - [isEnabled](#isenabled)
  - [isRecording](#isrecording)
  - [setSampleRate](#setsamplerate)
  - [record](#record)

## config

**函数原型:**

```cpp
mic_config_t config(void);
```

**功能说明:**

- 获取当前 Mic 配置信息

**传入参数:**

- null

**返回值:**

- mic_config_t: Mic 配置信息

```cpp line-num
  struct mic_config_t
  {
    /// i2s_data_in (for mic)
    int pin_data_in = -1;

    /// i2s_bclk
    int pin_bck = I2S_PIN_NO_CHANGE;

    /// i2s_mclk
    int pin_mck = I2S_PIN_NO_CHANGE;

    /// i2s_ws (lrck)
    int pin_ws = I2S_PIN_NO_CHANGE;

    /// input sampling rate (Hz)
    uint32_t sample_rate = 16000;

    union
    {
      struct
      {
        uint8_t left_channel : 1;
        uint8_t stereo : 1;
        uint8_t reserve : 6;
      };
      input_channel_t input_channel = input_only_right;
    };

    /// Sampling times of obtain the average value
    uint8_t over_sampling = 2;

    /// multiplier for input value
    uint8_t magnification = 16;

    /// Coefficient of the previous value, used for noise filtering.
    uint8_t noise_filter_level = 0;

    /// use analog input mic ( need only pin_data_in )
    bool use_adc = false;

    /// for I2S dma_buf_len
    size_t dma_buf_len = 128;

    /// for I2S dma_buf_count
    size_t dma_buf_count = 8;

    /// background task priority
    uint8_t task_priority = 2;

    /// background task pinned core
    uint8_t task_pinned_core = -1;

    /// I2S port
    i2s_port_t i2s_port = i2s_port_t::I2S_NUM_0;
  };
```

**函数原型:**

```cpp
void config(const mic_config_t& cfg);
```

**功能说明:**

- 配置 Mic 配置信息

**传入参数:**

- mic_config_t& cfg:
  - 配置信息引用

**返回值:**

- null

## begin

**函数原型:**

```cpp
bool begin(void);
```

**功能说明:**

- 初始化 Mic

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

- 判断当前 Mic 后台任务程序是否处于运行状态

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

- 判断当前 Mic 是否初始化

**传入参数:**

- null

**返回值:**

- bool:
  - true:已初始化
  - false:未初始化

## isRecording

**函数原型:**

```cpp
size_t isRecording(void);
```

**功能说明:**

- 判断当前 Mic 是否处于录制状态

**传入参数:**

- null

**返回值:**

- size_t:
  - not recording 未处于录制状态: 0
  - recording (There's room in the queue) 处于录制状态, 队列中还有空间: 1
  - recording (There's no room in the queue.) 处于录制状态，队列已满: 2

## setSampleRate

**函数原型:**

```cpp
void setSampleRate(uint32_t sample_rate);
```

**功能说明:**

- 设置录制采样率

**传入参数:**

- uint32_t sample_rate:
  - 采样率(Hz)

**返回值:**

- null

## record

**函数原型:**

```cpp
bool record(uint8_t* rec_data, size_t array_len, uint32_t sample_rate, bool stereo = false);
```

```cpp
bool record(int16_t* rec_data, size_t array_len, uint32_t sample_rate, bool stereo = false);
```

```cpp
bool record(uint8_t* rec_data, size_t array_len);
```

```cpp
bool record(int16_t* rec_data, size_t array_len);
```

**功能说明:**

- 录制 8bit 或 16bit 的 wav 原始音频数据

**传入参数:**

- uint8_t* rec_data:
  - 存放原始音频数据的指针
- size_t array_len:
  - 数组长度
- uint32_t sample_rate:
  - 录制的采样率(Hz)
- bool stereo:
  - true:立体声
  - false:单声道

**返回值:**

- bool:
  - true:执行成功
  - false:执行失败
