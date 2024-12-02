# Build a TrustZone example application

This section describes the particular steps that need to be done in order to build and run a TrustZone application. The demo applications workspace files are located in this folder:

```
<install_dir>/boards/<board_name>/trustzone_examples/<application_name>/iar/<application_name>_ns/mdk
```

```
<install_dir>/boards/<board_name>/trustzone_examples/<application_name>/iar/<application_name>_s/mdk
```

Begin with a simple TrustZone version of the Hello World application. The TrustZone Hello World Keil MSDK/μVision ® workspaces are located in this folder:

```
<install_dir>/boards/lpcxpresso55s16/trustzone_examples/hello_world/hello_world_ns/iar/hello_world_ns.eww
```

```
<install_dir>/boards/lpcxpresso55s16/trustzone_examples/hello_world/hello_world_s/mdk/hello_world_s.uvmpw
```

```
<install_dir>/boards/lpcxpresso55s16/trustzone_examples/hello_world/hello_world_s/iar/hello_world.eww
```

This project `hello_world.uvmpw` contains both secure and non-secure projects in one workspace and it allows the user to easily transition from one project to another.

Build both applications separately by clicking **Rebuild**. It is requested to build the application for the secure project first, because the non-secure project needs to know the secure project since CMSE library is running the linker. It is not possible to finish the non-secure project linker with the secure project because CMSE library is not ready.

**Parent topic:**[Run a demo using Keil® MDK/μVision](../topics/run_a_demo_using_keil__mdk_vision.md)

