# Unit PoE-P4 Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE 安装：参考 [Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。

- 2\. 板管理安装：参考[板管理安装教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5UnitPoEP4`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1217/quickstart_arduino_unit_poe-p4_select_board.png" width="70%">

- 3\. 驱动库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成 `M5Unified`、`M5GFX` 驱动库安装，并根据提示安装全部依赖库。

## 2. 端口选择

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1217/U213-download-mode.gif" width="40%">

将设备通过 USB Type-C 数据线连接至电脑，长按侧面的复位按键直到绿灯亮起，此时设备进入下载模式，可在 Arduino IDE 中选择对应的主控和设备端口。

## 3. 程序编译 & 烧录

打开 Ethernet 库中的案例程序 “ETH_TLK110”, 点击上传按钮，将自动进行程序编译与烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1217/quickstart_arduino_unit_poe-p4_select_demo.png" width="70%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1217/quickstart_arduino_unit_poe-p4_select_demoupload.png" width="70%" />

烧录成功后，打开串口监视器，将波特率设置为 115200，即可看到网络连接成功的输出信息。

串口输出示例：

- 网络连接成功

```
ETH Started
ETH Connected
ETH Got IP
*eth0: <UP,100M,FULL_DUPLEX,AUTO,ADDR:0x1> (DHCPC,GARP,IP_MOD)
      ether 30:ED:A0:EA:92:D2
      inet 192.168.20.121 netmask 255.255.255.0 broadcast 192.168.20.255
      gateway 192.168.20.1 dns 223.5.5.5


connecting to baidu.com
HTTP/1.1 301 Moved Permanently
Location: https://www.baidu.com/
Date: Sat, 28 Feb 2026 04:29:55 GMT
Content-Length: 57
Content-Type: text/html; charset=utf-8

<a href="https://www.baidu.com/">Moved Permanently</a>.

closing connection
```

- 网络连接失败

```
ETH Disconnected
ETH Connected
ETH Got IP
*eth0: <UP,100M,FULL_DUPLEX,AUTO,ADDR:0x1> (DHCPC,GARP,IP_MOD)
      ether 30:ED:A0:EA:92:D2
      inet 192.168.20.121 netmask 255.255.255.0 broadcast 192.168.20.255
      gateway 192.168.20.1 dns 223.5.5.5


connecting to google.com
connection failed
```

## 4. 相关资源

- **Arduino Library**

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- **Arduino API & Examples**
  - [Button](/zh_CN/arduino/m5unit_poe-p4/button)
  - [Ethernet](/zh_CN/arduino/m5unit_poe-p4/ethernet)
  - [IR NEC](/zh_CN/arduino/m5unit_poe-p4/ir_nec)
  - [RGB LED](/zh_CN/arduino/m5unit_poe-p4/rgb_led)
