# Debug QSPI FLASH XIP Application

Most demo applications use the RAM linker file by default. If users want to use the flash linker file for QSPI XIP debugging, the linker file for QSPI FLASH must be changed from the project default RAM linker file to the FLASH linker file.

1.  Open the hello\_world project and select the hello\_world top-level project as shown below. Once highlighted, one way to open the options is using 'Alt-F7'. This opens the option window. Then, select “Linker”. The “Config” tab is shown by default. Enable Override default and enter the location: *C:\\nxp\\SDK\_2.3\_EVK\_MCIMX7ULP\\devices\\MCIMX7U5\\iar\\MCIMX7U5xxx08\_flash.icf*.

    |![](../images/options_node_hello_world.jpg "Options for node "hello_world"")

|

    Clean the project once the linker control has been configured. Use the key combo 'Alt-P' to clean. Then, make project using the 'F7' key.

2.  Select the "Use macro files" and the "Use flashloader " as shown in the following pictures, and start debugging in IAR.

    |![](../images/use_maco_files_selection.png ""Use macro
												files"
												selection")

|

    |![](../images/use_flash_loaders_selection_imx7ulp.png ""Use flashloader
												"
												selection")

|


**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

