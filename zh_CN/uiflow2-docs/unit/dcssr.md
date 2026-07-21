# DCSSR Unit


<!-- .. include:: ../refs/unit.dcssr.ref -->

Support the following products:

    ![DCSSR Unit](https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR%20Unit/img-5e00db88-b5c7-4dd9-9061-b4700dc60c6e.webp)


## class DCSSRUnit


## Constructors


<!-- .. class:: DCSSRUnit(bus, address=0x50) -->

    Create an DCSSRUnit object.

    :param i2c: I2C bus or Modbus.
    :param address: Slave address. Default is 0x50 in I2C mode. Default is 0x04 in Modbus mode.

    UIFLOW2:

        ![init.png](https://static-cdn.m5stack.com/mpy_docs/unit/dcssr/init.png)


DCSSRUnit class inherits ACSSRUnit class, See :ref:`unit.ACSSRUnit.Methods <unit.ACSSRUnit.Methods>` for more details.