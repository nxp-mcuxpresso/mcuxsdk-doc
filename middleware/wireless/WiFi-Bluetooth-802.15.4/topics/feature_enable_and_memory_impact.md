# Feature enable and memory impact

|Features|Macros to enable the feature|Memory impact|
|--------|----------------------------|-------------|
|CSI|CONFIG\_CSI|Flash - 60K, RAM - 4K|
|DPP|CONFIG\_WPA\_SUPP\_DPP|Flash - 240K, RAM - 12K|
|Independent reset|CONFIG\_WIFI\_IND\_DNLD<br>CONFIG\_WIFI\_IND\_RESET|Minimal|
|Parallel firmware download Wi-Fi|CONFIG\_WIFI\_IND\_DNLD|Minimal|
|Parallel firmware download Bluetooth|CONFIG\_BT\_IND\_DNLD|Minimal|
|WPA3 enterprise|CONFIG\_WPA\_SUPP\_CRYPTO\_ENTERPRISE \[Macros specific to EAP-methods included\] <br>CONFIG\_EAP\_TLS <br>CONFIG\_EAP\_PEAP <br>CONFIG\_EAP\_TTLS <br>CONFIG\_EAP\_FAST <br>CONFIG\_EAP\_SIM <br>CONFIG\_EAP\_AKA <br>CONFIG\_EAP\_AKA\_PRIME|Flash - 165K, RAM - 18K|
|WPA2 enterprise|CONFIG\_WPA\_SUPP\_CRYPTO\_ENTERPRISE \[Macros specific to EAP-methods included\]<br> CONFIG\_EAP\_TLS <br>CONFIG\_EAP\_PEAP <br>CONFIG\_EAP\_TTLS <br>CONFIG\_EAP\_FAST <br>CONFIG\_EAP\_SIM <br>CONFIG\_EAP\_AKA <br>CONFIG\_EAP\_AKA\_PRIME|Flash - 165K, RAM - 18K|
|Host sleep|CONFIG\_HOST\_SLEEP|Minimal|
|WMM|CONFIG\_WMM<sup>1</sup>|Flash - 10K, RAM - 57K|
|802.11mc|CONFIG\_11MC <br>CONFIG\_CSI <br>CONFIG\_WLS\_CSI\_PROC<sup>2</sup> <br>CONFIG\_11AZ|Flash: 52.78KB, RAM : 121.1KB|
|802.11az|CONFIG\_11MC <br>CONFIG\_CSI\[2\] <br>CONFIG\_WLS\_CSI\_PROC<sup>2</sup> <br>CONFIG\_11AZ|Flash: 52.78KB, RAM : 121.1KB|
|Non-blocking firmware download mechanism|CONFIG\_FW\_DNLD\_ASYNC|—|
|Antenna diversity|CONFIG_WLAN_CALDATA_2ANT_DIVERSITY|-|
|P2P|CONFIG_WPA_SUPP_P2P |-|

**Note:**

-   For Wi-Fi, the macros are set with the value “**0**” by default in the file wifi\_config\_default.h located in <SDK\_PATH\>/middleware/wifi\_nxp/incl/ directory.

    To enable the features, set the value of the macros to “***1****” in the file wifi\_config.h located in*<SDK\_Wi-Fi\_Example\_PATH\>/ *directory****.***

-   Bluetooth

    To enable the features, set the value of the macros to “**1**” in the file app\_bluetooth\_config.h located in <SDK\_Bluetooth\_Example\_PATH\>/ directory.



[1] The macro is not used for IW416.

[2] Prerequisite macros for 802.11mc and 802.11az features

