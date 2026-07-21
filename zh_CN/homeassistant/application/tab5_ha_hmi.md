# Tab5 Home Assistant HMI 案例

本章节介绍将 Tab5 变为 Home Assistant 人机交互设备的实现方法和配置细节。

在这个案例中我们会用到几个 Home Assistant 中的实体，主要是温湿度传感器 (Unit ENV-Pro)，一个 RGB 灯 (Unit NeoHEX) 和一个红外远程空调实体。本案例使用的是 Atom VoiceS3R 作为平台，来集成温湿度、灯光和红外组件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_Home_Assistant_tutorial_cover_ZH.png" width="60%"/>

## 准备工作

- 一台 Home Assistant 主机。
- 安装并且启用了 [ESPHome Builder](https://esphome.io/guides/getting_started_hassio/) 加载项。
- 确保温湿度传感器 (Unit ENV-Pro)、RGB 灯 (Unit NeoHEX)、红外远程空调实体已被集成至 Home Assistant 中。
- 参考文档：
- [Unit ENV-Pro](/zh_CN/homeassistant/sensor/unit_env_pro_sensor)
- [Unit NeoHEX](/zh_CN/homeassistant/light/unit_neo_hex)
- [IR Remote Climate](https://esphome.io/components/climate/climate_ir/)

## 注意事项

1. 案例在 ESPHome `2025.10.3` 下编译，如果遇见编译或上传问题，考虑将 ESPHome 切换至此版本。
2. 案例仅做为演示，配置文件的内容可能更改。对于在 2025 年 10 月 14 日之后生产的产品，LCD / 触摸屏的 IC 已被更换为 ST723，目前的配置暂不支持该 IC，我们会持续优化驱动支持。

## 创建设备

1. 在 Home Assistant 中打开 ESPHome Builder，创建一个空的配置文件。

- 点击右下角的 `NEW DEVICE` 按钮。

- 弹出框单击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_esp_builder_2.webp" width="40%" />

- 选择 `Empty Configuration`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_create_empty_config.webp" width="30%" />

- 为文件命名 （可选）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_fill_config_name.webp" width="30%" />

- 在新生成的配置文件处点击 `EDIT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_edit_config_1.webp" width="40%" />

2. 复制 [tab5-ha-hmi.yaml](https://github.com/m5stack/esphome-yaml/blob/main/common/tab5-ha-hmi.yaml) 的内容到配置文件中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_edit_config_2.webp" width="60%" />

3. 根据需要，更改网络配置或者是 API 信息，比如创建一个 API Encryption Key 用于认证：

```yaml line-num
api:
  encryption:
    key: "Your_Encryption_Key"
```

\#> 提示 | 如果需要一个 Key，可以访问 [native api](https://esphome.io/components/api/) 生成一个（在 encryption 下）。

4. 依次点击右上角 `SAVE` 和 `INSTALL`，选择 `Manual download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_esphome_manual_download.webp" width="40%" />

5. 此时会生成代码并且编译工程。

\#> 提示 | 如果是第一次编译，可能会需要较长时间；具体取决于 Home Assistant 主机性能和网络连接情况。

6. 当编译完成后，选择 `Factory format` 下载固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_esphome_compile_finish.webp" width="60%" />

## 下载和烧录固件

1. 下载固件：通过 ESPHome Builder 的`Manual download`方式下载 Factory Format 固件。
2. 使用 web 工具烧录固件：

- 打开浏览器，访问 [ESPHome Web](https://web.esphome.io/) 上传固件。

- 使用 USB-C 数据线将 Tab5 连接至主机，点击 `CONNECT`，选择设备连接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_web_esp_flash_2.webp" width="70%" />

- 点击 `INSTALL`，选择之前下载的固件上传，再次点击 `INSTALL`，将固件烧录至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_web_esp_install.webp" width="40%" />

- 当烧录完成后，设备会自动重置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/atom_echos3r_webesp_success.webp" width="30%" />

## 开始使用

### HMI 集成

1. 当设备重启后，会自动连接之前配置的网络，正常情况下可以在 `Settings` -> `Devices & services` 发现设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_add_ha_integration.webp" width="30%" />

2. 点击 `Add` 将 Tab5 集成进入 Home Assistant，如果此前设置了 API Encryption Key，此处可能需要填入 API Encryption Key 验证。

3. Tab5 的 Dashboard 示例：

<div
style="display: flex; gap: 16px"
>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_ha_dashboard_1.webp" width="30%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_ha_dashboard_2.webp" width="30%" />
</div>

### 允许 Tab5 执行 Home Assistant Action

?> 重要 | 如果不开启本功能，Tab5 将无法控制 Home Assistant 上的实体。

1. 当设备添加完成后，在 Home Assistant 中点击 `Settings` 会发现一个待修复的问题。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_permit_ha_action_1.webp" width="50%" />

2. 查看详情：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_permit_ha_action_2.webp" width="50%" />

该问题告诉我们，Tab5 尝试访问 Home Assistant 上集成的实体并且修改某些属性，但是默认情况下 Home Assistant 不允许设备执行操作。

3. **解决方案**：

- 打开 `Settings` -> `Device & services` -> `ESPHome`，找到 Tab5 设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_permit_ha_action_3.webp" width="50%" />

- 点击右上的设置图标，勾选 `Allow the device to perform Home Assistant actions`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_permit_ha_action_4.webp" width="50%" />

- 点击 `Submit`。自此 Tab5 就能控制已经配置的 Home Assistant 实体。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_permit_ha_action_5.webp" width="30%"/>

### HMI 使用方法

- UI 主要是按照 Pages 分页展示，目前有三个页面，可以通过左侧 Sidebar 导航。Dashboard 页面主要展示一些简单信息，灯光页面可以操作某个具体的灯光实体，Climate 页面可以操控某个具体的空调。
- UI 设计和交互参考自 [Home Assistant dashboard](https://demo.home-assistant.io/#/lovelace/home)，在嵌入式设备上使用 LVGL 实现可能需要更多时间。

1. 灯光控制：

- 点击侧边栏的 `Light` 按钮，可以看见一个示例灯光。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_ha_hmi_light_card.jpg" width="50%" />

- 单击里面的 Icon Button，可以打开 / 关闭灯光。

<video
width="320"
autoplay
loop
muted
playsinline
preload="auto"> <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_ha_hmi_toggle_light.webm" type="video/webm"> </video>

- 如果点击卡片的空白区域，可以打开灯光控制的模态框用于控制灯光亮度和 RGB 色彩。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_ha_hmi_light_brightness.jpg" width="50%" />

<video
autoplay
loop
muted
playsinline
preload="auto"> <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_ha_hmi_change_light_brightness.webm" type="video/webm"> </video>

\#> 提示 | 设置 RGB 灯光色彩的配置需要依赖 Home Assistant 的 Script 实现，具体参考下文 "调整配置" 这一部分。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_ha_hmi_light_color.jpg" width="50%" />

<video
autoplay
loop
muted
playsinline
preload="auto"> <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_ha_hmi_change_light_color.webm" type="video/webm"> </video>

2. 空调控制：

- 点击左侧的 `Climate` 按钮，会出现一个示例的空调。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_ha_hmi_climate_card.jpg" width="50%" />

- 点击 Spinbox 两边的 `+` 和 `-`，会调整空调的目标温度（但无法设置空调状态，比如自动 / 制冷 / 制热等）。

- 点击卡片的空白区域会打开模态框，用于调整模式，风速和温度等。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_ha_hmi_climate_control.jpg" width="50%" />

### 调整配置

这一部分将介绍如何修改配置，您可以尝试将自己的灯光、空调等组件配置到 Tab5 中，此部分仅针对有 ESPHome 使用经验的用户，在此之前，可以参考 ESPHome 提供的集成方式：

- [Remote light button](https://esphome.io/cookbook/lvgl/#remote-light-button) 介绍了如何添加一个 LVGL 的灯光按钮，使其可以远程控制一个灯光实体。
- [Toggle state icon button](https://esphome.io/cookbook/lvgl/#toggle-state-icon-button) Remote light 的进阶版本，可以根据灯光开关情况修改 LVGL UI。
- [Light brightness slider](https://esphome.io/cookbook/lvgl/#light-brightness-slider) 介绍了如何绘制一个 LVGL Slider 并且绑定灯光亮度。
- [Native API Component](https://esphome.io/components/api/#homeassistantaction-action) 介绍了如何通过 `homeassistant.action` 来调用 Home Assistant，其中包含了一个设置 RGB 灯光颜色的案例。
- [Climate control](https://esphome.io/cookbook/lvgl/#climate-control) 介绍了如何创建一个 LVGL Spinbox 并且控制如空调 / 加热器等实体。
- [Home Assistant Text Sensor](https://esphome.io/components/text_sensor/homeassistant/) 特殊的 Text Sensor 类型，用于获取 Home Assistant 上实体的**状态值**和**属性值**。
- [Home Assistant Binary Sensor](https://esphome.io/components/binary_sensor/homeassistant/) 特殊的 Binary Sensor 类型，用于获取 Home Assistant 上的 Binary Sensor 的**读数**。
- [Home Assistant Sensor](https://esphome.io/components/sensor/) 特殊的 Sensor 类型，用于获取 Home Assistant 上的 Sensor 实体的**读数**。

了解了上面这些案例后，我们就可以大概绘制出目前的一个架构。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_block_diagram.webp" width="80%" />

#### 灯光

下面就以灯光组件作为一个范例。
在 LVGL（主要定义在 [tab5-lvgl.yaml](https://github.com/m5stack/esphome-yaml/blob/main/common/tab5-lvgl.yaml) 文件）中，我们绘制了一些组件，譬如 Icon Button，Slider 还有一个自定义的 Color Palette（调色盘）。当然在此之前，确保已经将灯光组件集成到了 Home Assistant 中（确保在 Home Assistant 中可以操作灯光）。由于在配置文件中定义的有 `text_sensor`:

```YAML line-num
text_sensor:
  - platform: homeassistant
    id: demo_light
    entity_id: light.unit_neo_hex_unit_neohex
    on_value:
      then:
        - lvgl.widget.update:
            id: xxx
            ...

        - lvgl.label.update:
            id: xxx
            ...

  - platform: homeassistant
    id: demo_light_brightness
    entity_id: light.unit_neo_hex_unit_neohex
    attribute: brightness
    on_value:
      - lvgl.slider.update:
          id: xxx
          ...

      - lvgl.label.update:
          id: xxx
          ...

  - platform: homeassistant
    id: demo_light_color
    entity_id: light.unit_neo_hex_unit_neohex
    attribute: rgb_color
    on_value:
      ...
  ...
```

1. 它有一个 `on_value` 属性用于自动化 (Automation) 的回调，当接收到 Home Assistant 更新的数据后，便可在其中调用 lvgl 相关动作 (actions) 用于更新 UI 内容。
   \#> 提示 | 灯光实体的各种属性，会由于灯的种类和配置不同而不同，可以在 Home Assistant 中找到 `Developer tools` -> `States` 搜索相关属性（比如输入 `light` 查找）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_ha_dev_tool_states.webp" width="60%" />

2. 而 LVGL 的组件事件触发（trigger）可以通过 `homeassistant.action` API 控制灯光：

```yaml line-num
   # Use a icon button to toggle the light
     ...
   - button:
       styles: card_sm_icon_btn
       id: demo_light_btn
       ...
       widgets:
         - label:
             id: demo_light_label
             ...
             text: "\U000F18DE"
             align: CENTER
       on_short_click:
         - homeassistant.action:
             action: light.toggle
             data:
               entity_id: light.unit_neo_hex_unit_neohex
     ...
   # Use a slider to control light brightness
   - slider:
       min_value: 0
       max_value: 255
       id: light_slider
       ...
       on_release:
         - homeassistant.action:
             action: light.turn_on
             data:
               entity_id: light.unit_neo_hex_unit_neohex
               brightness: !lambda return int(x);
       ...
```

3. 不同 LVGL 组件有不同的触发方式（Triggers），具体可以参考 [ESPHome - LVGL Widgets](https://esphome.io/components/lvgl/widgets/#dropdown)。

\#> 提示 | 并不是所有的实体属性可以在 `data` 中直接指定 `entity_id` 和属性名称进行更改，Home Assistant 会拒绝无效的属性更改，若要知道那些 action 可以被触发，可以打开 Home Assistant 的 `Developer tools` -> `Actions` 查看。比如搜索灯光有哪些 action 可以触发，此处 RGB 变色就是由 Home Assistant 脚本触发的，如需了解更多脚本和自动化内容，参考：

- [Automating Home Assistant](https://www.home-assistant.io/docs/automation/)。
- [Home Assistant Scripts](https://www.home-assistant.io/integrations/script/)。
- [Home Assistant Templating](https://www.home-assistant.io/docs/configuration/templating/)。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_ha_dev_tool_actions.webp" width="60%" />

4. 了解了上面这些内容后，如果想使用自己的 Light 实体：

- 在 `text_sensor` 中添加或修改你想更新的 `entity_id` 和 `attribute`，如果需要更新 LVGL UI，则需要编写更新的动作。
- 在自己希望触发灯光动作的 LVGL 组件回调中，将 `homeassistant.action` 中 `data` 下的 `entity_id` 修改为合适的 id，并确保 action 已经存在。

#### 传感器

1. 同样，对于传感器 `Sensor` 实体，其主要是发布数值（当然也有`文字`，ON/OFF 状态等），所以在配置文件中，如果需要知道 Home Assistant 上某个传感器的数值，也是指定 `entity_id` 即可。

```yaml line-num
   sensor:
     ...
   - platform: homeassistant
       id: cur_temp
       entity_id: sensor.temperature
       on_value:
         - lvgl.label.update:
             id: xxx

     - platform: homeassistant
       id: cur_humi
       entity_id: sensor.env_iv_kit_humidity
       on_value:
         - lvgl.label.update:
             id: xxx

     - platform: homeassistant
       id: cur_co2
       entity_id: sensor.env_iv_kit_co2_equivalent
       on_value:
         - lvgl.label.update:
             id: xxx
     ...
```

2. 这样 Tab5 便能读取到 Home Assistant 的传感器数据值，并且通过 `on_value` 将值更新至 LVGL UI 界面。

3. 如需使用自己的传感器，只需修改 `entity_id` 即可，如需更新 LVGL UI 则还需要编写相应的脚本。

\#> 提示 | 可以在 Home Assistant 的 `Settings` -> `Devices & services` 下的 `Entities` 找到各种实体。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_hmi_ha_show_entities.webp" width="60%" />

#### Climate

1. 同样在配置中定义的有一些关于 `Climate` 实体的属性:

```yaml line-num
   # AC Information
     - platform: homeassistant
       id: ac_state
       entity_id: climate.unit_neo_hex_central_ac
       on_value:
         - lvgl.label.update:
             id: xxx

         - lvgl.dropdown.update:
             id: xxx
       ...
     - platform: homeassistant
       id: ac_fan_mode
       entity_id: climate.unit_neo_hex_central_ac
       attribute: fan_mode
       on_value:
         - lvgl.label.update:
             id: xxx
         - lvgl.dropdown.update:
             id: xxx
       ...

     - platform: homeassistant
       id: ac_temp
       entity_id: climate.unit_neo_hex_central_ac
       attribute: temperature
       on_value:
         - lvgl.spinbox.update:
             id: xxx
       ...
```

2. 一样可以获取到这些属性，然后更新到 UI 上。

3. LVGL UI 控制 Climate 组件：

```yaml line-num
     ...
   - arc:
     id: ac_arc
     adjustable: true
     ...
     # Prevent frequent use of 'on_value'
     # In case of performance issue
     on_release:
       - lambda: id(set_ac_temp)->execute(float(x) / 10.0f);
     ...

   - dropdown:
   id: ac_mode_dd
   ...
   dir: TOP
   selected_text: "Off"
   options:
     - Heat_Cool
     - Heat
     - Cool
     - Dry
     - Only Fan
     - "Off" # In case conversions
   on_change:
     ...
     - lambda: id(set_ac_state)->execute(x);

   - dropdown:
     id: fan_mode_dd
     dir: TOP
     ...
     selected_text: "Auto"
     options:
       - High
       - Medium
       - Low
       - Auto
     on_change:
       ...
       - lambda: id(set_ac_fan_mode)->execute(x);
```

4. 这里将控制封装成了脚本，可以在 [tab5-scripts.yaml](https://github.com/m5stack/esphome-yaml/blob/main/common/tab5-scripts.yaml) 中找到。

```yaml line-num
# This script was used on dropdown widget
# to set ac state (ON/OFF/COOL/HEAT, etc)
- id: set_ac_state
  parameters:
    ac_mode_idx: int
  then:
    - homeassistant.action:
        action: climate.set_hvac_mode
        data:
          entity_id: climate.unit_neo_hex_central_ac
          hvac_mode: !lambda return id(hvac_state_table)[ac_mode_idx];
- id: set_ac_fan_mode
  parameters:
    ac_fan_mode_idx: int
  then:
    - homeassistant.action:
        action: climate.set_fan_mode
        data:
          entity_id: climate.unit_neo_hex_central_ac
          fan_mode: !lambda return id(fan_modes_table)[ac_fan_mode_idx];
# This script was used on spinbox/arc widget
# to set the temperature to climate entity
# it doesn't turn on/off, use the dropdown instead
- id: set_ac_temp
  parameters:
    temp_value: float
  then:
    - homeassistant.action:
        action: climate.set_temperature
        data:
          entity_id: climate.unit_neo_hex_central_ac
          temperature: !lambda return temp_value;
```

5. 同样，如果想要适配自己的 Climate 组件，可以修改 `entity_id` 和相关属性。

## 相关视频

<TabPanel>
<template #tab-Bilibili>
<div class="video-iframe">
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115660784929650&bvid=BV1Up2eBtEVi&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
</template>
<template #tab-Youtube>
<div class="video-iframe">
<iframe width="560" height="315" src="https://www.youtube.com/embed/2vDlxVUIwtA?si=TzCMtKkusH0VDNV9" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</template>
</TabPanel>
