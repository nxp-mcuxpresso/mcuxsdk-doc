# How to determine COM port

This section describes the steps necessary to determine the debug COM port number of your NXP hardware development platform. All NXP boards ship with a factory programmed, onboard debug interface, whether it is based on MCU-Link or the legacy OpenSDA, LPC-Link2, P&E Micro OSJTAG interface. To determine what your specific board ships with, see [Default debug interfaces](default_debug_interfaces.md).

1.  **Linux**: The serial port can be determined by running the following command after the USB Serial is connected to the host:

    ```
    $ dmesg | grep "ttyUSB"
      [503175.307873] usb 3-12: cp210x converter now attached to ttyUSB0
      [503175.309372] usb 3-12: cp210x converter now attached to ttyUSB1
    ```

    There are two ports, one is for core0 debug console and the other is for core1.

2.  **Windows**: To determine the COM port open Device Manager in the Windows operating system. Click the **Start** menu and type **Device Manager** in the search bar.

    In the Device Manager, expand the **Ports \(COM & LPT\)** section to view the available ports. The COM port names are different for all the NXP boards.

    1.  **CMSIS-DAP/mbed/DAPLink** interface:

        ![](images/mculink_cmsis_dap.png "MCU-Link – CMSIS-DAP/mbed/DAPLink interface")
        ![](images/opensda_cmsis_dap.png "OpenSDA – CMSIS-DAP/mbed/DAPLink interface")

    2.  **P&E Micro**:

        ![](images/opensda_pe_micro.png "P&E Micro")

    3.  **J-Link**:

        ![](images/opensda_jlink.png "J-Link")

    4.  **P&E Micro OSJTAG**:

        ![](images/pe_micro_osjtag.png "P&E Micro OSJTAG")

    5.  **MRB-KW01**:

        ![](images/mrb_kw01.png "MRB-KW01")

