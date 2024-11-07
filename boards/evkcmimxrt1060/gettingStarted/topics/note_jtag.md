# Note when debugging with JTAG mode {#note_jtag}

When debugging with JTAG mode, the JTAG\_MOD pin on MIMXRT1060-EVKC board is reused. If the M.2 device is plugged in, the JTAG\_MOD pin is pulled higher, resulting in debug failure. If this happens, ensure that the J103 Jumper is in the open state.

