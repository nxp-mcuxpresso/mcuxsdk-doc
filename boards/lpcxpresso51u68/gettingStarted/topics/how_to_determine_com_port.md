# How to determine COM port

This section describes the steps necessary to determine the debug COM port number of your NXP hardware development platform. All NXP boards ship with a factory programmed, on-board debug interface, whether it’s based on OpenSDA or the legacy P&E Micro OSJTAG interface. To determine what your specific board ships with, see [Default debug interfaces](default_debug_interfaces.md).

1.  To determine the COM port, open the Windows operating system Device Manager. This can be achieved by going to the Windows operating system **Start** menu and typing **Device Manager** in the search bar, as shown in [Figure 1](how_to_determine_com_port.md#DEVICEMANAGER):

    ![](../images/device_manager.png "Device manager")

2.  In the Device Manager, expand the **Ports \(COM & LPT\)** section to view the available ports. Depending on the NXP board you’re using, the COM port can be named differently:
    1.  LPC-Link2

        ![](../images/lpc_link2.jpg "LPC-Link2")


