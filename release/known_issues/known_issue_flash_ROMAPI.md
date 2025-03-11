# Flash ROMAPI
Note that:

-   If using ROM API for internal flash or SPI NOR operation, reserve RAM location 0x200030A0 - 0x200032CF \(`0x300030A0` - `0x300032CF`\).
-   If using kb API, reserve `0x20002000` - `0x200032FF` \(`0x30002000` - `0x300032FF`\).
