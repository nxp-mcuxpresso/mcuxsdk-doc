# Add a new system environment variable for ARMGCC\_DIR

Create a new *system* environment variable and name it `ARMGCC_DIR`. The value of this variable should point to the Arm GCC Embedded tool chain installation path. For this example, the path is:

```
$ export ARMGCC_DIR=/work/platforms/tmp/gcc-arm-none-eabi-7-2017-q4-major
```

```
$ export PATH= $PATH:/work/platforms/tmp/gcc-arm-none-eabi-7-2017-q4-major/bin
```

**Parent topic:**[Set up toolchain](../topics/set_up_toolchain_001.md)

