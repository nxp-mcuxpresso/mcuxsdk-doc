# NatureDSP Library

To facilitate application development on RT6xx HiFi4 DSP, NXP licensed NatureDSP signal processing library and embedded as is in source code format. It is found at `<SDK path>\middleware\dsp\naturedsp_hifi4`.

This is an extensive library, containing the most commonly used signal processing functions: FFT, FIR, vector, matrix, and common mathematics. API and programing guide in`.\doc\NatureDSP_Signal_Library_Reference_HiFi4.pdf`, and `performance data in .\doc\NatureDSP_Signal_Library_Performance_HiFi4.pdf`

As this is a huge library, it is impossible to build an all-in-one example on the RT6xx hardware. Fortunately, this library is in source code format and each function/ filter are wrapped in standalone source file. They could be integrated to any application as needed.

**Parent topic:**[HiFi4 System Programming](../topics/hifi4_system_programming.md)

