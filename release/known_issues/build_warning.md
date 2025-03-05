# Build warning in freertos_tickless example

A build warning appears in the freertos_tickless example while working in the ArmGCC environment.
    
    .. code-block:: none
        `c:\c\pkg\cmsis\core\include\core_cm0plus.h:854:52: warning: array subscript 14 is above array bounds of 'volatile uint32_t[8]' {aka 'volatile long unsigned int[8]'} [-Warray-bounds]`.

