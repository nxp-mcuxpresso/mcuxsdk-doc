# MCUXpresso SDK board support folders

The MCUXpresso SDK board support provides example applications for NXP development and evaluation boards for Arm Cortex-M cores. Board support packages are found inside of the top level boards folder. Each supported board has its own folder.(The MCUXpresso SDK package can support multiple boards). Within each `<board_name>` folder there are various sub-folders to classify the type of examples they contain. These include but are not limited to:

-   `cmsis_driver_examples`: Simple applications intended to concisely illustrate how to use CMSIS drivers.
-   `demo_apps`: Full-featured applications intended to highlight key functionality and use cases of the target MCU. These applications typically use multiple MCU peripherals and may leverage stacks and middleware.
-   `driver_examples`: Simple applications intended to concisely illustrate how to use the MCUXpresso SDK’s peripheral drivers for a single use case.
-   `rtos_examples`: Basic FreeRTOS OS examples showcasing the use of various RTOS objects \(semaphores, queues, and so on\) and interfacing with the MCUXpresso SDK’s RTOS drivers
-   `multicore_examples`: Simple applications intended to concisely illustrate how to use middleware/multicore stack.


```{include} ../topics/example_application_structure.md
:heading-offset: 1
```

```{include} ../topics/locating_example_application_source_files.md
:heading-offset: 1
```

