# [Module13.2 PPS](/zh_CN/module/Module13.2-PPS)

## 案例程序

持续读取并打印输出电流、输出电压和MCU温度（通过串口）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_pps_demo.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import module

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

pps = module.get(module.PPS)

pps.init_i2c_address(0x35)
pps.setOutput(True)
pps.setOutputVoltage(5.5)
pps.setOutputCurrent(1)
while True:
  print((str('output current:') + str((pps.readOutputCurrent()))))
  print((str('output voltage:') + str((pps.readOutputVoltage()))))
  print((str('MCU temperture:') + str((pps.readMcuTemperature()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_getI2CAddress.svg">

```python
pps.getI2CAddress()
```

- 获取当前设备的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_init.svg">

```python
pps.init_i2c_address(0x35)
```

- 初始化设备的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_readDataUpdateFlag.svg">

```python
pps.readDataUpdateFlag()
```

- 获取数据更新标志，返回一个整数值。这个标志通常用于指示数据是否已更新

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_readInputVoltage.svg">

```python
pps.readInputVoltage()
```

- 获取输入电压值，单位是伏特(V)，返回一个浮点数。这个值表示当前测量的输入电压

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_readMcuTemperature.svg">

```python
pps.readMcuTemperature()
```

- 获取 MCU 的温度值，单位是摄氏度(°C)，返回一个浮点数。这个值表示当前测量的微控制器温度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_readModuleId.svg">

```python
pps.readModuleId()
```

- 获取模块的 ID，返回一个整数值。这个 ID 用于唯一标识设备或模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_readOutputCurrent.svg">

```python
pps.readOutputCurrent()
```

- 获取输出电流值，单位是安培(A)，返回一个浮点数。这个值表示当前测量的输出电流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_readOutputVoltage.svg">

```python
pps.readOutputVoltage()
```

- 获取输出电流值，单位是伏特(V)，返回一个浮点数。这个值表示当前测量的输出电压

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_readPsuRunningMode.svg">

```python
pps.readPsuRunningMode()
```

- 获取电源模块的运行模式，返回一个整数值。这通常用于指示电源模块当前的工作状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_readUID.svg">

```python
pps.readUID()
```

- 获取唯一标识符(UID)，返回一个字节数组。UID 用于唯一标识设备或模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_setI2CAddress.svg">

```python
pps.setI2CAddress()
```

- 设置设备的 I2C 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_setOutput.svg">

```python
pps.setOutput(True)
```

- 设置输出状态。这个功能通常用于控制设备的输出，如开启或关闭某个功能或模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_setOutputCurrent.svg">

```python
pps.setOutputCurrent(1)
```

- 设置输出电流，范围是0到5安培。这用于控制设备的输出电流

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/pps/uiflow_block_module_pps_setOutputVoltage.svg">

```python
pps.setOutputVoltage(5.5)
```

- 设置设备的输出电压。范围是0到30伏特，用于调整设备输出的电压值，控制供电或调节输出电压水平

