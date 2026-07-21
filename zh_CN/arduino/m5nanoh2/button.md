# NanoH2 Button 按键

NanoH2 Button 按键案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5NanoH2

```cpp line-num
#define pin_BtnA 9
#define DEBOUNCE_MS 20    // Debounce time
#define HOLD_MS 500       // Holding threshold

bool last_state = HIGH;
unsigned long last_time = 0;
bool is_holding = false;

void setup() {
  pinMode(pin_BtnA, INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  bool current_state = digitalRead(pin_BtnA);
  unsigned long now = millis();

  // Debouncing
  if (current_state != last_state && now - last_time > DEBOUNCE_MS) {
    last_state = current_state;
    last_time = now;

    if (current_state == LOW) {  // Button pressed
      Serial.println("Button A pressed");
    } else {  // Button released
      Serial.println("Button A released");
      if (!is_holding) {
        Serial.println("Button A single clicked");
      }
      is_holding = false;
    }
  }

  // Long press detection
  if (current_state == LOW && now - last_time > HOLD_MS && !is_holding) {
    is_holding = true;
    Serial.println("Button A held");
  }

  delay(5);
}
```

该程序将检测 NanoH2 正面的输入按键的状态，并在串口监视器打印按键事件：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/arduino_nanoh2_button_example_serial_01.png" width="70%" >
