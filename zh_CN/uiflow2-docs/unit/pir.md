# PIR Unit


<!-- .. include:: ../refs/unit.pir.ref -->

Support the following products:

    ![PIR](https://static-cdn.m5stack.com/resource/docs/products/unit/PIR/img-4647c010-1e57-4cc9-85e3-cbd450882074.webp)


Micropython Example:

```python
# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

import os, sys, io
import M5
from M5 import *
from unit import PIRUnit


label0 = None
pir_0 = None


def pir_0_active_event(pir):
    global label0, pir_0
    label0.setText(str("Detected"))


def pir_0_negative_event(pir):
    global label0, pir_0
    label0.setText(str("Not detected"))


def setup():
    global label0, pir_0

    M5.begin()
    Widgets.fillScreen(0x222222)
    label0 = Widgets.Label("label0", 132, 109, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)

    pir_0 = PIRUnit((36, 26))
    pir_0.set_callback(pir_0_active_event, pir_0.IRQ_ACTIVE)
    pir_0.set_callback(pir_0_negative_event, pir_0.IRQ_NEGATIVE)
    pir_0.enable_irq()


def loop():
    global label0, pir_0
    M5.update()


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

    ![example.png](https://static-cdn.m5stack.com/mpy_docs/unit/pir/example.png)


<!-- .. only:: builder_html -->

    [pir_core_example.m5f2]


## class PIR


## Constructors


<!-- .. class:: PIR(IO1,IO2) -->

    Create a PIR object.

    The parameters are:
        - ``IO1,IO2`` I2C pin.

    UIFLOW2:

        ![init.png](https://static-cdn.m5stack.com/mpy_docs/unit/pir/init.png)


## Methods


<!-- .. method:: PIR.get_status() -->

    Get detection status.

    UIFLOW2:

        ![get_status.png](https://static-cdn.m5stack.com/mpy_docs/unit/pir/get_status.png)


<!-- .. method:: PIR.enable_irq() -->

   Enable Human detection function.

    UIFLOW2:

        ![enable_irq.png](https://static-cdn.m5stack.com/mpy_docs/unit/pir/enable_irq.png)


<!-- .. method:: PIR.disable_irq() -->

    Disable Human detection function.

    UIFLOW2:

        ![disable_irq.png](https://static-cdn.m5stack.com/mpy_docs/unit/pir/disable_irq.png)


<!-- .. method:: PIR.set_callback() -->

    Polling method, placed in the loop function, constantly check.

    UIFLOW2:

        ![set_callback.png](https://static-cdn.m5stack.com/mpy_docs/unit/pir/set_callback.png)