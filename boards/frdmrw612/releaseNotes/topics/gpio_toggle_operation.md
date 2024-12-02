# GPIO toggle operation not working on NCP SPI slave side with flash release build 

Due to IDE compile optimization for the flash release target, the GPIO toggle operation on the NCP SPI slave side to indicate RX DMA ready or slave to master transfer is not working. The issue occurs because the GPIO toggle time is too short for the host to detect it.

**Parent topic:**[Known issues](../topics/known_issues.md)

