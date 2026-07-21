# SwitchC6 Home Assistant 集成

本章节介绍将 SwitchC6 单火线开关控制器集成至 Home Assistant 的配置方法与实操步骤。

<div style="display: flex; gap: 15px; flex-wrap: wrap;">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_01.webp" width="30%"/>
</div>

## 准备工作

- Home Assistant 主机。
- 在 Home Assistant 中安装并启用 [ESPHome Builder](https://esphome.io/guides/getting_started_hassio/)。

## 注意事项

在本教程中，固件使用 ESPHome 2025.12.5 进行编译和上传。如果遇到编译 / 上传问题，请考虑将 ESPHome 切换到此版本。

## 创建设备

1. 创建新设备。

1.1 点击右下角的绿色按钮创建设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA28.webp" width="70%"/>

2. 创建设备名称。

2.1 点击 `CONTINUE`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA1.webp" width="30%"/>

2.2 点击 `New Device Setup`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA3.webp" width="30%"/>

2.3 输入设备名称并点击 `NEXT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6HA3.webp" width="40%"/>

3. 选择设备类型。

\#> 提示 | 这里我们使用 [Atom-Lite](/zh_CN/core/ATOM%20Lite) 作为主控制器来操作 SwitchC6 继电器开关。

3.1 点击 `ESP32`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA9.webp" width="30%"/>

3.2 点击 `SKIP`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA27.webp" width="30%"/>

4. 开始编辑 YAML 文件。点击 `EDIT`。我们可以通过 YAML 文件自定义设备功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6HA4.webp" width="70%"/>

## 设备配置

以下是代码的核心部分，同时提供了相关参考和说明。

### 外部组件配置

**添加 [External](https://esphome.io/components/external_components/) 组件：**

```yaml
external_components:
  - source: github://m5stack/esphome-yaml/components
    components: m5stack_switchc6
    refresh: 0s
```

### ESPNOW 配置

**添加 [ESPNOW](https://esphome.io/components/espnow/) 组件：**

```yaml
espnow:
  id: espnow1
  auto_add_peer: true
  peers:
    - XX:XX:XX:XX:XX:XX
  on_broadcast:
    - lambda: |-
        id(sw1).handle_broadcast(data, size);
```

\#> 提示 | 您需要在此处输入设备的 espnow 地址 `- XX:XX:XX:XX:XX:XX`。

### 开关配置

**添加 [Switch](https://esphome.io/components/switch/) 组件：**

```yaml
switch:
  - platform: m5stack_switchc6
    id: sw1
    name: "SwitchC6 Device 1"
    espnow_id: espnow1
    mac_address: "XX:XX:XX:XX:XX:XX"
    retry_count: 40
    retry_interval: 300
```

\#> 提示 | 要添加多个设备，需要同时更新 ESPNOW 配置和开关条目。例如：

```yaml
espnow:
  id: espnow1
  auto_add_peer: true
  peers:
    - AA:BB:CC:DD:EE:01
    - AA:BB:CC:DD:EE:02
  on_broadcast:
    - lambda: |-
        id(sw1).handle_broadcast(data, size);
        id(sw2).handle_broadcast(data, size);

switch:
  - platform: espnow_switch
    id: sw1
    name: "SwitchC6 Device 1"
    espnow_id: espnow1
    mac_address: "AA:BB:CC:DD:EE:01"
    retry_count: 40
    retry_interval: 300
  - platform: espnow_switch
    id: sw2
    name: "SwitchC6 Device 2"
    espnow_id: espnow1
    mac_address: "AA:BB:CC:DD:EE:02"
    retry_count: 40
    retry_interval: 300
```

## 下载和烧录固件

1. 完成修改后，点击右上角的 `SAVE` 和 `INSTALL`，然后在弹出窗口中选择 `Manual Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/timercamera_ha_esp_builder_install_method.webp" width="40%"/>

2. 固件编译完成后，点击 Download 并选择 `Factory format(Previously Modern)`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA8.webp" width="70%"/>

\#> 提示 | 点击 [SwitchC6](https://github.com/m5stack/esphome-yaml/blob/main/examples/Switch/switchc6.yaml) 查看完整的示例配置。首次构建可能需要一段时间，具体取决于 Home Assistant 主机的性能和网络质量。

3. 再次点击 `INSTALL` 进行烧录并等待完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6HA5.webp" width="70%"/>

4. 通过 USB Type-C 线缆将设备连接到主机。打开 [ESPHome Web](https://web.esphome.io/) 并点击 `CONNECT` 连接设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA12.webp" width="40%"/>

5. 找到对应的串口号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/HA4.webp" width="40%"/>

6. 点击 `INSTALL`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA9.webp" width="40%"/>

7. 选择之前编译的固件进行上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6HA6.webp" width="30%"/>

8. 烧录完成后重新启动设备。

## 开始使用

1. 点击 `Settings` -> `Device & services` 查看设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/HA23.webp" width="40%"/>

2. 点击`Add`将设备集成到 Home Assistant 中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6HA7.webp" width="40%"/>

3. 添加设备后，数据将正确显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6HA1.webp" width="30%"/>

4. 最后，我们将这些实体添加到仪表板中，以下显示其显示结果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6HA8.webp" width="30%"/>
