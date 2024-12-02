# Add a new system environment variable for ARMGCC\_DIR

Create a new *system* environment variable and name it `ARMGCC_DIR`. The value of this variable should point to the Arm GCC Embedded tool chain installation path. For this example, the path is:

```
$ export ARMGCC_DIR=/work/platforms/tmp/gcc-arm-none-eabi-<version>
```

```
$ export PATH= $PATH:/work/platforms/tmp/gcc-arm-none-eabi-<version>/bin
```

**Note:** If the ArmGCC version is not known, see the corresponding release notes document.

**Parent topic:**[Set up toolchain](../topics/set_up_toolchain_001.md)

