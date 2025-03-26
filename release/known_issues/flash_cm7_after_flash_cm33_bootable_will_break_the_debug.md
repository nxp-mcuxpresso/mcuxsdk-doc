# Flashing CM7 Image After Bootable CM33 Image Breaks Build

## Issue Description

In SPI boot mode (`SW5[1..4] = 0100`), after using IDE/Secure Provisioning Tool to flash a bootable CM33 image, if any `flexspi_nor` target CM7 image is programmed using IDE, the SOC will enter an 
unresponsive state and all further debugging attempts will fail.

## Prevention

To avoid this issue:
- After flashing a bootable CM33 image, always erase the flash before flashing any non-bootable CM7 image.

## Recovery Steps

If you accidentally enter this state:
1. Change to Internal Boot mode or Serial Download mode (`SW[1..4] = 0000/0001`)
2. Use IDE/Secure Provisioning Tool to erase the flash
3. The system should now be restored to normal operation

## Note for Customer Boards

For customer boards without a boot mode switch, we are working on a permanent fix which is expected to roll out soon.

## Reference

| Ticket     | Description                                                            | Version  |
|------------|------------------------------------------------------------------------|----------|
| MCUX-76778 | Flash a CM7 image following a CM33 bootable image will break the build | 25.03.00 |
