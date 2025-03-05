# Power Efficiency

RT6xx HiFi4 DSP has been equipped as a powerful processing core that can run at 600 MHz, but it may not be necessary at all time. It is always recommended to optimize the power efficiency at system level.

Voltage level and core frequency have huge impact on the power efficiency. Using FFT processing as example, continuous FFT may take ~130 mW at Vddcore 1.1 V / 452 MHz, and ~4 mW at Vddcore 0.7 V / 29 MHz, at room temperature. Profile or do cycle counts for software workload. If it only requires 300 MHz at peak, then the run at full power is not required. Instead, it can run with Vddcore 0.8 V 300 MHz. For more information on the Vddcore and DSP frequency operating conditions, see any *dsp example\\cm33\\pmic\_support.c BOARD\_SetPmicVoltageForFreq\(\)*, or see the data sheet, section 13.1 General Operating Conditions.

Some other tips for better power efficiency:

-   Turn off DSP/ set DSPSTALL, if needed.
-   If possible, make DSP clock adapts to its workload.
-   Call XT\_WAITI when DSP is in while loop waiting for interrupt. Similar to Arm side \_\_WFI\(\), it suspends some processor operations to reduce the power consumption.

    ```
    #include <xtensa/tie/xt_interrupt.h >
     extern void XT_WAITI(immediate s);
    ```

    The immediate value passed is the interrupt level or lower to be IGNORED. For example, if you call XT\_WAITI\(2\) both L1 and L2 interrupts are ignored and only L3 interrupts can wake up DSP.

    Current can further reduce when clocks are turned off to unused memory partitions. For more information, see User Manual 4.5.5.13 DSP SRAM access disable, Register SYSCTL0\_DSP\_SRAM\_ACCESS\_DISABLE.

-   PLLs consume power. Consider FFRO for low-power use cases.

**Parent topic:**[System Optimization](../topics/system_optimization.md)

