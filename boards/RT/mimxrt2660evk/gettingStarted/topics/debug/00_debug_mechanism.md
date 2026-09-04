# The New Debugging Mechanism

In previous RT 4-digit products, the debugging run and the POR (power-on reset) run
followed diverged paths:

- **Debugging run**: the debugger interrupted the ROM boot process and took over
  control, doing things like Flash / HyperRAM init, TRDC init and many other
  configurations, then downloaded the image, pointed PC/SP to a specified place and
  stopped there.
- **POR run**: ROM did all of the initialization work, including Flash / HyperRAM
  init, copying the image from flash memory to its load address and jumping to its
  entry. ROM also had its own strategy to configure TRDC.

This running-path difference caused a lot of production-time problems. Some issues
were exposed only on the customer side and were not caught during the NPI
development cycle, where the debugging run is used most of the time.

To resolve this problem, the debugging mechanism is re-designed in RT2660. For any
type of target (`debug` / `xspi_nor_debug` / `psram_debug`), the image is now linked
into flash-memory addresses with a valid image header that ROM can recognize. The
debugger uses a flashloader to download it to flash memory, then triggers a system
reset. ROM takes ownership this time: it recognizes the header, does the appropriate
configuration on the on-board memory and TRDC, and jumps to the application entry.
The debugger sets a watchpoint on the ROM-to-application entry and halts the CPU
there. The developer can debug normally from this point.

As can be seen, the new debugging method maximally utilizes the ROM boot procedures
and does not perform any debugger-specific configuration. This makes the debugging
run follow an identical path to the POR boot run.

Both Ozone and IAR debugging are supported. The remainder of this guide covers the
full set of RT2660 debug scenarios: patch install, build targets, per-toolchain
setup, and the concrete debug flows.
