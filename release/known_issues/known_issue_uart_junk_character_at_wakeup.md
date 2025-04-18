# Junk character printed on the UART after exiting lowpower

-   When printing UART character soon after a wakeup from lowpower some junk character can be observed on the output. The FRO192M that clocks the UART uses the system oscillator as trimming source. To avoid these junk characters you can wait the system oscillator to be valid at the wakeup from lowpower before releasing the software.
