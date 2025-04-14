# I2C sometimes fails to initialize accelerometer after flash or reset

The example has problem with identification of accelerometer.

**Solution:** Reset the I2C bus to its default state before initializing the sensor.
(Solution code will be added in next release.)

**Examples:** bubble, flexio_i2c_read_accel_value_transfer

**Affected toolchains:** mcux, iar, armgcc

**Affected platforms:** frdmmcxe31b