# How to determine COM port

This section describes the steps necessary to determine the debug COM port number of your NXP hardware development platform.

1.  To determine the COM port, open the Windows operating system Device Manager. This can be achieved by going to the Windows operating system **Start** menu and typing **Device Manager** in the search bar, as shown in [Figure 1](#FIG_DEVICEMANAGER).

    ![](../images/device_manager.png "Device Manager")

2.  In the **Device Manager**, expand the **Ports \(COM & LPT\)** section to view the available ports. Depending on the NXP board you are using, the COM port can be named differently.

    1.  OpenSDA – CMSIS-DAP/mbed/DAPLink interface:

        ![](../images/opensda_cmsis_dap.png "OpenSDA – CMSIS-DAP/mbed/DAPLink interface")

    2.  OpenSDA – P&E Micro:

        ![](../images/opensda_pe_micro.png "OpenSDA – P&E Micro")

    3.  OpenSDA – J-Link:

        ![](../images/opensda_jlink.png "OpenSDA – J-Link")

    4.  P&E Micro OSJTAG:

        ![](../images/pe_micro_osjtag.png "P&E Micro OSJTAG")

    5.  LPC-Link2:

        ![](../images/lpc-link2.png "LPC-Link2")

    6.  FTDI UART:

        ![](../images/ftdi_uart.png "FTDI UART")


