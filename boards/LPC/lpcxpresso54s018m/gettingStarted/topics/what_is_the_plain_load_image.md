# What is the plain load image?

The plain load image is linked to SRAMX. When building, it needs to be programmed to the external onboard flash. After reset, the bootloader starts to run. Then, it checks the image type \(which is set in the image header, which resides in the startup code\). If the type is plain load image, the bootloader copies the image to SRAMX, then jumps to SRAMX to run.

**Parent topic:**[Locating example application source files](../topics/locating_example_application_source_files.md)

