# DSP Core Initialization

In order to minimize power consumption, the DSP core is NOT powered when RT500 boots up.

To run or debug DSP applications: you will first need to execute some code on the ARM core to initialize the DSP.

A DSP management interface library is provided in the SDK, at `<SDK_ROOT>/devices/MIMXRT595S/drivers/fsl_dsp.c`:

```
/* Initialize DSP core. */
void DSP_Init(void);
/* Deinit DSP core. */
void DSP_Deinit(void);
/* Copy DSP image to destination address. */
void DSP_CopyImage(dsp_copy_image_t *dspCopyImage);
<SDK_ROOT>/devices/MIMXRT595S/drivers/fsl_dsp.h:
/* Start DSP core. */
void DSP_Start(void);
/* Stop DSP core. */
void DSP_Stop(void);
```

The SDK includes a helper function used by the DSP example applications at `<SDK_ROOT>/boards/evkmimxrt595/dsp_examples/hello_world_usart /cm33/`.

```
/* Prepare DSP core for code execution:
- Setup PMIC for DSP
- Initialize DSP clock and core
- (Optional) Copy DSP binary image into RAM
- Start DSP core
*/
void BOARD_DSP_Init(void);
```

After executing this function during your ARM application startup, the DSP is initialized and ready to run. The code is loaded and debugged on the DSP with Xplorer IDE and tools.

**Parent topic:**[Install MCUXpresso SDK](../topics/install_mcuxpresso_sdk.md)

