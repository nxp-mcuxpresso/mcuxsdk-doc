# Kconfig memory optimizer
The MCUXpresso SDK provides options to reduce the host memory usage with build-time configuration parameters referred to as Kconfig memory optimizer. The configuration parameters are used to reduce the use of the flash memory and SRAM. 

This section explains how to enable the host memory saving configurations within the Wi-Fi drivers of NXP wireless devices.

Memory impact of i.MX RT1060 EVKC + IW416 module (Murata 1XK):

-   Maximum Flash usage: 889 KB
-   Maximum SRAM usage: 418.77 KB

To reduce the use of the flash and SRAM, change the settings of the Kconfig macros listed in table in the file wifi_config.h located in <path-to-SDK_Wi-Fi_Example> directory.

|Kconfig macros|Feature disabled|
|-----------|----------------|
|CONFIG\_WIFI\_SLIM\_ROAM|CONFIG\_ROAMING <br>CONFIG\_11R|
|CONFIG\_WIFI\_SLIM\_STA|<br>CONFIG\_CLOUD\_KEEP\_ALIVE <br>CONFIG\_WIFI\_EU\_CRYPTO <br>CONFIG\_TX\_AMPDU\_PROT\_MODE <br>CONFIG\_WNM\_PS CONFIG\_TURBO\_MODE <br>CONFIG\_AUTO\_RECONNECT <br>CONFIG\_DRIVER\_OWE CONFIG\_OWE <br>CONFIG\_WIFI\_FORCE\_RTS <br>CONFIG\_WIFI\_FRAG\_THRESHOLD <br>CONFIG\_COMBO\_SCAN <br>CONFIG\_SCAN\_CHANNEL\_GAP|
|CONFIG\_WIFI\_SLIM\_UAP|CONFIG\_UAP\_STA\_MAC\_ADDR\_FILTER <br>CONFIG\_WIFI\_MAX\_CLIENTS\_CNT|
|CONFIG\_FREERTOS\_LOW\_MEMORY\_FOOTPRINT|If the macro is enabled, the heap memory usage is reduced by 10 KB \(from 70 KB to 60 KB\).|
|CONFIG\_LWIP\_LOW\_MEM\_FOOTPRINT|Curtails LWIP stack parameters, reduces data throughput, disables data net-stats|
|Non-blocking firmware download mechanism|CONFIG_FW_DNLD_ASYNC|

**Parent topic:**[Feature enable and memory impact](../topics/feature_enable_and_memory_impact.md)

