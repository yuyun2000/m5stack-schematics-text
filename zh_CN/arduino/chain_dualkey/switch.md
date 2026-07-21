# Chain DualKey Switch 开关

Chain DualKey Switch 开关相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.4
- 开发板选项 = M5ChainDualKey

```cpp line-num
#define SWITCH_BLE  8
#define SWITCH_WIFI 7

void setup() {
  pinMode(SWITCH_BLE,  INPUT);
  pinMode(SWITCH_WIFI, INPUT);

  Serial.begin(115200);
}

void loop() {
  if (digitalRead(SWITCH_BLE) == HIGH) {
    Serial.println("Switch in BLE position");
  } else if (digitalRead(SWITCH_WIFI) == HIGH) {
    Serial.println("Switch in WIFI position");
  } else {
    Serial.println("Switch in middle position");
  }

  delay(500);
}
```

该程序每 500 毫秒检测一次开关位置，并在串口监视器打印消息：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_07.webp" width="30%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Arduino_switch.png" width="90%">