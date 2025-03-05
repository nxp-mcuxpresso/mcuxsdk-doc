# Initialize DSP Core

To minimize the power consumption, the DSP core is not powered when RT600 boots up. To initialize, run, or debug DSP applications, you must execute some code on the Arm core.

The DSP management interface library provided in the SDK is available at the location: `<SDK_ROOT>/devices/MIMXRT685S/drivers/fsl_dsp.c`.

```
/* Initialize DSP core. */
void DSP_Init(void);
/* Deinit DSP core. */
void DSP_Deinit(void);
/* Copy DSP image to destination address. */
void DSP_CopyImage(dsp_copy_image_t *dspCopyImage);
/* Start DSP core. */
void DSP_Start(void);
/* Stop DSP core. */
void DSP_Stop(void);
```

The SDK includes a helper function used by the DSP example applications at: `<SDK_ROOT>/boards/evkmimxrt685/dsp_examples/dsp_support.c`.

```
/* Prepare DSP core for code execution:
   - Setup PMIC for DSP
   - Initialize DSP clock and core
   - (Optional) Copy DSP binary image into RAM
   - Start DSP core
 */
 void BOARD_DSP_Init(void);
```

After executing this function during your Arm application startup, the DSP is initialized and ready to run. From here, code is loaded and debugged on the DSP with Xplorer IDE and tools.

**Parent topic:**[Install MCUXpresso SDK](../topics/install_mcuxpresso_sdk.md)

