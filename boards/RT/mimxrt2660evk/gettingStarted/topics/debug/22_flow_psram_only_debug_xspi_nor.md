# Flow -- `psram_only` Debug (XSPI NOR + PSRAM system)

The one-time board setup (steps 2-a through 2-c) is required before the first debug session on each board. Skip to step 3 if PSRAM is already initialized.

---

## `psram_only` Debug -- XSPI NOR + PSRAM system

```
Step 1.   Install debug patch
          (see Patch Install section)

[One-time board setup -- first time only]

Step 2-a. Build auxiliary demo
          target: xspi_nor_psram_debug

Step 2-b. Set boot switch to 0b00  (XSPI NOR boot mode)

Step 2-c. Program auxiliary image into XSPI NOR flash
          (standard Unified Linkage flash flow, see Unified Linkage Debug flow or IDE Setup section)
          Boot ROM reads XMCD from auxiliary on every reset --
          PSRAM is now initialized automatically after each reset.

[Debug session -- every time]

Step 3.   Build with psram_only target

Step 4.   Connect debugger

Step 5.   Download ELF to PSRAM and debug

--> DONE
```

> **POR boot**: the image downloaded by the debugger is volatile and does not POR boot. To create a POR-bootable image, a boot header must be attached -- either at build time or via an external tool. Refer to the RAM ONLY Targets section of this guide for details.
