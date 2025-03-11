# Debugging problems

When debugging `hyperram_txt_debug` or `hyperram_txt_release` target, user may encounter issue when debug with breakpoint. The reason is because code is cached. The default breakpoint type is auto/software breakpoint, it will lead soc core and debugger misaligned. As a workaround, please set breakpoint type to hardware breakpoint.

In addition, `hyperram_txt` targets can't debug on IAR versions: 9.50.1, 9.50.2, 9.60.1. The resolution is: delete the selected contents as shown in [Figure 1](#fig_mp1_ww3_5bc) in IAR path: *arm\\config\\flashloader\\NXP\\FlashIMXRT1180-EVK\_FlexSPI\_M33.board*.
