.. _frdmmcxl255:

FRDM-MCXL255
####################

Overview
********

The FRDM-MCXL255 board is a design and evaluation platform based on the NXP MCXL255 microcontroller
(MCU). The MCXL255 MCU is a low-power microcontroller for industrial and consumer Internet of Things
(IoT) applications. It has one Arm Cortex-M33 core running at speeds of up to 96 MHz and one 
Arm Cortex-M0+ core up to 10 MHz.
This series features our Adaptive Dynamic Voltage Control (ADVC) for optimized power consumption at
low frequency operation. Compared to traditional low-power MCUs, a dedicated ultra-low-power (ULP)
Sense Domain allows operation of low-power peripherals while keeping the main core in Deep
Power Mode. This avoids event triggering and keeps data acquisition to extremely low power levels.

The board is compatible with Arduino boards (Arduino UNO R3 and Arduino A4/A5), Mikroe click boards, 
and Pmod boards. It can be used with IAR Embedded Workbench development tool.

For debugging the MCXA276 MCU, the FRDM-MCXL255 board uses an onboard (OB) debug probe, MCU-Link lite
OB, which is based on another NXP MCU: LPC55S16

MCU device and part on board is shown below:

 - Device: MCXL255
 - PartNumber: MCXL255VDF

Getting Started with MCUXpresso SDK Package
*******************************************
.. toctree::
   :maxdepth: 1

   ../../../gsd/package.rst

Getting Started with MCUXpresso SDK GitHub
*******************************************
.. toctree::
   :maxdepth: 1

   ../../../gsd/repo.rst

Release Notes
*******************************************
.. toctree::
   :maxdepth: 1

   releaseNotes/rnindex.md

ChangeLog
*******************************************
.. toctree::
   :maxdepth: 1

   changeLog/clindex.md

Currently supported drivers
***************************

- clock
- reset
- power (Limited. Currently supports only PD1, PD2 and DPD2.)
- lptmr
- qtmr
- lpi2c
- lpspi
- lpuart
- gpio (Without examples)
- kpp
- acmp (Driver and examples are named lpcmp. lpcmp periph. is not supported in this release)
- aon_lpadc (Not in package. Only available from NXP github.)
- flash (flash iap)
- mu
- edma


Driver API Reference Manual
****************************

This section provides a link to the Driver API RM, detailing available drivers and their usage to help you integrate hardware efficiently.

:ref:`MCXL255_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.


Multicore
=========

:ref:`multicore`




