# Updating MCU-Link board firmware 

MCU-Link is the NXP single, unified debug probe architecture for all NXP general-purpose Arm Cortex-M based MCUs. MCU-Link is implemented on the latest evaluation boards \(known as MCU-Link OB\) of NXP. This firmware in this debug interface may be updated using the host computer utility called MCU-Link firmware. This typically used when switching between the default debugger protocol \(CMSIS-DAP\) to SEGGER J-Link, or for updating this firmware with new releases of these. This section contains the steps to re-program the debug probe firmware.

NXP provides the MCU-Link firmware, which is the recommended tool for programming the latest versions of CMSIS-DAP and J-Link firmware onto MCU-Link. The utility can be downloaded from [MCU-Link Debug Probe Architecture](https://www.nxp.com/design/design-center/software/development-software/mcu-link-debug-probe-architecture:MCU-LINK-ARCHITECTURE).

These steps show how to update the debugger firmware on your board for Windows operating system. For Linux operating system, follow the similar steps.

1.  Install the MCU-Link firmware.
2.  Unplug the USB cable of the board.
3.  Enable ISP mode on MCU-Link Core - LPC55xxx \(install the jumper labeled ISP Enable\).
4.  Connect the probe to the host via USB \(use Link USB connector\).
5.  Open a command shell and call the appropriate script located in the MCU-Link firmware installation directory \(*<firmware install dir\>*\).

    1.  To program CMSIS-DAP debug firmware: *<firmware install dir\>/scripts/program\_CMSIS*
    2.  To program J-Link debug firmware: *<LPCScrypt install dir\>/scripts/program\_JLINK*
6.  Disable ISP mode on MCU-Link Core - LPC55xxx \(remove the jumper installed in [Step 3](#STEP3)\).
7.  Repower the board by removing the USB cable and plugging it in again.

**Parent topic:**[Updating debugger firmware](../topics/updating_debugger_firmware.md)

