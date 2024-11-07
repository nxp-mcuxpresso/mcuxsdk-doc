# MCUXpresso config tools

MCUXpresso Config Tools can help configure the processor and generate initialization code for the on chip peripherals. The tools are able to modify any existing example project, or create a new configuration for the selected board or processor. The generated code is designed to be used with MCUXpresso SDK version 2.x.

[Table 1](mcuxpresso_config_tools.md#TABLE_CONFIGTOOL) describes the tools included in the MCUXpresso config tools.

|Config tool|Description|Image|
|:---------:|-----------|:---:|
|**Pins tool**|For configuration of pin routing and pin electrical properties.​|![](../images/pins_tool.png)|
|**Clock tool**|For system clock configuration|![](../images/clock_tool.png)|
|**Peripherals tools**|For configuration of other peripherals|![](../images/peripheral_tool.png)|
|**TEE tool**|Configures access policies for memory area and peripherals helping to protect and isolate sensitive parts of the application.​|![](../images/tee_tool.png)|
|**Device Configuration tool**|Configures Device Configuration Data \(DCD\) contained in the program image that the Boot ROM code interprets to setup various on-​chip peripherals prior the program launch.​|![](../images/device_configuration_tool.png)|

MCUXpresso Config Tools can be accessed in the following products:

-   **Integrated** in the MCUXpresso IDE. Config tools are integrated with both compiler and debugger which makes it the easiest way to begin the development.
-   **Standalone version** available for download from [MCUXPRESSO](http://www.nxp.com/mcuxpresso). Recommended for customers using IAR Embedded Workbench, Keil MDK µVision, or Arm GCC.
-   **Online version** available on [MCUXPRESSO](http://mcuxpresso.nxp.com). Recommended to do a quick evaluation of the processor or use the tool without installation.

Each version of the product contains a specific *Quick Start Guide* document MCUXpresso IDE Config Tools installation folder that can help start your work.

