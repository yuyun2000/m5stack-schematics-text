# [IoT Base NB](/zh_CN/base/iot_base_nb_cn)

## 案例程序

测试 MQTT 连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_iotnb_exmple.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

setScreenColor(0x222222)

nb_topic = None
nb_msg = None

nbiot = module.get(module.NBIOT)

def iotbase_mqtt_cb(nb_mq_topic, nb_mq_payload):
  global nb_topic, nb_msg
  nb_topic = nb_mq_topic
  nb_msg = nb_mq_payload
  print(nb_topic)
  print(nb_msg)
  pass

nbiot.mqtt_to_connect('mqtt.m5stack.com', 1883, '', '', '', 120)
nbiot.mqtt_publish('subscribe', '', 0)
while True:
  if nbiot.mqtt_check_connection():
    print(nbiot.at_command_tester('AT', 'OK', 1000, 0))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_check_gprs_network_registration.svg">

```python
nbiot.get_gprs_network_registration()
```

- 检查设备是否已注册到 GPRS 网络中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_check_network_registration.svg">

```python
nbiot.get_network_registration()
```

- 检查设备是否已成功注册到网络(通用网络注册检查)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_check_single_quality.svg">

```python
nbiot.get_single_quality()
```

- 检查当前网络的信号质量，返回信号强度信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_check_status.svg">

```python
nbiot.check_status()
```

- 检查模块的状态，了解当前模块是否正常工作或有无问题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_coap_destroy.svg">

```python
nbiot.coap_destroy()
```

- 销毁 CoAP 连接，关闭 CoAP 会话或释放相关资源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_coap_get.svg">

```python
nbiot.coap_get('/m5stack-get')
```

- 通过指定的 URL 执行 CoAP GET 请求。可以设置安全选项，但此处选择的是无安全(None)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_coap_init_ip.svg">

```python
nbiot.coap_to_connect('120.77.157.90', 5683)
```

- 初始化 CoAP 连接，指定目标服务器的 IP 地址(如 120.77.157.90)和端口(如 5683)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_coap_post.svg">

```python
nbiot.coap_post('/m5stack-post', '', content_format=0)
```

- 通过指定的 URL 发送 CoAP POST 请求，将内容(payload)以文本(TEXT_PLAIN)的格式发送。此处 URL 为/m5stack-post

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_coap_put.svg">

```python
nbiot.coap_put('/m5stack-put', '', content_format=0)
```

- 通过指定的 URL 发送 CoAP PUT 请求，用于更新资源或数据。payload 的内容格式同样为 TEXT_PLAIN，URL 为/m5stack-put

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_ezdata_async_get_value.svg">

```python
nbiot.get_ezdata(ezdata_get_NRZBHcb, 'GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 通过指定的主题和令牌从云平台异步获取数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_ezdata_remove.svg">

```python
nbiot.remove_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 通过指定的主题和令牌从云平台中移除该主题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_ezdata_save.svg">

```python
nbiot.set_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '', '', 0)
```

- 将数据保存到指定的主题，并附带令牌用于验证

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_get_ccid.svg">

```python
nbiot.get_CCID()
```

- 获取设备的 CCID(集成电路卡识别码)，通常用于标识 SIM 卡

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_get_imei.svg">

```python
nbiot.get_IMEI()
```

- 获取设备的 IMEI(国际移动设备身份码)，用于唯一标识移动设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_init.svg">

```python
nbiot.modbus_init(15, 13, 115200, 1, 1)
```

- 初始化 Modbus 通信，配置 Tx 和 Rx 引脚、波特率、模式(主/从)以及从机地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_master_u_read_coils.svg">

```python
modbus.read_coils(1, 1, 0)
```

- 读取指定从机地址和起始地址的线圈状态，线圈数量可配置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_master_u_read_discrete_inputs.svg">

```python
modbus.read_discrete_inputs(1, 1, 0)
```

- 从指定的从机地址读取离散输入状态，可以配置起始地址和读取的输入数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_master_u_read_holding_registers.svg">

```python
modbus.read_holding_registers(1, 1, 0, True)
```

- 读取保持寄存器的值，指定从机地址、起始地址和寄存器数量，并选择读取值是否为有符号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_master_u_read_input_registers.svg">

```python
modbus.read_input_registers(1, 1, 0, True)
```

- 读取输入寄存器的值，指定从机地址、起始地址和寄存器数量，并选择是否读取有符号的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_master_u_write_multiple_coils.svg">

```python
modbus.write_multiple_coils(1, 1, 0)
```

- 向多个线圈写入输出值，指定从机地址、起始地址和输出值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_master_u_write_multiple_registers.svg">

```python
modbus.write_multiple_registers(1, 1, 0, True)
```

- 向多个寄存器写入值，指定从机地址、起始地址、寄存器值，并选择是否写入有符号的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_master_u_write_single_coil.svg">

```python
modbus.write_single_coil(1, 1, 0)
```

