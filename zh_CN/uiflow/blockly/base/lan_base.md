# [Base LAN](/zh_CN/base/lan_base)

## 案例程序

> 初始化一个 TCP 服务器，通过指定的 IP 和端口建立连接，并在循环中随机生成数据包发送，同时监控是否有可用的数据包接收，并打印接收的数据包大小

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module
import time

setScreenColor(0x222222)

counter = None

lan = module.get(module.LANBASE)

import random

counter = 0
print('Start the TCP Server')
print((str('Local IP address：') + str((lan.local_ip()))))
lan.tcp_udp_config('192.168.1.97', 55005, 1, 1)
print('TCP Connected')
print((str('Remote IP address：') + str((lan.remote_ip()))))
while True:
  counter = random.randint(100000, 999999)
  lan.tcp_send_packet(str(counter))
  wait(1)
  if lan.is_available_packet(1):
    print((str('TCP receive packet size') + str((lan.tcp_receive_packet(0)))))
  wait(1)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_available_packet.svg">

```python
lan.is_available_packet(1)
```

- 这个选项块表示当前可以使用的包协议为 TCP

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_ezdata_async_get_value.svg">

```python
 lan.get_ezdata(ezdata_get_fOkSZcb, 'GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 从指定的主题获取值，并使用提供的 token 进行验证

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_ezdata_remove.svg">

```python
lan.remove_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 删除与指定主题相关的数据，使用 token 进行验证

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_ezdata_save.svg">

```python
lan.set_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '', '', 0)
```

- 保存一个值到指定的主题，同样使用 token 进行验证，并可以选择保存的模式(如 Single)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_get_data.svg">

```python
req.text
```

- 从局域网中获取数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_get_if_config.svg">

```python
lan.get_if_config()
```

- 检查配置是否存在或获取当前配置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_get_status_code.svg">

```python
req.status_code
```

- 获取状态码，返回一个整数值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_http_request.svg">

```python
try:
    req = lan.http_request(method='GET', url='', headers={})
    gc.collect()
    req.close()
  except:
    pass
```

- Method：指定 HTTP 请求的方法，如 GET。
- URL：要请求的 URL 地址。
- Headers：可以通过创建一个映射来设置请求的头信息。
- Data：通过映射发送数据。
- Success 和 Fail：请求成功或失败后的回调操作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_init.svg">

```python
lan.tcp_udp_config('', 0, 1, 1)
```

- remote IP：远程设备的 IP 地址。
- port：通信端口。
- socket type：选择通信协议类型(TCP 或 UDP)。
- machine type：指定是服务器还是客户端

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_local_ip.svg">

```python
lan.local_ip()
```

- 获取本地设备的 IP 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_init.svg">

```python
lan.modbus_init(15, 5, 115200, 1, 1)
```

- bandrate：设置波特率，这里为115200。
- mode：选择主设备或从设备模式。
- slave addr：设置从设备的地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_master_u_read_coils.svg">

```python
modbus.read_coils(1, 1, 0)
```

- slave address：读取从设备的地址。
- starting address：开始读取的寄存器地址。
- coil qty：读取的线圈数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_master_u_read_discrete_inputs.svg">

```python
modbus.read_discrete_inputs(1, 1, 0)
```

- 从从设备的离散输入寄存器中读取数据。
    - slave address：从设备的地址。
    - starting address：开始读取的寄存器地址。
    - input qty：读取的输入数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_master_u_read_holding_registers.svg">

```python
modbus.read_holding_registers(1, 1, 0, True)
```

- 从从设备的保持寄存器中读取数据。
    - slave address：从设备的地址。
    - starting address：开始读取的寄存器地址。
    - register qty：读取的寄存器数量。
    - signed：指定数据是否为有符号数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_master_u_read_input_registers.svg">

```python
modbus.read_input_registers(1, 1, 0, True)
```

- 从设备的输入寄存器中读取数据。
    - slave address：从设备的地址。
    - starting address：开始读取的寄存器地址。
    - register qty：读取的寄存器数量。
    - signed：指定数据是否为有符号数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_master_u_write_multiple_coils.svg">

```python
modbus.write_multiple_coils(1, 1, 0)
```

- 向从设备的多个线圈寄存器写入数据。
    - slave address：从设备的地址。
    - starting address：开始写入的寄存器地址。
    - output value：写入的输出值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_master_u_write_multiple_registers.svg">

```python
modbus.write_multiple_registers(1, 1, 0, True)
```

- 向从设备的多个保持寄存器写入数据。
    - slave address：从设备的地址。
    - starting address：开始写入的寄存器地址。
    - register value：写入的寄存器值。
    - signed：指定数据是否为有符号数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_master_u_write_single_coil.svg">

```python
modbus.write_single_coil(1, 1, 0)
```

- 向从设备的单个线圈寄存器写入数据。
    - slave address：从设备的地址。
    - output address：线圈寄存器的地址。
    - output value：要写入的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_master_u_write_single_register.svg">

```python
modbus.write_single_register(1, 1, 0, True)
```

- 向从设备的单个保持寄存器写入数据。
    - slave address：从设备的地址。
    - register address：寄存器的地址。
    - register value：要写入的寄存器值。  
    - signed：数据是否为有符号数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_slave_rtu_fun_status.svg">

```python
lan.modbus_init(15, 5, 115200, 1, 1)
```

- 设置功能码，用于指定 Modbus 命令。
    - READ_COILS_STATUS：读取线圈状态的功能码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_slave_rtu_get_address.svg">

