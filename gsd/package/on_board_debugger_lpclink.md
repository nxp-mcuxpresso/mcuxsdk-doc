# On-board debugger LPC-Link

LPC-Link 2 is an extensible debug probe that can be used seamlessly with MCUXpresso IDE, and is also compatible with 3rd party IDEs that support CMSIS-DAP protocol. MCU-Link also includes a USB to UART bridge feature (VCOM) that can be used to provide a serial connection between the target MCU and a host computer. LPC-Link 2 is compatible with Windows, MacOS and Linux. A free utility from NXP provides an easy way to install firmware updates.

On-board LPC-Link 2 debugger supports CMSIS-DAP and J-Link firmware. See the table in [Default debug interfaces](default_debug_interfaces.md) to determine the default debug interface that comes loaded on your specific hardware platform.

**The corresponding host driver must be installed before debugging.**
- For boards with CMSIS-DAP firmware, visit [developer.mbed.org/handbook/Windows-serial-configuration](http://developer.mbed.org/handbook/Windows-serial-configuration) and follow the instructions to install the Windows operating system serial driver. If running on Linux OS, this step is not required.
- If using J-Link with either a standalone debug pod or MCU-Link, install the J-Link software \(drivers and utilities\) from [www.segger.com/jlink-software.html](www.segger.com/jlink-software.html).

## Updating LPC-Link firmware

The LPCXpresso hardware platform comes with a CMSIS-DAP-compatible debug interface \(known as LPC-Link2\). This firmware in this debug interface may be updated using the host computer utility called LPCScrypt. This typically used when switching between the default debugger protocol \(CMSIS-DAP\) to SEGGER J-Link, or for updating this firmware with new releases of these. This section contains the steps to reprogram the debug probe firmware.

**Note:** If MCUXpresso IDE is used and the jumper making DFUlink is installed on the board \(JP5 on some boards, but consult the board user manual or schematic for specific jumper number\), LPC-Link2 debug probe boots to DFU mode, and MCUXpresso IDE automatically downloads the CMSIS-DAP firmware to the probe before flash memory programming \(after clicking **Debug**\). Using DFU mode ensures that most up-to-date/compatible firmware is used with MCUXpresso IDE.

NXP provides the LPCScrypt utility, which is the recommended tool for programming the latest versions of CMSIS-DAP and J-Link firmware onto LPC-Link2 or LPCXpresso boards. The utility can be downloaded from [LPCScrypt](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/lpcscrypt:LPCSCRYPT).

These steps show how to update the debugger firmware on your board for Windows operating system. For Linux OS, follow the instructions described in LPCScrypt user guide \([LPCScrypt](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/lpcscrypt:LPCSCRYPT), select **LPCScrypt**, and then the documentation tab\).

1.  Install the LPCScript utility.
2.  Unplug the board's USB cable.
3.  Make the DFU link \(install the jumper labeled DFUlink\).
4.  Connect the probe to the host via USB \(use Link USB connector\).
5.  Open a command shell and call the appropriate script located in the LPCScrypt installation directory \(`<LPCScrypt install dir>`\).
    1.  To program CMSIS-DAP debug firmware: `<LPCScrypt install dir>/scripts/program_CMSIS`
    2.  To program J-Link debug firmware: `<LPCScrypt install dir>/scripts/program_JLINK`
6.  Remove DFU link \(remove the jumper installed in Step 3\).
7.  Repower the board by removing the USB cable and plugging it in again.

