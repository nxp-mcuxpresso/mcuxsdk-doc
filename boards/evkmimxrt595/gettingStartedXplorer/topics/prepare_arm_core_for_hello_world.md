# Prepare Arm Core for ‘Hello World’

The DSP demos contained in the MCUXpresso SDK each consist of two separate applications that run on the Arm core and DSP core. The Arm core application initializes the DSP core in the manner described in section 2.3 and executes other application-specific functionality.

In order to debug the ‘Hello World’ DSP application, first set up and execute the Arm application using an environment of your choosing:

-   Build and execute the ‘Hello World’ Arm demo at:

```
<SDK_ROOT>/boards/evkmimxrt595/dsp_examples/hello_world_usart/cm33/
```

Preparing an Arm core development environment is outside the scope of this document. For information on using the SDK for Arm core development, refer to the document ‘Getting Started with MCUXpresso SDK for MIMXRT500.pdf’ located under <SDK\_ROOT\>/docs/.

**Note:** SEGGER J-Link software version \>= 6.46 is required for compatibility with RT500. MCUXpresso IDE may ship with an older version, which is customized as in [Figure 1](prepare_arm_core_for_hello_world.md#CGSADGDAJ).

|![](../images/fig11.png "Customize
										MCUXpresso
										IDE options")

|

**Parent topic:**[Run and Debug DSP Demo using Xplorer IDE](../topics/run_and_debug_dsp_demo_using_xplorer_ide.md)

