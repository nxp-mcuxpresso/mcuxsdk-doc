# Run a demo using Arm GCC

This section describes the steps to configure the command line Arm GCC tools to build, run, and debug demo applications and necessary driver libraries provided in the MCUXpresso SDK. The `hello_world`demo application is targeted which is used as an example.

Only J-Link debugging interface is supported for JLinkGDBServer and GDB. **Since Segger is not ready for FRDMIMXRT1186 currently, 3rd party patch is provided: [iar_segger_support_patch_rt1186](https://mcuxpresso.nxp.com/download/e8ca8e655b4a5eeff3d9265ef11fa3f2)**


```{include} ../topics/armgcc_set_up_toolchain.md
:heading-offset: 1
```

```{include} ../topics/armgcc_build_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/armgcc_run_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/armgcc_build_and_run_a_multicore_example_application.md
:heading-offset: 1
```

