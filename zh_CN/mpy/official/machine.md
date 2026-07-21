## machine

```python
import machine

machine.freq()          # 获取当前CPU频率
machine.freq(240000000) # 配置CPU频率为 240 MHz
```

## esp

```python
import esp

esp.osdebug(None)       # 关闭O/S debugging信息
esp.osdebug(0)          # 重定向O/S debugging信息到 UART(0)

# 基础flash操作API
esp.flash_size()
esp.flash_user_start()
esp.flash_erase(sector_no)
esp.flash_write(byte_offset, buffer)
esp.flash_read(byte_offset, buffer)
```

## esp32

```python
import esp32

esp32.hall_sensor()     # 读取内部霍尔传感器
esp32.raw_temperature() # 读取 MCU 的内部温度，单位为华氏度
esp32.ULP()             # 访问超低功耗协处理器
```

## network

```python
import network

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points
wlan.isconnected()      # check if the station is connected to an AP
wlan.connect('essid', 'password') # connect to an AP
wlan.config('mac')      # get the interface's MAC address
wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses

ap = network.WLAN(network.AP_IF) # create access-point interface
ap.config(essid='ESP-AP') # set the ESSID of the access point
ap.config(max_clients=10) # set how many clients can connect to the network
ap.active(True)         # activate the interface
```

> WiFi 连接函数案例

```python
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('essid', 'password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
```

?> 完成网络连接后可以使用`socket` 模块创建和使用 TCP/UDP 套接字，使用`urequests`模块创建 HTTP 请求。

?> 在调用连接函数`wlan.connect()`后，设备将自动进行连接，验证失败或范围内并不存在该 AP 的情况，设备将不断尝试重连。使用`wlan.status()`能够获取当前连接状态，未完成连接前，返回值为`network.STAT_CONNECTING`，该状态将一直保持到连接成功或接口被禁用。支持通过调用`wlan.config(reconnects=n)`来更改重连次数，其中`n`是允许重连的尝试次数 (0 表示不重连，-1 表示不断重连)。

## time

```python
import time

time.sleep(1)           # sleep for 1 second
time.sleep_ms(500)      # sleep for 500 milliseconds
time.sleep_us(10)       # sleep for 10 microseconds
start = time.ticks_ms() # get millisecond counter
delta = time.ticks_diff(time.ticks_ms(), start) # compute time difference
```

## Timers

The ESP32 port has four hardware timers. - `machine.Timer <machine.Timer>` class
with a timer ID from 0 to 3 (inclusive)::

- 使用`machine.Timer`模块创建定时器. ESP32 内置 4 个硬件定时器，ID 为 0-3。

```python
from machine import Timer

tim0 = Timer(0)
tim0.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(0))

tim1 = Timer(1)
tim1.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(1))
```

The period is in milliseconds.

Virtual timers are not currently supported on this port.

## Pins and GPIO

- `machine.Pin <machine.Pin>`

```python
from machine import Pin

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
p0.on()                 # set pin to "on" (high) level
p0.off()                # set pin to "off" (low) level
p0.value(1)             # set pin to on/high

p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
print(p2.value())       # get value, 0 or 1

p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation
```

Available Pins are from the following ranges (inclusive): 0-19, 21-23, 25-27, 32-39.
These correspond to the actual GPIO pin numbers of ESP32 chip. Note that many
end-user boards use their own adhoc pin numbering (marked e.g. D0, D1, ...).
For mapping between board logical pins and physical chip pins consult your board
documentation.

\#>Notes:<br/>Pins 1 and 3 are REPL UART TX and RX respectively<br/>Pins 6, 7, 8, 11, 16, and 17 are used for connecting the embedded flash,
and are not recommended for other uses<br/>Pins 34-39 are input only, and also do not have internal pull-up resistors<br/>The pull value of some pins can be set to `Pin.PULL_HOLD` to reduce power consumption during deepsleep.

There's a higher-level abstraction :ref:`machine.Signal <machine.Signal>`
which can be used to invert a pin. Useful for illuminating active-low LEDs
using `on()` or `value(1)`.

## UART (serial bus)

- `machine.UART`

```python
from machine import UART

uart1 = UART(1, baudrate=9600, tx=33, rx=32)
uart1.write('hello')  # write 5 bytes
uart1.read(5)         # read up to 5 bytes
```

?>ESP32 内置了三组 UART：UART0、UART1 和 UART2。下表是它们的默认 GPIO 映射。支持 GPIO 重新映射，这意味着你可以配置 UART 的`TX`或`RX`为其他引脚。需要注意的是，部分的 IO 存在输入输出限制的限制，详情可参考[ESP32 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/esp32_datasheet_en.pdf)

