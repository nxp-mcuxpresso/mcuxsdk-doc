# Updating MCU-Link firmware

The RW61X hardware platform comes with a CMSIS-DAP-compatible debug interface \(known as MCU-Link\). This firmware in this debug interface may be updated using the host computer utility called MCU-Link. This is typically used when switching between the default debugger protocol \(CMSIS-DAP\) to SEGGER J-Link, or for updating this firmware with new releases of these. This section contains the steps to re-program the debug probe firmware.

NXP provides the MCU-Link utility, which is the recommended tool for programming the latest versions of CMSIS-DAP and J-Link firmware onto the FRDM-RW610FML board. The utility can be downloaded from [https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK](https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK).

These steps show how to update the debugger firmware on your board for the Windows operating system. For Linux OS, follow the instructions described in the MCU-Link user guide \([https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK](https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK), select the documentation tab\).

1.  Install the MCU-Link utility.
2.  Unplug the board's USB cable.
3.  Install the jumper JP10 on the FRDM-RW610FML board.

4.  Connect the probe to the host via USB type-c port J15.
5.  Open a command shell and call the appropriate script located in the MCU-Link installation directory \(`<MCU-Link install dir>`\).
    1.  To program CMSIS-DAP debug firmware: `<LPCScrypt install dir>/scripts/program_CMSIS`
    2.  To program J-Link debug firmware: `<LPCScrypt install dir>/scripts/program_JLINK`
6.  Remove the jumper installed in Step 3.
7.  Re-power the board by removing the USB cable and plugging it in again.

**Parent topic:**[Updating debugger firmware](../topics/updating_debugger_firmware.md)

