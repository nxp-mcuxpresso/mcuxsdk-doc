# Board debugger setup

Board debugger info:
 - Default debugger is OSJTAG.
 - Onboard debugger USB port is J8, which set the debugger and COM port.
 - Onboard debugger firmware update jumper is J6.

To download and run the application, perform the following steps:
 - Connect USB cable between the host PC and the debugger USB port.
 - Install the debugger driver and USB CDC driver as PC hint if it is the first time you run it on the PC. The debugger and USB CDC driver are provided by CodeWarrior by default.
 - The CodeWarrior may prompt to update the debugger firmware, which requires to connect the firmware update jumper on board and then follow the instruction by CodeWarrior to finish the firmware update.