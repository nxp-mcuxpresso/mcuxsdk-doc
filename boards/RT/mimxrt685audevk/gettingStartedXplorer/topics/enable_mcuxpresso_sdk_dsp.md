# Enable MCUXpresso SDK DSP

The following DSP-specific enablements are available inside the MCUXpresso SDK release package for RT600.

-   ```
<SDK_ROOT>/devices/MIMXRT685S/
```

    Unified device and peripheral driver source code that can be compiled for both Arm and DSP cores.

    **Note:** Only a limited subset of peripheral drivers and components is supported on the DSP.

-   ```
<SDK_ROOT>/boards/evkmimxrt685/dsp_examples/
```

    DSP example applications

-   ```
<SDK_ROOT>/middleware/multicore/rpmsg_lite/
```

    Unified RPMsg-Lite multicore communication library, with porting layers for Arm and DSP cores

-   ```
<SDK_ROOT>/middleware/dsp/audio_framework/
```

    Xtensa Audio Framework \(XAF\) for DSP core

-   ```
<SDK_ROOT>/middleware/dsp/audio_framework/libxa_af_hostless/
```

    Source code and documentation for the core XAF framework

-   ```
<SDK_ROOT>/middleware/dsp/audio_framework/testxa_af_hostless/
```

-   Utilities and tests for developing applications with the XAF framework

    ```
    <SDK_ROOT>/middleware/dsp/audio_framework/testxa_af_hostless/test/plugins
    ```

-   XAF components and codec binaries

-   ```
<SDK_ROOT>/middleware/dsp/naturedsp/hifi4/
```

    NatureDSP Math Library for HiFi4 DSP


**Parent topic:**[Install MCUXpresso SDK](../topics/install_mcuxpresso_sdk.md)

