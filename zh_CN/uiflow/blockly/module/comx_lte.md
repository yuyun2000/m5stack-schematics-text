# [Module COMX LTE](/zh_CN/module/comx_lte)

## 案例程序

### HTTP GET

初始化 LTE 模块的 TX 和 RX 引脚。<br/>打印模块状态、信号质量、网络注册状态和 GPRS 网络注册状态。<br/>在主循环中检查 GPRS 网络注册状态，如果注册成功，则执行 HTTP GET 请求访问 [http://www.m2msupport.net/m2msupport/test.php](http://www.m2msupport.net/m2msupport/test.php)，并从响应中获取数据并打印结果

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_com_lte_demo.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
from comx.lte import LTE

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

resp = None

lte = LTE(tx=13, rx=5)
print(lte.check_status())
print(lte.get_single_quality())
print(lte.get_network_registration())
print(lte.get_gprs_network_registration())
while True:
  if str((lte.get_gprs_network_registration())) == '1':
    # echo "test"
    resp = lte.http_get('http://www.m2msupport.net/m2msupport/test.php')
    if resp:
      print(resp[1])
  wait_ms(2)

```


### HTTP POST

初始化 LTE 模块的 TX 和 RX 引脚。<br/>打印模块状态、信号质量、网络注册状态和 GPRS 网络注册状态。<br/>在主循环中检查 GPRS 网络注册状态，如果注册成功，创建一个包含随机整数的字典，将其转换为 JSON 格式后，通过 HTTP POST 请求发送到 http://httpbin.org/post，然后解析响应并从中提取数据并打印结果

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_com_lte_demo_post.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
from comx.lte import LTE
import json

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

resp = None
post_data = None

import random

lte = LTE(tx=13, rx=5)
print(lte.check_status())
print(lte.get_single_quality())
print(lte.get_network_registration())
print(lte.get_gprs_network_registration())
while True:
  if str((lte.get_gprs_network_registration())) == '1':
    post_data = {'random1':random.randint(0, 100)}
    resp = lte.http_post('http://httpbin.org/post', 'application/json', str((json.dumps(post_data))))
    if resp:
      print((json.loads(resp[1]))['data'])
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_check_gprs_network_registration.svg">

```python
lte.get_gprs_network_registration()
```

- 检查设备是否已注册到 GPRS 网络。这通常用于确定设备是否已成功连接到 GPRS 网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_check_network_registration.svg">

```python
lte.get_network_registration()
```

- 检查设备是否已注册到移动网络。这用于验证设备是否已连接到任何可用的移动网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_check_single_quality.svg">

```python
lte.get_single_quality()
```

- 检查当前网络信号的质量。返回信号强度的数值，这对于评估网络连接的稳定性非常重要

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_check_status.svg">

```python
lte.check_status()
```

- 检查模块的状态。这个命令用于获取设备的运行状态，例如是否正常工作，是否有错误等

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_enable_pdp_context.svg">

```python
lte.enable_PDP_context()
```

- 启用 PDP(分组数据协议)上下文。这是用于激活数据连接的必要步骤，使设备能够通过移动网络发送和接收数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_http_get.svg">

```python
lte.http_get('')
```

- 发起一个 HTTP(S) GET 请求，向指定的 URL 获取数据。常用于从服务器获取信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_http_post.svg">

```python
lte.http_post('', 'application/json', '')
```

- 发起一个 HTTP(S) POST 请求，向指定的 URL 发送数据。数据可以是 JSON 格式或其他类型，用于上传数据到服务器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_http_terminate.svg">

```python
lte.http_terminate()
```

- 终止当前的 HTTP(S)连接。用于关闭已建立的 HTTP(S)连接，以释放资源或结束会话

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_init.svg">

```python
LTE(tx=13, rx=5)
```

- 初始化 LTE 模块，设置串口 TX 和 RX 引脚。此操作用于准备 LTE 模块进行通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_power_down_module.svg">

```python
lte.poweroff()
```

- 关闭模块电源。这会将模块置于低功耗模式或完全关闭，以节省电力

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_reset_module.svg">

```python
lte.reset()
```

- 重置模块。这会使模块重新启动并恢复到初始状态，用于清除故障或重新配置模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_lte/uiflow_block_comlte_set_echo_mode.svg">

```python
lte.set_command_echo_mode(0)
```

- 设置命令回显模式。选择 OFF 将关闭命令回显，这意味着模块将不再回显接收到的 AT 命令。这通常用于减少通信中的冗余信息

