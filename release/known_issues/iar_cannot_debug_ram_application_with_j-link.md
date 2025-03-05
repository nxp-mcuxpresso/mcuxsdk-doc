# IAR cannot debug RAM application with J-Link

Currently, IAR will call J-Link reset after the application is downloaded to SRAM, but such operation will cause SRAM data lost.

Here is a workaround to avoid real reset, with the cost of no any reset during the debugging, and hardware status uncleared.

1.  Build and debug IAR project once and see the settings folder created.
2.  Create the \_.JLinkScript file in the settings folder with the following contents.

    ```
    void ResetTarget(void) {
    JLINK_TARGET_Halt();
    }
    ```

3.  Debug the project again and now it can work.