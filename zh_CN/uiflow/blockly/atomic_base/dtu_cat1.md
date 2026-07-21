# [Atom DTU Cat1](/zh_CN/atom/atom_dtu_cat1)

## 案例程序

这个程序使用 MQTT 协议与服务器进行通信，连接后会订阅`cat_topic`主题并发布消息“hello”。当接收到来自该主题的消息时，程序会更新 RGB 灯的颜色并打印消息内容。每次接收消息后，`cat_msg`变量会被清空，并在下一次循环前等待1秒。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_atomic_base_cat1_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.DTU_CAT1 import DTU_CAT1
import time

cat_topic = None
cat_msg = None

def cat_mqtt_cb(cat_mq_topic, cat_mq_payload):
  global cat_topic, cat_msg
  cat_topic = cat_mq_topic
  cat_msg = cat_mq_payload
  rgb.setColorAll(0xffff00)
  pass

cat = DTU_CAT1()
cat.mqtt_to_connect('mqtt.m5stack.com', 1883, 'cat1_4399', 'm5', 'm5', 120)
if cat.is_connect_mqtt():
  rgb.setColorAll(0x33cc00)
  print('MQTT Connected')
if cat.mqtt_subscribe('cat_topic', cat_mqtt_cb, 0):
  print('topic subscribed')
cat.mqtt_publish('cat_topic', 'hello', 0)
while True:
  cat.mqtt_poll()
  if cat_msg != None:
    print((str(((str(((str('message from topic: ') + str(cat_topic)))) + str(' : ')))) + str(cat_msg)))
    cat_msg = None
    rgb.setColorAll(0x33cc00)
  wait(1)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_init.svg">

```python
cat = DTU_CAT1()
```

- 初始化 CAT1 DTU 模块，准备开始使用该模块进行通信。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_init.svg">

```python
modbus = cat.modbus_init(23, 33, 115200, 1, 1)
```

- 设置 Modbus 通信的波特率为 115200，模式为主机模式 (Master)，并指定从机地址为 1。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_slave_rtu_init_func.svg">

```python
modbus.function_init(1, 0, 0)
```

- 初始化 Modbus 功能代码，用于读取线圈状态。你可以指定读取的起始地址 (start addr)、读取的数量 (quantity)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_check_gprs_network_registration.svg">

```python
cat.get_gprs_network_registration()
```

- 检查 CAT1 DTU 模块是否已在 GPRS 网络中注册。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_check_network_registration.svg">

```python
cat.get_network_registration()
```

- 检查模块的网络注册状态，确认是否已注册到网络。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_check_single_quality.svg">

```python
cat.get_single_quality()
```

- 检查模块当前的信号质量，通常用于评估信号的强度和稳定性。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_check_status.svg">

```python
cat.check_status()
```

- 检查模块的当前状态，确保模块正常工作或获取故障信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_enable_pdp_context.svg">

```python
cat.enable_PDP_context()
```

- 启用 PDP(分组数据协议)上下文，用于 CAT1 DTU 模块连接移动网络并开始数据传输。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_ezdata_async_get_value.svg">

```python
cat.get_ezdata(ezdata_get_nOfcOcb, 'GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 从指定的主题获取值。该操作使用提供的 token 来检索数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_ezdata_remove.svg">

```python
cat.remove_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 删除某个主题。指定 token 来从主题中删除数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_ezdata_save.svg">

```python
cat.set_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '', '', 0)
```

- 将数据保存到指定的主题中。你可以选择数据的存储模式，如 Single(单条数据)模式，并通过 token 标识主题。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_get_ccid.svg">

```python
cat.get_CCID()
```

- 获取 SIM 卡的 CCID(集成电路卡标识)，用于识别插入的 SIM 卡。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_get_imei.svg">

```python
cat.get_IMEI()
```

- 获取 CAT1 DTU 模块设备的 IMEI(国际移动设备标识)，用于设备识别。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_http_get.svg">

```python
cat.http_get('')
```

- 发送一个 HTTP(S) GET 请求，指定目标 URL，用于从服务器获取数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_http_post.svg">

```python
cat.http_post('', 'application/json', '')
```

- 发送一个 HTTP(S) POST 请求，指定 URL 和数据类型(如 JSON)，将数据发送到服务器。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_http_terminate.svg">

```python
cat.http_terminate()
```

- 终止当前的 HTTP(S) 连接。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_master_u_read_coils.svg">

```python
modbus.read_coils(1, 1, 0)
```

- 从 Modbus 从机读取线圈状态，提供从机地址、起始地址和线圈数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_master_u_read_discrete_inputs.svg">

```python
modbus.read_discrete_inputs(1, 1, 0)
```

- 从 Modbus 从机读取离散输入信号，提供从机地址、起始地址和输入数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_master_u_read_holding_registers.svg">

```python
modbus.read_holding_registers(1, 1, 0, True)
```

- 从 Modbus 从机读取保持寄存器，提供从机地址、起始地址和寄存器数量，还可以选择寄存器数据是否为有符号数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_master_u_read_input_registers.svg">

```python
modbus.read_input_registers(1, 1, 0, True)
```

- 从 Modbus 从机读取输入寄存器，类似于读取保持寄存器，但通常用于传感器数据读取。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_master_u_write_multiple_coils.svg">

```python
modbus.write_multiple_coils(1, 1, 0)
```

