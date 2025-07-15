# Modify dummy cycles value for external qspi flash

More NXP SOCs now support executed code in external flash. Projects require higher QSPI speed. According to QSPI flash device
datasheet descriptions, higher QSPI speed operates stably only when you pair it with the appropriate dummy cycle value.

Note that some board XIP files directly modify the dummy cycle value in external flash through ROM using the volatile method.
Such modifications may not work with released toolchain versions. Upgrade the current toolchain to the latest version. NXP
also optimizes the corresponding flashloader.

When users modify dummy cycle value in non-volatile register of external flash, the NXP flashloader becomes invalid. Users
need to create their own flashloader to adapt to the external flash dummy cycle requirements.

**Affected platforms**: mimxrt1020-evk, mimxrt1060-evkb, mimxrt1160-evk, mimxrt1170-evkb