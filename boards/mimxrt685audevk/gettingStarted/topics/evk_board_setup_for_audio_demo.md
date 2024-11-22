# EVK Board Setup for Audio Demo

The DSP audio demo is tested against EVK-MIMXRT685 Rev E and requires UART for serial console.

For the codec to output audio properly, attach one jumper on the board as follows:

JP7-1 <==\> JP8-2

**Note:** DSP operates DMA and audio peripherals same as CM33 side. Jumper settings, I2S configs, or pin mux settings are all same with CM33 side. For information on steps to operate I2S, DMIC and DMA, see the SDK CM33 side driver examples. SDK\\boards\\evkmimxrt685\\driver\_examples\\i2s;

**Note:** Jumper settings are different on different version of EVKs or validation boards. The above mentioned setting is for SDK 2.8.0 and Rev E EVK or later only. For old version of boards or SDKs, double check the SDK driver examples for correct settings for the pin mux and jumper settings.

The demo uses the UART for console input and output. Connect the EVK board to a PC via the USB debug interface \(J5\) and open up a serial interface on your PC using a terminal tool such as PuTTY on Windows or screen on Linux.

**Parent topic:**[Run and Debug DSP Audio Framework](../topics/run_and_debug_dsp_audio_framework.md)

