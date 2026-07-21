# [IoT Base Catm](/zh_CN/base/iot_base_catm)

## 案例程序

测试 MQTT 连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_iotcatm_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

setScreenColor(0x222222)

catm_topic = None
catm_msg = None

catmiot = module.get(module.CATMIOT)

def iotbasecatm_mqtt_cb(catm_mq_topic, catm_mq_payload):
  global catm_topic, catm_msg
  catm_topic = catm_mq_topic
  catm_msg = catm_mq_payload
  print((str('topic:') + str(catm_topic)))
  print((str('msg:') + str(catm_msg)))
  pass

catmiot.init_modem(True)
catmiot.mqtt_to_connect('mqtt.m5stack.com', 1883, '', '', '', 120)
while True:
  if catmiot.mqtt_ischeck_connect():
    print(catmiot.mqtt_subscribe('m5stack', iotbasecatm_mqtt_cb, 0))
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_check_gprs_network_registration.svg">

```python
catmiot.get_gprs_network_registration()
```

- 检查设备是否已在 GPRS 网络中注册

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_check_network_registration.svg">

```python
catmiot.get_network_registration()
```

- 检查设备是否已在常规网络中注册

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_check_single_quality.svg">

```python
catmiot.get_single_quality()
```

- 检查设备当前的信号质量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_check_status.svg">

```python
catmiot.check_status()
```

- 检查模块的状态，查看模块是否正常工作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_coap_delete.svg">

```python
catmiot.delete_coap()
```

- 发送 CoAP 协议中的 DELETE 请求，用于删除服务器上的资源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_coap_get.svg">

```python
catmiot.coap_request('/m5stack-get')
```

- 发送 CoAP 协议中的 GET 请求，从指定的 URL 中获取资源
  - /m5stack-get: 指定的 URL 路径，从中获取资源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_coap_init.svg">

```python
catmiot.coap_to_connect('120.77.157.90', 5683)
```

- 初始化连接到指定的 IP 地址和端口号，用于建立 CoAP 协议的通信
  - IP: 120.77.157.90
  - Port: 5683

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_coap_post.svg">

```python
catmiot.coap_request('/m5stack-post', 2, '')
```

- 通过 CoAP 协议向指定的 URL 发送 POST 请求
  - URL: /m5stack-post
  - Payload: 发送的数据负载。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_disable_power_save_mode.svg">

```python
catmiot.power_save_mode(0, 0, 0, 0, False)
```

- 禁用设备的省电模式，以确保设备能够持续保持高性能运行
<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_disconnect_server.svg">

```python
catmiot.disconnect_server()
```

- 断开当前设备与 HTTP 服务的连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_enable_pdp_context.svg">

```python
catmiot.enable_PDP_context()
```

- 启用 PDP 上下文，通常用于 GPRS 或 LTE 网络通信，确保数据传输的上下文建立

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_ezdata_async_get_value.svg">

```python
catmiot.get_ezdata(ezdata_get_kslNzcb, 'GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 从指定的主题(topic)中获取数据
  - Token: dCtdfg3u5id72J8YCubqu16zMqQunDQh


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_ezdata_remove.svg">

```python
catmiot.remove_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 从远程服务器中删除指定的主题
  - Token: dCtdfg3u5id72J8YCubqu16zMqQunDQh

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_ezdata_save.svg">

```python
catmiot.set_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '', '', 0)
```

- 将数据保存到指定的主题中，并通过指定的 token 进行验证
  - Token: dCtdfg3u5id72J8YCubqu16zMqQunDQh
  - Mode: Single (表示数据的保存模式为单一数据)
  - Data: 需要保存的数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_get_ccid.svg">

```python
catmiot.get_CCID()
```

- 获取当前 SIM 卡的 CCID (Integrated Circuit Card Identifier)号，即 SIM 卡的唯一标识

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_get_imei.svg">

```python
catmiot.get_IMEI()
```

- 获取设备的 IMEI (International Mobile Equipment Identity)号，即设备的唯一标识

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_gprs_service.svg">

```python
catmiot.gprs_service(1)
```

