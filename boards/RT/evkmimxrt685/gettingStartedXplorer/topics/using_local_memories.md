# Using Local Memories

RT6xx HiFi4 DSP has 64 K data TCM and 64 K instruction TCM. The TCM is filled with less than 2 K of kernel vectors and the rest is available for application needs. They are the fastest RAM available with no access latency, and can improve critical data/ instruction performance considerably. Consider using TCM as much as possible.

To program code/ data to TCM area:

1.  Define macros for sections in TCM. Reuse existing .drm0 and .iram0 sections. Both sections are default TCM sections for every Xplorer project/ memory map. The following are the sections in fsl\_common.h.

    ```
    #define DRAM0_DATA __attribute__((section(".dram0.data")))
    #define DRAM0_BSS __attribute__((section(".dram0.bss")))
    #define IRAM0_TEXT __attribute__((section(".iram0.text")))
    #define ALIGNED(alignbytes) __attribute__((aligned(alignbytes)))
    ```

2.  Use macros to declare code and data to be placed in TCM. The data and bss/ uninitialized data are different sections. The following is an example for an FFT function call.

    ```
    DRAM0_DATA const static int32_t fft_in_ref[FFT_LENGTH] = {
    DRAM0_DATA const static int32_t fft_out_ref[FFT_LENGTH] = {
    DRAM0_BSS static int32_t fft_out[FFT_LENGTH];
    IRAM0_TEXT int TEST_FFT()
    {
      …
            fft_cplx32x32(fft_out, fft_in, FFT_HANDLE, 3);
      …
    }
    ```

3.  The TCM addresses start from 0x2400 0000, which is too far away to main\(\). Therefore, the project enables long calls to ensure that main\(\) is able to call sub functions. To enable, select **Build Properties \> Optimization \> Enable long calls** and select the **Yes** checkbox. Alternatively, add -mlongcalls to the compiler flags.

**Parent topic:**[System Optimization](../topics/system_optimization.md)

