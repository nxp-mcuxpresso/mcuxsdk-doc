# HiFi4 System Programming

This section provides more examples, tips, and some best practices about HiFi4 programming on RT600 EVKs. It focuses more on RT6xx and SDK. For general HiFi programming, see the Xtensa IDE documents. You can find them in the directory **Xtensa Xplorer IDE menu Help \> PDF Documentation**.

The following are some frequently used references:

-   Xtensa Instruction Set Architecture \(ISA\) Reference Manual: Architecture/ high-level overview.
-   HiFi 4 DSP User's Guide: Most useful reference manual for DSP programmer. It has all details about HiFi4 instructions and intrinsics, as well as some algorithm optimization techniques.
-   Xtensa XOS Reference Manual: XOS is the default and native embedded kernel for Xtensa HiFi cores. SDK examples use XOS as well.
-   Xtensa System Software Reference Manual: XTOS, also known as the basic runtime and handlers, has been depreciated and moved toward XOS. However, the Xtensa Processor Hardware Abstraction Layer/ HAL is still very useful in many perspectives. SDK examples use HAL functions.
-   Xtensa Linker Support Packages \(LSPs\) Reference Manual and GNU Linker User's Guide: Both documents are useful for understanding the HiFi program linker and the memory map.

Specifically for RT6xx, the user manual and the data sheet are the most important references. All product specifications are found in the user guide and data sheet documents.


```{include} ../topics/hifi4_boot_loader_and_memory_map.md
:heading-offset: 1
```

```{include} ../topics/peripheral_drivers_and_interrupts.md
:heading-offset: 1
```

```{include} ../topics/messaging_unit_semaphore_and_ipc.md
:heading-offset: 1
```

```{include} ../topics/naturedsp_library.md
:heading-offset: 1
```

```{include} ../topics/system_optimization.md
:heading-offset: 1
```

