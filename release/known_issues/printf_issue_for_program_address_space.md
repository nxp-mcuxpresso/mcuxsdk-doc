# PRINTF issue for program address space

When project is compiled with SDM, print the address in program address space malfunction.

* Failed example when SDM
  - `PRINTF("%p", main);`
  Root cause: in SDM, `%p` is treated as 16-bit value, however `main` in program address space is still considered as 32-bit.
* Workaround(compliant with SDM and LDM)
  - `PRINTF("0x%lx", (uint32_t)main);`

