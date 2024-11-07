# Build a TrustZone example application

This section describes the steps to build and run a TrustZone application. The demo application build scripts are located in this folder:

```
<install_dir>/boards/<board_name>/trustzone_examples/<application_name>/[<core_type>]/<application_name>_ns/armgcc
```

```
<install_dir>/boards/<board_name>/trustzone_examples/<application_name>/[<core_type>]/<application_name>_s/armgcc
```

Begin with a simple TrustZone version of the Hello World application. The TrustZone Hello World GCC build scripts are located in this folder:

```
<install_dir>/boards/evkmimxrt685/trustzone_examples/hello_world/hello_world_ns/armgcc/build_debug.bat
```

```
<install_dir>/boards/evkmimxrt685/trustzone_examples/hello_world/hello_world_s/armgcc/build_debug.bat
```

Build both applications separately, following steps for single core examples as described in *Section 6.2, "Build an example application”*. It is requested to build the application for the secure project first, because the non-secure project must know the secure project, since CMSE library is running the linker. It is not possible to finish the non-secure project linker with the secure project because the CMSE library is not ready.

|![](../images/hello_world_s_example_build_successful_arm_trustzo.jpg "hello_world_s
									example
									build successful")

|

|![](../images/hello_world_ns_example_build_successful_arm_trustz.jpg "hello_world_ns example build
									successful")

|

**Parent topic:**[Run a demo using Arm GCC](../topics/run_a_demo_using_arm__gcc.md)
