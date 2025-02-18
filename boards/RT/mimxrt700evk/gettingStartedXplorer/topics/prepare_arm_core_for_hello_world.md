# Prepare Arm Core for ‘Hello World’

Each of the DSP demos included in the MCUXpresso SDK consists of two separate applications that run on the Arm core and DSP core. The Arm core application initializes the DSP core and executes other application-specific functionality.

To debug the ‘Hello World’ DSP application, you must first set up and execute the Arm application using an environment of your choice. It is required to modify the global preprocessor macro, DSP\_IMAGE\_COPY\_TO\_RAM, to control loading of the DSP binary application.

When this macro is set to ‘0'/FALSE, the Arm application and DSP application are independently loaded and debugged.

-   Build and execute the ‘Hello World’ Arm demo located in: `<SDK_ROOT>/boards/mimxrt700evk/dsp_examples/hello_world_usart/cm33/`.

Preparing an Arm core development environment is outside the scope of this document.

**Note:** IAR Embedded Workbench may require a patch to enable compatibility with RT700. For details on the patch, contact NXP directly.

**Note:** If you are using MCUXpresso, it is highly recommended to upgrade to latest version of the SDK and match the latest EVK board.

**Parent topic:**[Run and Debug DSP Demo using Xplorer IDE](../topics/run_and_debug_dsp_demo_using_xplorer_ide.md)

