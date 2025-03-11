# Corrupted data in freertos\_lpspi\_b2b \(slave\) example

Corrupted data in freertos\_lpspi\_b2b\(slave\) example.

Tool: Keil MDK

Target: freertos\_lpspi\_b2b\_slave\_flexspi\_nor\_debug.

Changing the optimization level from -01 to -00 can avoid the issue. However, the optimization level -O1 is not the root cause
