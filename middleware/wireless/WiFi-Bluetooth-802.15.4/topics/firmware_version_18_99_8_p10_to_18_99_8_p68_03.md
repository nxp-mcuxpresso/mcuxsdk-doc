# Firmware version: 18.99.8.p10 to 18.99.8.p68

|Component|Description|
|-----------|-------------|
|Wi-Fi|<ul><li>Fixed WPA3 SAE security failure observed in WiFi CLI app during initiating connection with AP.</ul></li> <ul><li>Fixed TX power increase of ~3 dBm observed after connecting to a DFS channel and then reconnecting to a non-DFS channel. TX_POWER_LUT_EXTENSION_SUPPORT did not account for the one-channel DPD case, causing TX power to exceed the configured limit on subsequent non-DFS channel connections.</ul></li>|
|BLuetooth|<ul><li>Implementation of PaWR (Periodic Advertisement with response) feature</ul></li>|
|Coexistance|<ul><li>Fixed driver assert issue when wake up wifi cpu1</ul></li><ul><li>Wi-Fi throughput drops to 0 when Wi-Fi and OT traffic run concurrently on non-overlapping channels at an RSSI of -80 dBm.</ul></li><ul><li>Fixed high PING latency (up to ~1876 ms average ~397 ms) and packet loss observed with external FEM in Wi-Fi + Thread coexistence mode. RF control lines were switching excessively between Wi-Fi and Narrowband, disrupting Wi-Fi PSM operation and degrading throughput/latency.</ul></li> |

**Parent topic:**[Bug fixes and/or feature enhancements](../topics/bug_fixes_andor_feature_enhancements_03.md)

