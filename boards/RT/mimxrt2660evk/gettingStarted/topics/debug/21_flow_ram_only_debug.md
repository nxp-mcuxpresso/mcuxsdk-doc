# Flow -- `ram_only` Debug

---

## `ram_only` Debug

```
Step 1.  Install debug patch
         (see Patch Install section)

Step 2.  Set boot switch to 0b00  (XSPI NOR boot mode)

Step 3.  Build with ram_only target

Step 4.  Connect debugger

Step 5.  Download ELF to ITCM and debug

--> DONE
```

> **POR boot**: the image downloaded by the debugger is volatile and does not POR boot. To create a POR-bootable image, a boot header must be attached -- either at build time or via an external tool. Refer to the RAM ONLY Targets section of this guide for details.
