# Unit ID

<span class="product-sku">SKU:U124</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/id/id_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/id/id_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/718/U124_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/id/id_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/id/id_06.webp">
</PictureViewer>

## 描述

**Unit ID**是一款具有基于硬件的安全密钥存储的加密协处理器，集成 ATECC608B 硬件加密芯片，采用 I2C 通信接口。芯片内置 10Kb EEPROM，可用于存储密钥、证书、数据、消费记录和安全配置。通过限制对内存区域的访问策略，能够锁定配置以防止更改。

每个 ATECC608B 都附带有保证的唯一 72 位序列号，并包括多项安全功能，以防止对设备本身的物理攻击，或对设备之间传输的数据进行逻辑攻击。

支持 Trust\&GO 平台 (预置通用证书，适用于基于 TLS 的网络安全身份验证，如 :AWS-IoT，Azure，Google 等云平台验证注册)，可通过工具直接获取加密芯片内部证书，完成自动注册，无私钥暴露环节。

## 注意事项

?>Trust\&GO| 预配置的 Trust\&GO 安全元件仅支持 "Microchip Trust Platform"。欲知更多详情，请参阅以下链接。<https://www.microchip.com/en-us/product/ATECC608B-TNGTLS>

## 产品特性

- ATECC608B-TNGTLSU-G
- I2C 通信接口
- 自带保护外壳，更加稳定可靠
- 最多 16 个密钥、证书或数据的受保护存储
- 数据存储 / 锁定
- 随机数发生器
- 预置证书和密钥
- 72bit 唯一序列号

## 包装内容

- 1 x Unit ID
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 物联网端点密钥管理和交换
- 设备身份验证
- 数据加密

## 规格参数

| 规格             | 参数                                          |
| ---------------- | --------------------------------------------- |
| 加密芯片型号     | ATECC608B-TNGTLSU-G                           |
| 支持算法类型     | ECC-P256 (ECDH 和 ECDSA) 、SHA256、AES128-GCM |
| 支持密钥储存个数 | 16                                            |
| 通信接口         | I2C 通信 @ 0x35，总线最大速度 1Mbps           |
| 供电电压         | DC 5V                                         |
| 产品尺寸         | 24.0 x 24.0 x 8.0mm                           |
| 产品重量         | 3.3g                                          |
| 包装尺寸         | 138.0 x 93.0 x 9.0mm                          |
| 毛重             | 6.5g                                          |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/id/id_sch_01.webp" width="80%">

## 管脚映射

### Unit ID

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/id/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 数据手册

- [ATECC608B](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/id/ATECC608B-CryptoAuthentication-Device-Summary-Data-Sheet-DS40002239A.pdf)

## 软件开发

### Arduino

- [Unit ID Arduino 驱动库](https://github.com/sparkfun/SparkFun_ATECCX08A_Arduino_Library)

### UiFlow1

- [Unit ID UiFlow1 文档](/zh_CN/uiflow/blockly/unit/id)

### UiFlow2

- [Unit ID UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/id.html)

### ESP-IDF

- [ECC608-TNG-AWS-Connect](https://github.com/kmwebnet/ECC608-TNG-AWS-Connect)

### 其他

- [Generate manifest file](https://github.com/espressif/esp-cryptoauthlib/blob/master/esp_cryptoauth_utility/README.md)
