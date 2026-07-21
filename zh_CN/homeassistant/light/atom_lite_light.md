# Atom-Lite HA Light Home Assistant 集成

本教程将指导你完成 Atom-Lite 与 Home Assistant 的灯光控制集成。

## 准备工作

- 参考 [Home Assistant 官网文档](https://www.home-assistant.io/getting-started/) 安装 Home Assistant。
- 在 `Setting` -> `Add-ons` -> `Add-ons STORE` 中安装 ESPHome Builder 插件。
- ESPHome Builder 插件安装成功后，在其管理页面选中 `Show in sidebar` 将其添加至左侧导航栏。
- 本教程参考自 [HA 官方使用文档](https://esphome.io/guides/getting_started_hassio)，如有需要可自行访问。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-1.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-2.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-3.png" width="70%"/>

## 快速体验

可点击下方按钮，一键完成固件烧录，按提示完成配置， 即可快速体验 Atom-Lite 接入 Home Assistant。一键烧录及后续配置的方法可参考[教程](/zh_CN/homeassistant/web_flash)。

<EspWebTool manifest="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/atom_lite_rgb_manifest_2026.3.0.json">一键烧录固件</EspWebTool>

## 注意事项

\#> 固件编译提示：| 通过 HA 进行固件编译较为耗费资源，首次编译可能会需要较长时间进行资源下载，跟实际部署 HA 服务的设备以及网络质量相关。尝试编译失败的情况，也可以点击下方的 web tools 烧录按钮，烧录我们已经打包完成的固件。并在烧录完成后按照提示配置 Wi-Fi 连接信息。(配置失败情况下可断开连接，刷新页面重试)

## 创建设备

1. 打开 ESPHome 插件页面，右下角点击 `NEW DEVICE`，创建一个新设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-4.png" width="70%"/>

2. 出现 New device 提示界面，点击 `CONTINUE` 按钮。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-5.png" width="30%"/>

3. 为设备填写名称，该名称可自定义，这里填写为 `Atom-Lite`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-6.png" width="30%"/>

4. 随后出现选择设备类型界面，需要先将 `Use recommended settings` 取消勾选，然后选择 `ESP32` 进入详情页。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-7.png" width="30%"/>

5. 在详情页中寻找到 `M5Stack-ATOM`，选中后点击 `NEXT` 按钮。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-8.png" width="30%"/>

6. 出现设备配置成功界面，把 `key` 复制后点击 `INSTALL` 进入安装步骤。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-9.png" width="30%"/>

7. 选择 `Manual download` 开始进行程序编译并等待编译安装完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-10.png" width="30%"/>

## 修改配置

1. 当上述步骤完成后，回到 ESPHome Builder 主界面会发现多了一个 `Atom-Lite` 的设备，点击 `EDIT` 按钮进入 yaml 文件编辑页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-11.png" width="70%"/>

2. 把以下代码复制到 `yaml` 文件中，并将图示位置的 `ssid` 和 `password` 修改为你的 Wi-Fi 账号和密码。

```yaml line-num
esphome:
  name: atom-lite
  friendly_name: Atom-Lite

esp32:
  board: m5stack-atom
  flash_size: 4MB
  framework:
    type: esp-idf

logger:
api:
  encryption:
    key: "*********"

ota:
  - platform: esphome
    password: "*****************"

wifi:
  ssid: "*********"
  password: "***********"
  ap:
    ssid: "Atom-Lite Fallback Hotspot"
    password: "jFsIc2XGuKRe"

captive_portal:

binary_sensor:
  - platform: gpio
    pin:
      number: GPIO39
      mode: INPUT
      inverted: true
    name: "Atom Button"
    id: atom_button
    filters:
      - delayed_on: 50ms
      - delayed_off: 50ms
    on_multi_click:
      - timing:
          - ON for at most 0.8s
          - OFF for at most 0.5s
          - ON for at most 0.8s
          - OFF for at least 0.2s
        then:
          - logger.log: "Double Clicked"
          - light.turn_on:
              id: atom_light
              red: 100%
              blue: 50%
              green: 20%
              brightness: 50%
      - timing:
          - ON for at least 0.8s
        then:
          - logger.log: "Single Long Clicked"
          - light.turn_on:
              id: atom_light
              green: 100%
              blue: 50%
              red: 30%
              brightness: 100%

light:
  - platform: esp32_rmt_led_strip
    rgb_order: GRB
    pin: GPIO27
    num_leds: 1
    chipset: SK6812
    name: "Atom RGB Light"
    id: atom_light
    restore_mode: RESTORE_DEFAULT_OFF
    effects:
      - random:
          name: "Random"
          transition_length: 1s
          update_interval: 1s
```

\#> 更新说明 | 自 [ESPHome 2025.10](https://esphome.io/changelog/2025.10.0/#release-overview) 起，Arduino 不再作为单独的 Framework ，而是`ESP-IDF` 的组件使用，原来 Arduino 下的 [`NeoPixelBus Light`](https://esphome.io/components/light/neopixelbus/) 不支持 `ESP-IDF` 框架，新版 ESPHome 请使用 [`ESP32 RMT LED Strip`](https://esphome.io/components/light/neopixelbus/) 组件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-12.png" width="70%"/>

3. 先点击 `SAVE` 按钮保存 yaml 文件，再点击 `INSTALL` 按钮开始编译固件并烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-13.png" width="70%"/>

4. 再次点击 `Manual download` 开始编译固件并等待完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-14.png" width="70%"/>

## 下载和烧录固件

1. 等待编译完成后，点击 `DOWNLOAD` 按钮会出现烧录方式选择的界面，这里我们选择 `Factory format` 以保存到本地。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-15.png" width="70%"/>

2. 等待程序本地下载完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-16.png" width="70%"/>

3. 回到主界面选择 `INSTALL` 进入烧录选择界面，这次选择 `Plug into this computer`，并将设备与电脑用 USB 连接以烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-17.png" width="70%"/>

4. 选择 `Open ESPHome Web` 进入烧录界面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-18.png" width="70%"/>

5. 先点击 `CONNECT` 按键，然后选择接入电脑的串口设备并连接（若此处没有出现串口请自行检查是否硬件连接有误）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-19.png" width="70%"/>

6. 点击 `INSTALL` 进入本地固件文件选择界面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-20.png" width="70%"/>

7. 选择刚刚保存到本地的固件文件，点击 `INSTALL` 并等待烧录完毕。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-21.png" width="70%"/>

烧录完成：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-22.png" width="70%"/>

## 开始使用

1. 完成固件烧录后，设备开机将自动进行 Wi-Fi 连接。点击 `Setting` 进入设置界面查看 `Discovered` 处的设备，点击 `ADD` 添加设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-23.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-24.png" width="50%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-26.png" width="50%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-27.png" width="50%"/>

2. 点击 `Settings` 进入设置界面并选择 `Devices & services`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-25.png" width="70%"/>

3. 在搜索栏中搜索 `ESP` 即可找到 `ESPHome`，进入并选择 `Atom-Lite`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-28.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-29.png" width="70%"/>

4. 在 `Atom-Lite` 配置页面中，可以看到 `Atom RGB Light` 和 `Atom Button` 两个 `Entity`，自动化就是通过配置各种 `Entity` 来实现逻辑的，我们点击 `+` 号添加 `Automations`，随后跟着指引操作即可。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-30.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-31.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-32.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-33.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-34.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-35.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-36.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-37.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-38.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-39.png" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-40.png" width="70%"/>

就这样我们用 `Atom Button` 和 `Atom RGB Light` 两个实体来组成了一个 `Automation`，这个自动化的效果是当单击按钮时会切换灯光状态。

5. 点击 `Overview` 菜单，进入组件控制界面，点击右上角的 `edit` 按钮，进入编辑界面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-41.png" width="70%"/>

6. 在 `By card` 界面搜索 `Light` 并选择 `Atom RGB Light` 实体组件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-42.png" width="70%"/>

组件配置如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-43.png" width="70%"/>

7. 双击按钮 RGB 灯切换为粉色。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-45.jpg" width="50%"/>

8. 按钮长按 2s 以上，RGB 灯切换为绿色。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-44.jpg" width="50%"/>

RGB 灯的状态不仅会体现在组件上，还可以直接通过组件来控制实体。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/Atom-Lite-HA-46.jpg" width="50%"/>
