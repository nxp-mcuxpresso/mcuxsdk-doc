# Firmware version: 18.99.8.p68 to 18.99.8.p141

|Component|Description|
|-----------|-------------|
|Wi-Fi|<ul><li>The device connects successfully but fails to roam when signal degrades.</ul></li><ul><li>Fixed an issue where DHCP renewal was not triggered when roaming between independent APs sharing the same SSID </ul></li><ul><li>Fixed an issue where ping responses failed on the first uAP BSS start in 2.4 GHz</ul></li><ul><li> Fixed an issue where the DUT failed to fall back to legacy roaming after 802.11k/11v roaming returned no usable target AP</li></ul>|
|Bluetooth|<ul><li>Fixed an issue where the BR/EDR Coex shell app incorrectly initialized the Nighthawk (IW610) module and downloaded firmware instead of IW612, causing NB UART firmware download to fail with "HDR SIG not found" (-22) and subsequently WLAN initialization to fail.</li></ul><ul><li>Fixed a sporadic LE RX degradation issue , where GATT indication delays exceeding 500 ms were observed due to excessive retransmissions in a concurrent BTC ACL + eSCO + BLE scatternet scenario. </li></ul><ul><li>Fixed a issue where DUT sends HCI Hardware Error (0x22)</li></ul><ul><li>Fixed a issue where DUT establishes LE connections with two devices using same connection handle</li></ul><ul><li>Fixed a issue where Controller will choose connection interval that won't collide with eSCO link paremeters.</li></ul>|


**Parent topic:** [Bug fixes and/or feature enhancements](../topics/bug_fixes_andor_feature_enhancements_02.md)

