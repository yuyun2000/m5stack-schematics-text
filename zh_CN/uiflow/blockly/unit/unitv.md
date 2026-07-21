# [UnitV](/zh_CN/unit/unitv)

### 案例程序

> 检测当面画面的变化情况，判断检测区域内的物体是否存在运动。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/motion_detect/uiflow_block_v_motion_detect_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)
motion = V_0.init(V_0.MOTION)
motion.setMotionDetectThreshold(0)
motion.setDetectMode(0)
while True:
  if (motion.getMaxDiff()) >= 50:
    print('Moved')
  else:
    print('Not Move')
  wait_ms(2)
```


### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/motion_detect/uiflow_block_v_motion_detect_init.svg">

```python
import unit
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)
motion = V_0.init(V_0.MOTION)
```

- 初始化


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/motion_detect/uiflow_block_v_set_detect_threshold.svg">

```python
motion.setMotionDetectThreshold(0)
```

- 设置变化率阈值：
  - 当变化量小于该数值的像素，将不被认为发生了变化，其变化量则不纳入画面变量率中。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/motion_detect/uiflow_block_v_set_detect_mode.svg">

```python
motion.setDetectMode(0)
```

- 设置检测模式：
   - dynamic(0): 动态检测模式，配置后将不断拍摄图片，对比前后两帧之间的变化
   - static(1): 静态检测模式，执行后将拍摄并保存一张基准图片，后续的画面将不断与该图片进行对比。若需要拍摄新的基准图片，需要先切换回动态检测模式，然后再次执行静态检测模式设置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/motion_detect/uiflow_block_v_get_rate_difference.svg">

```python
motion.getRateOfDiff()
```

- 获取画面变化率：
  - 画面变化率： 检测比较前后两帧之间变化像素的变化量。假设有2个像素发生了变化，像素 A 变化了27,像素 B 变化了10,则改数值为27+10=37。将两个像素点的 R.G.B 分量的差求值和即为变化量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/motion_detect/uiflow_block_v_get_max_difference.svg">

```python
motion.getMaxDiff()
```

- 获取最高变化率：
  - 最高变化率：变化最剧烈的像素的变化量。 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/motion_detect/uiflow_block_v_motion_set_scan_interval.svg">

```python
motion.setScanInterval(0, 0)
```

- 设置在 x 轴以及 y 轴上的扫描间隔。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/motion_detect/uiflow_block_v_motion_get_track_box_number.svg">

```python
print(motion.getBoxNumber())
```

- 获取由像素变化产生的边界框数数目。 


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/motion_detect/uiflow_block_v_motion_get_track_box_detail.svg">

```python
print(motion.getBoxDetail(1))
```

- 获取 x 号边界框信息：
  - x 号边界框的详细信息以列表返回，包括该边界框内变化像素的数量，边界框 x 轴坐标，边界框 y 轴坐标，编边界框宽度，边界框高度。 
- 返回值
  - list[0] number of pixels changed
  - list[1] x
  - list[2] y
  - list[3] width
  - list[4] height


## Target Track

### 案例程序

设置追踪目标，实时获取目标对象处于画面中位置信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/target_track/uiflow_block_v_target_track_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)

target = V_0.init(V_0.TARGET_TRACK)
target.setTrackAreaCoordinate(50, 50, 30, 30)
while True:
  print((str('X :') + str(((str((target.getBoxDetail())[0]) + str(((str('Y :') + str((target.getBoxDetail())[2])))))))))
  wait(1)
  wait_ms(2)
```


### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/target_track/uiflow_block_v_target_track_init.svg">

```python
import unit
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)
target = V_0.init(V_0.TARGET_TRACK)
```

- 初始化


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/target_track/uiflow_block_v_set_track_coordinate.svg">

```python
target.setTrackAreaCoordinate(50, 50, 30, 30)
```

- 设置跟踪框坐标 x y 跟踪框， 宽， 高
  - 设置框选目标，参数为当前目标所在图像上的位置 (尽可能选取具有显著颜色特征的目标)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/target_track/uiflow_block_v_get_target_track_box_detail.svg">

