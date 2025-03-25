# EdgeFast_Bluetooth handsfree example codec init fail

The audio codec initialization can fail during "bt aincall" command.

**Workaround**: Manually release the I2C bus by temporarily configuring the I2C pin as GPIO before codec initialization
**Examples**: handsfree, handsfree_ag
**Affected platforms**: mimxrt700evk