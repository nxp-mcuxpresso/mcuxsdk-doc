# Device support {#topic_gfn_ldj_lyb}

The device folder contains the whole software enablement available for the specific System-on-Chip \(SoC\) subfamily. This folder includes clock-specific implementation, device register header files, device register feature header files, CMSIS derived device SVD, and the system configuration source files. Included with the standard SoC support are folders containing peripheral drivers, toolchain support, and a standard debug console.

The device-specific header files provide a direct access to the microcontroller peripheral registers. The device header file provides an overall SoC memory mapped register definition. The folder also includes the feature header file for each peripheral on the microcontroller.

The toolchain folder contains the startup code and linker files for each supported toolchain. The startup code is a CMSIS-compliant startup code that efficiently transfers the code execution to the `main()` function.


```{include} ../topics/board_support.md
:heading-offset: 2
```

```{include} ../topics/demo_applications_and_other_examples.md
:heading-offset: 2
```

**Parent topic:**[MCUXpresso SDK release package](../topics/mcuxpresso_sdk_release_package.md)