```python
modbus.find_address
```

- 获取从设备的地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_slave_rtu_get_function.svg">

```python
modbus.find_function
```

- 获取当前的功能码


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_slave_rtu_get_quantity.svg">

```python
modbus.find_quantity
```

- 获取数据量。用于查询读取/写入的寄存器数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_slave_rtu_init_func.svg">

```python
modbus.function_init(1, 0, 0)
```

- 初始化功能码和相关参数。
    - READ_COILS_STATUS：读取线圈状态的功能码。
    - start addr：开始地址。
    - quantity：读取或操作的线圈数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_slave_rtu_receive_adu.svg">

```python
modbus.receive_req_create_pdu()
```

- 接收 ADU(Application Data Unit)请求，Modbus 主机与从机之间的数据交换使用 ADU 来传输

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_slave_rtu_send.svg">

```python
modbus.create_slave_response(1)
```

- 发送 ADU 响应数据，提供给 Modbus 主机响应数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_modbus_slave_rtu_update_func.svg">

```python
modbus.update_process(1, 0, 0, [0, 0, 0])
```

- 更新功能的数据信息。
    - start addr：要操作的开始地址。
    - quantity：更新的数据数量。
    - value：实际要更新的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_mqtt_check_connection.svg">

```python
lan.mqtt_is_connect()
```

- 检查与 MQTT 服务器的连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_mqtt_connect.svg">

```python
lan.mqtt_connect()
```

- 连接到 MQTT 服务器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_mqtt_disconnect.svg">

```python
lan.mqtt_disconnect()
```

- 从 MQTT 服务器断开连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_mqtt_init.svg">

```python
lan.mqtt_config('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 初始化
  - mqtt.m5stack.com：服务器地址。
  - port 1883：通讯端口。
  - client id：客户端标识符。
  - username：用户名。
  - password：密码。
  - keepalive 120：保持连接的心跳时间(秒)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_mqtt_poll.svg">

```python
  lan.mqtt_poll_loop()
```

- 用于轮询从 MQTT 服务器接收的下行消息，即检查是否有新的消息从服务器传送到设备端

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_mqtt_publish.svg">

```python
lan.mqtt_publish('', '', 0)
```

- 用于发布消息到指定的主题。设备可以通过该语句向其他订阅了相同主题的设备发送消息
  - topic：发布消息的主题。
  - payload：要发送的消息内容。
  - QoS：服务质量等级(通常0表示消息最多发送一次，不要求确认)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_mqtt_sub.svg">

```python
lan.mqtt_subscribe('', lan_base_mqtt_cb, 0)
```

- 用于订阅某个主题，以接收该主题下发布的消息
    - topic：需要订阅的主题，订阅后设备将接收来自该主题的消息。
    - QoS：控制订阅消息的服务质量等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_mqtt_sub_cb.svg">

```python
def lan_base_mqtt_cb(lan_mq_topic, lan_mq_payload):
  global ezdata_value1, lan_topic, lan_msg
  lan_topic = lan_mq_topic
  lan_msg = lan_mq_payload
  pass
```

- 当设备接收到订阅主题的消息时，该语句会触发回调函数，并显示接收到的主题和消息内容。
    - lan_topic：接收到的消息所属的主题。
    - lan_msg：接收到的消息内容

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_remote_ip.svg">

```python
lan.remote_ip()
```

- 设置远程服务器的 IP 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_set_ifconfig.svg">

```python
lan.set_if_config('192.168.1.100', '255.255.255.0', '192.168.1.1', '8.8.8.8')
```

- 配置设备的 IP 地址、子网掩码、网关和 DNS 信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_socket_close.svg">

```python
lan.socket_close()
```

- 关闭当前的 TCP 或 UDP 连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_tcp_receive_packet.svg">

```python
lan.tcp_receive_packet(0)
```

- 设置 TCP 接收数据包的大小

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_tcp_send_packet.svg">

```python
 lan.tcp_send_packet('1234')
```

- 发送指定的数据包内容通过 TCP 协议

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_uart_any.svg">

```python
modbus._mdbus_uart.any()
```

- 检查并保留 UART 缓存中的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_uart_read.svg">

```python
modbus._mdbus_uart.read()
```

- 读取 UART 缓存中的所有数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_uart_readline.svg">

```python
modbus._mdbus_uart.readline()
```

- 读取 UART 缓存中的一整行数据，直到遇到换行符为止

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_uart_read_characters.svg">

```python
modbus._mdbus_uart.read(10)
```

- 读取指定数量的字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_uart_write.svg">

```python
modbus._mdbus_uart.write('')
```

- 通过 UART 发送指定的字符串数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_uart_write_line.svg">

```python
modbus._mdbus_uart.write(''+"\r\n")
```

- 通过 UART 发送一行字符串数据，通常会在末尾附加换行符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_uart_write_raw_data.svg">

```python
modbus._mdbus_uart.write(bytes([0, 0, 0]))
```

- 通过 UART 发送一个原始数据列表，通常用于传输二进制数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_udp_receive_packet.svg">

```python
lan.udp_receive_packet(0)
```

- 设置接收 UDP 数据包的大小

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan_base/uiflow_block_lan_base_udp_send_packet.svg">

```python
lan.udp_send_packet('', 0, '')
```

- 通过指定的 IP 地址、端口号和有效载荷发送 UDP 数据包