- 向单个线圈写入输出值，指定从机地址、输出地址和输出值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_master_u_write_single_register.svg">

```python
modbus.write_single_register(1, 1, 0, True)
```

- 向单个寄存器写入值，指定从机地址、寄存器地址和寄存器值，并选择是否写入有符号的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_slave_rtu_fun_status.svg">

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

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_slave_rtu_get_address.svg">

```python
modbus.find_address
```

- 获取从机的地址信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_slave_rtu_get_function.svg">

```python
modbus.find_function
```

- 获取当前使用的功能码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_slave_rtu_get_quantity.svg">

```python
modbus.find_quantity
```

- 获取要读取的数据数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_slave_rtu_init_func.svg">

```python
modbus.function_init(1, 0, 0)
```

- 初始化 Modbus 从机功能，设置起始地址和要读取的数量，用于读取线圈状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_slave_rtu_receive_adu.svg">

```python
modbus.receive_req_create_pdu()
```

- 用于从主机接收 ADU(应用数据单元)的请求

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_slave_rtu_send.svg">

```python
modbus.create_slave_response(1)
```

- 发送 ADU 响应，通常用于从机回复主机的请求

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modbus_slave_rtu_update_func.svg">

```python
modbus.update_process(1, 0, 0, [0, 0, 0])
```

- 更新 Modbus 功能块(如 READ_COILS_STATUS)的数据，设置起始地址、数量和要写入的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_modem_power.svg">

```python
nbiot.modem_power(True)
```

- 控制通信模块的电源开关，可以选择开启或关闭

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_mqtt_check_connection.svg">

```python
nbiot.mqtt_check_connection()
```

- 检查 MQTT 的连接状态，确保设备与 MQTT 服务器连接正常

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_mqtt_connect.svg">

```python
nbiot.mqtt_to_connect('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 初始化 MQTT 服务器的连接，设置服务器地址、端口、客户端 ID、用户名、密码和心跳保持时间。用于连接到 MQTT 服务器进行数据通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_mqtt_disconnect.svg">

```python
nbiot.mqtt_disconnect()
```

- 断开与 MQTT 服务器的连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_mqtt_poll.svg">

```python
nbiot.mqtt_poll()
```

- 查询并接收从 MQTT 服务器下行的消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_mqtt_publish.svg">

```python
nbiot.mqtt_publish('', '', 0)
```

- 发布消息到指定的 MQTT 主题，发送的消息内容包括负载和服务质量(QoS)等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_mqtt_sub.svg">

```python
nbiot.mqtt_subscribe('', iotbase_mqtt_cb, 0)
```

- 订阅指定的 MQTT 主题(Topic)，接收来自该主题的消息。QoS 定义了消息服务质量等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_mqtt_sub_cb.svg">

```python
def iotbase_mqtt_cb(nb_mq_topic, nb_mq_payload):
  global ezdata_value1, nb_topic, nb_msg
  nb_topic = nb_mq_topic
  nb_msg = nb_mq_payload
  pass
```

- 注册一个回调函数，处理从订阅的 MQTT 主题中接收到的消息。nb_topic 和 nb_msg 用于获取主题和消息内容

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_mqtt_unsubscribe.svg">

```python
nbiot.mqtt_unsubscribe('')
```

- 取消订阅指定的 MQTT 主题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_power_down_module.svg">

```python
nbiot.poweroff()
```

- 关闭模块的电源，通常用于省电或关闭设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_reset_module.svg">

```python
nbiot.reset()
```

- 重置模块，使其恢复到初始状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_set_echo_mode.svg">

```python
nbiot.set_command_echo_mode(0)
```

- 设置命令回显模式。可以选择是否在执行命令时显示设备返回的命令回显

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_uart_any.svg">

```python
modbus._mdbus_uart.any()
```

- 检查并保留缓存的数据，用于判断 UART 缓冲区中是否有未读取的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_uart_read.svg">

```python
modbus._mdbus_uart.read()
```

- 读取 UART 缓存中的所有数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_uart_readline.svg">

```python
modbus._mdbus_uart.readline()
```

- 从 UART 读取一行数据，直到遇到换行符为止

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_uart_read_characters.svg">

```python
modbus._mdbus_uart.read(10)
```

- 从 UART 读取指定数量的字符。这个示例中，读取10个字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_uart_write.svg">

```python
modbus._mdbus_uart.write('')
```

- 将指定的文本或数据写入 UART 串口

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_uart_write_line.svg">

```python
modbus._mdbus_uart.write(''+"\r\n")
```

- 将指定的文本或数据以一行的形式写入 UART，并在末尾附加一个换行符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/iot_base_nb/uiflow_block_iotbase_uart_write_raw_data.svg">

```python
modbus._mdbus_uart.write(bytes([0, 0, 0]))
```

- 将原始数据以字节列表的形式写入 UART，这个块可以发送二进制数据，常用于传输原始数据或非文本数据

