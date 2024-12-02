# MCUXpresso SDK board support package folders 
MCUXpresso SDK board support package provides example applications for NXP development and evaluation boards for Arm Cortex-M cores including Freedom, Tower System, and LPCXpresso boards. Board support packages are found inside the top-level boards folder and each supported board has its own folder \(an MCUXpresso SDK package can support multiple boards\). Within each *<board\_name\>* folder, there are various subfolders to classify the type of examples it contains. These include \(but are not limited to\):

-   `cmsis_driver_examples`: Simple applications intended to show how to use CMSIS drivers.
-   `demo_apps`: Full-featured applications that highlight key functionality and use cases of the target MCU. These applications typically use multiple MCU peripherals and may leverage stacks and middleware.
-   `driver_examples`: Simple applications that show how to use the MCUXpresso SDK peripheral drivers for a single use case. These applications typically only use a single peripheral but there are cases where multiple peripherals are used \(for example, SPI conversion using DMA\).
-   `emwin_examples`: Applications that use the emWin GUI widgets.
-   `rtos_examples`: Basic FreeRTOS OS examples that show the use of various RTOS objects \(semaphores, queues, and so on\) and interfaces with the MCUXpresso SDK RTOS drivers.
-   `usb_examples`: Applications that use the USB host/device/OTG stack.


```{include} ../topics/example_application_structure.md
:heading-offset: 1
```

```{include} ../topics/locating_example_application_source_files.md
:heading-offset: 1
```