```python
target.getBoxDetail()
```

- 获取跟踪框轨迹详情
  - 读取框选目标所在图像上的坐标，返回值为列表形式，其中包含选框的左上角坐标 x,y 以及选框的宽度，高度
- 返回值：
  - list[0] x
  - list[1] y
  - list[2] width
  - list[3] height


## Color Track

### 案例程序

设置 LAB 颜色阈值，追踪画面中符合阈值目标，并实时获取目标对象处于画面中位置信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/color_track/uiflow_block_v_color_track_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)

box_detail = None

color_track = V_0.init(V_0.COLOR_TRACK)
while True:
  box_detail = color_track.getBoxDetail(1)
  print((str('Box number: ') + str((color_track.getBoxNumber()))))
  print((str('Box1 pixels changed: ') + str(box_detail[0])))
  print((str('Box1 x: ') + str(box_detail[1])))
  print((str('Box1 y: ') + str(box_detail[2])))
  print((str('Box1 w: ') + str(box_detail[3])))
  print((str('Box1 h: ') + str(box_detail[4])))
  wait_ms(2)

```


### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/color_track/uiflow_block_v_color_track_init.svg">

```python
import unit
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)
color_track = V_0.init(V_0.COLOR_TRACK)
```

- 初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/color_track/uiflow_block_v_set_track_color.svg">

```python
color_track.setTrackColorByLAB(0, 0, 0, 0, 0, 0)
```

- 设置追踪的 LAB 阈值(LAB 颜色空间的颜色值，在该范围外的颜色将会被过滤)


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/color_track/uiflow_block_v_color_set_scan_interval.svg">

```python
color_track.setScanInterval(0, 0)
```

- 设置 X 轴和 y 轴上的扫描间隔，[0, 40],设置为0则关闭边界框检测。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/color_track/uiflow_block_v_set_merge_threshold.svg">

```python
color_track.setBoxMergeThreshold(0)
```

- 设置边界框合并阈值。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/color_track/uiflow_block_v_set_threshold.svg">

```python
color_track.setBoxWidthThreshold(0, 0)
```

- 设置边框宽阈值 0 高阈值 0

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/color_track/uiflow_block_v_color_get_track_box_number.svg">

```python
print(color_track.getBoxNumber())

```

- 获取边框数目

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/color_track/uiflow_block_v_color_get_track_box_detail.svg">

```python
print(color_track.getBoxDetail(1))
```

- 获取边框的详情，包括该边界框内变化像素的数量，边界框 x 轴坐标，边界框 y 轴坐标，边界框宽，边界框高。
- 返回值：
  - list[0] number of pixels changed
  - list[1] x
  - list[2] y
  - list[3] width
  - list[4] height

## Face Detect

### 案例程序

识别画面中的人脸信息，并返回识别个数，对象坐标，置信率。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/face_detect/uiflow_block_v_face_detect_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)

data_detail = None

face = V_0.init(V_0.FACE_DETECT)
while True:
  print((str('FaceNumber: ') + str((face.getFaceNumber()))))
  data_detail = face.getFaceDetail(1)
  print((str('Face1 value: ') + str(((str(("%.2f"%((data_detail[0] * 100)))) + str('%'))))))
  print((str('Face1 X: ') + str(data_detail[1])))
  print((str('Face1 Y: ') + str(data_detail[2])))
  print((str('Face1 W: ') + str(data_detail[3])))
  print((str('Face1 H: ') + str(data_detail[4])))
  wait_ms(2)

```


### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/face_detect/uiflow_block_v_face_detect_init.svg">

```python
import unit
V_0 = unit.get(unit.V_FUNCTION, unit.PORTB)
face = V_0.init(V_0.FACE_DETECT)
```

- 初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/face_detect/uiflow_block_v_get_face_number.svg">

```python
face.getFaceNumber()
```

- 读取识别到的人脸数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/face_detect/uiflow_block_v_get_face_detail.svg">

```python
face.getFaceDetail(1)
```