- 设置或检查设备的 GPRS 服务状态。此处设置为 ACTIVE，表示启用 GPRS 服务

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_http_services.svg">

```python
catmiot.http_service(1, '', '', {}, '')
```

- 使用 HTTP 协议发送 GET 请求，获取远程服务器的数据
  - Method: GET (HTTP 请求的方法)
  - URL: 请求的地址
  - Headers: 创建一个包含 HTTP 请求头信息的 Map
  - Payload: 如果是 POST 请求，可以通过此参数传递数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_init_modem.svg">

```python
catmiot.init_modem(True)
```

- 启动并初始化模块，为后续的通信和数据交互做好准备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_init.svg">

```python
catmiot.modbus_init(15, 13, 115200, 1, 1)
```

- 初始化 UART 通信接口，设置 TX(发送)引脚为15，RX(接收)引脚为13，波特率为115200，模式为主设备(Master)，从设备地址为1

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_master_u_read_coils.svg">

```python
modbus.read_coils(1, 1, 0)
```

- 读取从设备地址1的线圈状态，从起始地址1开始，读取数量为0个

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_master_u_read_discrete_inputs.svg">

```python
modbus.read_discrete_inputs(1, 1, 0)
```

- 从设备地址1的离散输入状态，从起始地址1开始，读取数量为0个

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_master_u_read_holding_registers.svg">

```python
modbus.read_holding_registers(1, 1, 0, True)
```

- 从设备地址1的保持寄存器读取数据，从起始地址1开始，读取数量为0个，读取的数据是带符号数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_master_u_read_input_registers.svg">

```python
modbus.read_input_registers(1, 1, 0, True)
```

- 从设备地址1的输入寄存器读取数据，从起始地址1开始，读取数量为0个，读取的数据是带符号数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_master_u_write_multiple_coils.svg">

```python
modbus.write_multiple_coils(1, 1, 0)
```

- 向从设备地址1的多个线圈写入数据，从起始地址1开始，写入的输出值为0

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_master_u_write_multiple_registers.svg">

```python
modbus.write_multiple_registers(1, 1, 0, True)
```

- 向从设备地址1的多个寄存器写入数据，从起始地址1开始，写入的寄存器值为0，数据为带符号值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_master_u_write_single_coil.svg">

```python
modbus.write_single_coil(1, 1, 0)
```

- 向从设备地址1的单个线圈写入值，输出地址为1，写入的值为0

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_master_u_write_single_register.svg">

```python
modbus.write_single_register(1, 1, 0, True)
```

- 向从设备地址1的单个寄存器写入数据，寄存器地址为1，写入的值为0，数据为带符号值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_slave_rtu_fun_status.svg">

```python
print((str('code:') + str((1))))
```

- 设置 MODBUS 函数码为 READ_COILS_STATUS，用于读取线圈的状态
  - 1:READ_COILS_STATUS
  - 2:READ_INPUT_STATUS
  - 3:READ_HOLDING_REGISTERS
  - 4:READ_INPUT_REGISTERS
  - 5:WRITE_SINGLE_COIL
  - 6:WRITE_SINGLE_REGISTER
  - 7:WRITE_MULTIPLE_COILS
  - 8:WRITE_MULTIPLE_REGISTERS
  
<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_slave_rtu_get_address.svg">

```python
modbus.find_address
```

- 获取当前 MODBUS 通信中的从设备地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_slave_rtu_get_function.svg">

```python
modbus.find_function
```

- 获取当前 MODBUS 操作的函数码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_slave_rtu_get_quantity.svg">

```python
modbus.find_quantity
```

- 获取当前 MODBUS 请求中读取或写入的数量值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_slave_rtu_init_func.svg">

```python
modbus.function_init(1, 0, 0)
```

- 初始化 MODBUS 从机功能码为 READ_COILS_STATUS，用于从指定起始地址和数量读取线圈的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_slave_rtu_receive_adu.svg">

```python
modbus.receive_req_create_pdu()
```

- 接收 ADU(Application Data Unit)请求，表示接收到主设备的请求数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_slave_rtu_send.svg">

```python
modbus.create_slave_response(1)
```

