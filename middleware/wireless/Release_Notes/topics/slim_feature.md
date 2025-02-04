# SLIM feature {#topic_d2a98636-e88b-43ee-b8e4-c9be1a554855}

The SLIM feature is used to reduce the consumption of the flash memory and SRAM of low-end boards like the FRDM MCXN947.

Memory impact:

-   Maximum Flash usage: 607.62 KB \(29.67%\).
-   Maximum SRAM usage: 297.73 KB \(58.15%\)

|SLIM macros|Feature disabled|
|-----------|----------------|
|CONFIG\_WIFI\_SLIM\_ROAM|CONFIG\_ROAMING<br>CONFIG\_11K<br> CONFIG\_11V <br>CONFIG\_11R|
|CONFIG\_WIFI\_SLIM\_STA|CONFIG\_5GHz\_SUPPORT\ (applicable for RW612\) <br>CONFIG\_CLOUD\_KEEP\_ALIVE <br>CONFIG\_WIFI\_EU\_CRYPTO <br>CONFIG\_TX\_AMPDU\_PROT\_MODE <br>CONFIG\_WNM\_PS CONFIG\_TURBO\_MODE <br>CONFIG\_AUTO\_RECONNECT <br>CONFIG\_DRIVER\_OWE CONFIG\_OWE <br>CONFIG\_WIFI\_FORCE\_RTS <br>CONFIG\_WIFI\_FRAG\_THRESHOLD <br>CONFIG\_COMBO\_SCAN <br>CONFIG\_SCAN\_CHANNEL\_GAP|
|CONFIG\_WIFI\_SLIM\_UAP|CONFIG\_UAP\_STA\_MAC\_ADDR\_FILTER <br>CONFIG\_WIFI\_MAX\_CLIENTS\_CNT|
|CONFIG\_FREERTOS\_LOW\_MEMORY\_FOOTPRINT|When the macro is enabled, the heap memory usage is reduced by 10 KB \(from 70 KB to 60 KB\).|
|CONFIG\_LWIP\_LOW\_MEM\_FOOTPRINT|When the macro is enabled:<ul><li>The memory usage is reduced by curtailing LWIP stack parameters.</li><li>The data throughput is reduced.</li><li>Data net-stats are disabled.</li></ul>|

**Parent topic:**[Feature enable and memory impact](../topics/feature_enable_and_memory_impact.md)