- 读取指定编号的人脸详情数据，返回格式为列表，其中包含人脸框选坐标，长度宽度，以及置信率
- 返回值：
  - list[0] face probability
  - list[1] x
  - list[2] y
  - list[3] width
  - list[4] height


## QR Code

### 案例程序

识别画面中的二维码，并返回识别结果，以及版本。使用固件`Find code`

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/qr_code/uiflow_block_v_qr_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)
qr = V_1.init(V_1.QR_CODE)
while True:
  print((str('QRcode version: ') + str((qr.getQRversion()))))
  print((str('Code text: ') + str((qr.getQRtext()))))
  wait_ms(2)
```


### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/qr_code/uiflow_block_v_qr_init.svg">

```python
import unit
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)
qr = V_1.init(V_1.QR_CODE)
```

- 初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/qr_code/uiflow_block_v_get_qr_text.svg">

```python
qr.getQRtext()
```

- 读取识别到的二维码内容

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/qr_code/uiflow_block_v_get_qr_version.svg">

```python
qr.getQRversion()
```

- 读取识别到的二维码版本

## Apriltag Code

### 案例程序

识别画面中的 Apriltag 码(仅支持 Tag36H11类型),并获取其位置的偏移。使用固件`Find code` 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/apriltag_code/uiflow_block_v_apriltag_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)

tag = V_1.init(V_1.APRILTAG)
while True:
  print((str('AprilTag location: ') + str((tag.getAprilTagcodeLocation()))))
  print((str('AprilTag rotation: ') + str((tag.getAprilTagcodeRotation()))))
  print((str('AprilTag translation: ') + str((tag.getAprilTagcodeTranslation()))))
  wait_ms(2)
```


### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/apriltag_code/uiflow_block_v_apriltag_init.svg">

```python
import unit
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)
tag = V_1.init(V_1.APRILTAG)
```

- 初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/apriltag_code/uiflow_block_v_get_apriltag_location.svg">

```python
tag.getAprilTagcodeLocation()
```

- 读取识别到的 AprilTag 码的框选坐标，中心坐标，长度宽度，返回值为列表

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/apriltag_code/uiflow_block_v_get_apriltag_rotation.svg">

```python
tag.getAprilTagcodeRotation()
```

- 返回以弧度计的 AprilTag 的旋度(int)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/apriltag_code/uiflow_block_v_get_apriltag_Translation.svg">

```python
tag.getAprilTagcodeTranslation()
```

- 读取 Apriltag 码的位置偏移

## Bar Code

### 案例程序

识别画面中的条形码，并返回识别结果，以及版本。使用固件`Find code`

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/bar_code/uiflow_block_v_bar_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)

bar = V_1.init(V_1.BARCODE)
while True:
  print((str('Code text: ') + str((bar.getBARcodeText()))))
  print((str('Code type: ') + str((bar.getBARcodeRotation()))))
  print((str('Code rotation: ') + str((bar.getBARcodeType()))))
  print((str('Code location: ') + str((bar.getBARcodeLocation()))))
  wait_ms(2)
```


### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/bar_code/uiflow_block_v_bar_init.svg">

```python
import unit
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)
bar = V_1.init(V_1.BARCODE)
```

- 初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/bar_code/uiflow_block_v_get_bar_location.svg">

```python
bar.getBARcodeLocation()
```

- 读取识别到的条码的框选坐标，长度宽度，返回值为列表


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/bar_code/uiflow_block_v_get_bar_rotation.svg">

```python
bar.getBARcodeRotation()
```


- 读取识别到的条码旋转角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/bar_code/uiflow_block_v_get_bar_text.svg">

```python
bar.getBARcodeText()
```

- 读取识别到的条形码内容

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/bar_code/uiflow_block_v_get_bar_type.svg">

```python
bar.getBARcodeType()
```

- 读取识别到的条码类别

## Datamatrix Code

### 案例程序

识别画面中的 Datamatrix 码，并返回识别结果，以及码旋转角度，坐标数据。使用固件`Find code`

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/datamatrix_code/uiflow_block_v_datamatrix_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)

dm = V_1.init(V_1.DATAMATRIX)
while True:
  print((str('DM code rotation: ') + str((dm.getDMcodeRotation()))))
  print((str('DM code location: ') + str((dm.getDMcodeLocation()))))
  print((str('DM code text: ') + str((dm.getDMcodeText()))))
  wait_ms(2)
```


### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/datamatrix_code/uiflow_block_v_datamatrix_init.svg">

```python
import unit
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)
dm = V_1.init(V_1.DATAMATRIX)
```

- 初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/datamatrix_code/uiflow_block_v_get_datamatrix_location.svg">

```python
dm.getDMcodeLocation()
```

- 读取识别到的 Datamatrix 码的框选坐标，长度宽度，返回值为列表

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/datamatrix_code/uiflow_block_v_get_datamatrix_rotation.svg">

```python
dm.getDMcodeRotation()

```

- 读取识别到的 Datamatrix 码旋转角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/datamatrix_code/uiflow_block_v_get_datamatrix_text.svg">

```python
dm.getDMcodeText()
```

- 读取识别到的 Datamatrix 码内容


## Line Tracker

### 案例程序

检测画面中指定的颜色线条，并返回偏移角度。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/line_tracker/uiflow_block_v_line_tracker_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)

line_tracker = V_1.init(V_1.LINE_TRACKER)
while True:
  print((str('Line angle') + str((line_tracker.getAngle()))))
  wait_ms(2)
```

### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/line_tracker/uiflow_block_v_line_tracker_init.svg">

```python
import unit
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)
line_tracker = V_1.init(V_1.LINE_TRACKER)
```

- 初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/line_tracker/uiflow_block_v_get_angle.svg">

```python
line_tracker.getAngle()
```

- 获取线条偏移角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/line_tracker/uiflow_block_v_set_line_area_weight.svg">

```python
line_tracker.setLineAreaWeight(0, 0, 0)
```

- 设置线条区域权重：三个权重分别对应图中三个区域对角度的贡献值。比如把 weight_2的值设置的大一些，则当转弯时角度变化将更加剧烈。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/line_tracker/uiflow_block_v_set_line_color.svg">

```python
line_tracker.setLineColorByLAB(0, 0, 0, 0, 0, 0)
```

- 设置追踪的 LAB 阈值(LAB 颜色空间的颜色值，在该范围外的颜色将会被过滤)


## Tag Reader

### 案例程序

检测画面中的标签卡，并返回二进制序列。注：仅识别固定标签卡格式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/tag_reader/uiflow_block_v_tag_reader_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)

tag_reader = V_1.init(V_1.TAG_READER)
while True:
  print((str('Total number: ') + str((tag_reader.getTotalNumber()))))
  print((str('Tag location: ') + str((tag_reader.getTagLocation(number=0)))))
  print((str('Code: ') + str((tag_reader.getCode(number=0)))))
  print((str('Binstr: ') + str((tag_reader.getBinstr(number=0)))))
  wait_ms(2)
```

### 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/tag_reader/uiflow_block_v_tag_reader_init.svg">

```python
import unit
V_1 = unit.get(unit.V_FUNCTION, unit.PORTB)
tag_reader = V_1.init(V_1.TAG_READER)
```

- 初始化


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/tag_reader/uiflow_block_v_get_total_number.svg">

```python
tag_reader.getTotalNumber()
```

- 当前画面识别到的标签卡数量


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/tag_reader/uiflow_block_v_get_binstr.svg">

```python
tag_reader.getBinstr(number=0)
```

- 识别结果的二进制数据的字符串，当有多个卡片时，传入下标可选择不同的卡片内容。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/tag_reader/uiflow_block_v_get_code.svg">

```python
tag_reader.getCode(number=0)
```

- uint64_t 类型的内容二进制代码，本键值最大编码64位(8 x 8)的 TAG。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/unitv/tag_reader/uiflow_block_v_get_tag_location.svg">

```python
tag_reader.getTagLocation(number=0)
```

- 标签卡的坐标与长宽信息


## 相关工具

- [下载 LAB 取色工具](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/LAB-Color-Tool.exe)

