# usb_device_mtp example cannot boot on Keil MDK µVision

After reset, the usb_device_mtp and usb_device_mtp_lite examples cannot boot successfully when using Keil MDK µVision. Adding the *--predefine="-DXIP_BOOT_HEADER_ENABLE=1"* into **Options for target \> Linker \> Misc controls** can fix this issue.
