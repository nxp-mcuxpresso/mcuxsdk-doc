# Non XIP target debug issue on toolchain MDK

When debugging non XIP targets in flash boot mode, if application changes any settings which have impacts on flexspi, the build output window might show “Debug access failed” when start debugging next time. It is recommended to keep the board in serial downloader mode when debugging non XIP targets.

