# EVK Board Setup for Audio Demo

The DSP audio demo is tested against EVK-MIMXRT595 and requires the CODEC line out \(J4\), and UART for serial console.

In order for the CODEC to output audio properly, you must attach two jumpers on the board as follows:

-   JP7-1 is connected to JP8-2

The demo uses the UART for console input and output. Connect the EVK board to a PC via the USB debug interface \(J40\) and open up a serial interface on your PC using a terminal tool such as Tera term or PuTTY on Windows or screen on Linux.

-   Remove Jumpers JP17, JP18, JP19 for SWD to connect to the chip and Serial interface on J40.
-   DSP debugging is through SWD only, so connect J-Link to SWD interface.

**Parent topic:**[Run and Debug DSP Audio Framework](../topics/run_and_debug_dsp_audio_framework.md)

