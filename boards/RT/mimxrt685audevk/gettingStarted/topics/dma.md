# DMA

RT6xx has two DMA controllers. Each has the same DMA request and trigger input possibilities. The two intended scenarios for their use are:

-   One DMA controller \(DMA0\) is used by the CM33, the other \(DMA1\) is used by the HiFi4. This case can apply to systems where there is no need to differentiate security between the CPUs or between different tasks.
-   One DMA controller \(DMA0\) is secured and has access to secure spaces and peripherals. The other \(DMA1\) is not secured and does not have access to secure spaces and peripherals. In this scenario, only the secure code running on the CM33 has access to the secure DMA controller. The other code and the HiFi4 share the non-secure DMA controller \(if needed\).

HiFi4 DSP always uses DMA1 controller. Again, it is the same to call DMA drivers at HiFi4 DSP side. The DMA destination buffer and DMA descriptor have to be in non-cached area to ensure that each transaction flushes to memory immediately. The below example code showing how to create a DMIC DMA channel:

```
AT_NONCACHEABLE_SECTION_ALIGN(
  static uint8_t s_buffer[BUFFER_SIZE * BUFFER_NUM], 4
);
AT_NONCACHEABLE_SECTION_ALIGN(
dma_descriptor_t s_dmaDescriptorPingpong[2], 16
);
#define DEMO_DMA (DMA1)
#define DEMO_DMIC_RX_CHANNEL DMAREQ_DMIC0
DMA_Init(DEMO_DMA);
DMA_EnableChannel(DEMO_DMA, DEMO_DMIC_RX_CHANNEL);
DMA_SetChannelPriority(DEMO_DMA, DEMO_DMIC_RX_CHANNEL, kDMA_ChannelPriority2);
DMA_CreateHandle(&s_dmicRxDmaHandle, DEMO_DMA, DEMO_DMIC_RX_CHANNEL);
```

Macro `AT_NONCACHEABLE_SECTION_ALIGN` is defined in SDK driver layer and refer to non-cached area specified by memory map.

For more details about DMA, see the User Manual Chapter 11 RT6xx DMA Controller and SDK DMA examples in `<SDK path>\boards\evkmimxrt685\driver_examples\dma`.

For audio peripherals/ DMIC/ I2S DMA, see `<SDK path>\boards\evkmimxrt685\driver_examples\dmic` and `<SDK path>\boards\evkmimxrt685\driver_examples\i2s`.

**Parent topic:**[Peripheral Drivers and Interrupts](../topics/peripheral_drivers_and_interrupts.md)

