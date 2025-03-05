# Run a demo using Arm GCC

This section describes the steps to configure the command-line Arm GCC tools to build, run, and debug demo applications and necessary driver libraries provided in the MCUXpresso SDK. The `hello_world` demo application is targeted for the RD-RW61X hardware platform which is used as an example.

**Note:** ARMGCC version 8-2019-q3 is used as an example in this document. The latest GCC version for this package is as described in the *MCUXpresso SDK Release Notes Supporting RD-RW61X* \(document MCUXSDKRDRW61XRN\). IAR/Segger officially does not support RW61x. Therefore, contact the support team to get iar\_segger\_support\_patch\_rw610\_prc.zip and install the JLink patch before debugging with gdb.


```{include} ../topics/set_up_toolchain.md
:heading-offset: 1
```

```{include} ../topics/build_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/run_an_example_application_002.md
:heading-offset: 1
```

