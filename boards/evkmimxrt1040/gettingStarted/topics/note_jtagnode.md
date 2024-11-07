# Note when debugging with JTAG mode {#note_jtagnode}

When debugging with JTAG mode, the JTAG\_MOD pin on MIMXRT1040-EVK board is reused. If the M.2 device is plugged in, the JTAG\_MOD pin is pulled higher, resulting in debug failure. If this happens, ensure that the J80 Jumper is in the open state.

