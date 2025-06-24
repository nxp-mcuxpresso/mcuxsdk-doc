# Wi-Fi Generic features

|Features|Sub features|88W8987|IW416|IW611/IW612|RW610/RW612|IW610|AW611|
|--------|------------|-------|-----|-----------|-----------|-----|-----|
|Generic|Firmware download \(parallel\)[^1]|Y|Y|Y|N|N|Y|
|Generic|Secure boot|N|N|Y|Y|Y|Y|
|Generic|Kconfig memory optimizer|Y|Y|Y|Y|Y|Y|
|Generic|Firmware Compression[^2]|N|Y|N|N|N|N|
|Generic|u-AP intra-BSS|Y|N|Y|Y|Y|Y|
|Generic|Net Monitor Mode|N|N|N|Y|Y|N|
|Generic|Net Monitor Mode with packet transmission|N|N|N|Y|Y|N|
|Generic|In-Channel Net Monitor mode|N|N|N|N|N|N|


**Parent topic:**[Wi-Fi radio](../topics/wi-fi_radio.md)

[^1] Feature not enabled by default in the SDK. Refer to [Feature enable and memory impact](feature_enable_and_memory_impact.md) for the macro to enable the feature and the impact on the memory when enabling the feature.
[^2] The feature is used to compress the Wi-Fi Bluetooth firmware and optimize the flashing of the host

