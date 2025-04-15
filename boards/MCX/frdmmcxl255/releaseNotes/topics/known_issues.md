# Known Issues

This section lists the known issues, limitations, and/or workarounds.

## I2C examples on cm33 does not work on pins specified in readme
Use following pins of J7 PMOD header:
 - P3_11 for SDA
 - P3_10 for SCL

Another option is to switch example to use LPI2C0. But this requires 
configuration of appropriate pins, clocks and resets. 


## Missing release from reset of all lptimer examples
Please add following line to the end of function ``BOARD_InitHardware(void)``
in hardware_init.c to make example work:

``RESET_ReleasePeripheralReset(kAonLPTMR_RST_SHIFT_RSTn);``

## QTMR inputcapture_outputpwm is not able to measure PWM
You can skip measurement by commenting out first for cycle in qtmr_timer.c.

	for (i = 0; i < 10; i++)
	{
       	/* Check whether compare interrupt occurs */
       	while (!(qtmrIsrFlag))
       	{
       	}
       	PRINTF("\r\n Timer interrupt has occurred !");
       	qtmrIsrFlag = false;
    }
Then is necessary to swap channels in app.h:

    #define BOARD_QTMR_INPUT_CAPTURE_CHANNEL kQTMR_Channel_0
    #define BOARD_QTMR_PWM_CHANNEL           kQTMR_Channel_1

Example will then generate pwm signal.

## inputcapture_outputpwm_dma example cannot work 
QTMR is not supported by DMA.

## Don't use KPP example on cm0+ core
Example does not work because keyboard uses same pins as AON UART. 

Use example on cm33 core instead.

## UART seven_bit examples do not work

## CLOCK driver - CLOCK_GetFroAonFreq() returns wrong freq
Function ``CLOCK_GetFroAonFreq()`` returns 4M instead of 10M and vice versa.  

## aon_lpadc is not present int package
Please find aon_lpadc and its examples on NXP github.