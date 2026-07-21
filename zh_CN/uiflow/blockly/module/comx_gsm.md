# [Module COMX GSM](/zh_CN/module/comx_gsm)

## 案例程序

通过 M5Stack 设备进行 Ping 测试、建立 TCP 连接并发送消息，同时发送和接收 HTTP 请求，并将这些操作的结果在屏幕上显示出来

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from comx.sim800 import SIM800

setScreenColor(0x222222)

gsm = SIM800()

if gsm.tcp_client(0, '118.190.93.84', 2317, 'Hai M5'):
  label5.setText('Success')
else:
  label5.setText('Unsuccess')
gsm.http_destroy()
label3.setText(str(gsm.http_services(1, 'http://header.json-json.com/', 'application/x-www-form-urlencoded', 'hai m5')))
label3.setText(str(gsm.http_services(0, 'http://api.m5stack.com/v1', 'application/json', '')))
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_check_gprs_network_registration.svg">

```python
gsm.get_gprs_network_registration()
```

- 检查 GPRS 网络注册状态，返回模块是否已经成功注册到 GPRS 网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_check_gprs_service.svg">

```python
gsm.check_gprs_service()
```

- 检查 GPRS 服务状态，确认 GPRS 服务是否可用

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_check_network_registration.svg">

```python
gsm.get_network_registration()
```

- 检查网络注册状态，返回模块是否已经成功注册到蜂窝网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_check_single_quality.svg">

```python
gsm.get_single_quality()
```

- 检查信号质量，返回当前的信号强度信息，用于评估网络连接的质量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_check_status.svg">

```python
gsm.check_status()
```

- 检查模块状态，返回模块的当前运行状态信息，包括是否正常运行或是否存在错误

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_get_ccid.svg">

```python
gsm.get_CCID()
```

- 获取 SIM 卡的 CCID(集成电路卡标识符)，这是 SIM 卡的唯一标识符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_get_imei.svg">

```python
gsm.get_IMEI()
```

- 获取设备的 IMEI(国际移动设备识别码)，这是设备的唯一标识符，用于识别移动设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_http_destroy.svg">

```python
gsm.http_destroy()
```

- 销毁 HTTP 会话，释放资源。用于终止当前的 HTTP 连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_http_service.svg">

```python
gsm.http_services(0, '', 'application/json', '')
```

- 使用指定的 HTTP 方法(GET、POST 等)向特定 URL 发送请求，并处理响应。
  - method：选择 HTTP 方法，如 GET 或 POST。
  - url：指定目标 URL。
  - content type：选择内容类型，如 JSON 或 TEXT。  
  - payload：在 POST 或 PUT 请求中发送的数据负载。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_ping_request.svg">

```python
gsm.ping_request('')
```

- 向指定的 URL 发送 Ping 请求，以测试该 URL 的响应性或网络连接质量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_set_echo_mode.svg">

```python
gsm.set_command_echo_mode(0)
```

- 设置命令回显模式。0表示关闭回显，1表示开启回显。当设置为 OFF 时，设备不会在发送 AT 命令后回显命令字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_set_pdp_address.svg">

```python
gsm.PDP_address(1)
```

- 设置 PDP(分组数据协议)地址的上下文标识符(CID)。CID 是用于标识网络上下文的标识符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_set_pdp_context.svg">

```python
gsm.set_PDP_context_status(1)
```

- 设置 PDP 上下文状态，Active 表示激活 PDP 上下文，用于网络连接和数据传输

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_gsm/uiflow_block_com_gsm_tcp_client.svg">

```python
gsm.http_services(0, '', 'application/json', '')
```

- 创建一个 TCP 客户端连接。
  - method: 指定为 TCP 协议。
  - IP: 目标服务器的 IP 地址。
  - port: 目标服务器的端口号。
  - payload: 要发送的数据负载。

