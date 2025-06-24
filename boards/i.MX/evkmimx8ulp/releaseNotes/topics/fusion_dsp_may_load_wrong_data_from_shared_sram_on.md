# Fusion DSP may load wrong data from shared SRAM on Silicon A0.1 with specific command sequence

There is issue in the shared SRAM controller prefetch logic for silicon A0.1.

A back-2-back access to the same memory location without any “nop” cycle in between corrupts the prefetch buffer under the following conditions.

First cycle access is a read to address N, immediately followed by the second cycle-partial write \(1 byte or halfword \(16-bits\)\) to address N.

The partial write is not updated to prefetch buffer. Subsequent reading from the Shared SRAM address N returns incorrect data.

**Parent topic:**[Known issues](../topics/known_issues.md)

