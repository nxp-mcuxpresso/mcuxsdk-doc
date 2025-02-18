# Interrupts

HiFi4 DSP has total 32 interrupts and 4 interrupt levels. Besides the first five interrupts, the rest interrupt 5 ~ 31 are multiplexed to allow more control over priorities and more general flexibility. To see the full list, see the User Manual section 8.6.3 DSP Interrupt Input Multiplexers.

It only requires few lines of code to enable an interrupt by calling XOS function calls, and peripheral controls are identical as Cortex M33 side. For example, the below code shows how to enable a UTick timer at DSP side:

First, include XOS system header files and libraries to enable necessary XOS functions.

To include libraries, go to Build **Properties \> Libraries \> Add libraries \> Select ‘xos’ & ‘xtutil’** and **OK** to accept.

```
#include <xtensa/config/core.h>
#include <xtensa/xos.h>
```

Set up the UTick callback and delay functions. This part is identical with Cortex M33 side. For Cortex M33 side implementation, see `SDK path\\boards\evkmimxrt685\driver_examples\utick`

```
#define UTICK_TIME_1S        (1000000UL)
#define EXAMPLE_UTICK        UTICK0
static volatile bool utickExpired;
static void UTickCallback(void)
{
utickExpired = true;
}
static void UTickDelay(uint32_t usec)
{
/* Set the UTICK timer to wake up the device from reduced power mode */
UTICK_SetTick(EXAMPLE_UTICK, kUTICK_Onetime, usec - 1, UTickCallback);
while (!utickExpired)
{
}
utickExpired = false;
}
```

Initialize the XOS and start UTick timer. The XOS function calls are the differences with Cortex M33 side:

```
/* Initialize XOS thread and start scheduler. Priority 7*/
xos_start_main("main", 7, 0);
/* Init board hardware. */
CLOCK_AttachClk(kLPOSC_to_UTICK_CLK);
CLOCK_EnableClock(kCLOCK_InputMux);
UTICK_Init(EXAMPLE_UTICK);
INPUTMUX_AttachSignal(INPUTMUX, 10U, kINPUTMUX_Utick0ToDspInterrupt);
/* To register interrupt callback */
xos_register_interrupt_handler(15, (XosIntFunc *)UTICK0_DriverIRQHandler, NULL);
/* To enable the interrupt */
xos_interrupt_enable(15);
while (1)
{
UTickDelay(UTICK_TIME_1S);
PRINTF("DSP UTICK TIMER every 1s\r\n");
}
```

Pay attention to the instant numbers. Pick interrupt 15, which maps to DSP\_INT0\_SEL10 as a L1 interrupts, lowest priority level. For more details about RT6xx HiFi4 DSP interrupt configuration, see User Manual section 51.7 Interrupt. Therefore, for Inputmux, attach UTick interrupt to 10. 15-5=10 as first five interrupts are reserved, not user configurable. To get it to highest priority level, for example L3, configure interrupt as follows.

```
INPUTMUX_AttachSignal(INPUTMUX, 24U,
kINPUTMUX_Utick0ToDspInterrupt);
xos_register_interrupt_handler(29, (XosIntFunc
*)UTICK0_DriverIRQHandler, NULL);
xos_interrupt_enable(29);
```

kINPUTMUX\_Utick0ToDspInterrupt specifies DSP interrupt multiplexing value. It has been defined in SDK and matching User Manual section 8.6.3 DSP Interrupt Input Multiplexers.

For more details about XOS interrupt handling, see the Xtensa XOS Reference Manual Chapter 18 Interrupt and Exception Handling, and Chapter 26 Interrupt Handler Restrictions.

**Parent topic:**[Peripheral Drivers and Interrupts](../topics/peripheral_drivers_and_interrupts.md)

