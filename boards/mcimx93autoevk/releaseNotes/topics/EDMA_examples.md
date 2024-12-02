# eDMA examples accessing AIPS peripheral bridge memory must run through U-Boot loading method

Non-secure access to Arm IP Bus \(AIPS\) must be configured in Trusted Resource Domain Control \(TRDC\) for enhanced direct memory access \(eDMA\) controller. Due to the limitation that Sentinel ROM can release TRDC only once, such examples must run through U-Boot loading method after Trusted Firmware-A \(TF-A） configuring TRDC.

To make low-power boot mode work for only M core in such example, you need to implement the request of the TRDC release and configure TRDC. However, it will break the single boot mode with TF-A/Linux BSP.

The following eDMA examples need access to AIPS.

-   cmsis\_lpi2c\_edma\_b2b\_transfer\_master
-   cmsis\_lpi2c\_edma\_b2b\_transfer\_slave
-   cmsis\_lpuart\_edma\_transfer
-   flexcan\_loopback\_edma\_transfer
-   lpi2c\_edma\_b2b\_transfer\_master
-   lpi2c\_edma\_b2b\_transfer\_slave
-   lpuart\_edma\_transfer
-   pdm\_edma\_transfer
-   sai\_edma\_transfer

**Parent topic:**[Known Issues](../topics/known_issues.md)

