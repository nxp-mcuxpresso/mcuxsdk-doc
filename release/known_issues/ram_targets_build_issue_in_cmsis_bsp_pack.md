# RAM targets build issue in CMSIS bsp pack

CMSIS pack does not support different macro definitions for different targets, all RAM targets for projects inside CMSIS BSP PACKs for RT10XX boards will get the same macro definitions with Flash targets, resulting in build failure. To pass build for RAM targets, manually update the XIP\_EXTERNAL\_FLASH and XIP\_BOOT\_HEADER\_ENABLE value to 0 in RTE\_Components.h.

