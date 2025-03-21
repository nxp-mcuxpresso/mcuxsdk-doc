# Board debugger setup

Board debugger info:
 - Default debugger is multilink.
 - Onboard debugger USB port is J12, which set the debugger port.
 - Onboard USB UART bridge USB port is J26, which set the COM port.

To download and run the application, perform the following steps:
 - Connect USB cable between the host PC and the debugger USB port.
 - Connect USB cable between the host PC and the USB UART bridge USB port.
 - Install the debugger driver as PC hint if it is the first time you run it on the PC. The debugger driver are provided by CodeWarrior by default.
 - Install the USB UART bridge driver as PC hint if it is the first time you run it on the PC. The USB to UART bridge (CP2102) driver may be found on [SILICON LAB](https://www.silabs.com/).
