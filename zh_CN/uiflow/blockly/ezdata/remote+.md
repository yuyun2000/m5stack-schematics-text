# Remote+

\#> 简介 | 通过 Remote + 功能创建一个由控件组成的网页，可用于远程控制 M5Stack 设备。该功能相对于旧版 Remote 提供了更多的功能控件， 并且支持 Ezdata 数据联动， 功能更加强大。该页面与设备的 API KEY 相关联，将长期保存在 M5 服务中，并提供固定的访问链接，用户可随时随地访问与分享设备信息或远程操控设备。<br/>**注意：<br/>1. 该功能需使用在线版 UiFlow<br/>2. 离线下载运行时，需添加 WiFi 连接程序至 setup. [查看 WiFi 连接程序说明](/zh_CN/uiflow/blockly/hardwares/network)<br/>3. 使用前需先推送程序，然后才可以获取访问页面的二维码 / URL**

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
remoteInit()

setScreenColor(0x222222)

switch_value = None
slider_value = None
stepper_value = None
rp_label1_data = None

from numbers import Number

def button_1_callback():
  global rp_label1_data, switch_value, slider_value, stepper_value
  print('Button Press')

def switch_1_callback(switch_value):
  global rp_label1_data, slider_value, stepper_value
  print(switch_value)

def slider_1_callback(slider_value):
  global rp_label1_data, switch_value, stepper_value
  print(slider_value)

def stepper_1_callback(stepper_value):
  global rp_label1_data, switch_value, slider_value
  print(stepper_value)

def label_1_callback():
  global rp_label1_data, switch_value, slider_value, stepper_value
  return rp_label1_data
lcd.qrcode('https://flow.m5stack.com/remote?id=undefined', 72, 32, 176)
rp_label1_data = 0
while True:
  rp_label1_data = (rp_label1_data if isinstance(rp_label1_data, Number) else 0) + 1
  wait(1)
  wait_ms(2)
```

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_example_monitor_01.jpg">

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_example_monitor_02.jpg">

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remoteplus_set_qrcode.svg">

```python
lcd.qrcode('https://flow.m5stack.com/remote?id=undefined', 72, 32, 176)
```

- 设置生成网页的二维码显示位置与大小。注： 网页首次运行后， 将自动更新代码中 URL 的 remote 参数，因此该 API 需先通过 UiFlow 在线模式运行一次。

- 在程序块菜单中， 点击 Remote + 功能，在页面的右侧将出现预览窗口用于添加控件，用户可以通过拖拽的方式，往页面空白处添加控件。在配置好所有控件且完成程序推送后，点击预览窗口上方的二维码能够获取控制页面链接。

## Button

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_button.svg">

```python
def button_1_callback():
  pass
```

- 添加一个触控按键到控制页面中， 每添加一个按键，在编程区域将自动生成一个对应的 Callback 函数， 按下按键后将触发执行函数的内容。

| 控件属性   | 描述                             |
| ---------- | -------------------------------- |
| Name       | 控件标题                         |
| Show Title | 是否显示控件标题 True/False      |
| Color      | Title 字体颜色                   |
| Background | Title 背景颜色                   |
| Edges      | 按键边缘样式， sharp/Pill        |
| Style      | 设置按键填充样式。 Outline/Solid |

## Switch

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_switch.svg">

```python
def switch_1_callback(switch_value):
  print(switch_value)
```

- 添加一个切换开关到控制页面中， 每添加一个切换开关，在编程区域将自动生成一个对应的 Callback 函数， 开关动作时将触发执行函数的内容，并通过变量`switch_value`传递开关状态。开关动作时将触发执行函数的内容，并通过变量`switch_value`传递开关状态。switch_value: 1 (ON)/0 (OFF)

| 控件属性       | 描述                        |
| -------------- | --------------------------- |
| Name           | 控件标题                    |
| Show Title     | 是否显示控件标题 True/False |
| Off Label      | 关闭状态标识                |
| On Label       | 打开状态标识                |
| Off Color      | 关闭状态字体颜色            |
| On Color       | 打开状态字体颜色            |
| Off Background | 关闭状态背景颜色            |
| On Background  | 打开状态背景颜色            |

## Slider

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_slider.svg">

```python
def slider_1_callback(slider_value):
  print(slider_value)
```

- 添加一个滑动条到控制页面中， 每添加一个滑动条，在编程区域将自动生成一个对应的 Callback 函数， 滑动条动作时将触发执行函数的内容，并通过变量`slider_value`传递开关状态。滑动条动作时将触发执行函数的内容，并通过变量`slider_value`传递滑动条位置状态。slider_value: 可通过控件属性配置数值范围。

| 控件属性   | 描述                              |
| ---------- | --------------------------------- |
| Name       | 控件标题                          |
| Show Title | 是否显示控件标题 True/False       |
| Show Value | 是否显示当前滑动条数值 True/False |
| Color      | 滑动条颜色                        |
| Min Value  | 滑动条范围最小值                  |
| Max Value  | 滑动条范围最大值                  |

## Stepper

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_stepper.svg">

```python

def stepper_1_callback(stepper_value):
  print(stepper_value)
```

- 添加一个 Stepper 到控制页面中， 每添加一个滑动条，在编程区域将自动生成一个对应的 Callback 函数， Stepper 动作时将触发执行函数的内容，并通过变量`stepper_value`传递当前数值状态。

| 控件属性   | 描述                        |
| ---------- | --------------------------- |
| Name       | 控件标题                    |
| Show Title | 是否显示控件标题 True/False |
| Min Value  | Stepper 范围最小值          |
| Max Value  | Stepper 范围最大值          |
| Step       | 设置每次点击的 Step 值      |

## Label

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_label.svg">

```python
def label_1_callback():
  global rp_label1_data
  return rp_label1_data
