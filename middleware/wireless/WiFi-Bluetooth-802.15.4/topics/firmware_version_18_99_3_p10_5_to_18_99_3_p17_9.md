# Firmware version: 18.99.3.p10.5 to 18.99.3.p17.9

|Component|Description|
|-----------|-------------|
|Wi-Fi|<ul><li>After performing independent reset \(out-of-band mode\), the STAUT fails to connect to the external AP via `wlan-connect` command, observed command timeout `0x107` error.</li></ul>|
|Bluetooth|<ul><li>Audio glitches observed with Google Pixel 7 Pro streaming audio after CIS is established with DUT.</li><li>During Call Gateway \(CG\) / Call Terminal \(CT\) Use Case, the firmware periodically sends NULL PDU, which results in frequent Audio Glitch on both CG and CT sides.</li><li>Heavy audio glitches observed with CIS SRC Google Pixel 7 Pro</li><li>Continuous audio glitches observed in 1 CIS and 2 CIS for 48\_3 and 48\_4 config.</li></ul>|

**Parent topic:**[Bug fixes and/or feature enhancements](../topics/bug_fixes_andor_feature_enhancements_02.md)

