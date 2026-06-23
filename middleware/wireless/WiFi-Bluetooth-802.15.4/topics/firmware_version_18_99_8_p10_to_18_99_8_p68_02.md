# Firmware version: 18.99.8.p10 to 18.99.8.p68

|Component|Description|
|-----------|-------------|
|Wi-Fi|<ul><li>Duplicate Packet Reception in JP Region due to Missing BA/ACK Transmission</ul></li><ul><li>Fixed STA setting wrong primary channel when external AP has incorrect secondary channel offset field.</ul></li><ul><li>Fixed WPA3 STA datapath ping stuck until next reassociation; fixed DUT TX throughput dropping to 0 or getting stuck in pre-sleep state under stress.</ul></li><ul><li>Fixed scan results taking more than 5 seconds to appear in AP+STA mode.</ul></li><ul><li>Fixed RSSI_INFO (0xa4) command timeout when DUT is left idle for extended periods in AP+STA mode.</ul></li>|
|Bluetooth|<ul><li>Sequential Removal of CIS Handles as per current Controller implementation i.e CIS Disconnection sequence should be in sequence => CIS - 4,3,2,1</ul></li><ul><li>While 4-CIS streaming,audio glitches observed on all CIS SINK with Samsung Galaxy buds</ul></li><ul><li>Fixed missing Disconnect Complete event from controller causing host to get stuck after ACL link disconnection.</ul></li><ul><li>Added mechanism to detect BT slave link FST on odd-numbered offset</ul></li><ul><li>Fixed firmware crash observed after eSCO connection complete event.</ul></li><ul><li>Fixed BTC ACL link disconnection due to CCM counter not being incremented during encryption</ul></li><ul><li>Fixed BLE and BTC power backoff not working when BTU power control is disabled in MFG firmware.</ul></li>|

**Parent topic:**[Bug fixes and/or feature enhancements](../topics/bug_fixes_andor_feature_enhancements_02.md)

