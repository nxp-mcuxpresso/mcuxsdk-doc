# How to set the board to the Bootloader ISP mode {#topic_fsm_prg_5wb}

On the KW45B41Z-EVK board:

1.  Press and hold the BOOT CONFIG switch, **SW4**.
2.  Connect the KW45B41Z-EVK board via the micro-USB connector to the PC.
3.  Release the switch **SW4**.
4.  Check the associated USB port number on the PC \(such as, COM10\).
5.  While the KW45B41Z is in bootloader ISP mode, navigate to the folder where *blhost.exe* is located.
6.  Type the command `.\blhost.exe -p COM10 -- get-property 1` to make sure that the KW45B41Z is in Bootloader ISP mode, you should see:

    Ping responded in 1 attempt\(s\)

    Inject command 'get-property'

    Response status = 0 \(0x0\) Success.

    Response word 1 = 1258488064 \(0x4b030100\)

    Current Version = K3.1.0


On a custom board:

1.  Short the BOOT\_CFG pin to VDD while reset.
