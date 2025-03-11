# Edgefast\_Bluetooth stack New Project Wizard compile failure 

To prevent compile failure, when using Edgefast\_Bluetooth New Project Wizard \(NPW\), some actions are done manually.

1.  The EDGEFAST Bluetooth New Project Wizard \(NPW\) does not support the "no board" option. Therefore, a board must be selected when creating project.
2.  The c/c++ library type must be set to "NewlibNano \(none\)".
3.  There is a new region “LITTLEFS\_FLASH\_region” which should be added in Memory configuration setting GUI.

    The region "LITTLEFS\_FLASH\_region" is split from region "BOARD\_FLASH".

    The size of the region "LITTLEFS\_FLASH\_region" should meet the following conditions:

    -   Condition 1, The size should not be less than 16 kB.
    -   Condition 2, The size should be a multiple of the erase page. The multiple should not be less than 4.
4.  Memory configuration: The memory region sequence should follow the order below.

    | Memory region         | Location   | Region Size |
	| --------------------- | ---------- | ----------- |
	| BOARD_FLASH           | 0x60000000 | 0x600000    |
	| LITTLEFS_FLASH_region | 0x60600000 | 0x200000    |
	| SRAM_OC               | 0x20200000 | 0x40000     |
	| SRAM_DTC              | 0x20000000 | 0x20000     |
	| SRAM_ITC              | 0x00000000 | 0x20000     |
	| BOARD_SDRAM           | 0x80000000 | 0x1E00000   |
	| NCACHE_REGION         | 0x81E00000 | 0x200000    |


