# Voice Pyramid Home Assistant 集成

本教程介绍如何将 Voice Pyramid 语音底座集成至 Home Assistant。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_HA_tutorial_01.jpg" width="60%"/>

## 准备工作

- Home Assistant 主机。
- 在 Home Assistant 中安装并启用 [ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。
- 主控控制器 [AtomS3R](/zh_CN/core/AtomS3R)

## 注意事项

- 本教程使用 ESPHome 2026.1.2 版本进行固件编译和烧录。如果你在编译 / 烧录过程中遇到问题，建议将 ESPHome 切换到该版本后重试。

## 创建设备

1. 点击右下角的绿色按钮来创建一个新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="90%"/>

2. 点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="40%"/>

3. 点击 `New Device Setup`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="40%"/>

4. 输入设备名称，然后点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/HA5.webp" width="40%"/>

5. 选择 `ESP32-S3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA5.webp" width="40%"/>

6. 点击 `SKIP` 跳过。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="40%"/>

7. 点击 `EDIT`，通过 YAML 文件来自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/HA4.webp" width="70%"/>

## 修改配置

下面是配置中的核心部分，后文会给出相关参考链接和说明。

### PSRAM 配置

**添加 [PSRAM](https://esphome.io/components/psram/) 组件：**

```yaml
psram:
  mode: octal
  speed: 80MHz
```

### 外部组件

**添加 [External](https://esphome.io/components/external_components/) 外部组件：**

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: [aw87559, si5351, lp5562, pyramidrgb, pyramidtouch]
    refresh: 0s
```

### I2C 总线配置

**添加 [I2C](https://esphome.io/components/i2c/) 组件：**

```yaml
i2c:
  - id: bsp_bus
    sda: GPIO45
    scl: GPIO0
    scan: true
  - id: ext_bus # 用于 Atomic Echo 底座
    sda: GPIO38
    scl: GPIO39
```

### I2S 音频配置

**添加 [I2S Audio](https://esphome.io/components/i2s_audio/) 组件：**

```yaml
i2s_audio:
  - id: i2s_audio_bus
    i2s_lrclk_pin: GPIO8
    i2s_bclk_pin: GPIO6
```

### 音频 DAC 配置

**添加 [Audio DAC](https://esphome.io/components/audio_dac/) 组件：**

```yaml
audio_dac:
  - platform: es8311
    id: es8311_dac
    i2c_id: ext_bus
    bits_per_sample: 16bit
    sample_rate: 16000
```

### 音频 ADC 配置

**添加 [Audio ADC](https://esphome.io/components/audio_adc/) 组件：**

```yaml
audio_adc:
  - platform: es7210
    id: es7210_adc
    i2c_id: ext_bus
    address: 0x40
    bits_per_sample: 16bit
    sample_rate: 16000
```

### 麦克风配置

**添加 [Microphone](https://esphome.io/components/microphone/) 组件：**

```yaml
microphone:
  - platform: i2s_audio
    id: i2s_mic
    sample_rate: 16000
    i2s_din_pin: GPIO5
    bits_per_sample: 16bit
    adc_type: external
    channel: stereo
```

### 扬声器配置

**添加 [Speaker](https://esphome.io/components/speaker/) 组件：**

```yaml
speaker:
  - platform: i2s_audio
    id: i2s_speaker
    i2s_dout_pin: GPIO7
    dac_type: external
    bits_per_sample: 16bit
    sample_rate: 16000
    channel: mono
    audio_dac: es8311_dac
```

## 下载和烧录固件

1. 修改配置后，点击右上角的 `SAVE` 和 `INSTALL`，在弹出的窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

2. 固件编译完成后，点击下载并选择 `Factory format(Previously Modern)`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%"/>

\#> 提示 | 点击 [Voice Pyramid](https://github.com/m5stack/esphome-yaml/blob/main/examples/voice_assistant/echo_pyramid_example.yaml) 可查看完整示例配置。首次编译可能需要较长时间，具体取决于 Home Assistant 主机性能和网络状况。

1. 使用 USB Type‑C 线将设备连接到主机。打开 [ESPHome Web](https://web.esphome.io/)，点击 `CONNECT` 连接设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%"/>

4. 找到对应的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA13.webp" width="40%"/>

5. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%"/>

6. 选择编译好的固件进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/HA6.webp" width="40%"/>

7. 烧录完成后，重新启动设备。

## 开始使用

1. 在 Home Assistant 中点击 `Settings` -> `Device & services` 检查设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%"/>

2. 可以在 `Discover` 区域中发现对应的设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/HA1.webp" width="40%"/>

3. 添加设备后，即可看到相关数据正确显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/HA2.png" width="40%"/>

最终，用户可以通过控制面板配置 Voice Pyramid 上各类可控硬件，并配合自定义唤醒词 `(Echo-Pyramid Wake Word)` 来激活设备，实现如查询天气、时间和日期等智能语音交互功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/HA3.png" width="40%"/>

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=116288789678323&bvid=BV19BQmBpEJg&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/pEA222LXi9k?si=7JFMaxDJYbLOUUrP" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
