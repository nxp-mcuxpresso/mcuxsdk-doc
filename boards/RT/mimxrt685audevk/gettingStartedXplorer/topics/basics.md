# Basics

As both cores use shared SRAM and all digital peripherals, SDK drivers work the same on HiFi4 DSP. User Manual section 1.3 Block Diagram shows the system architect on this perspective. For applications, it is the same to use SDK drivers on HiFi4 DSP with Cortex M33 core. SDK has a DSP hello world UART example showing how easy to use UART on DSP side, same as Cortex M33 programming:

```
#include <xtensa/config/core.h>
#include "fsl_debug_console.h"
    /* Init board hardware. */
    BOARD_InitDebugConsole();
    PRINTF("Hello World running on DSP core '%s', %s_%s\r\n", XCHAL_CORE_ID);
```

Compare with Hello world programming on Cortex M33 side. There are two major differences:

-   Pin initialization is not necessary for DSP. It is doable but it is highly recommended managing all pins from Cortex M33 side to make pins all-in-one place. It is also to avoid possible conflicts when you set pins on two different cores;
-   Clock setting is not necessary for DSP. It is also doable but same it is highly recommended managing all clock sources all-in-one place;

**Parent topic:**[Peripheral Drivers and Interrupts](../topics/peripheral_drivers_and_interrupts.md)

