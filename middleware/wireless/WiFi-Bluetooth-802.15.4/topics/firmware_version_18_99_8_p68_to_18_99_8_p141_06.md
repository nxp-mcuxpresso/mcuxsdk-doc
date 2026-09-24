# Firmware version: 18.99.8.p68 to 18.99.8.p141

|Component|Description|
|-----------|-------------|
|Wi-Fi|<ul><li>Fixed Wi-Fi RF Test Mode continuous-wave tone transmission stopping when run for a long duration (30 seconds to 15 minutes).</li></ul><ul><li>Fixed an issue where DHCP renewal was not triggered when roaming between independent APs sharing the same SSID.</li></ul><ul><li>Fixed an issue where Wi-Fi initialization failed after a JLink reset, requiring a power cycle to recover.</li></ul><ul><li>Fixed an issue where the MCU RTOS hung permanently after executing wlan-reset.</li></ul><ul><li>Fixed an issue where the DUT failed to fall back to legacy roaming after 802.11k/11v roaming returned no usable target AP.</li></ul>|
|Bluetooth LE|<ul><li>Fixed an issue where the DUT hung during BLE LE Scan when Wi-Fi was associated with a WPA2 security SSID concurrently.</li></ul><ul><li>Fixed an issue where BLE scan failed to stop cleanly, causing an assertion/hang after issuing bt scan off.</li></ul>|
|Coex|<ul><li>Fixed an issue where adding a WPA3-SAE or Enterprise Wi-Fi profile caused a crash/hang, preventing Wi-Fi association during concurrent BLE L2CAP coexistence testing.</li></ul><ul><li>Fixed an issue where BLE re-initialization failed during a BLE init/disable loop test while Wi-Fi was associated and running PING traffic.</li></ul>|

**Parent topic:** [Bug fixes and/or feature enhancements](../topics/bug_fixes_andor_feature_enhancements_06.md)