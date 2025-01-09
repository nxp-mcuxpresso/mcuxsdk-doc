# Internal Example, Device and Board Development

## Example

Internal examples mean examples which are located in `examples_int` repository folder. 

> In this chapter, we only focus on [repository example](./example_development.md#repository-examples), not [freestanding example](./example_development.md#freestanding-examples).

The construction of internal examples is no different from the public examples in `examples` folder. Please refer [Example Development](./example_development.md) chapter for more details.

Internal examples can support both public boards or internal boards. For public boards, internal examples **won't** be public in any cases.

## Device

Internal devices are located under `devices_int` repository folder. The construction of internal devices are no different from normal public devices. Please refer [Device](./device_board_shield_definition.md#device) chapter for more details.

In the device variable.cmake located in the root of Internal devices, the `device_root` variable shall be set to `devices_int` to indicate that the device contents are located under `devices_int` folder:

```cmake
mcux_set_variable(device_root devices_int)
```

> For public device, the `device_root` value is `devices`.

**The internal device can only be used by internal boards because either of them can or will be public.**

## Board

Internal boards are located under `examples_int/_boards` repository folder. The construction of internal boards are no different from normal public boards except the `example.yml`.  

For public boards, the board example.yml is used to provide board level supported toolchains and build configuration targets. In each example, the example self example.yml will provide customized boards/toolchains/build configuration targets which work together with board example.yml to decide the final example boards/toolchains/build configuration targets enablement status. You can refer [example.yml](./example_development.md#example-yml) chapter for more details.

For internal boards, since it cannot be exposed in the public example example.yml `boards` data attribute to indicate they are supported by the public examples, so we introduce new rules for internal board example.yml: the supported examples will be directly listed in the internal board example.yml like

```yaml
board.toolchains: 
- +armgcc@debug
- +armgcc@release
- +iar@debug
- +iar@release
- +mdk@debug
- +mdk@release

hello_world:   
  toolchains:        # optional
    - +iar@ddr_debug # add a new build configuration target
    - -mdk@debug     # reduce a build configuration target
```

In the above example, the hello_world example supports

- iar toolchain with debug, release and ddr_debug build configuration targets
- mdk toolchain with release build configuration target
- armgcc toolchain with debug and release build configuration targets

In this way, just with the single board example.yml, we can get all the supported examples with the toolchains and build  configuration targets.

In the board variable.cmake located in the root of Internal boards, the `board_root` variable shall be set to `examples_int/_boards` to indicate that the board contents are located under `examples_int/_boards` folder:

```cmake
mcux_set_variable(board_root examples_int/_boards)
```

> For public board, the `board_root` value is `examples_int/_boards`.