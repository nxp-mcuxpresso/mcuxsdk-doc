# Firmware version: 18.99.6.p46 to 18.99.6.p47

|Component|Description|
|-----------|-------------|
|Wi-Fi|<ul><li>Enabled mbedtls 3.x</ul></li><ul><li>Host sleep with WoWLAN fails due to command response timeout (cmd 0x10d) during MCU sleep/wake transitions on WiFi NCP over UART, leading to system assert during sleep exit</ul></li><ul><li>Ping failures observed during concurrent network operations (fast ping from AP backend and DUT), with ICMP unreachable errors indicating routing/forwarding issues and performance degradation under specific network load conditions</ul></li>|

**Parent topic:**[Bug fixes and/or feature enhancements](../topics/bug_fixes_andor_feature_enhancements_03.md)

