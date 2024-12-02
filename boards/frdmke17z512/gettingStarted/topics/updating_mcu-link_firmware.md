# Updating MCU-LINK firmware 

The Freedom hardware platform comes with a CMSIS-DAP-compatible debug interface \(known as MCU-Link\). This firmware in this debug interface may be updated using the host computer scripts. It is typically used when switching between the default debugger protocol \(CMSIS-DAP\) to SEGGER J-Link, or for updating this firmware with new releases of these. This section contains the steps to re-program the debug probe firmware.

NXP provides the MCU-Link utility, which is the recommended tool for programming the latest versions of CMSIS-DAP and J-Link firmware onto MCU-Link. The utility can be downloaded from [MCU-Link Debug Probe](https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK).

These steps show how to update the debugger firmware on your board for the Windows operating system. For Linux operating system, follow the instructions described in the *Getting Started with the MCU-Link* \(document [GS-MCU-LINK](https://www.nxp.com/doc/GS-MCU-LINK)\).

1.  Install the MCU-Link utility.
2.  Unplug the USB cable of the board.
3.  Install the jumper on JP3.
4.  Connect the probe to the host via USB \(use Link USB connector\).
5.  Open a command shell and call the appropriate script located in the MCU-Link installation directory \(<MCU-Link install dir\>\).

    1.  To program CMSIS-DAP debug firmware: *<MCU-Link install dir\>/scripts/program\_CMSIS*
    2.  To program J-Link debug firmware: *<MCU-Link install dir\>/scripts/program\_JLINK*
6.  Remove the jumper on JP3.
7.  Re-power the board by removing the USB cable and plugging it in again.

**Parent topic:**[Updating debugger firmware](../topics/updating_debugger_firmware.md)

