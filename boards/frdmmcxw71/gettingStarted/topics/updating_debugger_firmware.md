# Updating debugger firmware {#topic_rrw_l2h_5wb}

The K32W148-EVK board comes with a CMSIS-DAP-compatible debug interface \(known as MCU-Link\). This firmware in this debug interface may be updated using the host computer scripts. This typically used when switching between the default debugger protocol \(CMSIS-DAP\) to SEGGER J-Link, or for updating this firmware with new releases of these. This section contains the steps to re-program the debug probe firmware.

NXP provides the MCU-Link utility, which is the recommended tool for programming the latest versions of CMSIS-DAP and J-Link firmware onto MCU-Link. The utility can be downloaded from [https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK](https://www.nxp.com/design/microcontrollers-developer-resources/mcu-link-debug-probe:MCU-LINK).

These steps show how to update the debugger firmware on your board for Windows operating system. For Linux OS, follow the instructions described in MCU-Link user guide, [https://www.nxp.com/design/software/development-software/mcuxpresso-software-and-tools-/mcu-link-debug-probe:MCU-LINK](https://www.nxp.com/design/software/development-software/mcuxpresso-software-and-tools-/mcu-link-debug-probe:MCU-LINK).

1.  Install the MCU-Link utility.
2.  Unplug the board's USB cable.
3.  Install the jumper on JP20.
4.  Connect the probe to the host via USB \(use Link USB connector\).
5.  Open a command shell and call the appropriate script located in the MCU-Link installation directory, *<MCU-Link install dir*\>.

    1.  To program CMSIS-DAP debug firmware: *<MCU-Link install dir\>/scripts/program\_CMSIS*.
    2.  To program J-Link debug firmware: *<MCU-Link install dir\>/scripts/program\_JLINK*.
6.  Remove the jumper on JP20.
7.  Re-power the board by removing the USB cable and plugging it in again.

