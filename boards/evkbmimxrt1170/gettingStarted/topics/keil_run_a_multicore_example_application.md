# Run a multicore example application

The primary core debugger flashes both the primary and the auxiliary core applications into the SoC flash memory. To download and run the multicore application, switch to the primary core application project and perform Steps [1](keil_run_an_example_application.md#step1) – [5](keil_run_an_example_application.md#step5) as described in [Run an example application](keil_run_an_example_application.md). These steps are common for both single-core and dual-core applications in μVision.

Both the primary and the auxiliary image is loaded into the flash memory. After clicking **Run**, the primary core application is executed. During the primary core code execution, the auxiliary core code is re-allocated from the SPI flash memory to the RAM, and the auxiliary core is released from the reset. The `hello_world` multicore application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

![](../images/keil_hello_world_from_primary_core_message.png "Hello World from primary core message")

An LED controlled by the auxiliary core starts flashing indicating that the auxiliary core has been released from the reset and is running correctly.

Attach the running application of the auxiliary core by opening the auxiliary core project in the second μVision instance and

clicking the **Start/Stop Debug Session** button. After this, the second debug session is opened and the auxiliary core

application can be debugged.

![](../images/keil_second_debugging_auxiliary_core_application.png "Second debugging auxiliary core application")

**Parent topic:**[Run a demo using Keil MDK/μVision](../topics/run_a_demo_using_keil_mdk_vision.md)

