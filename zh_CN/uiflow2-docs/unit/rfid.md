
# RFID Unit

<!-- .. sku:U031 -->
<!-- .. include:: ../refs/unit.rfid.ref -->

RFIDUnit is a hardware module designed for RFID card reading and writing operations. It extends the MFRC522 driver, supporting card detection, reading, writing, and advanced features like selecting and waking up RFID cards.

Support the following products:

![RFIDUnit](https://static-cdn.m5stack.com/resource/docs/products/unit/rfid/rfid_01.webp)

Micropython Example:

```python
# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

import os, sys, io
import M5
from M5 import *
from hardware import *
from unit import RFIDUnit
import time


title0 = None
i2c0 = None
rfid_0 = None


def setup():
    global title0, i2c0, rfid_0

    M5.begin()
    Widgets.fillScreen(0x222222)
    title0 = Widgets.Title(
        "RFIDUnit CoreS3 Example", 3, 0xFFFFFF, 0x0000FF, Widgets.FONTS.DejaVu18
    )

    i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
    rfid_0 = RFIDUnit(i2c0)


def loop():
    global title0, i2c0, rfid_0
    print(rfid_0.is_new_card_present())
    print(rfid_0.read_card_uid())
    print(rfid_0.read(1))
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

    ![example.png](https://static-cdn.m5stack.com/mpy_docs/unit/rfid/example.png)

<!-- .. only:: builder_html -->

    [rfid_cores3_example.m5f2]

## class RFIDUnit


## Constructors


<!-- .. class:: RFIDUnit(i2c, address) -->

    Initialize the RFIDUnit with I2C communication and an optional address.

    :param  i2c: The I2C interface instance.
    :param int address: The I2C address of the RFIDUnit. Default is 0x28.

    UIFLOW2:

        ![init.png](https://static-cdn.m5stack.com/mpy_docs/unit/rfid/init.png)


## Methods


<!-- .. method:: RFIDUnit.is_new_card_present() -->

    Check if a new RFID card is present.


    UIFLOW2:

        ![is_new_card_present.png](https://static-cdn.m5stack.com/mpy_docs/unit/rfid/is_new_card_present.png)

<!-- .. method:: RFIDUnit.read_card_uid() -->

    Read the UID of the RFID card if available.


    UIFLOW2:

        ![read_card_uid.png](https://static-cdn.m5stack.com/mpy_docs/unit/rfid/read_card_uid.png)

<!-- .. method:: RFIDUnit.read(block_addr) -->

    Read a specific block from the RFID card.

    :param  block_addr: The block address to read data from.

    UIFLOW2:

        ![read.png](https://static-cdn.m5stack.com/mpy_docs/unit/rfid/read.png)

<!-- .. method:: RFIDUnit.write(block_addr, buffer) -->

    Write data to a specific block on the RFID card.

    :param  block_addr: The block address to write data to.
    :param  buffer: The data buffer to write to the block.

    UIFLOW2:

        ![write.png](https://static-cdn.m5stack.com/mpy_docs/unit/rfid/write.png)

<!-- .. method:: RFIDUnit.close() -->

    Halt the PICC and stop the encrypted communication session.


    UIFLOW2:

        ![close.png](https://static-cdn.m5stack.com/mpy_docs/unit/rfid/close.png)

<!-- .. method:: RFIDUnit.wakeup_all() -->

    Wake up all RFID cards within range.

<!-- .. method:: RFIDUnit.picc_select_card() -->

    Select the currently active RFID card.