# MCUXpresso SDK board support package folders {#GUID-F32E779B-EB99-4520-9ECB-082327CD4EC5}

MCUXpresso SDK board support package provides example applications for NXP development and evaluation boards for Arm Cortex-M cores. Board support packages are found inside the top level boards folder and each supported board has its own folder \(an MCUXpresso SDK package can support multiple boards\). Within each `<board_name>` folder, there are various sub-folders to classify the type of examples it contains. These types include \(but are not limited to\):

-   `cmsis_driver_examples`: Simple applications intended to show how to use CMSIS drivers.
-   `demo_apps`: Full-featured applications that highlight key functionality and use cases of the target MCU. These applications typically use multiple MCU peripherals and may leverage stacks and middleware.
-   `driver_examples`: Simple applications that show how to use the MCUXpresso SDK’s peripheral drivers for a single use case. These applications typically only use a single peripheral but there are cases where multiple peripherals are used \(for example, SPI conversion using DMA\).
-   `rtos_examples`: Basic FreeRTOS examples that show the use of various RTOS objects \(semaphores, queues, and so on\) and interfaces with the MCUXpresso SDK’s RTOS drivers.
-   `Other_examples`: See detail in package *boards/evkmimxrt1180*.


```{include} ../topics/example_application_structure.md
:heading-offset: 1
```

```{include} ../topics/locating_example_application_source_files.md
:heading-offset: 1
```

