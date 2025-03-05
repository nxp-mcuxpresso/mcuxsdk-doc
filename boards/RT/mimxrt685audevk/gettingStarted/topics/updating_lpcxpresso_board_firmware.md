# Updating LPCXpresso board firmware

The LPCXpresso hardware platform comes with a CMSIS-DAP-compatible debug interface \(known as LPC-Link2\). This firmware in this debug interface may be updated using the host computer utility called LPCScrypt. This typically used when switching between the default debugger protocol \(CMSIS-DAP\) to SEGGER J-Link, or for updating this firmware with new releases of these. This section contains the steps to reprogram the debug probe firmware.

**Note:** If MCUXpresso IDE is used and the jumper making DFUlink is installed on the board \(JP5 on some boards, but consult the board user manual or schematic for specific jumper number\), LPC-Link2 debug probe boots to DFU mode, and MCUXpresso IDE automatically downloads the CMSIS-DAP firmware to the probe before flash memory programming \(after clicking **Debug**\). Using DFU mode ensures that most up-to-date/compatible firmware is used with MCUXpresso IDE.

NXP provides the LPCScrypt utility, which is the recommended tool for programming the latest versions of CMSIS-DAP and J-Link firmware onto LPC-Link2 or LPCXpresso boards. The utility can be downloaded from [www.nxp.com/lpcutilities](http://www.nxp.com/lpcutilities).

These steps show how to update the debugger firmware on your board for Windows operating system. For Linux OS, follow the instructions described in LPCScrypt user guide \([www.nxp.com/lpcutilities](http://www.nxp.com/lpcutilities), select **LPCScrypt**, and then the documentation tab\).

1.  Install the LPCScript utility.
2.  Unplug the board's USB cable.
3.  Make the DFU link \(install the jumper labeled DFUlink\).
4.  Connect the probe to the host via USB \(use Link USB connector\).
5.  Open a command shell and call the appropriate script located in the LPCScrypt installation directory \(`<LPCScrypt install dir>`\).
    1.  To program CMSIS-DAP debug firmware: `<LPCScrypt install dir>/scripts/program_CMSIS`
    2.  To program J-Link debug firmware: `<LPCScrypt install dir>/scripts/program_JLINK`
6.  Remove DFU link \(remove the jumper installed in [Step 3](updating_lpcxpresso_board_firmware.md#STEP3)\).
7.  Repower the board by removing the USB cable and plugging it in again.

**Parent topic:**[Updating debugger firmware](../topics/updating_debugger_firmware.md)

