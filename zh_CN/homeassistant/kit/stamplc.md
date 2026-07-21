# StamPLC 控制器 Home Assistant 集成

本章节介绍将物联网可编程逻辑控制器 StamPLC 集成至 Home Assistant 的方法。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/STAMPLC-Home_Assistant_tutorial_cover_ZH.png" width="60%"/>

\#> Note | 非常感谢来自 ESPHome 社区贡献者 [@Beormund](https://github.com/Beormund) 提供的配置文件，如需参考更多，可以访问 https://github.com/Beormund/esphome-m5stamplc。

## 准备工作

- Home Assistant 主机。
- 在 Home Assistant 中安装并启用[ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 StamPLC 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/stamplc_manifest_2026.3.0.json">一键烧录固件</EspWebTool>

## 注意事项

- 本教程中，套件在 ESPHome 2025.10.3 下编译和上传，如果遇见编译 / 上传问题，考虑将 ESPHome 切换至此版本。

## 创建设备

1. 在 Home Assistant 中打开 ESPHome Builder，创建一个空的配置文件。

- 点击右下角的 `NEW DEVICE` 按钮。

- 弹出框单击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_2.webp" width="40%" />

- 选择 `Empty Configuration`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_create_empty_config.webp" width="30%" />

- 为文件命名（可选）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_esphome_builder_naming.webp" width="30%" />

- 在新生成的配置文件处点击 `EDIT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_esphome_builder_new_file.webp" width="40%" />

2. 复制 [configurations.yaml](https://github.com/Beormund/esphome-m5stamplc/blob/main/configuration.yaml) 的内容到配置文件中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_esphome_builder_configurations.webp" width="60%" />

3. 根据需要，更改网络配置或者是 API 信息等，比如创建一个 API Encryption Key 用于认证：

```yaml line-num
api:
  encryption:
    key: "Your_Encryption_Key"
```

\#> 提示 | 如果需要一个 Key，可以访问 [native api](https://esphome.io/components/api/) 生成一个（在 encryption 下）。

或者是更改时区设置：

```yaml line-num
timezone: Europe/London
```

改为合适的时区：

```yaml line-num
timezone: Asia/Shanghai
```

4. 依次点击右上角 `SAVE` 和 `INSTALL`，选择 `Manual download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_install_method.webp" width="40%" />

此时会生成代码并且编译工程。

\#> 提示 | 如果是第一次编译，可能会需要较长时间；具体取决于 Home Assistant 主机性能和网络连接情况。

5. 当编译完成后，选择 `Factory format` 下载固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_download_method.webp" width="60%" />

## 下载和烧录固件

1. 下载固件：通过 ESPHome Builder 的`Manual download`方式下载 Factory Format 固件。
2. 使用 web 工具烧录固件：

- 打开浏览器，访问 [ESPHome Web](https://web.esphome.io/) 上传固件。

- 使用 USB-C 数据线将 StamPLC 连接至主机，点击 `CONNECT`，选择设备连接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_2.webp" width="70%" />

- 点击 `INSTALL`，选择之前下载的固件上传，再次点击 `INSTALL`，将固件烧录至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_web_esp_install.webp" width="40%" />

- 当烧录完成后，设备会自动重置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_success.webp" width="30%" />

## 开始使用

### 添加设备至 Home Assistant 集成

1. 当设备重启后，会自动连接之前配置的网络，正常情况下可以在 `Settings` -> `Devices & services` 发现设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_ha_device_discover.webp" width="30%" />

2. 点击 `Add` 将 StamPLC 集成进入 Home Assistant，如果此前设置了 API Encryption Key，此处可能需要填入 API Encryption Key 验证。
   StamPLC 的 Dashboard 示例：

<div
style="display: flex; gap: 16px"
>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_ha_dash_1.webp" style="object-fit: contain;" width="30%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_ha_dash_2.webp" width="30%" />
</div>

<div style="display: flex; gap: 16px">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_ha_dash_3.webp" style="object-fit: contain;" width="30%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_ha_dash_4.webp" width="30%" />
</div>

3. 实机运行：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_ha_demo_pic.jpg" width="40%" />

### 拓展

StamPLC 支持拓展，可以通过右侧的 16 Pin 引脚接入其它拓展。

#### StamPLC AC

1. 产品介绍： <img
   src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_01.webp"
   width="30%"
   />

StamPLC AC 是一款适配 StamPLC 主机的交流继电器拓展模块。模块集成交流负载控制与整机供电功能，有效简化应用供电布线。采用触点式继电器（单刀单掷 - 常开型）, 最大支持 AC 240V@10A 线路通断。内置 AC-DC 隔离转换电路，支持 AC 100~240V 输入，可在为继电器负载供电的同时，降压输出 DC 12V 为整机供电。板载可编程三色 LED 灯，用于工作状态指示。StamPLC 主控通过 I2C 协议的 IO 拓展芯片对继电器、RGB LED 进行编程控制，有效节省 IO 资源。适用于交流负载设备开关、电磁阀控制等工业级应用场景。

2. 配置 StamPLC AC：
   在此前 StamPLC 的配置之上，YAML 配置中需要添加一些组件：

- 新增 IO Expander：

```yaml
pi4ioe5v6408:
  - id: pi4ioe5v6408_1
    address: 0x43
  # Configuration of i2c GPIO Expander 2
  # on the StamPLC AC expansion
  - id: pi4ioe5v6408_2
    address: 0x44
```

- 新增 AC Relay 的开关：

```yaml
     switch:
       ...
       - platform: gpio
         restore_mode: RESTORE_DEFAULT_OFF
         name: "StamPLC AC Relay"
         id: ac_r1
         pin:
           pi4ioe5v6408: pi4ioe5v6408_2
           number: 2
           mode:
             output: true
         on_state:
           - component.update: vdu
```

- 新增 AC Relay 顶部的 LED 颜色控制：

```yaml
     switch:
       ...
       # led indicator on StamPLC AC expansion
       - platform: gpio
         restore_mode: ALWAYS_OFF
         id: "ac_relay_led_red"
         pin:
           pi4ioe5v6408: pi4ioe5v6408_2
           number: 5
           inverted: true
           mode:
             output: true

       - platform: gpio
         restore_mode: ALWAYS_OFF
         id: "ac_relay_led_green"
         pin:
           pi4ioe5v6408: pi4ioe5v6408_2
           number: 6
           inverted: true
           mode:
             output: true

       - platform: gpio
         restore_mode: ALWAYS_OFF
         id: "ac_relay_led_blue"
         pin:
           pi4ioe5v6408: pi4ioe5v6408_2
           number: 7
           inverted: true
           mode:
             output: true
```

- 为 Display 组件新增 AC Relay UI：

```yaml
     display:
       ...
       lambda: |-
         ...
         it.print(5, 80, id(font1), Color(orange), "Relays 1-4");
         it.filled_rectangle(5, 99, 25, 25, id(r1).state ? id(red) : id(grey));
         it.filled_rectangle(34, 99, 25, 25, id(r2).state ? id(red) : id(grey));
         it.filled_rectangle(63, 99, 25, 25, id(r3).state ? id(red) : id(grey));
         it.filled_rectangle(92, 99, 25, 25, id(r4).state ? id(red) : id(grey));
         it.print(141, 80, id(font1), Color(orange), "AC Expansion");    // The AC Relay Expansion
         it.filled_rectangle(141, 99, 25, 25, id(ac_r1).state ? id(red) : id(grey));
       ...
```

3. 完成配置后，重新编译和上传固件，将设备添加至 Home Assistant 即可通过额外的开关控制 AC Relay。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/stamplc_ac_ha_relay.webp" width="30%" />

4. 开启和关闭开关，LCD 的状态会同步改变。

<video
width="320"
autoplay
loop
muted
playsinline
preload="auto"> <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/stamplc_ac_demo.webm" type="video/webm"> </video>

#### StamPLC PoE

1. 产品介绍： <img
   src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_01.webp"
   width="30%"
   />

StamPLC PoE 是一款适配 StamPLC 主机的以太网控制模块，支持 PoE（有源以太网）技术，可通过网线同时实现数据传输与供电。该模块内置 W5500 嵌入式以太网控制器，集成 TCP/IP 协议栈，具备 8 路独立硬件 Socket、10/100M 以太网数据链路层（MAC）及物理层（PHY），支持 UDP、TCP 等主流网络通信方式。

2. 配置 StamPLC PoE：

?> 兼容性警告 | 由于 PoE（W5500 Ethernet) 组件会单独占用 SPI 硬件资源，此处 LCD Display 和 PoE 会使用同一组 SPI 引脚，同时定义会引发冲突；因此硬件上，PoE 和 Display 功能只能二选一。<br>
网络组件中，`wifi` 组件和 `ethernet` 组件是互斥选项，只能二选一。

如需使用 PoE 功能，需要禁用 `wifi`、`display`、`spi` 组件（在配置文件中删除相关声明 / 定义），之后在原始配置文件中添加：

```yaml
ethernet:
  id: ethernet_1
  type: W5500
  clk_pin: GPIO7
  mosi_pin: GPIO8
  miso_pin: GPIO9
  cs_pin: GPIO11
  clock_speed: 20MHz
```

3. 保存并重新编译，上传工程。使用 PoE 交换机或者路由器为设备供电同时供网。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/stamplc_poe_esphome_demo.jpg" width="30%" />

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115681940996354&bvid=BV1GU2rB9EkL&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/DztoQoaNR7M?si=ErzQG6NMfCHV3tx9" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
