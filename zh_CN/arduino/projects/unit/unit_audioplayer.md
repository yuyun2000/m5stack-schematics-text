# Unit AudioPlayer Arduino 使用教程

## 1. 准备工作

- 1\. 环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 2\. 使用到的驱动库:

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-AudioPlayer](https://github.com/m5stack/M5Unit-AudioPlayer)

- 3\. 使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit AudioPlayer](https://shop.m5stack.com/products/audio-player-unit-n9301)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-02.webp" width="20%">

## 2. 播放基础配置

Unit AudioPlayer 通过接收指令实现音频播放功能，信号由 3.5mm 插座输出，可提供清晰的音频输出，并支持循环播放和组合播放，通过串口返回当前的指令对应操作的信息。通过使用 Unit AudioPlayer，我们能够实现音频的播放与灵活控制。

### 初始化及播放模式

- **1. 初始化控制串口端口**

  使用 `audioplayer.begin()` 设置主机与 Unit AudioPlayer 相连的串口端口并初始化返回状态标志，传入的参数依次为：串口号、信号接收引脚号、信号发送引脚号。

- **2. 播放模式**

  使用 `audioplayer.setPlayMode()` 可以设置歌曲播放模式。Unit AudioPlayer 支持 7 种播放模式，详细信息如下表：

| 模式                          | 说明                             | 数值 |
| ----------------------------- | -------------------------------- | ---- |
| AUDIO_PLAYER_MODE_ALL_LOOP    | 按顺序循环播放全部歌曲           | 00   |
| AUDIO_PLAYER_MODE_SINGLE_LOOP | 单曲循环当前歌曲                 | 01   |
| AUDIO_PLAYER_MODE_FOLDER_LOOP | 按顺序循环播放当前文件夹全部歌曲 | 02   |
| AUDIO_PLAYER_MODE_RANDOM      | 随机播放当前盘中歌曲             | 03   |
| AUDIO_PLAYER_MODE_SINGLE_STOP | 单次播放当前歌曲                 | 04   |
| AUDIO_PLAYER_MODE_ALL_ONCE    | 按顺序单次播放全部歌曲           | 05   |
| AUDIO_PLAYER_MODE_FOLDER_ONCE | 单次播放当前文件夹全部歌曲       | 06   |

### 歌曲索引号

使用 `audioplayer.selectAudioNum()` 可以切换播放指定歌曲，目前 Unit AudioPlayer 仅支持通过索引号选中歌曲。

?> 特别说明 | 索引编号是根据**歌曲存入 SD 卡中的时间**从早到晚进行排序的，存入时间越晚编号越大，而非歌曲文件名称。

**案例程序：**

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <unit_audioplayer.hpp>

AudioPlayerUnit audioplayer;
m5::touch_detail_t touchDetail;
LGFX_Button button_pre, button_play, button_next;

void setup()
{
    auto cfg            = M5.config();
    cfg.serial_baudrate = 115200;
    M5.begin(cfg);
    M5.Power.setExtOutput(true);
    M5.Lcd.fillScreen(WHITE);
    M5.Lcd.setTextFont(&fonts::DejaVu18);
    M5.Lcd.setTextColor(TFT_BLACK);
    M5.Display.drawString("Unit AudioPlayer Example", 0, 0);

    int8_t port_a_pin1 = -1, port_a_pin2 = -1;
    port_a_pin1 = M5.getPin(m5::pin_name_t::port_a_pin1);
    port_a_pin2 = M5.getPin(m5::pin_name_t::port_a_pin2);
    Serial.printf("getPin: RX:%d TX:%d\n", port_a_pin1, port_a_pin2);
    //To change the serial port, please modify this section.
    while (!audioplayer.begin(&Serial1, port_a_pin1, port_a_pin2)) {//Default UART Num: 1,
        delay(1000);
    }
    Serial.println("Unit AudioPlayer is ready");
    audioplayer.setPlayMode(AUDIO_PLAYER_MODE_SINGLE_STOP);//Default Play Mode: single stop
    audioplayer.playAudio();
    audioplayer.selectAudioNum(1);//Default Audio Num: 1
    M5.Display.drawString("Audio Num:1", 0, 80);
    audioplayer.setVolume(25);

    button_pre.initButton(&M5.Lcd, 47, 215, 60, 60, TFT_WHITE, TFT_PINK, TFT_BLACK, "<", 1, 1);
    button_pre.drawButton();
    button_play.initButton(&M5.Lcd, 157, 215, 60, 60, TFT_WHITE, TFT_PINK, TFT_BLACK, ">\\||", 1, 1);
    button_play.drawButton();
    button_next.initButton(&M5.Lcd, 267, 215, 60, 60, TFT_WHITE, TFT_PINK, TFT_BLACK, ">", 1, 1);
    button_next.drawButton();
}

void loop()
{
    static uint8_t lastPlayStatus = 255;
    static uint8_t lastAudioNum = 0, lastVolume = 0;
    static bool refreshAudioNum = false;

    uint8_t playStatus = audioplayer.checkPlayStatus();
    uint8_t volume     = audioplayer.getVolume();
    uint8_t audioNum   = 0;

    if (refreshAudioNum) {
        audioNum        = audioplayer.getCurrentAudioNumber();
        refreshAudioNum = false;
    } else {
        audioNum = lastAudioNum;
    }

    if (playStatus != lastPlayStatus) {
        static String playStatusStr;
        if (playStatus == AUDIO_PLAYER_STATUS_PAUSED) {
            playStatusStr = "Paused";
        } else if (playStatus == AUDIO_PLAYER_STATUS_STOPPED) {
            playStatusStr = "Stopped";
        } else if (playStatus == AUDIO_PLAYER_STATUS_PLAYING) {
            playStatusStr = "Playing";
        }

        M5.Display.fillRect(0, 40, 320, 20, WHITE);
        M5.Display.drawString("Play Status:" + playStatusStr, 0, 40);

        lastPlayStatus = playStatus;
    }

    if (volume != lastVolume) {
        M5.Display.fillRect(0, 120, 320, 20, WHITE);
        M5.Display.drawString("Volume:" + String(volume), 0, 120);
        lastVolume = volume;
    }

    if (audioNum != lastAudioNum && audioNum != AUDIO_PLAYER_STATUS_ERROR) {
        M5.Display.fillRect(0, 80, 320, 20, WHITE);
        M5.Display.drawString("Audio Num:" + String(audioNum), 0, 80);
        lastAudioNum = audioNum;
    }

    M5.update();
    touchDetail = M5.Touch.getDetail();

    if (touchDetail.isPressed()) {
        if(button_pre.contains(touchDetail.x, touchDetail.y)){
            Serial.println("Btn_pre pressed");
            audioplayer.previousAudio();
            refreshAudioNum = true;
        }
        else if(button_play.contains(touchDetail.x, touchDetail.y)){
            Serial.println("Btn_play pressed");
            if (playStatus == AUDIO_PLAYER_STATUS_PLAYING) {
                audioplayer.pauseAudio();
                Serial.println("pause_audio");
            } else {
                audioplayer.playAudio();
                Serial.println("play_audio");
            }
        }
        else if(button_next.contains(touchDetail.x, touchDetail.y)){
            Serial.println("Btn_next pressed");
            audioplayer.nextAudio();
            refreshAudioNum = true;
        }
    }
}
```

## 3. 编译上传

- 1\. 下载模式：不同设备进行程序烧录前需要下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

  CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/unit_AudioPlayer_arduino_upload.png" width="70%">

## 4. 简单音乐播放器

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/unit_AudioPlayer_arduino_demo.jpg" width="50%">
