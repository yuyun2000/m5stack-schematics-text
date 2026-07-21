<!-- .. currentmodule:: bleuart -->

# class BLEUARTServer


<!-- .. include:: ../refs/system.bleuart.server.ref -->

BLEUARTServer class is a BLE UART server, which can be connected to by a BLE UART client and communicate with it.


Micropython Example:

```python
# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

import os, sys, io
import M5
from M5 import *
from bleuart import *
import time


label0 = None
ble_periph = None


data = None


def setup():
    global label0, ble_periph, data

    M5.begin()
    Widgets.fillScreen(0x222222)
    label0 = Widgets.Label("Text", 20, 31, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)

    ble_periph = BLEUARTServer(name="ble-uart")


def loop():
    global label0, ble_periph, data
    M5.update()
    if (ble_periph.any()) > 0:
        data = ble_periph.read()
        label0.setText(str(data))
        ble_periph.write(data)
    else:
        time.sleep_ms(100)


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

    ![example.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/example.png)


<!-- .. only:: builder_html -->

    [cores3_bleuart_server_example.m5f2]


## Constructors


<!-- .. class:: bleuart.BLEUARTServer(name="", rxbuf=100, verbose=False) -->

    Create a BLE UART server.

    :param str name: The name of the ble device.
    :param int rxbuf: The size of the receive buffer.
    :param bool verbose: Enable verbose output.

    UIFLOW2:

        ![init.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/init.png)


## Methods


<!-- .. method:: BLEUARTServer.irq() -->

    The irq of the ble uart server.


<!-- .. method:: BLEUARTServer.any() -> int -->

    Check if there is any data in the receive buffer.

    :return: The number of bytes in the receive buffer.

    UIFLOW2:

        ![any.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/any.png)


<!-- .. method:: BLEUARTServer.read(sz=None) -> bytes -->

    Read data from the receive buffer.

    :param int sz: The number of bytes to read. If not specified, read all data.

    :return: The data read from the receive buffer.

    UIFLOW2:

        ![read_all.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/read_all.png)

        ![read_bytes.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/read_bytes.png)

        ![read_raw_data.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/read_raw_data.png)

        ![readline.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/readline.png)


<!-- .. method:: BLEUARTServer.write(data: bytes) -->

    Write data to the ble uart server.

    :param bytes data: The data to write.

    UIFLOW2:

        ![write.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/write.png)

        ![write1.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/write1.png)

        ![write_line.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/write_line.png)

        ![write_list.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/write_list.png)

        ![write_raw_data.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/write_raw_data.png)

        ![write_raw_data1.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/write_raw_data1.png)


<!-- .. method:: BLEUARTServer.close() -->

    Close the ble uart server.

    UIFLOW2:

        ![close.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/close.png)

<!-- .. method:: BLEUARTServer.deinit() -->

    Deinitialize the ble uart server.

    UIFLOW2:

        ![deinit.png](https://static-cdn.m5stack.com/mpy_docs/system/ble_uart/server/deinit.png)