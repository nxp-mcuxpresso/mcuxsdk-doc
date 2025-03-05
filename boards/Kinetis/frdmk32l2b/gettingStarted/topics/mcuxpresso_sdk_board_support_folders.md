# MCUXpresso SDK board support folders

MCUXpresso SDK board support provides example applications for NXP development and evaluation boards for Arm® Cortex®-M cores including Freedom, Tower System, and LPCXpresso boards. Board support packages are found inside of the top level boards folder, and each supported board has its own folder \(an MCUXpresso SDK package can support multiple boards\). Within each <board\_name\> folder, there are various sub-folders to classify the type of examples they contain. These include \(but are not limited to\):

-   cmsis\_driver\_examples: Simple applications intended to concisely illustrate how to use CMSIS drivers.
-   demo\_apps: Full-featured applications intended to highlight key functionality and use cases of the target MCU. These applications typically use multiple MCU peripherals and may leverage stacks and middleware.
-   driver\_examples: Simple applications intended to concisely illustrate how to use the MCUXpresso SDK’s peripheral drivers for a single use case. These applications typically only use a single peripheral, but there are cases where multiple peripherals are used \(for example, SPI conversion using DMA\).
-   rtos\_examples: Basic FreeRTOSTM OS examples showcasing the use of various RTOS objects \(semaphores, queues, and so on\) and interfacing with the MCUXpresso SDK’s RTOS drivers.
-   usb\_examples: Applications that use the USB host/device/OTG stack.


```{include} ../topics/example_application_structure.md
:heading-offset: 1
```

```{include} ../topics/locating_example_application_source_files.md
:heading-offset: 1
```

