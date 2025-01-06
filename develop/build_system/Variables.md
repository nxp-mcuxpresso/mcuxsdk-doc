# Variables

Variable mechanism is introduced to facilitate data record in both CMake and Kconfig for MCUXpresso SDK.

For example in a cmake file with a `board` variable in the `BASE_PATH`, one copy of the following project segment data can be shared by all boards examples without any duplication.

```cmake
if(CONFIG_MCUX_PRJSEG_module.board.suite)
    mcux_add_source(
        BASE_PATH ${SdkRootDirPath}/examples/_boards/${board} # "board" variable shall be defined in each board so that each board can use this project segment
        SOURCES dcd.c dcd.h
    )
endif()
```

In Kconfig, the same `board` variable can set the board Kconfig path for all boards.

```bash
rsource "${board}/Kconfig"
```

There are some required variables which must be provided for each build to make the CMake configuration process run passed.

Besides, customized variables are allowed for some software data recorded although not suggested.

## Required Variables

There are some required variables which shall be defined in advance to make the build workable. These variables are generally related to hardware related information. All these required variables can be defined in cmake files, but to enable the switch across device parts in run time with Kconfig, most hardware related variables are moved into `Kconfig.chip` because Kconfig mechanism can make sure that when you switch device part, all related variables can be switch at the same time.

Here is the cmake files stored variable table:

| Variable Name        |      | Explanation                              | Acquisition                              | Used in           |
| -------------------- | ---- | ---------------------------------------- | ---------------------------------------- | ----------------- |
| SdkRootDirPath       |      | SDK root directory<br />Specify sdk root path | Automatically set by build system        | CMake             |
| board                |      | board name, like evkbmimxrt1170          | Provided in cli argument, also need to record it in board<br /> variable cmake | CMake and Kconfig |
| board_root           |      | board root folder<br />For public boards, it is `examples/_boards`<br />For internal boards, it is `examples_int/_boards` | Board variable cmake                     | CMake and Kconfig |
| device               |      | device name, like MIMXRT1176             | Device variable cmake                    | CMake and Kconfig |
| device_root          |      | device root folder<br />For public devices, it is `devices`<br />For internal devices, it is `devices_int` | Device variable cmake                    | CMake and Kconfig |
| soc_series           |      | soc series, like RT1170                  | Device variable cmake                    | CMake and Kconfig |
| soc_portfolio        |      | soc portfolio, like RT                   | Soc portfolio variable cmake             | CMake and Kconfig |
| soc_periph           |      | soc periph, like periph                  | Device variable cmake                    | CMake and Kconfig |
| core_id              |      | Core id, like cm33_core0                 | Device variable cmake. This is only required for multicore device. | Kconfig           |
| core_id_suffix_name  |      | Core id suffix name                      | Device variable cmake                    | CMake             |
| multicore_foldername |      | multicore folder name                    | Device variable cmake                    | CMake             |

The above variables shall anyway be provided in CMake because they are used by Kconfig process.

## Customized Variables

Besides above variables, you can set your own variables in CMake to facilitate your data record with extension `mcux_set_variable`.

- For the required variables, build system will guarantee that they are defined before used.
- For you customized variables, **please make sure that your variables are defined before used**.

## Tips For Variable Usage

- Variable value replacement is invisible in CMake process, to avoid potential issues, please minimize the usage of variable.
- To make Kconfig integrable for other Kconfig system, please don't use variables in Kconfig data other than `rsource`. `rsource` is only to load Kconfig files and it only support required variables, not customized ones.
