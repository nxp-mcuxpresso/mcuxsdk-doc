# HCI black box application for MCXW23 – Insufficient stack size on iar and armclang
hci_bb_mcxw23 binaries compiled using iar or armclang toolchain have an insufficient stack size and can crash when issuing HCI commands requiring a bigger stack size like LE_Extended_Advertising_Enable.
Binaries compiled with gcc don't suffer from this issue.


# Wireless UART application – Bluetooth Low Energy advertising and connection loss issue
When using the Wireless UART application with default settings, functionality is as expected. However, the following issue occurs when the Bluetooth Low Energy advertising interval is set to 20 milliseconds and the connection interval is set to 7.5 milliseconds:
After two devices establish a connection, the central device fails to start advertising to a third device after a button press. The HCI command to start advertising returns success, but the device does not transmit any advertising packets. Additionally, the supervision timeout causes the existing connection to drop unexpectedly.

# Bluetooth Synopsys Controller
-   Stability observation during extended testing
    The llhwc_set_adv_param function shows unexpected behavior during extended sequences of link layer tests, typically after 1.5 hours of continuous execution without a hardware reset.
    -   This rare behavior occurs only under specific test conditions.
    -   The behavior relates to the extended advertising feature.
    -   This behavior does not impact regular usage scenarios.
