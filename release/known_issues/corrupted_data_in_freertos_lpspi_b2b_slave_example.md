# Corrupted data in freertos_lpspi_b2b \(slave\) example

Corrupted data in freertos_lpspi_b2b\(slave\) example.
Tool: Keil MDK
Target: freertos_lpspi_b2b_slave_flexspi_nor_debug.

**Workaround:** Changing the optimization level from -01 to -00 can avoid the issue. However, the optimization level -O1 is not the root cause