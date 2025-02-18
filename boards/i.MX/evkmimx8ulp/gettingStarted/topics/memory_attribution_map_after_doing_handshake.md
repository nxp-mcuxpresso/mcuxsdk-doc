# Memory attribution map after doing handshake 

The memory attribution map settings after the handshake procedure is successful between Cortex-M33 and Cortex-A35.

|Name|Memory block checker/ Memory region checker \(MBC/MRC\)|Resulting access level| |
|----|-------------------------------------------------------|----------------------|--|
|FLEXSPI1 \(alias\)|Non Secure|Non Secure|0x5FFF\_FFFF|
|0x5000\_0000|
|FLEXSPI1|Non Secure|Non Secure|0x4FFF\_FFFF|
|0x4000\_0000|
|PBridge1 FlexCAN0 \(alias\)|Non Secure|Non Secure|0x380A\_BFFF|
|0x380A\_8000|
|PBridge1 SAI0 \(alias\)|Non Secure|Non Secure|0x3809\_C0FF|
|0x3809\_C000|
|PBridge1 LPUART1 \(alias\)|Non Secure|Non Secure|0x3809\_B02F|
|0x3809\_B000|
|PBridge1 LPI2C0 \(alias\)|Non Secure|Non Secure|0x3809\_8173|
|0x3809\_8000|
|PBridge1 FlexSPI1 \(alias\)|Non Secure|Non Secure|0x3809\_22FF|
|0x3809\_2000|
|PBridge0 LPSPI1 \(alias\)|Non Secure|Non Secure|0x3803\_F7FF|
|0x3803\_F000|
|PBridge0 FlexIO0 \(alias\)|Non Secure|Non Secure|0x3803\_C91F|
|0x3803\_C000|
|PBridge0 FlexSPI0 \(alias\)|Non Secure|Non Secure|0x3803\_92FF|
|0x3803\_9000|
|PBridge1 FlexCAN0|Non Secure|Non Secure|0x280A\_BFFF|
|0x280A\_8000|
|PBridge1 SAI0|Non Secure|Non Secure|0x2809\_C0FF|
|0x2809\_C000|
|PBridge1 LPUART1|Non Secure|Non Secure|0x2809\_B02F|
|0x2809\_B000|
|PBridge1 LPI2C0|Non Secure|Non Secure|0x2809\_8173|
|0x2809\_8000|
|PBridge1 FlexSPI1|Non Secure|Non Secure|0x2809\_22FF|
|0x2809\_2000|
|PBridge0 LPSPI1|Non Secure|Non Secure|0x2803\_F7FF|
|0x2803\_F000|
|PBridge0 FlexIO0|Non Secure|Non Secure|0x2803\_C91F|
|0x2803\_C000|
|PBridge0 FlexSPI0|Non Secure|Non Secure|0x2803\_92FF|
|0x2803\_9000|
|SSRAM P6 \(alias\)|Non Secure|Non Secure|0x3007\_FFFF|
|0x3006\_0000|
|SSRAM P5 \(alias\)|Non Secure|Non Secure|0x3005\_FFFF|
|0x3004\_0000|
|SSRAM P4 \(alias\)|Non Secure|Non Secure|0x3003\_FFFF|
|0x3003\_0000|
|SSRAM P3 \(alias\)|Non Secure|Non Secure|0x3002\_FFFF|
|0x3002\_0000|
|SSRAM P2 \(alias\)|Non Secure|Non Secure|0x3001\_FFFF|
|0x3001\_0000|
|SSRAM P1 \(alias\)|Non Secure|Non Secure|0x3000\_FFFF|
|0x3000\_8000|
|SSRAM P0 \(alias\)|Non Secure|Non Secure|0x3000\_7FFF|
|0x3000\_0000|
|SSRAM P6|Non Secure|Non Secure|0x2007\_FFFF|
|0x2006\_0000|
|SSRAM P5|Non Secure|Non Secure|0x2005\_FFFF|
|0x2004\_0000|
|SSRAM P4|Non Secure|Non Secure|0x2003\_FFFF|
|0x2003\_0000|
|SSRAM P3|Non Secure|Non Secure|0x2002\_FFFF|
|0x2002\_0000|
|SSRAM P2|Non Secure|Non Secure|0x2001\_FFFF|
|0x2001\_0000|
|SSRAM P1|Non Secure|Non Secure|0x2000\_FFFF|
|0x2000\_8000|
|SSRAM P0|Non Secure|Non Secure|0x2000\_7FFF|
|0x2000\_0000|
|SSRAM P7 \(alias\)|Non Secure|Non Secure|0x1FFF\_FFFF|
|0x1FFC\_0000|
|FlexSPI0 \(alias\)|Non Secure|Non Secure|0x1BFF\_FFFF|
|0x1400\_0000|
|SSRAM P7|Non Secure|Non Secure|0x0FFF\_FFFF|
|0x0FFC\_0000|
|FlexSPI0|Non Secure|Non Secure|0x0BFF\_FFFF|
|0x0400\_0000|

**Note:**

1.  Assign Domain 1 for DMA1, USB0, USB1, ENET, USDHC0, USDHC1, USDHC2, and CAAM Master.
2.  The bus attribute for DMA1, USB0, USB1, ENET, USDHC0, USDHC1, and USDHC2 is Non Secure.
3.  The bus attribute for CAAM Master is Secure.
4.  Security level of MBC/MRC settings of other memory space that are not be shown in the table for Domain 1 are Secure, so master cannot access resources that are controlled by MBC/MRC in other memory spaces when master is in Non Secure state.