- 向指定的 Modbus 从机地址写入多个线圈状态。设置从机地址、起始地址和输出值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_master_u_write_multiple_registers.svg">

```python
modbus.write_multiple_registers(1, 1, 0, True)
```

- 向指定的 Modbus 从机地址写入多个保持寄存器。设置从机地址、起始地址、寄存器值，并选择数据是否为有符号数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_master_u_write_single_coil.svg">

```python
modbus.write_single_coil(1, 1, 0)
```

- 向指定的 Modbus 从机地址写入单个线圈状态。设置从机地址、输出地址和输出值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_master_u_write_single_register.svg">

```python
modbus.write_single_register(1, 1, 0, True)
```

- 向指定的 Modbus 从机地址写入单个保持寄存器。设置从机地址、寄存器地址、寄存器值，并选择数据是否为有符号数。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_slave_rtu_fun_status.svg">

```python
1-6,15-16
```

- 初始化 Modbus 功能代码，用于读取线圈状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_slave_rtu_get_address.svg">

```python
modbus.find_address
```

- 获取当前通信的 Modbus 从机地址。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_slave_rtu_get_function.svg">

```python
modbus.find_function
```

- 获取当前正在使用的 Modbus 功能代码。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_slave_rtu_get_quantity.svg">

```python
modbus.find_quantity
```

- 获取 Modbus 请求中读取的数据数量。通常与线圈或寄存器数量有关。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_slave_rtu_receive_adu.svg">

```python
modbus.receive_req_create_pdu()
```

- 接收 Modbus RTU 的应用数据单元(ADU)请求。这是从 Modbus 主设备接收到的数据帧。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_slave_rtu_send.svg">

```python
modbus.create_slave_response(1)
```

- 将 ADU 数据响应发送回 Modbus 主设备。这里发送了数值 1 作为响应。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_modbus_slave_rtu_update_func.svg">

```python
modbus.update_process(1, 0, 0, [0, 0, 0])
```

- 更新 Modbus 功能代码的执行结果。此功能是用于读取线圈状态的操作，指定了起始地址、数量、值，并用列表形式创建了一个新的数据值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_mqtt_check_connect.svg">

```python
cat.is_connect_mqtt()
```

- 检查 MQTT 连接状态，确保与 MQTT 服务器的连接正常。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_mqtt_connect.svg">

```python
cat.mqtt_to_connect('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 初始化与 MQTT 服务器的连接，服务器地址为 mqtt.m5stack.com，端口为 1883。此处需要填写 client id、username 和 password 来进行验证。keepalive 设置为 120 秒，表示保持连接的心跳时间间隔。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_mqtt_disconnect.svg">

```python
cat.mqtt_disconnect()
```

- 断开与 MQTT 服务器的连接。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_mqtt_poll.svg">

```python
cat.mqtt_poll()
```

- 轮询 MQTT 服务器是否有下行消息到达客户端。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_mqtt_publish.svg">

```python
cat.mqtt_publish('', '', 0)
```

- 向指定的 MQTT 主题发布消息。需要填写发布的 topic(主题)、payload(负载数据)以及 QoS(服务质量级别，默认为 0)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_mqtt_sub.svg">

```python
cat.mqtt_subscribe('', cat_mqtt_cb, 0)
```

- 订阅指定的 MQTT 主题，需要提供 topic(主题名)和 QoS(服务质量级别)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_mqtt_sub_cb.svg">

```python
def cat_mqtt_cb(cat_mq_topic, cat_mq_payload):
  global ezdata_value1, cat_topic, cat_msg
  cat_topic = cat_mq_topic
  cat_msg = cat_mq_payload
  pass
```

- 为已订阅的 MQTT 主题设置回调函数，当接收到指定 topic 的消息时，触发相应的 msg(消息处理逻辑)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_mqtt_unsubscribe.svg">

```python
cat.mqtt_unsubscribe('')
```

- 取消订阅指定的 MQTT 主题。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_power_down_module.svg">

```python
cat.poweroff()
```

- 关闭模块电源，进入低功耗模式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_reset_module.svg">

```python
cat.reset()
```

- 重置模块，重新启动模块。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_set_echo_mode.svg">

```python
cat.set_command_echo_mode(0)
```

- 设置命令回显模式，可以选择打开或关闭(OFF)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_uart_any.svg">

```python
modbus._mdbus_uart.any()
```

- 读取 UART 缓存，检查是否有可读取的数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_uart_read.svg">

```python
modbus._mdbus_uart.read()
```

- 从 UART 中读取所有可用的数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_uart_readline.svg">

```python
modbus._mdbus_uart.readline()
```

- 从 UART 中按行读取数据，直到读取到换行符为止。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_uart_read_characters.svg">

```python
modbus._mdbus_uart.read(10)
```

- 从 UART 中读取指定数量的字符，这里设置为读取 10 个字符。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_uart_write.svg">

```python
modbus._mdbus_uart.write('')
```

- 通过 UART 发送指定的数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_uart_write_line.svg">

```python
modbus._mdbus_uart.write(''+"\r\n")
```

- 将一整行数据写入 UART，通常以换行符结尾，适合发送字符串数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/dtu_cat1/uiflow_block_dtu_cat1_uart_write_raw_data.svg">

```python
modbus._mdbus_uart.write(bytes([0, 0, 0]))
```

- 将原始数据以字节列表的形式写入 UART，适合发送二进制数据或非字符串格式的数据。

