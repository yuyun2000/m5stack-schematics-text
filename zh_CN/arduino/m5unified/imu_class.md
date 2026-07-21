# M5Unified IMU Class

- [IMU Class](#m5unified-imu-class)
  - [begin](#begin)
  - [init](#init)
  - [sleep](#sleep)
  - [setClock](#setclock)
  - [update](#update)
  - [getImuData](#getimudata)
  - [setAxisOrder](#setaxisorder)
  - [setAxisOrderRightHanded](#setaxisorderrighthanded)
  - [setAxisOrderLeftHanded](#setaxisorderlefthanded)
  - [getAccel](#getaccel)
  - [getGyro](#getgyro)
  - [getMag](#getmag)
  - [getTemp](#gettemp)
  - [isEnabled](#isenabled)
  - [getType](#gettype)
  - [setINTPinActiveLogic](#setintpinactivelogic)
  - [setCalibration](#setcalibration)
  - [saveOffsetToNVS](#saveoffsettonvs)
  - [loadOffsetFromNVS](#loadoffsetfromnvs)
  - [clearOffsetData](#clearoffsetdata)
  - [setOffsetData](#setoffsetdata)
  - [getOffsetData](#getoffsetdata)
  - [getRawData](#getrawdata)
  - [getImuInstancePtr](#getimuinstanceptr)

## begin

**函数原型:**

```cpp
bool begin(I2C_Class* i2c = nullptr, board_t board = board_t::board_unknown);
```

**功能说明:**

- 初始化 IMU, 并指定初始化的 I2C 接口和板卡类型

**传入参数:**

- I2C_Class* i2c
  - 使用的 I2C 接口
- board_t board
  - M5Stack 板卡类型

**返回值:**

- bool:
  - true: 初始化成功
  - false: 初始化失败

## init

**函数原型:**

```cpp
bool init(I2C_Class* i2c = nullptr) { return begin(i2c); }
```

**功能说明:**

- 初始化 IMU, 并指定初始化的 I2C 接口

**传入参数:**

- I2C_Class* i2c
  - 使用的 I2C 接口

**返回值:**

- bool:
  - true: 初始化成功
  - false: 初始化失败

## sleep

**函数原型:**

```cpp
bool sleep(void);
```

**功能说明:**

- IMU 进入休眠模式

**传入参数:**

- null

**返回值:**

- bool:
  - true: 进入休眠模式成功
  - false: 进入休眠模式失败

## setClock

**函数原型:**

```cpp
void setClock(std::uint32_t freq);
```

**功能说明:**

- 设置内部 IMU 内部时钟频率

**传入参数:**

- uint32_t freq:
  - 时钟频率

**返回值:**

- null

## update

**函数原型:**

```cpp
sensor_mask_t update(void);
```

**功能说明:**

- 获取 IMU 数据更新

**传入参数:**

- null

**返回值:**

- sensor_mask_t:
  - 传感器数据采集 mask 数值:
    - sensor_mask_none:`0000`
    - sensor_mask_accel:`0001`
    - sensor_mask_gyro:`0010`
    - sensor_mask_mag:`0100`

```cpp line-num
enum sensor_index_t
{
  sensor_index_accel = 0,
  sensor_index_gyro  = 1,
  sensor_index_mag   = 2,
};

enum sensor_mask_t
{
  sensor_mask_none = 0,
  sensor_mask_accel = 1 << sensor_index_accel,
  sensor_mask_gyro  = 1 << sensor_index_gyro,
  sensor_mask_mag   = 1 << sensor_index_mag,
};
```

## getImuData

**函数原型:**

```cpp
void getImuData(imu_data_t* imu_data);
```

```cpp
const imu_data_t& getImuData(void) { getImuData(&_last_data); return _last_data; }
```

**功能说明:**

- 获取当前 IMU 数据

**传入参数:**

- null

**返回值:**

- imu_data_t data:
  - `data.accel.x`: accel x-axis value.
  - `data.accel.y`: accel y-axis value.
  - `data.accel.z`: accel z-axis value.
  - `data.accel.value`: accel 3values array [0]=x / [1]=y / [2]=z.
  - `data.gyro.x`: gyro x-axis value.
  - `data.gyro.y`: gyro y-axis value.
  - `data.gyro.z`: gyro z-axis value.
  - `data.gyro.value`: gyro 3values array [0]=x / [1]=y / [2]=z.
  - `data.mag.x`: mag x-axis value.
  - `data.mag.y`: mag y-axis value.
  - `data.mag.z`: mag z-axis value.
  - `data.mag.value`: mag 3values array [0]=x / [1]=y / [2]=z.
  - `data.value`: all sensor 9values array [0-2]=accel / [3-5]=gyro / [6-8]=mag

## setAxisOrder

**函数原型:**

```cpp
bool setAxisOrder(axis_t axis0, axis_t axis1, axis_t axis2);
```

**功能说明:**

- 指定轴顺序。默认为 X+,Y+,Z+

**传入参数:**

- axis_t axis0, axis_t axis1, axis_t axis2

```cpp line-num
enum axis_t
{
  axis_x_pos = 0,
  axis_x_neg = 1,
  axis_y_pos = 2,
  axis_y_neg = 3,
  axis_z_pos = 4,
  axis_z_neg = 5,
};
```

**返回值:**

- bool:
  - true: 轴顺序设置成功
  - false: 轴顺序设置失败

## setAxisOrderRightHanded

**函数原型:**

```cpp
bool setAxisOrderRightHanded(axis_t axis0, axis_t axis1);
```

**功能说明:**

- 指定轴顺序。默认为 X+,Y+,Z+

**传入参数:**

- axis_t axis0, axis_t axis1, axis_t axis2

**返回值:**

- bool:
  - true: 轴顺序设置成功
  - false: 轴顺序设置失败

## setAxisOrderLeftHanded

**函数原型:**

```cpp
bool setAxisOrderLeftHanded(axis_t axis0, axis_t axis1);
```

## getAccel

**函数原型:**

```cpp
bool getAccel(float* ax, float* ay, float* az);
```

**功能说明:**

- 读取三轴加速度

**传入参数:**

- float* ax, float* ay, float* a

**返回值:**

- bool:
  - true: 读取成功
  - false: 读取失败

## getGyro

**函数原型:**

```cpp
bool getGyro(float* gx, float* gy, float* gz);
```

**功能说明:**

- 读取三轴角速度

**传入参数:**

- float* gx, float* gy, float* gz

**返回值:**

- bool:
  - true: 读取成功
  - false: 读取失败

## getMag

**函数原型:**

```cpp
bool getMag(float* mx, float* my, float* mz);
```

**功能说明:**

- 读取三轴磁力

**传入参数:**

- float* mx, float* my, float* mz

**返回值:**

- bool:
  - true: 读取成功
  - false: 读取失败

## getTemp

**函数原型:**

```cpp
bool getTemp(float *t);
```

**功能说明:**

- 读取温度测量数据

**传入参数:**

- float *t

**返回值:**

- bool:
  - true: 读取成功
  - false: 读取失败

## isEnabled

**函数原型:**

```cpp
bool isEnabled(void) const { return _imu != imu_none; }
```

**功能说明:**

- 判断 IMU 是否初始化

**传入参数:**

- null

**返回值:**

- bool:
  - true: IMU 已经初始化
  - false: IMU 未初始化

## getType

**函数原型:**

```cpp
imu_t getType(void) const { return _imu; }
```

**功能说明:**

- 获取 IMU 类型

**传入参数:**

- null

**返回值:**

- imu_t:
  - IMU 芯片类型

```cpp line-num
enum imu_t
{ imu_none,
  imu_unknown,
  imu_sh200q,
  imu_mpu6050,
  imu_mpu6886,
  imu_mpu9250,
  imu_bmi270,
};
```

## setINTPinActiveLogic

**函数原型:**

```cpp
bool setINTPinActiveLogic(bool level);
```

**功能说明:**

- 设置中断引脚活动电平

**传入参数:**

- bool level: 活动电平

**返回值:**

- bool:
  - true: 设置成功
  - false: 设置失败

## setCalibration

**函数原型:**

```cpp
void setCalibration(uint8_t accel_strength, uint8_t gyro_strength, uint8_t mag_strength);
```

**功能说明:**

- 指定每个传感器的自动偏移调整功能的强度。 0=无自动调节 1~255=有自动调节, 每次 M5.Imu.update 期间都会执行实际校准操作。

**传入参数:**

- uint8_t accel_strength
- uint8_t gyro_strength
- uint8_t mag_strength

**返回值:**

- null

## saveOffsetToNVS

**函数原型:**

```cpp
bool saveOffsetToNVS(void);
```

**功能说明:**

- 保存 IMU 偏移值到 NVS

**传入参数:**

- null

**返回值:**

- bool:
  - true: 保存成功
  - false: 保存失败

## loadOffsetFromNVS

**函数原型:**

```cpp
bool loadOffsetFromNVS(void);
```

**功能说明:**

- 从 NVS 中加载 IMU 偏移值

**传入参数:**

- null

**返回值:**

- bool:
  - true: 加载成功
  - false: 加载失败

## clearOffsetData

**函数原型:**

```cpp
void clearOffsetData(void);
```

**功能说明:**

- 清除 NVS 中的 IMU 偏移值

**传入参数:**

- null

**返回值:**

- bool:
  - true: 清除成功
  - false: 清除失败

## setOffsetData

**函数原型:**

```cpp
void setOffsetData(size_t index, int32_t value);
```

**功能说明:**

- 设置 IMU 偏移值

**传入参数:**

- size_t index:
  - 设置轴的索引
- int32_t value
  - 偏移值

**返回值:**

- null

## getOffsetData

**函数原型:**

```cpp
int32_t getOffsetData(size_t index);
```

**功能说明:**

- 获取 IMU 偏移值

**传入参数:**

- size_t index:
  - 读取轴的索引

**返回值:**

- int32_t: 偏移值

## getRawData

**函数原型:**

```cpp
int16_t getRawData(size_t index);
```

**功能说明:**

- 获取 IMU Raw 数据

**传入参数:**

- size_t index:
  - 读取轴的索引

**返回值:**

- int32_t: IMU Raw 数据

## getImuInstancePtr

**函数原型:**

```cpp
IMU_Base* getImuInstancePtr(int idx) const { return _imu_instance[idx].get(); }
```

**功能说明:**

- 获取 IMU 实例指针

**传入参数:**

- int idx:
  - 实例序号

**返回值:**

- IMU_Base:
  - IMU 实例