|Name|MBC/MRC|Resulting access level| |
|----|:-----:|:--------------------:|::|
|PBridge1|Non Secure|Non Secure|0x280F\_FFFF|
|0x2808\_0000|
|SSRAM P2|Secure|No Access|0x2001FFFF|
|0x20018000|
|Non Secure|Non Secure|0x20017FFF|
|0x20010000|

**Note:**

1.  Assign Domain 1 for DMA1, USB0, USB1, ENET, UDSHC0, USDHC1, UDSHC2, and CAAM Master.
2.  Security level of MBC/MRC settings of other memory space that are not shown in the table for Domain 1 are Secure, so the master cannot access resources that are controlled by MBC/MRC in other memory spaces.

|Name|SAU|IDAU|MBC/MRC|Resulting access level| |
|----|---|----|-------|:--------------------:|::|
|GPIOC\_REGS \(alias\)|Secure|Secure|Secure|Secure|0x3882\_FFFF|
|0x3882\_0000|
|GPIOB\_REGS \(alias\)|Secure|Secure|Secure|Secure|0x3881\_FFFF|
|0x3881\_0000|
|GPIOA\_REGS \(alias\)|Secure|Secure|Secure|Secure|0x3880\_FFFF|
|0x3880\_0000|
|MICFIL \(alias\)|Secure|Secure|Secure|Secure|0x3811\_10AB|
|0x3811\_1000|
|SAI3 \(alias\)|Secure|Secure|Secure|Secure|0x3811\_00FF|
|0x3811\_0000|
|SAI2 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_F0FF|
|0x3810\_F000|
|LPSPI3 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_E7FF|
|0x3810\_E000|
|LPSPI2 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_D7FF|
|0x3810\_D000|
|LPUART3 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_C02F|
|0x3810\_C000|
|LPUART2 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_B02F|
|0x3810\_B000|
|I3C1 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_AFFF|
|0x3810\_A000|
|LPI2C3 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_9173|
|0x3810\_9000|
|LPI2C2 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_8173|
|0x3810\_8000|
|MRT \(alias\)|Secure|Secure|Secure|Secure|0x3810\_70FF|
|0x3810\_7000|
|TPM3 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_6087|
|0x3810\_6000|
|TPM2 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_5087|
|0x3810\_5000|
|PCC2 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_2047|
|0x3810\_2000|
|WDOG2 \(alias\)|Secure|Secure|Secure|Secure|0x3810\_100F|
|0x3810\_1000|
|MU1\_B \(alias\)|Secure|Secure|Secure|Secure|0x3810\_028F|
|0x3810\_0000|
|FlexCAN0 \(alias\)|Secure|Secure|Secure|Secure|0x380A\_BFFF|
|0x380A\_8000|
|ADC1 \(alias\)|Secure|Secure|Secure|Secure|0x380A\_2303|
|0x380A\_2000|
|IOMUXC0 \(alias\)|Secure|Secure|Secure|Secure|0x380A\_1AEB|
|0x380A\_1000|
|SAI1 \(alias\)|Secure|Secure|Secure|Secure|0x3809\_D0FF|
|0x3809\_D000|

**Note:**

1.  SAU is disabled.
2.  Cortex-M33 can access all of the secure resources. All of the resources \(the security level of these resources that are controlled by MBC/MRC\) are secure when Cortex-M33 is in secure state.
3.  Assign domain 6 for Cortex-M33.

|Name|MBC/MRC|Resulting access level| | |
|----|-------|----------------------|--|--|
|PBridge1 IOMUXC0|Non Secure|Non Secure|0x280A\_1AEB|
|0x280A\_1000|
|PBridge1 LPI2C0|Non Secure|Non Secure|0x2809\_8173|
|0x2809\_8000|
|PBridge1 TPM0|Non Secure|Non Secure|0x2809\_5087|
|0x2809\_5000|
|PBridge1 PCC1|Non Secure|Non Secure|0x2809\_10BF|
|0x2809\_1000|
|PBridge0 FlexSPI0|Non Secure|Non Secure|0x2803\_92FF|
|0x2803\_9000|
|PBridge0 SEMA42\_0|Non Secure|Non Secure|0x2803\_7043|
|0x2803\_7000|
|PBridge0 CGC0|Non Secure|Non Secure|0x2802\_FFFF|
|0x2802\_F000|
|PBridge0 SIM0-S|Non Secure|Non Secure|0x2802\_B3FF|
|0x2802\_B000|
|S400 MU-AP of EdgeLock secure enclave|Non Secure|Non Secure|0x2702\_028C|
|0x2702\_0000|
|FSB of EdgeLock secure enclave|Non Secure|Non Secure|0x2701\_0BFC|
|0x2701\_0000|
|SSRAM P7|Non Secure|Non Secure|0x1FFF\_FFFF|
|0x1FFF\_8000|
|Secure|Secure|0x1FFF\_7FFF|
|0x1FFC\_0000|
|FlexSPI0|Non Secure|Non Secure|0x0BFF\_FFFF|
|0x0400\_0000|

**Note:**

1.  Security level of MBC/MRC settings of Other memory space that are not shown in the table for Domain 7 are Secure. The master can access resources that are controlled by MBC/MRC in other memory spaces when the master is in secure state.
2.  Assign domain 7 for Cortex-A35.

