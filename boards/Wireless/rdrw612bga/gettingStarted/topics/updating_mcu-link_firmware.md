# Updating MCU-Link firmware

The LPCXpresso and RW61X hardware platform comes with a CMSIS-DAP-compatible debug interface \(known as LPC-Link2\). This firmware in this debug interface may be updated using the host computer utility called MCU-Link. This typically used when switching between the default debugger protocol \(CMSIS-DAP\) to SEGGER J-Link, or for updating this firmware with new releases of these. This section contains the steps to re-program the debug probe firmware.

**Note:** If MCUXpresso IDE is used and the jumper making DFUlink is installed on the board \(JP5 on some boards, but consult the board user manual or schematic for specific jumper number\), LPC-Link2 debug probe boots to DFU mode, and MCUXpresso IDE automatically downloads the CMSIS-DAP firmware to the probe before flash memory programming \(after clicking **Debug**\). Using DFU mode ensures most up-to-date/compatible firmware is used with MCUXpresso IDE.

NXP provides the MCU-Link utility, which is the recommended tool for programming the latest versions of CMSIS-DAP and J-Link firmware onto RD-RW61X or LPCXpresso boards. The utility can be downloaded from [https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK](https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK).

These steps show how to update the debugger firmware on your board for Windows operating system. For Linux OS, follow the instructions described in the MCU-Link user guide \([https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK](https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK), select the documentation tab\).

1.  Install the MCU-Link utility.
2.  Unplug the board's USB cable.
3.  Make the DFU link \(install the jumper labelled DFUlink, JP10 on RD-RW61X-BGA board\).
4.  Connect the probe to the host via USB \(use Link USB connector\).
5.  Open a command shell and call the appropriate script located in the MCU-Link installation directory \(`<MCU-Link install dir>`\).
    1.  To program CMSIS-DAP debug firmware: `<LPCScrypt install dir>/scripts/program_CMSIS`
    2.  To program J-Link debug firmware: `<LPCScrypt install dir>/scripts/program_JLINK`
6.  Remove DFU link \(remove the jumper installed in [Step 3](updating_mcu-link_firmware.md#STEP3)\).
7.  Re-power the board by removing the USB cable and plugging it in again.

**Parent topic:**[Updating debugger firmware](../topics/updating_debugger_firmware.md)

