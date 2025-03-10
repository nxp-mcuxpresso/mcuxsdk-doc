# DSP examples cannot boot the Fusion core 

The examples in the dsp\_examples folder can not run properly since they can not boot the Fusion DSP core. It can be fixed by removing line 633 from board.c: `TRDC_MbcSetMemoryBlockConfig(TRDC, &mbcBlockConfig)`; under comment /\* non secure state can access CGC0 \(Pbridge0, slot 47\) for HIFI4 DSP \*/. This will be fixed in the next release.

For the dsp\_voice\_spot\_demo there is a wrong incbin.S file used. Please use the same file as for the rest of the DSP examples.

