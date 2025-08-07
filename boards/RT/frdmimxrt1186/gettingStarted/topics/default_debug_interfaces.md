# Default debug interfaces

The MCUXpresso SDK supports various hardware platforms that come loaded with a variety of factory programmed debug interface configurations. [Table 1](default_debug_interfaces.md#TABLE_HWPLATFORMS) lists the hardware platforms supported by the MCUXpresso SDK, their default debug interface, and any version information that helps differentiate a specific interface configuration.

|Hardware platform|Default interface|OpenSDA details[1](#fntarg_1)|
|-----------------|-----------------|-----------------------------|
|EVK-​MC56F83000|P&E Micro OSJTAG|N/​A|
|EVK-​MIMXRT595|CMSIS-​DAP|N/​A|
|EVK-​MIMXRT685|CMSIS-​DAP|N/​A|
|FRDM-IMXRT1186|CMSIS-DAP|OpenSDA v2.2|
|FRDM-​K22F|CMSIS-​DAP/​mbed/​DAPLink|OpenSDA v2.​1|
|FRDM-​K28F|DAPLink|OpenSDA v2.​1|
|FRDM-​K32L2A4S|CMSIS-​DAP|OpenSDA v2.​1|
|FRDM-​K32L2B|CMSIS-​DAP|OpenSDA v2.​1|
|FRDM-​K32W042|CMSIS-​DAP|N/​A|
|FRDM-​K64F|CMSIS-​DAP/​mbed/​DAPLink|OpenSDA v2.​0|
|FRDM-​K66F|J-​Link OpenSDA|OpenSDA v2.​1|
|FRDM-​K82F|CMSIS-​DAP|OpenSDA v2.​1|
|FRDM-​KE15Z|DAPLink|OpenSDA v2.​1|
|FRDM-​KE16Z|CMSIS-​DAP/​mbed/​DAPLink|OpenSDA v2.​2|
|FRDM-​KL02Z|P&E Micro OpenSDA|OpenSDA v1.​0|
|FRDM-​KL03Z|P&E Micro OpenSDA|OpenSDA v1.​0|
|FRDM-​KL25Z|P&E Micro OpenSDA|OpenSDA v1.​0|
|FRDM-​KL26Z|P&E Micro OpenSDA|OpenSDA v1.​0|
|FRDM-​KL27Z|P&E Micro OpenSDA|OpenSDA v1.​0|
|FRDM-​KL28Z|P&E Micro OpenSDA|OpenSDA v2.​1|
|FRDM-​KL43Z|P&E Micro OpenSDA|OpenSDA v1.​0|
|FRDM-​KL46Z|P&E Micro OpenSDA|OpenSDA v1.​0|
|FRDM-​KL81Z|CMSIS-​DAP|OpenSDA v2.​0|
|FRDM-​KL82Z|CMSIS-​DAP|OpenSDA v2.​0|
|FRDM-​KV10Z|CMSIS-​DAP|OpenSDA v2.​1|
|FRDM-​KV11Z|P&E Micro OpenSDA|OpenSDA v1.​0|
|FRDM-​KV31F|P&E Micro OpenSDA|OpenSDA v1.​0|
|FRDM-​KW24|CMSIS-​DAP/​mbed/​DAPLink|OpenSDA v2.​1|
|FRDM-​KW36|DAPLink|OpenSDA v2.​2|
|FRDM-​KW41Z|CMSIS-​DAP/​DAPLink|OpenSDA v2.​1 or greater|
|Hexiwear|CMSIS-​DAP/​mbed/​DAPLink|OpenSDA v2.​0|
|HVP-​KE18F|DAPLink|OpenSDA v2.​2|
|HVP-​KV46F150M|P&E Micro OpenSDA|OpenSDA v1|
|HVP-​KV11Z75M|CMSIS-​DAP|OpenSDA v2.​1|
|HVP-​KV58F|CMSIS-​DAP|OpenSDA v2.​1|
|HVP-​KV31F120M|P&E Micro OpenSDA|OpenSDA v1|
|JN5189DK6|CMSIS-​DAP|N/​A|
|LPC54018 IoT Module|N/​A|N/​A|
|LPCXpresso54018|CMSIS-​DAP|N/​A|
|LPCXpresso54102|CMSIS-​DAP|N/​A|
|LPCXpresso54114|CMSIS-​DAP|N/​A|
|LPCXpresso51U68|CMSIS-​DAP|N/​A|
|LPCXpresso54608|CMSIS-​DAP|N/​A|
|LPCXpresso54618|CMSIS-​DAP|N/​A|
|LPCXpresso54628|CMSIS-​DAP|N/​A|
|LPCXpresso54S018M|CMSIS-​DAP|N/​A|
|LPCXpresso55s16|CMSIS-​DAP|N/​A|
|LPCXpresso55s28|CMSIS-​DAP|N/​A|
|LPCXpresso55s69|CMSIS-​DAP|N/​A|
|MAPS-​KS22|J-​Link OpenSDA|OpenSDA v2.​0|
|MIMXRT1170-​EVK|CMSIS-​DAP|N/​A|
|MIMXRT1180-​EVK|CMSIS-DAP|OpenSDA v2.2|
|TWR-​K21D50M|P&E Micro OSJTAG|N/​AOpenSDA v2.​0|
|TWR-​K21F120M|P&E Micro OSJTAG|N/​A|
|TWR-​K22F120M|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​K24F120M|CMSIS-​DAP/​mbed|OpenSDA v2.​1|
|TWR-​K60D100M|P&E Micro OSJTAG|N/​A|
|TWR-​K64D120M|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​K64F120M|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​K65D180M|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​K65D180M|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​KV10Z32|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​K80F150M|CMSIS-​DAP|OpenSDA v2.​1|
|TWR-​K81F150M|CMSIS-​DAP|OpenSDA v2.​1|
|TWR-​KE18F|DAPLink|OpenSDA v2.​1|
|TWR-​KL28Z72M|P&E Micro OpenSDA|OpenSDA v2.​1|
|TWR-​KL43Z48M|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​KL81Z72M|CMSIS-​DAP|OpenSDA v2.​0|
|TWR-​KL82Z72M|CMSIS-​DAP|OpenSDA v2.​0|
|TWR-​KM34Z75M|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​KM35Z75M|DAPLink|OpenSDA v2.​2|
|TWR-​KV10Z32|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​KV11Z75M|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​KV31F120M|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​KV46F150M|P&E Micro OpenSDA|OpenSDA v1.​0|
|TWR-​KV58F220M|CMSIS-​DAP|OpenSDA v2.​1|
|TWR-​KW24D512|P&E Micro OpenSDA|OpenSDA v1.​0|
|USB-​KW24D512|N/​A External probe|N/​A|
|USB-​KW41Z|CMSIS-​DAP\\DAPLink|OpenSDA v2.​1 or greater|

[1](#fnsrc_1) The OpenSDA details is not applicable to LPC.

