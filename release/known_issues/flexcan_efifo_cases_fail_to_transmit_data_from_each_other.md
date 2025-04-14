# The flexcan_efifo cases fail to transmit data from each other

On some platform, if the High-resolution Timestamp feature is not enabled, the read enhanced RX FIFO High-resolution Timestamp field with memcpy API results in hard fault. When it is read with EDMA, the timestamp cannot be read.

**Workaround:** When read enhanced rx fifo, enable High resolution Timestamp if this feature exists. Read 20 words
with EDMA if enhanced rx fifo feature exists.

*flexcan_efifo_interrupt_transfer and flexcan_efifo_edma_transfer:*
```C
#if (defined(FSL_FEATURE_FLEXCAN_HAS_HIGH_RESOLUTION_TIMESTAMP) && FSL_FEATURE_FLEXCAN_HAS_HIGH_RESOLUTION_TIMESTAMP)
    /* Select free-running timer as message buffer TIME_STAMP field timebase. */
    flexcanConfig.captureTimeBase = kFLEXCAN_CANTimer;
    /* Enable high resolution timestamp feature to read HR TIMESTAMP in enhanced Rx FIFO. */
    flexcanConfig.capturePoint = kFLEXCAN_CANFrameStart;
#endif
```
*flexcan_efifo_edma_transfer:*
```C
#if (defined(FSL_FEATURE_FLEXCAN_HAS_HIGH_RESOLUTION_TIMESTAMP) && FSL_FEATURE_FLEXCAN_HAS_HIGH_RESOLUTION_TIMESTAMP)
        rxEhFifoConfig.dmaPerReadLength = kFLEXCAN_20WordPerRead;
#else
        rxEhFifoConfig.dmaPerReadLength = kFLEXCAN_19WordPerRead;
#endif
```

**Examples:** flexcan_efifo_interrupt_transfer, flexcan_efifo_edma_transfer

**Affected toolchains:** mcux, iar, armgcc

**Affected platforms:** frdmmcxe31b