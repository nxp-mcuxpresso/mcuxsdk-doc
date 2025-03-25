.. _frdmmcxe247:

FRDM-MCXE247
####################

Overview
********

The FRDM-MCXE247 board is a design and evaluation platform based on the NXP MCXE247
microcontroller (MCU). NXP MCXE247 MCU based on an Arm Cortex- M4F core, running
at speeds of up to 112 MHz with a 2.70–5.5 V supply.
The FRDM-MCXE247 board consists of one MCXE247 device with a 64 Mbit external serial
flash (provided by Winbond). The board also features FXLS8974CFR3 I2C accelerometer
sensor, one NMH1000 I2C Magnetic switch, three TJA1057GTK/3Z CAN PHY, Ethernet PHY,
RGB LED, push buttons, and MCU-Link debug probe circuit.
The board is compatible with the Arduino shield modules, Pmod boards, and mikroBUS.
For debugging the MCXE247 MCU, the FRDM-MCXE247 board uses an onboard (OB) debug
probe, MCU-Link OB, which is based on another NXP MCU: LPC55S16. 

.. image:: ./frdmmcxe247.png
   :width: 240px
   :align: center
   :alt: FRDM-MCXE247

MCU device and part on board is shown below:

 - Device: MCXE247
 - PartNumber: MCXE247VLQ


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

**This is an Early Access Release (EAR) for FRDM-MCXE247 development board. It shall be used for pre-production development only.**

Only drivers which has its example(s) in mcuxsdk/examples/_boards/frdmmcxe247/driver_examples folder were tested.

Supported Development Tools
===========================
 - MCUXpresso for VS Code v25.03
 - GCC Arm Embedded Toolchain

.. toctree::
   :maxdepth: 1

   releaseNotes/rnindex.md

ChangeLog
*******************************************
.. toctree::
   :maxdepth: 1

   changeLog/clindex.md

Driver API Reference Manual
****************************

This section provides a link to the Driver API RM, detailing available drivers and their usage to help you integrate hardware efficiently.

:ref:`MCXE247_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.


FreeMASTER
==========

.. toctree::
   :maxdepth: 1

   ../../../middleware/freemaster/doc/index.md



FreeRTOS
========

:ref:`freertos`
