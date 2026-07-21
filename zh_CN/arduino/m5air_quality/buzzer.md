# Air Quality 蜂鸣器

Air Quality 蜂鸣器相关API与案例程序。

## 案例程序

```cpp line-num
#include <M5Unified.h>

#define BUZZER_PIN  G9

// 音符频率
#define NOTE_C4  262
#define NOTE_D4  294
#define NOTE_E4  330
#define NOTE_F4  349
#define NOTE_G4  392
#define NOTE_A4  440

// 曲调和节拍（Twinkle Twinkle Little Star 前 14 个音符）
int melody[] = {
  NOTE_C4, NOTE_C4, NOTE_G4, NOTE_G4,
  NOTE_A4, NOTE_A4, NOTE_G4,
  NOTE_F4, NOTE_F4, NOTE_E4, NOTE_E4,
  NOTE_D4, NOTE_D4, NOTE_C4
};
int noteDurations[] = {
  4,4,4,4,4,4,2,
  4,4,4,4,4,4,2
};

void setup() {
  // 初始化 M5Unified
  M5.begin();
  // 清屏并设置文本属性
  M5.Display.clear(TFT_BLACK);
  M5.Display.setTextSize(2);
  M5.Display.setTextColor(TFT_WHITE, TFT_BLACK);

  // 在屏幕上显示英文标题
  M5.Display.setCursor( 20,  20);
  M5.Display.print("Playing:");
  M5.Display.setCursor( 20,  60);
  M5.Display.print("Twinkle Twinkle");
  M5.Display.setCursor( 20, 100);
  M5.Display.print("Little Star");

  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  int notes = sizeof(melody) / sizeof(melody[0]);

  for (int i = 0; i < notes; i++) {
    // 播放当前音符
    int duration = 1000 / noteDurations[i];
    tone(BUZZER_PIN, melody[i], duration);
    delay(duration * 1.2);
    noTone(BUZZER_PIN);

    M5.update();
  }

  // 播放完毕后停在最后,循环播放开关
//   while (true) {
//     delay(1000);
//   }
}
```

上传完成就可以看到下面的效果了，循环播放《小星星》

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/m5air_quality_arduino_quickstart_buzzer.jpg" width="30%">
