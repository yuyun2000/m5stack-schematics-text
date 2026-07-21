# IR Unit


<!-- .. include:: ../refs/unit.ir.ref -->

Support the following products:

    ![IR](https://static-cdn.m5stack.com/resource/docs/products/unit/ir/ir_01.webp)


Micropython Example:

```python
import os, sys, io
import M5
from M5 import *
from unit import IRUnit
import time


ir_0 = None


def setup():
    global ir_0

    M5.begin()
    Widgets.fillScreen(0x222222)

    ir_0 = IRUnit((36, 26))


def loop():
    global ir_0
    M5.update()
    ir_0.tx(0, 0)
    time.sleep(1)


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

    ![example.png](https://static-cdn.m5stack.com/mpy_docs/unit/ir/example.png)


<!-- .. only:: builder_html -->

    [ir_core_example.m5f2]


## class IRUnit


## Constructors


<!-- .. class:: IRUnit(port) -->

    Create an IRUnit object.

    :param tuple port: The port to which the IR unit is connected. the tuple is a pair of values, the first value is the receive pin, and the second value is the transmit pin.

    UIFLOW2:

        ![init.png](https://static-cdn.m5stack.com/mpy_docs/unit/ir/init.png)


## Methods


<!-- .. method:: IRUnit.tx() -->

    Sends an ir signal value to an address.

    UIFLOW2:

        ![tx.png](https://static-cdn.m5stack.com/mpy_docs/unit/ir/tx.png)


<!-- .. method:: IRUnit.rx_event() -->

    Determine when the infrared signal is read and start to do some processing procedures.

    UIFLOW2:

        ![rx_event.png](https://static-cdn.m5stack.com/mpy_docs/unit/ir/rx_event.png)