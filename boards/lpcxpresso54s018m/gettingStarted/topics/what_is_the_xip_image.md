# What is the XIP image?

When an XIP \(Execute-in-Place\) image is used, the MCU executes instructions and uses data directly from external \(quad\) SPI flash. When building, it needs to be programmed to the external onboard flash. After reset, the bootloader starts to run. Then, it checks the image type \(which is set in the image header, which resides in the startup code\). If the type is XIP image, the device executes in the external flash.

**Parent topic:**[Locating example application source files](../topics/locating_example_application_source_files.md)

