# Run a demo using Arm GCC {#GUID-0C8A7571-0107-4F06-993E-D81B29A5255B}

This section describes the steps to configure the command line Arm GCC tools to build, run, and debug demo applications and necessary driver libraries provided in the MCUXpresso SDK. The `hello_world`demo application is targeted which is used as an example.

Only J-Link debugging interface is supported for JLinkGDBServer and GDB. It is recommended to set `SW5[1..4]` to `0001` when using these tools to debug. It is required to reset board for each download/debug.


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

