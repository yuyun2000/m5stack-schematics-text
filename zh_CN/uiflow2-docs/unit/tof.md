# ToF Unit


<!-- .. include:: ../refs/unit.tof.ref -->

Support the following products:

    ![ToFUnit](https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-1389686c-b643-4b4f-a74b-4dc070a32103.webp)


Micropython Example:

```python
# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

import os, sys, io
import M5
from M5 import *
from hardware import *
from unit import ToFUnit


label0 = None
i2c0 = None
tof_0 = None


def setup():
    global label0, i2c0, tof_0

    M5.begin()
    Widgets.fillScreen(0x222222)
    label0 = Widgets.Label("label0", 132, 109, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)

    i2c0 = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
    tof_0 = ToFUnit(i2c0)


def loop():
    global label0, i2c0, tof_0
    M5.update()
    label0.setText(str((str((tof_0.get_range())) + str("mm"))))


if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg

            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")

```


UIFLOW2 Example:

    ![example.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/example.png)


<!-- .. only:: builder_html -->

    [tof_core_example.m5f2]


## class ToFUnit


## Constructors


<!-- .. class:: ToFUnit(i2c: I2C, address: int = 0x29, io_timeout_ms: int = 0) -->

    Create a DLight object.

    :param i2c: the I2C object.
    :param address: the I2C address of the device. Default is 0x23.
    :param io_timeout_ms: the timeout of I2C communication. Default is 0ms.

    UIFLOW2:

        ![init.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/init.png)


<!-- .. _unit.ToFUnit.Methods: -->

## Methods


<!-- .. method:: ToFUnit.get_distance() -> float -->

    Get distance in centimeters.

    :return: distance in millimeters.

    UIFLOW2:

        ![get_distance.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/get_distance.png)


<!-- .. method:: ToFUnit.get_data_ready() -> bool -->

    Get data ready status.

    :return: data ready status.

    UIFLOW2:

        ![get_data_ready.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/get_data_ready.png)


<!-- .. method:: ToFUnit.get_range() -> int -->

    Get distance in millimeters.

    :return: distance in millimeters.

    UIFLOW2:

        ![get_range.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/get_range.png)

<!-- .. method:: ToFUnit.is_continuous_mode() -> bool -->

    Get continuous mode status.

    :return: continuous mode status.

    UIFLOW2:

        ![is_continuous_mode.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/is_continuous_mode.png)


<!-- .. method:: ToFUnit.get_measurement_timing_budget() -> int -->

    Get measurement timing budget. The budget is in microseconds.

    :return: measurement timing budget. The budget is in microseconds.

    UIFLOW2:

        ![get_measurement_timing_budget.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/get_measurement_timing_budget.png)


<!-- .. method:: ToFUnit.set_measurement_timing_budget(budget_us: int) -> None -->

    Set measurement timing budget. The budget_us is in microseconds.

    :param budget_us: measurement timing budget in microseconds.

    UIFLOW2:

        ![set_measurement_timing_budget.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/set_measurement_timing_budget.png)


<!-- .. method:: ToFUnit.get_signal_rate_limit() -> float -->

    Get signal rate limit.

    :return: signal rate limit.

    UIFLOW2:

        ![get_signal_rate_limit.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/get_signal_rate_limit.png)


<!-- .. method:: ToFUnit.set_signal_rate_limit(val: float) -> None -->

    Set signal rate limit.

    :param val: signal rate limit.

    UIFLOW2:

        ![set_signal_rate_limit.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/set_signal_rate_limit.png)


<!-- .. method:: ToFUnit.start_continuous() -> None -->

    Start continuous mode.

    UIFLOW2:

        ![start_continuous.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/start_continuous.png)


<!-- .. method:: ToFUnit.stop_continuous() -> None -->

    Stop continuous mode.

    UIFLOW2:

        ![stop_continuous.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/stop_continuous.png)


<!-- .. method:: ToFUnit.set_address(new_address: int) -> None -->

    Set I2C address.

    :param new_address: new I2C address.

    UIFLOW2:

        ![set_address.png](https://static-cdn.m5stack.com/mpy_docs/unit/tof/set_address.png)