| \   | UART0 | UART1 | UART2 |
| --- | ----- | ----- | ----- |
| tx  | 1     | 10    | 17    |
| rx  | 3     | 19    | 16    |

## PWM

PWM can be enabled on all output-enabled pins. The base frequency can range from 1Hz to 40MHz but there is a tradeoff; as the base frequency _increases_ the duty resolution _decreases_. See [LED Control](https://docs.espressif.com/projects/esp-idf/zh-cn/latest/api-reference/peripherals/ledc.html) for more details.

- `machine.PWM`

```python
from machine import Pin, PWM

pwm0 = PWM(Pin(0))         # create PWM object from a pin
freq = pwm0.freq()         # get current frequency (default 5kHz)
pwm0.freq(1000)            # set PWM frequency from 1Hz to 40MHz

duty = pwm0.duty()         # get current duty cycle, range 0-1023 (default 512, 50%)
pwm0.duty(256)             # set duty cycle from 0 to 1023 as a ratio duty/1023, (now 25%)

duty_u16 = pwm0.duty_u16() # get current duty cycle, range 0-65535
pwm0.duty_u16(65535*3/4)  # set duty cycle from 0 to 65535 as a ratio duty_u16/65535, (now 75%)

duty_ns = pwm0.duty_ns()   # get current pulse width in ns
pwm0.duty_ns(250_000)      # set pulse width in nanoseconds from 0 to 1_000_000_000/freq, (now 25%)

pwm0.deinit()              # turn off PWM on the pin

pwm2 = PWM(Pin(2), freq=20000, duty=512)  # create and configure in one go
print(pwm2)                               # view PWM settings
```

ESP chips have different hardware peripherals:

| Hardware specification                                 | ESP32 | ESP32-S2 | ESP32-C3 |
| ------------------------------------------------------ | ----- | -------- | -------- |
| Number of groups (speed modes)                         | 2     | 1        | 1        |
| Number of timers per group                             | 4     | 4        | 4        |
| Number of channels per group                           | 8     | 8        | 6        |
| Different PWM frequencies (groups \* timers)           | 8     | 4        | 4        |
| Total PWM channels (Pins, duties) (groups \* channels) | 16    | 8        | 6        |

A maximum number of PWM channels (Pins) are available on the ESP32 - 16 channels,
but only 8 different PWM frequencies are available, the remaining 8 channels must
have the same frequency. On the other hand, 16 independent PWM duty cycles are
possible at the same frequency.

See more examples in the :ref:`esp32_pwm` tutorial.

## ADC

On the ESP32 ADC functionality is available on Pins 32-39. Note that, when
using the default configuration, input voltages on the ADC pin must be between
0.0v and 1.0v (anything above 1.0v will just read as 4095). Attenuation must
be applied in order to increase this usable voltage range.

- `machine.ADC`

```python
from machine import ADC

adc = ADC(Pin(32))          # create ADC object on ADC pin
adc.read()                  # read value, 0-4095 across voltage range 0.0v - 1.0v

adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)
adc.read()                  # read value using the newly configured attenuation and width
```

ESP32 specific ADC class method reference:

.. method:: ADC.atten(attenuation)

This method allows for the setting of the amount of attenuation on the
input of the ADC. This allows for a wider possible input voltage range,
at the cost of accuracy (the same number of bits now represents a wider
range). The possible attenuation options are:

- `ADC.ATTN_0DB`: 0dB attenuation, gives a maximum input voltage
  of 1.00v - this is the default configuration
- `ADC.ATTN_2_5DB`: 2.5dB attenuation, gives a maximum input voltage
  of approximately 1.34v
- `ADC.ATTN_6DB`: 6dB attenuation, gives a maximum input voltage
  of approximately 2.00v
- `ADC.ATTN_11DB`: 11dB attenuation, gives a maximum input voltage
  of approximately 3.6v

\#>Despite 11dB attenuation allowing for up to a 3.6v range, note that the absolute maximum voltage rating for the input pins is 3.6v, and so going near this boundary may be damaging to the IC!

.. method:: ADC.width(width)

This method allows for the setting of the number of bits to be utilised
and returned during ADC reads. Possible width options are:

- `ADC.WIDTH_9BIT`: 9 bit data
- `ADC.WIDTH_10BIT`: 10 bit data
- `ADC.WIDTH_11BIT`: 11 bit data
- `ADC.WIDTH_12BIT`: 12 bit data - this is the default configuration

## Software SPI

Software SPI (using bit-banging) works on all pins, and is accessed via the
:ref:`machine.SoftSPI <machine.SoftSPI>`

```python
from machine import Pin, SoftSPI

# construct a SoftSPI bus on the given pins
# polarity is the idle state of SCK
# phase=0 means sample on the first edge of SCK, phase=1 means the second
spi = SoftSPI(baudrate=100000, polarity=1, phase=0, sck=Pin(0), mosi=Pin(2), miso=Pin(4))

spi.init(baudrate=200000) # set the baudrate

spi.read(10)            # read 10 bytes on MISO
spi.read(10, 0xff)      # read 10 bytes while outputting 0xff on MOSI

buf = bytearray(50)     # create a buffer
spi.readinto(buf)       # read into the given buffer (reads 50 bytes in this case)
spi.readinto(buf, 0xff) # read into the given buffer and output 0xff on MOSI

spi.write(b'12345')     # write 5 bytes on MOSI

buf = bytearray(4)      # create a buffer
spi.write_readinto(b'1234', buf) # write to MOSI and read from MISO into the buffer
spi.write_readinto(buf, buf) # write buf to MOSI and read MISO back into buf
```

\#>Currently all of `sck`, `mosi` and `miso` _must_ be specified when initialising Software SPI.

\#> 注：`sck`, `mosi`,`miso`必须在初始化 SPI 前配置。

## Hardware SPI

There are two hardware SPI channels that allow faster transmission
rates (up to 80Mhz). These may be used on any IO pins that support the
required direction and are otherwise unused (see :ref:`Pins_and_GPIO`)
but if they are not configured to their default pins then they need to
pass through an extra layer of GPIO multiplexing, which can impact
their reliability at high speeds. Hardware SPI channels are limited
to 40MHz when used on pins other than the default ones listed below.

| \    | HSPI (id=1) | VSPI (id=2) |
| ---- | ----------- | ----------- |
| sck  | 14          | 18          |
| mosi | 13          | 23          |
| miso | 12          | 19          |

- `machine.SPI`

```python
from machine import Pin, SPI

hspi = SPI(1, 10000000)
hspi = SPI(1, 10000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
vspi = SPI(2, baudrate=80000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
```

## Software I2C bus

Software I2C (using bit-banging) works on all output-capable pins, and is

- `machine.SoftI2C`

```python
from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=100000)

i2c.scan()              # scan for devices

i2c.readfrom(0x3a, 4)   # read 4 bytes from device with address 0x3a
i2c.writeto(0x3a, '12') # write '12' to device with address 0x3a

buf = bytearray(10)     # create a buffer with 10 bytes
i2c.writeto(0x3a, buf)  # write the given buffer to the peripheral
```

## Hardware I2C

There are two hardware I2C peripherals with identifiers 0 and 1. Any available
output-capable pins can be used for SCL and SDA but the defaults are given
below.

| \   | I2C(0) | I2C(1) |
| --- | ------ | ------ |
| scl | 18     | 25     |
| sda | 19     | 26     |

The driver is accessed via the :ref:`machine.I2C <machine.I2C>` class and
has the same methods as software I2C above::

```python
from machine import Pin, I2C

i2c = I2C(0)
i2c = I2C(1, scl=Pin(5), sda=Pin(4), freq=400000)
```

## I2S bus

- `machine.I2S`

```python
from machine import I2S, Pin

i2s = I2S(0, sck=Pin(13), ws=Pin(14), sd=Pin(34), mode=I2S.TX, bits=16, format=I2S.STEREO, rate=44100, ibuf=40000) # create I2S object
i2s.write(buf)             # write buffer of audio samples to I2S device

i2s = I2S(1, sck=Pin(33), ws=Pin(25), sd=Pin(32), mode=I2S.RX, bits=16, format=I2S.MONO, rate=22050, ibuf=40000) # create I2S object
i2s.readinto(buf)          # fill buffer with audio samples from I2S device
```

The I2S class is currently available as a Technical Preview. During the preview period, feedback from
users is encouraged. Based on this feedback, the I2S class API and implementation may be changed.

ESP32 has two I2S buses with id=0 and id=1

## Real time clock (RTC)

- `machine.RTC <machine.RTC>` ::

```python
from machine import RTC

rtc = RTC()
rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0)) # set a specific date and time
rtc.datetime() # get date and time
```

## WDT (Watchdog timer)

- `machine.WDT <machine.WDT>`

```python
from machine import WDT

# enable the WDT with a timeout of 5s (1s is the minimum)
wdt = WDT(timeout=5000)
wdt.feed()
```

## Deep-sleep mode

The following code can be used to sleep, wake and check the reset cause::

```python
import machine

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

# put the device to sleep for 10 seconds
machine.deepsleep(10000)
```

Notes:

- Calling `deepsleep()` without an argument will put the device to sleep
  indefinitely
- A software reset does not change the reset cause
- There may be some leakage current flowing through enabled internal pullups.
  To further reduce power consumption it is possible to disable the internal pullups::

p1 = Pin(4, Pin.IN, Pin.PULL_HOLD)

After leaving deepsleep it may be necessary to un-hold the pin explicitly (e.g. if
it is an output pin) via::

p1 = Pin(4, Pin.OUT, None)

## SD card

- `machine.SDCard <machine.SDCard>`

```python
import machine, os

# Slot 2 uses pins sck=18, cs=5, miso=19, mosi=23
sd = machine.SDCard(slot=2)
os.mount(sd, "/sd")  # mount

os.listdir('/sd')    # list directory contents

os.umount('/sd')     # eject
```

## RMT

RMT 功能允许生成精确的数字脉冲，分辨率可达 12.5ns

```python
import esp32
from machine import Pin

r = esp32.RMT(0, pin=Pin(18), clock_div=8)
r   # RMT(channel=0, pin=18, source_freq=80000000, clock_div=8)
# The channel resolution is 100ns (1/(source_freq/clock_div)).
r.write_pulses((1, 20, 2, 40), 0) # Send 0 for 100ns, 1 for 2000ns, 0 for 200ns, 1 for 4000ns
```

## OneWire driver

The OneWire driver is implemented in software and works on all pins::

```python
from machine import Pin
import onewire

ow = onewire.OneWire(Pin(12)) # create a OneWire bus on GPIO12
ow.scan()               # return a list of devices on the bus
ow.reset()              # reset the bus
ow.readbyte()           # read a byte
ow.writebyte(0x12)      # write a byte on the bus
ow.write('123')         # write bytes on the bus
ow.select_rom(b'12345678') # select a specific device by its ROM code
```

There is a specific driver for DS18S20 and DS18B20 devices::

```python
import time, ds18x20
ds = ds18x20.DS18X20(ow)
roms = ds.scan()
ds.convert_temp()
time.sleep_ms(750)
for rom in roms:
    print(ds.read_temp(rom))
```

Be sure to put a 4.7k pull-up resistor on the data line. Note that
the `convert_temp()` method must be called each time you want to
sample the temperature.

## NeoPixel and APA106 driver

Use the `neopixel` and `apa106` modules::

```python
from machine import Pin
from neopixel import NeoPixel

pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (255, 255, 255) # set the first pixel to white
np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour
```

The APA106 driver extends NeoPixel, but internally uses a different colour order::

```python
from apa106 import APA106
ap = APA106(pin, 8)
r, g, b = ap[0]
```

For low-level driving of a NeoPixel::

```python
import esp
esp.neopixel_write(pin, grb_buf, is800khz)
```

\#>By default `NeoPixel` is configured to control the more popular *800kHz*units. It is possible to use alternative timing to control other (typically 400kHz) devices by passing `timing=0` when constructing the`NeoPixel` object.

The low-level driver uses an RMT channel by default. To configure this see
`RMT.bitstream_channel`.

APA102 (DotStar) uses a different driver as it has an additional clock pin.

## Capacitive touch

Use the `TouchPad` class in the `machine` module::

```python
from machine import TouchPad, Pin

t = TouchPad(Pin(14))
t.read()              # Returns a smaller number when touched
```

`TouchPad.read` returns a value relative to the capacitive variation. Small numbers (typically in
the _tens_) are common when a pin is touched, larger numbers (above _one thousand_) when
no touch is present. However the values are _relative_ and can vary depending on the board
and surrounding composition so some calibration may be required.

There are ten capacitive touch-enabled pins that can be used on the ESP32: 0, 2, 4, 12, 13
14, 15, 27, 32, 33. Trying to assign to any other pins will result in a `ValueError`.

Note that TouchPads can be used to wake an ESP32 from sleep::

```python
import machine
from machine import TouchPad, Pin
import esp32

t = TouchPad(Pin(14))
t.config(500)               # configure the threshold at which the pin is considered touched
esp32.wake_on_touch(True)
machine.lightsleep()        # put the MCU to sleep until a touchpad is touched
```

For more details on touchpads refer to `Espressif Touch Sensor <https://docs.espressif.com/projects/esp-idf/zh-cn/latest/api-reference/peripherals/touch_pad.html>`\_.

## DHT driver

The DHT driver is implemented in software and works on all pins::

```python
import dht
import machine

d = dht.DHT11(machine.Pin(4))
d.measure()
d.temperature() # eg. 23 (°C)
d.humidity()    # eg. 41 (% RH)

d = dht.DHT22(machine.Pin(4))
d.measure()
d.temperature() # eg. 23.6 (°C)
d.humidity()    # eg. 41.3 (% RH)
```
