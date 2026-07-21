# [Unit CO2](/zh_CN/unit/co2)

## 案例程序

> 获取 Unit CO2 采集的大气 CO2 浓度，温度，湿度，大气压强数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
co2_0 = unit.get(unit.CO2_SCD40, unit.PORTA)

co2_0.stop_periodic_measurement()
print(co2_0.serial_number())
print(co2_0.get_calibration_enabled())
co2_0.start_periodic_measurement()
wait(1)
while True:
  if co2_0.data_isready():
    co2_0.read_sensor_measurement()
    print((str('data status:') + str((co2_0.data_isready()))))
    print((str('CO2:') + str((co2_0.co2))))
    print((str('Temperature:') + str((co2_0.temperature))))
    wait_ms(25)
  wait_ms(2)
```

## 功能说明

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_stop_periodic_measurement.svg" >

```python
co2_0.stop_periodic_measurement()
```

- 停止定期测量

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_factory_reset.svg" >

```python
co2_0.factory_reset()
```

- 执行出厂复位

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_force_calibration.svg" >

```python
co2_0.force_calibration(400)
```

- 执行强制重新校准 CO2

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_get_calibration_enabled.svg" >

```python
print(co2_0.get_calibration_enabled())
```

- 获取是否启用自动校准

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_get_data_ready_status.svg" >

```python
print(co2_0.data_isready())
```

- 获取数据准备的状态

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_get_sensor_altitude.svg" >

```python
print(co2_0.get_sensor_altitude())
```

- 获取传感器高度

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_get_sensor_measurement.svg" >

```python
co2_0.read_sensor_measurement()
```

- 等待更新传感器测量

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_get_serial_number.svg" >

```python
print(co2_0.serial_number())
```

- 获取传感器序列号

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_get_temperature_offset.svg" >

```python
print(co2_0.get_temperature_offset())
```

- 获得温度偏移量

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_persist_setting.svg" >

```python
co2_0.persist_settings()
```

- 所有设置保存在 EEPROM 中

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_power_down.svg" >

```python
co2_0.sleep_mode()
```

- 设置传感器为休眠模式

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_read_parameter.svg" >

```python
print(co2_0.co2)
```

- 获取 co2/湿度/温度值

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_reinit.svg" >

```python
co2_0.reinit()
```

- 重新初始化传感器

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_self_test.svg" >

```python
co2_0.self_test()
```

- 进行自检测试

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_set_ambient_pressure.svg" >

```python
co2_0.set_ambient_pressure(0)
```

- 设置周围环境空气压力

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_set_auto_calibration.svg" >

```python
co2_0.set_calibration_enabled(1)
```

- 设置是否自动校准传感器

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_set_sensor_altitude.svg" >

```python
co2_0.set_sensor_altitude(0)
```

- 设置传感器放置距离地面的高度(标记)

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_set_temperature_offset.svg" >

```python
co2_0.set_temperature_offset(4)
```

- 设定温度偏移

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_start_low_periodic_measurement.svg" >

```python
co2_0.start_low_periodic_measurement()
```

- 开始低周期测量(30 秒获取一次数值)

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_start_periodic_measurement.svg" >

```python
co2_0.start_periodic_measurement()
```

- 启动设备测量

<img  class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/co2/uiflow_block_unit_co2_wake_up.svg" >

```python
co2_0.wake_up()
```

- 唤醒传感器
