# Complete Example

To present better how peripheral drivers work on HiFi4 DSP, below list a bare-metal DSP example program that transfers data from DMIC to codec on RT6xx EVKs. The full workspace located in `<SDK path>\boards\evkmimxrt685\dsp_examples\audio_demo_bm`. This example is derived from Cortex M33 driver `<SDK path>\boards\evkmimxrt685\driver_examples\dmic\dmic_i2s_dma` with below slightly modifications to adapt to HiFi4 DSP.

-   Move DMA buffer and descriptors into non-cached memory partitions;
-   Using DMA1 for DSP;
-   Calling XOS functions to enable interrupts.
-   This example does not contain any pin mux initializing or clock configurations. See the above Cortex M33 example dmic\_i2s\_dma to set up Cortex M33 side. Once Cortex M33 side ready, this example is compiled and run same as any other SDK DSP examples.

Connect headphone/earphone on audio out of the board, speak on DMIC, or play song nearby the DMIC, you can hear sound on the left channel of headphone/earphone.

```
/* Start XOS */
xos_start_main("main", 7, 0);
/* Disable DSP cache for noncacheable sections. DMA MUST run on none-cacheable/ cache bypass area*/
xthal_set_region_attribute((uint32_t *)&NonCacheable_start,
                           (uint32_t)&NonCacheable_end - (uint32_t)&NonCacheable_start, XCHAL_CA_BYPASS, 0);
xthal_set_region_attribute((uint32_t *)&NonCacheable_init_start,
                           (uint32_t)&NonCacheable_init_end - (uint32_t)&NonCacheable_init_start, XCHAL_CA_BYPASS,
                           0);
PRINTF("Configure DMA\r\n");
/* DSP_INT0_SEL18 = DMA1 */
INPUTMUX_AttachSignal(INPUTMUX, 18U, kINPUTMUX_Dmac1ToDspInterrupt);
/* Map DMA IRQ handler to INPUTMUX selection DSP_INT0_SEL18
 * EXTINT19 = DSP INT 23 */
xos_register_interrupt_handler(XCHAL_EXTINT19_NUM, (XosIntFunc *)DMA_IRQHandle, DMA1);
xos_interrupt_enable(XCHAL_EXTINT19_NUM);
/* The rest DMA & DMIC operations are identical with CM33 side */
```

**Parent topic:**[Peripheral Drivers and Interrupts](../topics/peripheral_drivers_and_interrupts.md)

