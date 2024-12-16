# Program NBU firmware 

The Narrow Band Unit \(NBU\) firmware is included in the SDK folder as a signed and encrypted FW. SDK v2.16.0:

**MCX-W72 A1 silicon:**

*SDK\_2\_16\_0\_MCX-W72-EVK\\middleware\\wireless\\ble\_controller\\bin\\mcxw72\_nbu\_ble\_hosted.bin*

To program the NBU software for the MCX-W72, perform the following steps:

1.  While holding pressed the **SW4** on the MCX-W72-EVK board, attach the USB connector J14 to your computer. Then, release the **SW4** after you plugged the USB cable on your computer.

    ![](../images/nbu_boot_config.png "Attach the USB connector J14")

2.  Verify which COM port is assigned to your MCX-W72-EVK board. To check the assigned COM port, in the Windows **Device Manager** program, search for Ports **\(COM & LPT\)** and save the COM port number. In this example, the assigned COM port is **COM3**.

    ![](../images/nbu_check_com_port.png "Check the assigned COM port")

3.  Open the *04. Tools* folder that comes together with this document and go to the *script* folder. Locate the *MCXW72-EVK\_NBUProgram.cmd* and open it using any text editor. Replace all the references to **COMX** with the COM Port assigned to your MCX-W72-EVK board. Save the changes applied to the script.

    **Note:** To run the script, place the *blhost.exe* and the *MCX-W72-EVK\_NBUProgram.cmd* script in the same folder. Both scripts can be found in the *04. Tools* folder。

4.  Double click on the *MCX-W72-EVK\_NBUProgram.cmd* script to program the NBU and load the FAT software. This script first executes a command to make sure the **MCXW72** has entered ISP mode properly. If the device did not enter in ISP mode, it cannot be programmed. The following examples show when the device did not enter in ISP \(left\) and when the device was programmed properly \(right\).

    ![](../images/nbu_programmed.png "Load the FAT software")

