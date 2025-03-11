# OSJTAG USB function failure

The JM60 USB port, **J8**, is used for OSJTAG and USB CDC bridge. The JM60 USB port cannot work properly after being replugged when board is powered by another power source.

One example of the failure case:

1.  Power the board with DSC USB port, **J21**.
2.  Replug/Re-power the JM60 USB port.