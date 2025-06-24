# Run a demo using Keil® MDK/μVision

This section describes the steps required to build, run, and debug example applications provided in the MCUXpresso SDK.

The hello\_world demo application targeted for the LPCXpresso54018 hardware platform is used as an example, although these steps can be applied to any demo or example application in the MCUXpresso SDK.

Before downloading and running the application, perform these steps:

1.  Download and install LPCScrypt or the Windows® operating systems driver for LPCXpresso boards from [www.nxp.com/lpcutilities](http://www.nxp.com/lpcutilities). This installs the required drivers for the board.
2.  Connect the development platform to your PC via USB cable between the Link2 USB connector \(named Link for some boards\) and the PC USB connector. If you are connecting for the first time, allow about 30 seconds for the devices to enumerate.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug COM port \(to determine the COM port number, see Appendix A\). Configure the terminal with these settings:
    1.  115200 or 9600 baud rate, depending on your board \(reference BOARD\_DEBUG\_UART\_BAUDRATE variable in board.h file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit

        ![](../images/terminal_putty_configuration.png "Terminal (PuTTY) configuration")

```{include} ../topics/install_cmsis_device_pack.md
:heading-offset: 1
```

```{include} ../topics/build_a_non-xip_plain_load_example_application.md
:heading-offset: 1
```

```{include} ../topics/run_a_non-xip_plain_load_example_application.md
:heading-offset: 1
```

```{include} ../topics/how_to_program_the_non-xip_plain_load_example_appl_001.md
:heading-offset: 1
```

```{include} ../topics/how_to_program_the_non-xip_plain_load_example_appl.md
:heading-offset: 1
```

```{include} ../topics/build_an_xip_example_application_001.md
:heading-offset: 1
```

```{include} ../topics/run_an_xip_example_application_003.md
:heading-offset: 1
```

