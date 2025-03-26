# Changes on IAR debugging support after 25.03.00
Starting from 25.03.00, we make enhancement to debugging experience to make it more robust and user friendly

These changes involves debugging code update on both SDK side and IAR toolchain side. It is expected to be integrated to IAR Embedded Workbench for Arm 9.60.4. 

## Update to latest IAR version
You can check [IAR Product Updates](https://updates.iar.com/?product=EWARM) to know when IAR Embedded Workbench for Arm 9.60.4 will be rolled out. Befor that, the following manual change is needed inside you IAR installation directory.

## Necessary Change in your IAR installation (<= 9.60.3)
1. Navigate to `<iar installation directory>/arm/config/devices/NXP/i.MX/i.MXRT/`, change `MIMXRT1189xxx8_M33.i79` and `MIMXRT1189xxx8_M7.i79`, commenting out the following lines
   ```
   // JLinkScriptFile=$TOOLKIT_DIR$/config/debugger/NXP/mimxrt1180_cm33.jlinkscript
   // JLinkScriptFile=$TOOLKIT_DIR$/config/debugger/NXP/mimxrt1180_cm7.jlinkscript
   ```
2. Replace the following files under `<iar installation directory>/arm/config/debugger/NXP` with the files in `<SDK root>/boards/evkmimxrt1180/dmac/iMXRT_1180.dmac`
   ```
   iMXRT_1180.dmac
   iMXRT_1180_cm33.dmac
   iMXRT_1180_cm7.dmac
   ```