- 发送 ADU 响应数据缓冲区，响应主机的请求

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_modbus_slave_rtu_update_func.svg">

```python
modbus.update_process(1, 0, 0, [0, 0, 0])
```

- 更新 READ_COILS_STATUS 功能，从起始地址读取指定数量的线圈状态，并返回相应的数据列表

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_mqtt_check_connection.svg">

```python
catmiot.mqtt_ischeck_connect()
```

- 检查 MQTT 服务器的连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_mqtt_connect.svg">

```python
catmiot.mqtt_to_connect('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 初始化 MQTT 服务器连接，设置服务器地址、端口、客户端 ID、用户名、密码和保持连接时间

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_mqtt_disconnect.svg">

```python
catmiot.mqtt_disconnect()
```

- 断开与 MQTT 服务器的连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_mqtt_poll.svg">

```python
catmiot.mqtt_poll()
```

- 轮询下行消息，检查 MQTT 服务器是否有新的消息发送到设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_mqtt_publish.svg">

```python
catmiot.mqtt_publish('', '', 0)
```

- 向指定的 MQTT 主题发布消息，包含消息内容(payload)和 QoS(服务质量)设置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_mqtt_sub.svg">

```python
catmiot.mqtt_subscribe('', iotbasecatm_mqtt_cb, 0)
```

- 订阅指定的 MQTT 主题，并设置 QoS(服务质量)级别

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_mqtt_sub_cb.svg">

```python
def iotbasecatm_mqtt_cb(catm_mq_topic, catm_mq_payload):
  global ezdata_value1, catm_topic, catm_msg
  catm_topic = catm_mq_topic
  catm_msg = catm_mq_payload
  pass
```

- 设置 MQTT 主题订阅后的回调函数，处理接收到的主题消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_mqtt_unsubscribe.svg">

```python
catmiot.mqtt_unsubscribe('')
```

- 取消订阅指定的 MQTT 主题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_network_active.svg">

```python
catmiot.network_active(0, 1)
```

- 激活指定的网络 ID 并设置该网络的动作为 active(激活状态)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_network_ip_id.svg">

```python
catmiot.get_network_ip(0)
```

- 获取指定网络的 IP 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_power_down_module.svg">

```python
catmiot.poweroff()
```

- 关闭模块的电源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_power_save_mode.svg">

```python
catmiot.power_save_mode(0, 10, 0, 5)
```

- 启用节电模式，设置周期 TAU(时间间隔)和活跃时间段
    - Periodic-TAU：以10分钟为单位设置，10 表示唤醒时间间隔为 10 x 10分钟，即100分钟。  
    - Active Time：以2秒为单位设置，5 表示设备在唤醒后会保持活动10秒。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_set_echo_mode.svg">

```python
catmiot.set_command_echo_mode(0)
```

- 设置命令回显模式为 OFF，即关闭命令的回显

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_show_pdp_address.svg">

```python
catmiot.show_PDP_address()
```

- 显示 PDP(分组数据协议)地址，通常用于设备的网络连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_uart_any.svg">

```python
modbus._mdbus_uart.any()
```

- 检查串口缓存区是否有数据剩余

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_uart_read.svg">

```python
modbus._mdbus_uart.read()
```

- 从串口读取所有可用的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_uart_readline.svg">

```python
modbus._mdbus_uart.readline()
```

- 从串口读取一行数据，直到遇到换行符(通常是\n)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_uart_read_characters.svg">

```python
modbus._mdbus_uart.read(10)
```

- 从串口中读取指定数量的字符，这里设定为读取10个字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_uart_write.svg">

```python
modbus._mdbus_uart.write('')
```

- 将指定的数据写入到串口

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_uart_write_line.svg">

```python
modbus._mdbus_uart.write(''+"\r\n")
```

- 将一行数据写入到串口，通常会附带换行符(\n)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_catm/uiflow_block_iotbasecatm_uart_write_raw_data.svg">

```python
modbus._mdbus_uart.write(bytes([0, 0, 0]))
```

- 将原始数据列表写入串口
  - 这里使用了一个创建列表的模块，列表中包含三个值 0, 0, 0，表示将这些数值通过 UART 发送

