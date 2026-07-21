# [Atom DTU NB IoT](/zh_CN/atom/atom_dtu_nb)

## 案例程序

该程序通过 NB-IoT DTU 连接到 MQTT 服务器，订阅主题`SubTopic`，并在收到消息时打印主题和消息内容。按下按钮 A 时，随机生成一个整数并发布到主题`PubTopic`。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_atomic_base_nbiot_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.DTU_NB import DTU_NB

nb_topic = None
nb_msg = None
Rand = None

import random

def nbiot_mqtt_cb(nb_mq_topic, nb_mq_payload):
  global nb_topic, nb_msg, Rand
  nb_topic = nb_mq_topic
  nb_msg = nb_mq_payload
  print(nb_topic)
  print(nb_msg)
  pass

def buttonA_wasPressed():
  global nb_topic, nb_msg, Rand
  dtu_nb.mqtt_publish('PubTopic', str(Rand), 0)
  pass
btnA.wasPressed(buttonA_wasPressed)

dtu_nb = DTU_NB()
dtu_nb.mqtt_to_connect('mqtt.m5stack.com', 1883, 'm5mqtt9', '', '', 120)
print(dtu_nb.mqtt_check_connection())
print(dtu_nb.mqtt_subscribe('SubTopic', nbiot_mqtt_cb, 0))
while True:
  if (dtu_nb.mqtt_check_connection()) != None:
    Rand = random.randint(100000, 999999)
    dtu_nb.mqtt_poll()
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_init.svg">

```python
dtu_nb = DTU_NB()
```

- 初始化 NB-IoT DTU 模块。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_modbus_init.svg">

```python
modbus = dtu_nb.modbus_init(23, 33, 115200, 1, 1)
```

- 设置串口通信的 TX(发送引脚)、RX(接收引脚)，波特率为 115200，模式为主设备(Master)，以及从设备地址(Slave Addr)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_modbus_slave_rtu_init_func.svg">

```python
modbus.function_init(1, 0, 0)
```

- 初始化 Modbus 功能码，用于读取线圈状态，指定起始地址和读取数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_any.svg">

```python
modbus._mdbus_uart.any()
```

- 保持缓存，可能用于存储数据或其他信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_check_gprs_network_registration.svg">

```python
dtu_nb.get_gprs_network_registration()
```

- 检查 GPRS 网络注册状态，确保设备已连接至网络。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_check_network_registration.svg">

```python
dtu_nb.get_network_registration()
```

- 检查网络注册状态，确认设备是否已注册到网络。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_check_single_quality.svg">

```python
dtu_nb.get_single_quality()
```

- 检查信号质量，以评估设备的信号强度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_check_status.svg">

```python
dtu_nb.check_status()
```

- 检查模块状态，确保模块正常工作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_coap_connect_ip.svg">

```python
dtu_nb.coap_to_connect('120.77.157.90', 5683)
```

- 使用 CoAP 协议连接到指定的 IP 地址和端口(此例中 IP 地址为 120.77.157.90，端口为 5683)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_coap_destroy.svg">

```python
dtu_nb.coap_destroy()
```

- 销毁 CoAP 连接，用于关闭或重置 CoAP 会话。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_coap_get.svg">

```python
dtu_nb.coap_get('/m5stack-get')
```

- 发送 CoAP GET 请求到指定的 URL(如 /m5stack-get)，并且指定安全性(此处为 None)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_coap_post.svg">

```python
dtu_nb.coap_post('/m5stack-post', '', content_format=0)
```

- 发送 CoAP POST 请求到指定的 URL(如 /m5stack-post)，附带有效负载(payload)，内容格式为 TEXT_PLAIN，安全性为 None。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_coap_put.svg">

```python
dtu_nb.coap_put('/m5stack-put', '', content_format=0)
```

- 发送 CoAP PUT 请求到指定的 URL(如 /m5stack-put)，附带有效负载(payload)，内容格式为 TEXT_PLAIN，安全性为 None。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_modbus_slave_rtu_fun_status.svg">

```python
1-6,15-16
```

- 读取或设置 Modbus 功能码，在该例中，选择了 READ_COILS_STATUS 作为功能码。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_modbus_slave_rtu_get_address.svg">

```python
modbus.find_address
```

- 获取从机的地址。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_modbus_slave_rtu_get_function.svg">

```python
modbus.find_function
```

- 获取当前功能码。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_modbus_slave_rtu_get_quantity.svg">

```python
modbus.find_quantity
```

- 用于获取当前的数量，可能用于读取从机的数据数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_modbus_slave_rtu_receive_adu.svg">

```python
modbus.receive_req_create_pdu()
```

- 接收 ADU(Application Data Unit)请求，通常用于 Modbus 协议中的数据通信。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_modbus_slave_rtu_send.svg">

```python
modbus.create_slave_response(1)
```