```

- 添加一个显示标签到控制页面中， 每添加一个显示标签，在编程区域将自动生成一个对应的 Event 定时器函数， 设备程序运行时将自动按照指定间隔时间上传数据内容 (默认间隔为 3000ms)，上传的内容将自动更新显示到页面控件上。

| 控件属性      | 描述                        |
| ------------- | --------------------------- |
| Name          | 控件标题                    |
| Show Title    | 是否显示控件标题 True/False |
| Font Size     | 文本字体大小                |
| Color         | 数据文本显示颜色            |
| Interval (ms) | 数据上报间隔时间 /ms        |

## Joystick

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_joystick.svg">

```python
def joystick_1_callback(joystick_x_value, joystick_y_value):
  print(joystick_y_value)
  print(joystick_x_value)
```

- 添加一个摇杆控件到控制页面中， 每添加一个摇杆控件，在编程区域将自动生成一个对应的 Callback 函数， 摇杆控件移动时将触发执行函数的内容，并通过变量`joystick_x_value`和`joystick_y_value`传递当前摇杆状态。

| 控件属性    | 描述                                    |
| ----------- | --------------------------------------- |
| Name        | 控件标题                                |
| Show Title  | 是否显示控件标题 True/False             |
| Color       | 摇杆颜色                                |
| Auto Return | 释放摇杆时，是否自动回到原点 True/False |
| X Min       | X 轴最小位置数值                        |
| X Max       | X 轴最大位置数值                        |
| Y Min       | Y 轴最小位置数值                        |
| Y Max       | Y 轴最大位置数值                        |

## Input

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_input.svg">

```python
def input_1_callback(input_value):
  print(input_value)
```

- 添加一个输入文本框到控制页面中， 每添加一个输入文本框，在编程区域将自动生成一个对应的 Callback 函数， 输入框文本变动时将触发执行函数的内容，并通过变量`input_value`传递输入文本。

| 控件属性        | 描述                        |
| --------------- | --------------------------- |
| Name            | 控件标题                    |
| Show Title      | 是否显示控件标题 True/False |
| Font Size       | 文本字体大小                |
| Color           | 数据文本显示颜色            |
| Hint            | 输入文本提示                |
| Character Limit | 输入字符长度限制，默认为 8  |

## Image

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_image.svg">

```python
def image_1_callback():
  global rp_img1_url
  return rp_img1_url
```

- 添加一个图像控件到控制页面中， 访问控制页面时候，页面将按照指定间隔时间向指定 URL 获取图片数据 (默认间隔为 3000ms)，并更新显示到页面控件上。

| 控件属性      | 描述                        |
| ------------- | --------------------------- |
| Name          | 控件标题                    |
| Show Title    | 是否显示控件标题 True/False |
| Interval (ms) | 数据上报间隔时间 /ms        |
| Fallback URL  | 请求的图像的 URL            |

## Gauge

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/remote_plus/uiflow_block_remote_plus_gauge.svg">

```python
def gauge_1_callback():
  global rp_gauge1_data
  return rp_gauge1_data
```

- 添加一个仪表盘到控制页面中， 每添加一个仪表盘，在编程区域将自动生成一个对应的 Event 定时器函数， 设备程序运行时将自动按照指定间隔时间上传数据内容 (默认间隔为 3000ms)，上传的内容将自动更新显示到页面控件上。

| 控件属性      | 描述                        |
| ------------- | --------------------------- |
| Name          | 控件标题                    |
| Show Title    | 是否显示控件标题 True/False |
| Label         | 仪表盘标题                  |
| Color         | 仪表盘显示颜色              |
| Suffix        | 仪表盘数据后缀              |
| Min Value     | 仪表盘量程最小值            |
| Max Value     | 仪表盘量程最大值            |
| Interval (ms) | 数据上报间隔时间 /ms        |

## Chart

添加一个图表到控制页面中， 该图标需通过[Ezdata 功能](/zh_CN/uiflow/blockly/ezdata/ezdata)指定数据来源，支持配置图表刷新间隔与基本样式。

\#> 注意事项：|[1. 使用前请点击此处，了解 Ezdata 的基本使用](/zh_CN/uiflow/blockly/ezdata/ezdata)<br/>2. Ezdata 结合 Chart 使用， 需使用到的数据保存方式`是 List`，`不是 Topic`<br/>3. 传递数据时候需要使用`map`(字典) 传递`key-value`形式的数据。其中 key 需要对应 chart 控件中的 X，Y Data Source 字段， 如留空会造成数据无法显示。

| 控件属性            | 描述                                                                               |
| ------------------- | ---------------------------------------------------------------------------------- |
| Name                | 控件标题                                                                           |
| Show Title          | 是否显示控件标题 True/False                                                        |
| Theme               | 设置图表主题 Light/Dark                                                            |
| Color               | 设置图表元素颜色                                                                   |
| Chart Type          | 设置图表类型， Bar/Line                                                            |
| Interval (ms)       | 设置图表刷新间隔                                                                   |
| Show Legend         | 显示图例 True/False                                                                |
| Dataset Name        | 配置数据集名称                                                                     |
| Y Axis Label Suffix | 配置 Y 轴数据后缀                                                                  |
| EzData Token        | 配置 EzData 数据源 Token                                                           |
| List                | EzData 数据源的指定 List                                                           |
| X Data Source       | 设置 List 数据中的某一字段为 X 轴内容 (通常使用时间作为数据，形成历史记录)         |
| Y Data Source       | 设置 List 数据中的某一字段为 Y 轴内容 (通常使用监测内容作为数据，形成数据变化趋势) |
| Max Count           | 当前图表最大显示数据量                                                             |
