# Complex Dependency

MCUXpresso SDK build system provides complex dependencies record and resolve for both sections(examples and components) and sources.

## Section Level Dependency

[Kconfig](https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html) dependency mechanism and tool is used to describe and resolve section level dependency.

### Dependency Mechanisms

[Kconfig](https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html) provides `depends on`, `select` and `choice` dependency mechanisms.

- depends on

  It defines a dependency for Kconfig symbol. If multiple dependencies are defined, they can be connected with `&&`, `||`, and `!` for NOT.

  The Kconfig item won’t be showed if the `depends on` is not satisfied.
- select

  It forces a symbol to true which means the depended component is selected anyway no matter its dependency is satisfied or not.
- choice

  It defines a choice group. The single choice can only be of type bool or tristate. If no type is specified for a choice, its type will be determined by the type of the first choice element in the group or remain unknown if none of the choice elements have a type specified.

Kconfig processor will give detailed warnings about unsatisfied component selection so that  you can immediately find it and update.

### Practice Recommendation

- For software components depending on hardware related dependency items like `board`, `device`, `device_id`, please use `depends on`. In this way, for any component whose hardware dependencies are not satisfied, it will not be showed so that not bloat the Kconfig GUI.
- For software components depending on software component, priority to use `select`. It helps to auto select component dependency.
- For cycle dependency case like FOO needs to `select` BAR and BAR needs to `select` FOO, since Kconfig doesn't support cycle dependency, so you cannot use mutually `select` between FOO and BAR. The recommendation is use both `select` and `depends on`. For example, FOO `select` BAR and BAR `depends on` FOO. In this way, when you  tick FOO, then BAR will be automatically selected. When FOO dependency is not satisfied, BAR cannot be showed.
- If there are `any of` dependencies, `choice` can satisfy the need.

### Hardware Dependency Items

Following Harry dependency items are provided for components to `depends on`:

| Dependency Item               | Illustration                         |
| ----------------------------- | ------------------------------------ |
| MCUX_HW_DEVICE_\<device>      | Device, like MIMXRT1176              |
| MCUX_HW_DEVICE_ID_\<device_id>| Device id, like MIMXRT1176xxxxx      |
| MCUX_HW_CORE_\<core_name>     | Core name, like cm4f                 |
| MCUX_HW_CORE_ID_\<core_id>    | Core id, like cm4                    |
| MCUX_HW_BOARD_\<board name>   | Board name, like evkbmimxrt1170      |
| MCUX_HW_KIT_\<kit name>       | Kit name, like mimxrt700evk_a8974    |
| MCUX_HW_\<fpu type>           | fpu type name, like  MCUX_HW_FPV4_SP |
| MCUX_HW_DSP                   | DSP or no DSP                        |
| MCUX_HW_MPU                   | MPU or no MPU                        |
| MCUX_HW_SAU                   | Secure or nonsecure                  |

**All these dependency items shall be defined in device Kconfig.chip.**

## Source Level Dependency

Source level dependency is achieved through the CMake extension, like

```cmake
mcux_add_source(
    SOURCES portable/GCC/ARM_CM0/port.c
    # The following 2 lines mean port.c only supports cm0p core and toolchain armgcc, mcux and mdk
    CORES cm0p
    TOOLCHAINS armgcc mcux mdk
)
```

Please refer the [mcux_add_source/mcux_add_include extension arguments](./Build_System.md#source-and-include) for supported dependency items.
