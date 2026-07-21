# TTN (The Things Network) 平台连接与使用

\#> 本教程将展示如何在 TTN 中创建应用、添加注册节点设备，配置 M5Stack LoRaWAN 模块连接至 TTN 服务，实现数据发送与接收。<br/>
注：**本教程仅适用于 TTN 网关覆盖区域**，未覆盖区域个人用户需要自建网关进行连接。

## 注册账号

访问 [TTN网站](https://www.thethingsnetwork.org/) 并注册 / 登录**个人账户**，在控制台`Console`中根据地理位置等条件选择一个集群。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lorawan/ttn_01.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_01_registerPlatform.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_02_console.png" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lorawan/ttn_02.jpg" width="70%">

## 创建应用

点击`Create application`，自定义填写`Application ID`和应用名称，点击`Create application`完成创建。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_03_createApp.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_04_createApp.png" width="70%">

## 添加设备

进入已经创建好的应用管理页面，点击`+ Register end device`添加注册节点设备， 选择`Enter end device specifics manually`自定义配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_05_registerDevice.png" width="70%">

根据地理位置及设备使用的频段来确定各个选项，确保要添加的节点设备使用的频段与网关使用的频段相匹配。LoRaWAN 版本、区域参数版本需根据实际硬件支持的协议版本选择，详情可参考对应产品的文档页面。

> 在本步骤中需要选择节点设备的激活（连接）模式，有两种：`OTAA`/`ABP`<br/>
> 在 OTAA（Over the air activation）模式下，设备加入网络时会与服务器动态协商设备地址和会话密钥，安全性更高，但入网连接速度相对慢一些。<br/>
> 在 ABP（Activation by personalization）模式下，设备使用预先配置好的设备地址和会话密钥进行通信，无需入网直接开始数据收发，但灵活性、安全性和可扩展性较差。

关于这两种激活连接模式及其参数的详细介绍，可以参考官方文档：

- [End Device Activation | TTN Docs](https://www.thethingsnetwork.org/docs/lorawan/end-device-activation/)
- [ABP vs OTAA | TTN Docs](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

### OTAA 模式的配置项

选择 OTAA 模式时需要填写的`JoinEUI`（也叫`AppEUI`），是设备厂商为每一个硬件设备预先配置的参数。由于我们的产品是可编程设备，因此此处`JoinEUI`可以任意填写，只要保证在后续编程时也使用同一个值即可。填写的格式为 16 个 16 进制字符，即 0~9、A~F。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_06_OTAA.png" width="70%">

填写后点击`Confirm`，会出现更多配置项。`DevEUI`和`AppKey`这两个参数可以点击后面的`🔁 Generate`按钮来生成，生成后建议记录下来以备后续使用。自定义填写`End device ID`然后点击`Register end device`完成节点设备注册。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_07_OTAA.png" width="70%">

### ABP 模式的配置项

选择 ABP 模式时，`DevEUI`、`Device address`、`AppSKey`、`NwkSKey`这四个参数可以点击后面的`🔁 Generate`按钮来生成，生成后建议记录下来以备后续使用。自定义填写`End device ID`然后点击`Register end device`完成节点设备注册。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_08_ABP.png" width="70%">

## 设备编程与入网通信

在上面的几个步骤中，我们已经成功在 TTN 平台完成了创建应用、添加设备，接下来需要给设备编程使其通过网关与平台通信。前面添加设备时填写或生成的各个参数要对应地填入下面的示例程序中。如果你之前没有记录这些参数，也可以在 TTN 平台的设备设置中找到它们。

- OTAA 连接模式需要用到 `JoinEUI`、`DevEUI`、`AppKey`；
- ABP 连接模式需要用到 `Device address`、`AppSKey`、`NwkSKey`。

<!--
### UiFlow

以 Unit LoRaWAN868 为例，将前面步骤中得到的连接参数对应地填入配置程序块中，确保各项配置与实际设备相匹配，然后运行程序进行测试。

UiFlow 中其他的 LoRaWAN 模块 Block 支持与该程序基本一致，可以参考本案例进行修改、运行测试。

- OTAA 连接模式示例程序：

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lorawan/uiflow_block_lorawan868_example_01.svg">
-->

### Arduino

点击下方标签，获取对应设备的驱动库与示例程序，并参考对应配置函数的格式及顺序填入前面步骤中得到的连接参数。

<TabPanel>
    <template #tab-Unit_LoRaWANxxx>
        <ul>
            <li><a href="https://github.com/m5stack/M5-LoRaWAN">M5-LoRaWAN</a></li>
            <li><a href="https://github.com/m5stack/M5-LoRaWAN/blob/master/examples/LoRaWAN_OTAA/LoRaWAN_OTAA.ino">M5-LoRaWAN - OTAA example</a></li>
            <li><a href="https://github.com/m5stack/M5-LoRaWAN/blob/master/examples/LoRaWAN_ABP/LoRaWAN_ABP.ino">M5-LoRaWAN - ABP example</a></li>
        </ul>
        <pre><code class="language-cpp">
            LoRaWAN.configOTAA(
                "****************",                  // DevEUI
                "****************",                  // AppEUI / JoinEUI
                "********************************",  // AppKey
                "2"  // Upload Download Mode
            );
        </code></pre>
        <pre><code class="language-cpp">
            LoRaWAN.configABP(
                "********",                          // Device address
                "********************************",  // AppSKey
                "********************************",  // NwkSKey
                "2"  // Upload Download Mode
            );
        </code></pre>
    </template>
    <template #tab-Atom_DTU_LoRaWANxxx>
        <ul>
            <li><a href="https://github.com/m5stack/ATOM_DTU_LoRaWAN">ATOM_DTU_LoRaWAN</a></li>
            <li><a href="https://github.com/m5stack/ATOM_DTU_LoRaWAN/blob/master/examples/LoRaWAN_OTAA/LoRaWAN_OTAA.ino">ATOM_DTU_LoRaWAN - OTAA example</a></li>
            <li><a href="https://github.com/m5stack/ATOM_DTU_LoRaWAN/blob/master/examples/LoRaWAN_ABP/LoRaWAN_ABP.ino">ATOM_DTU_LoRaWAN - ABP example</a></li>
        </ul>
        <pre><code class="language-cpp">
            LoRaWAN.configOTAA(
                "****************",                  // DevEUI
                "****************",                  // AppEUI / JoinEUI
                "********************************",  // AppKey
                "2"  // Upload Download Mode
            );
        </code></pre>
        <pre><code class="language-cpp">
            LoRaWAN.configABP(
                "********",                          // Device address
                "********************************",  // AppSKey
                "********************************",  // NwkSKey
                "2"  // Upload Download Mode
            );
        </code></pre>
    </template>
    <template #tab-Unit_LoRaWAN-XXxxx>
        <ul>
            <li><a href="https://github.com/m5stack/M5-LoRaWAN-RAK">M5-LoRaWAN-RAK</a></li>
            <li><a href="https://github.com/m5stack/M5-LoRaWAN-RAK/blob/main/examples/LoRaWAN/OTAA/OTAA.ino">M5-LoRaWAN-RAK - OTAA example</a></li>
            <li><a href="https://github.com/m5stack/M5-LoRaWAN-RAK/blob/main/examples/LoRaWAN/ABP/ABP.ino">M5-LoRaWAN-RAK - ABP example</a></li>
        </ul>
        <pre><code class="language-cpp">
            #define DEVEUI "****************"
            #define APPEUI "****************"
            #define APPKEY "********************************"
        </code></pre>
        <pre><code class="language-cpp">
            #define DEVADDR "********"
            #define APPSKEY "********************************"
            #define NWKSKEY "********************************"
        </code></pre>
    </template>
    <template #tab-Atom_DTU_LoRaWAN-XXxxx>
        <ul>
            <li><a href="https://github.com/m5stack/M5-LoRaWAN-RAK">M5-LoRaWAN-RAK</a></li>
            <li><a href="https://github.com/m5stack/M5-LoRaWAN-RAK/blob/main/examples/LoRaWAN/OTAA/OTAA.ino">M5-LoRaWAN-RAK - OTAA example</a></li>
            <li><a href="https://github.com/m5stack/M5-LoRaWAN-RAK/blob/main/examples/LoRaWAN/ABP/ABP.ino">M5-LoRaWAN-RAK - ABP example</a></li>
        </ul>
        <pre><code class="language-cpp">
            #define DEVEUI "****************"
            #define APPEUI "****************"
            #define APPKEY "********************************"
        </code></pre>
        <pre><code class="language-cpp">
            #define DEVADDR "********"
            #define APPSKEY "********************************"
            #define NWKSKEY "********************************"
        </code></pre>
    </template>
</TabPanel>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_09_OTAA_Arduino.png" width="50%">

## TTN 数据收发

### Live Data 实时数据

完成上述各步操作后，若设备正常连接网关，在 TTN 管理页面我们能够看到设备的连接日志，以及上行的数据信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_10_liveData.png" width="70%">

### Messaging 数据下发

点击 `Messaging` 功能可以通过网页手动下发数据至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_11_messaging.png" width="70%">

## MQTT Client

通过 MQTT client 获取 TTN 服务器数据，实现数据收发。MQTT server 地址、端口、连接名称密码可在 TTN 应用管理页面的 `Other Integrations`-`MQTT` 中获取。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/TTN_12_MQTT.png" width="70%">

- Uplink Topic: `v3/{application id}@{tenant id}/devices/{device id}/up`

- Downlink Topic: `v3/{application id}@{tenant id}/devices/{device id}/down/push`

- 默认订阅数据的 payload 为`base64`编码格式。

关于 MQTT 消息的 topic、格式，可以参考官方文档：

- [MQTT Server | TTN Docs](https://www.thethingsindustries.com/docs/integrations/other-integrations/mqtt/)

## 更多信息

- [Glossary (1) | TTN Docs](https://www.thethingsnetwork.org/docs/lorawan/glossary/)

- [Glossary (2) | TTN Docs](https://www.thethingsindustries.com/docs/getting-started/glossary/)

- [Integrations | TTN Docs](https://www.thethingsindustries.com/docs/integrations/)
