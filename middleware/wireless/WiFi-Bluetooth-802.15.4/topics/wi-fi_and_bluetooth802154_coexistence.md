# Wi-Fi and Bluetooth/802.15.4 coexistence

|Features|Sub features|IW612|IW610|RW612|
|--------|------------|-----|-----|-----|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|STA + Bluetooth|Y|N|N|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|Mobile AP + Bluetooth|Y|N|N|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|Bluetooth LE + Wi-Fi|Y|Y|Y|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|Bluetooth + Bluetooth LE + Wi-Fi|Y|N|N|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|OpenThread + Bluetooth|Y|N|N|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|OpenThread + Bluetooth LE[^2]|Y|Y|Y|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|OpenThread + Bluetooth + Bluetooth LE|Y|N|N|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|OpenThread + Wi-Fi|Y|Y|Y|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|Bluetooth + OpenThread + Wi-Fi|Y|N|N|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|Bluetooth LE + OpenThread + Wi-Fi|Y|Y|Y|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|Bluetooth + Bluetooth LE + OpenThread + Wi-Fi|Y|N|N|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|Single antenna configuration|Y|Y|Y|
|BCA\_TDM separate antenna[^1] \(lower and higher isolation\) 1x1 Wi-Fi, \(Bluetooth and 802.15.4 shared\)|External Coexistence PTA|N|Y|Y|

**Parent topic:**[Coexistence](../topics/coexistence.md)

[^1] Experimental feature intended for evaluation/early development only and not production. Incomplete mandatory certification.

[^2] The narrow-band radio can be configured to support Bluetooth LE, 802.15.4, and to time-slice between Bluetooth LE and 802.15.4.

