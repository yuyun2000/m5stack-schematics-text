# [Module13.2 Stepmotor Driver](/zh_CN/module/stepmotor_driver)

## 案例程序

初始化步进电机的 I2C 地址和频率设置，设置电机 X 和电机 Y 的方向，读取设备的固件版本和 I2C 地址然后在循环中执行重置电机 X 和 Y、启用/禁用电机，并在一定时间间隔内进行状态的切换

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x000000)

stepmotor = module.get(module.STEPMOTORDRIVER)

stepmotor.initDevice(0x27)
stepmotor.setStepPulse(500, 0)
stepmotor.setStepPulse(500, 1)
stepmotor.setStepPulse(500, 2)
stepmotor.setStepDir(0, 1)
stepmotor.setStepDir(1, 1)
stepmotor.enableMotor(1)
print(stepmotor.readStatus(0XFE))
print(stepmotor.readStatus(0XFF))
while True:
  stepmotor.resetMotor(0, 1)
  wait(2)
  stepmotor.resetMotor(1, 1)
  wait(2)
  stepmotor.enableMotor(0)
  wait(2)
  stepmotor.enableMotor(1)
  wait(2)
  stepmotor.resetMotor(0, 0)
  wait(2)
  stepmotor.resetMotor(1, 0)
  wait(2)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_enable_motor.svg">

```python
stepmotor.enableMotor(0)
```

- 禁用所有步进电机的运行状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_init.svg">

```python
stepmotor.initDevice(0x27)
```

- 初始化步进电机驱动器的 I2C 地址为0x27

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_modbus_init.svg">

```python
stepmotor.modbus_init(26, 34, 115200, 1, 1)
```

- 初始化步进电机驱动器的通信其具体参数如下：
    - Tx 26：指定用于发送数据的引脚编号
    - Rx 34：指定用于接收数据的引脚编号
    - baudrate 115200：设定 Modbus 通信的波特率为115200bps
    - mode Master：设置通信模式为主模式
    - slave addr 1：指定从设备的地址为1

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_read_device_status.svg">

```python
stepmotor.readStatus(0XFE)
```

- 读取步进电机驱动器的固件版本号(Firmware Version)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_read_fault_status.svg">

```python
stepmotor.readFaultPinStatus(0)
```

- 读取指定电机(如电机 X)的故障状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_read_io_status.svg">

```python
stepmotor.readIOstatus()
```

- 读取所有限位开关的输入输出(IO)状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_read_pin_status.svg">

```python
stepmotor.readPinStatus(0)
```

- 读取特定限位开关(如 IO 0)的状态，判断该限位开关是否被触发

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_reset.svg">

```python
stepmotor.resetMotor(0, 1)
```

- 复位电机 X，并将其状态设为 TRUE

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_set_i2c.svg">

```python
stepmotor.setI2cAddress(0x27)
```

- 为步进电机驱动器设定 I2C 通信地址为0x27

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_set_micro_stepselect.svg">

```python
stepmotor.setMicroStepSelect(0)
```

- 将步进电机的微步模式设置为“全步”模式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_set_single_motor.svg">

```python
stepmotor.singleMotorCtrl(0, 0)
```

- 将单个电机 X 的状态设置为暂停(Pause)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_set_step_dir.svg">

```python
stepmotor.setStepDir(0, 0)
```

- 设置电机 X 的运行方向为“反向”(Reverse)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_driver_set_step_pulse2.svg">

```python
stepmotor.setStepPulse(500, 0)
```

- 将电机 X 的脉冲频率设置为500Hz

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_master_u_read_coils.svg">

```python
modbus.read_coils(1, 1, 0)
```

- 读取从设备地址为1的线圈状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_master_u_read_discrete_inputs.svg">

```python
modbus.read_discrete_inputs(1, 1, 0)
```

- 从 Modbus 从设备地址1开始读取离散输入

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_master_u_read_holding_registers.svg">

```python
modbus.read_holding_registers(1, 1, 0, True)
```

- 从设备地址1读取保持寄存器、

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_master_u_read_input_registers.svg">

```python
modbus.read_input_registers(1, 1, 0, True)
```

- 从 Modbus 从设备地址1读取输入寄存器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_master_u_write_multiple_coils.svg">

```python
modbus.write_multiple_coils(1, 1, 0)
```

- 向从设备地址1的多个线圈写入输出值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_master_u_write_multiple_registers.svg">

```python
modbus.write_multiple_registers(1, 1, 0, True)
```

- 向从设备地址1的多个寄存器写入值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_master_u_write_single_coil.svg">

```python
modbus.write_single_coil(1, 1, 0)
```

- 向从设备地址1的单个线圈写入值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_master_u_write_single_register.svg">

```python
modbus.write_single_register(1, 1, 0, True)
```

- 向从设备地址1的单个寄存器写入值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_slave_rtu_fun_status.svg">

```python
print((str('code:') + str((1))))
```

- 定义 Modbus 通信中使用的功能码，此处设置为 READ_COILS_STATUS，表示读取线圈状态
    - READ_COILS_STATUS：读取线圈状态
    - READ_INPUT_STATUS：读取输入状态
    - READ_HOLDING_REGISTERS：读取保持寄存器
    - READ_INPUT_REGISTERS：读取输入寄存器
    - WRITE_SINGLE_COIL：写入单个线圈
    - WRITE_SINGLE_REGISTER：写入单个保持寄存器
    - WRITE_MULTIPLE_COILS：写入多个线圈
    - WRITE_MULTIPLE_REGISTERS：写入多个保持寄存器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_slave_rtu_get_address.svg">

```python
modbus.find_address
```

- 获取 Modbus 从设备的地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_slave_rtu_get_function.svg">

```python
modbus.find_function
```

- 获取当前 Modbus 请求中所使用的功能码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_slave_rtu_get_quantity.svg">

```python
modbus.find_quantity
```

- 获取要读取或写入的寄存器或线圈的数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_slave_rtu_init_func.svg">

```python
modbus.function_init(1, 0, 0)
```

- 该语句初始化 Modbus 从设备的功能码操作，设置起始地址为0

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_slave_rtu_receive_adu.svg">

```python
modbus.receive_req_create_pdu()
```

- 接收应用数据单元(ADU)请求，这是 Modbus 协议传输的数据帧

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_slave_rtu_send.svg">

```python
modbus.create_slave_response(0)
```

- 发送 ADU 响应，其中包含 Modbus 从设备的响应数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_modbus_slave_rtu_update_func.svg">

```python
modbus.update_process(1, 0, 0, [0, 0, 0])
```

- 更新 Modbus 从设备功能代码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_uart_any.svg">

```python
modbus._mdbus_uart.any()
```

- 检查 UART 缓存区中是否有数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_uart_read.svg">

```python
modbus._mdbus_uart.read()
```

- 读取 UART 缓存区中的所有可用数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_uart_readline.svg">

```python
modbus._mdbus_uart.readline()
```

- 从 UART 中读取一行数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_uart_read_characters.svg">

```python
modbus._mdbus_uart.read(10)
```

- 从 UART 中读取指定数量的字符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_uart_write.svg">

```python
modbus._mdbus_uart.write('')
```

-  UART 写入数据，用于串口通信中的数据发送

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_uart_write_line.svg">

```python
modbus._mdbus_uart.write(''+"\r\n")
```

- 通过 UART 写入一行数据并自动加上换行符

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor_driver/uiflow_block_stepmotor_uart_write_raw_data.svg">

```python
modbus._mdbus_uart.write(bytes([0, 0, 0]))
```

- 通过 UART 发送原始数据