- 发送 ADU 响应缓冲区中的数据，缓冲区大小为1。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_modbus_slave_rtu_update_func.svg">

```python
modbus.update_process(1, 0, 0, [0, 0, 0])
```

- 更新 Modbus 的功能，当前设置为 READ_COILS_STATUS，可以指定起始地址、数量和更新的值，并创建一个包含数值的列表。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_mqtt_check_connection.svg">

```python
dtu_nb.mqtt_check_connection()
```

- 检查 MQTT 的连接状态，确保与 MQTT 服务器的连接是否正常。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_mqtt_connect.svg">

```python
dtu_nb.mqtt_to_connect('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 连接 MQTT 服务器，指定服务器地址(如 mqtt.m5stack.com)，端口(默认是1883)，并且可以设置客户端 ID、用户名、密码和保持连接时间(keepalive，单位为秒)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_mqtt_disconnect.svg">

```python
dtu_nb.mqtt_disconnect()
```

- 断开 MQTT 连接，与服务器断开连接。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_mqtt_poll.svg">

```python
dtu_nb.mqtt_poll()
```

- 轮询下行消息，用于检查从 MQTT 服务器发送来的下行数据消息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_mqtt_publish.svg">

```python
dtu_nb.mqtt_publish('', '', 0)
```

- 发布主题消息到 MQTT 服务器，用户可以指定要发布的主题、消息的内容(payload)，以及消息传递质量服务等级(QoS)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_mqtt_sub.svg">

```python
dtu_nb.mqtt_subscribe('', nbiot_mqtt_cb, 0)
```

- 订阅指定主题，用户可以选择订阅的主题名称以及消息传递质量服务等级(QoS)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_mqtt_sub_cb.svg">

```python
def nbiot_mqtt_cb(nb_mq_topic, nb_mq_payload):
  global nb_topic, nb_msg
  nb_topic = nb_mq_topic
  nb_msg = nb_mq_payload
  pass
```

- 设置订阅的回调函数，当指定的主题收到消息时，会执行相应的处理，消息内容可以通过变量(如 nb_msg)获取。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_mqtt_unsubscribe.svg">

```python
dtu_nb.mqtt_unsubscribe('')
```

- 取消订阅指定主题。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_power_down_module.svg">

```python
dtu_nb.poweroff()
```

- 关闭模块电源，用于节省能量或在不需要时关闭模块。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_read.svg">

```python
modbus._mdbus_uart.read()
```

- 读取所有模块中的相关信息或数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_readline.svg">

```python
modbus._mdbus_uart.readline()
```

- 读取一行数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_read_characters.svg">

```python
modbus._mdbus_uart.read(10)
```

- 读取指定数量的字符(如读取10个字符)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_read_coils.svg">

```python
modbus.read_coils(1, 1, 0)
```

- 读取线圈状态，指定从站地址、起始地址和线圈数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_read_discrete_inputs.svg">

```python
modbus.read_discrete_inputs(1, 1, 0)
```

- 读取离散输入，指定从站地址、起始地址和输入数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_read_holding_registers.svg">

```python
modbus.read_holding_registers(1, 1, 0, True)
```

- 读取保持寄存器，指定从站地址、起始地址、寄存器数量和数据是否为有符号数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_read_input_registers.svg">

```python
modbus.read_input_registers(1, 1, 0, True)
```

- 读取输入寄存器，指定从站地址、起始地址、寄存器数量和数据是否为有符号数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_reset_module.svg">

```python
dtu_nb.reset()
```

- 重置模块，执行模块的复位操作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_set_echo_mode.svg">

```python
dtu_nb.set_command_echo_mode(0)
```

- 设置命令回显模式(如开启或关闭回显)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_write.svg">

```python
modbus._mdbus_uart.write('')
```

- 在 UART 中写入指定内容。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_write_line.svg">

```python
modbus._mdbus_uart.write(''+"\r\n")
```

- 在 UART 中写入一行内容。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_write_multiple_coils.svg">

```python
modbus.write_multiple_coils(1, 1, 0)
```

- 写入多个线圈，指定从站地址、起始地址和输出值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_write_multiple_registers.svg">

```python
modbus.write_multiple_registers(1, 1, 0, True)
```

- 写入多个寄存器，指定从站地址、起始地址、寄存器值，并可以设置为有符号数或无符号数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_write_raw_data.svg">

```python
modbus._mdbus_uart.write(bytes([0, 0, 0]))
```

- 在 UART 中写入原始数据，使用列表形式指定要写入的数值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_write_single_coil.svg">

```python
modbus.write_single_coil(1, 1, 0)
```

- 写入单个线圈，指定从站地址、输出地址和输出值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_nb_iot/uiflow_block_base_dtunb_write_single_register.svg">

```python
modbus.write_single_register(1, 1, 0, True)
```

- 写入单个寄存器，指定从站地址、寄存器地址、寄存器值，并可以设置为有符号数或无符号数。

