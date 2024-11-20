# Build a TrustZone example application {#GUID-AD3F048E-11BB-4AA5-83AA-0064F54B30AF}

This section describes the particular steps that must be done in order to build and run a TrustZone application. The demo applications workspace files are located in this folder:

```
<install_dir>/boards/<board_name>/trustzone_examples/<application_name>/<core_type>/iar/<application_name>_ns/iar
```

```
<install_dir>/boards/<board_name>/trustzone_examples/<application_name>/<core_type>/iar/<application_name>_s/iar
```

Begin with a simple TrustZone version of the Hello World application. The TrustZone Hello World IAR workspaces are located in this folder:

```
<install_dir>/boards/lpcxpresso55s69/trustzone_examples/hello_world/cm33_core0/hello_world_ns/iar/hello_world_ns.eww
```

```
<install_dir>/boards/lpcxpresso55s69/trustzone_examples/hello_world/cm33_core0/hello_world_s/iar/hello_world_s.eww
```

```
<install_dir>/boards/lpcxpresso55s69/trustzone_examples/hello_world/cm33_core0/hello_world_s/iar/hello_world.eww
```

This project `hello_world.eww` contains both secure and non-secure projects in one workspace and it allows the user to easily transition from one project to another. Build both applications separately by clicking **Make**. It is requested to build the application for the secure project first, because the non-secure project must know the secure project, since the CMSE library is running the linker. It is not possible to finish the non-secure project linker with the secure project since CMSE library is not ready.

**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

