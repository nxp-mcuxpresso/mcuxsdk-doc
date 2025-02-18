# MCUXpresso SDK board support folders

MCUXpresso SDK provides example applications for development and evaluation boards. Board support packages are found inside the top level `<board_name>` folder, and each supported board has its own folder \(an MCUXpresso SDK package can support multiple boards\). Within each `<board_name>` folder, there are various sub-folders for each example they contain. These include \(but are not limited to\):

-   `demo_apps`: Applications intended to highlight key functionality and use cases of the target MCU. These applications typically use multiple MCU peripherals and may leverage stacks and middleware.
-   `driver_examples`: Simple applications intended to concisely illustrate how to use the MCUXpresso SDK’s peripheral drivers for a single use case. These applications typically only use a single peripheral, but there are cases where multiple are used.
-   `rtos_examples`: Basic FreeRTOS examples showcasing the use of various RTOS objects \(semaphores, queues, and so on\) and interfacing with the MCUXpresso SDK’s RTOS drivers.
-   `cmsis_driver_examples`: Simple applications intended to concisely illustrate how to use CMSIS drivers.
-   `multicore_examples`: Simple applications intended to concisely illustrate how to use middleware/multicore stack.
-   `mmcau_examples`: Simple applications intended to concisely illustrate how to use middleware/mmcau stack.


```{include} ../topics/example_application_structure.md
:heading-offset: 1
```

```{include} ../topics/locating_example_application_source_files.md
:heading-offset: 1
```

