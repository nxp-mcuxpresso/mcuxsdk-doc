:pdf-download: ../../../_assets/boards/lpcxpresso860max/mcuxsdk-lpcxpresso860max.pdf
.. _lpcxpresso860max:

LPCXpresso860MAX
####################

Overview
********

The LPC86x are an Arm Cortex-M0+ based, low-cost 32-bit MCU family operating at CPU frequencies of up to 48 MHz. The LPC86x support up to 64 KB of flash memory and 8 KB of SRAM.

The peripheral complement of the LPC86x includes a CRC engine, one I2C-bus interface, one I3C-MIPI bus interface, up to three USARTs, up to two SPI interfaces, one multi-rate timer, self-wake-up timer, two FlexTimers, a DMA, one 12-bit ADC, one analog comparator, function-configurable I/O ports through a switch matrix, an input pattern match engine, and up to 54 general-purpose I/O pins.

.. image:: ./lpcxpresso860max.png
   :width: 240px
   :align: center
   :alt: LPCXpresso860MAX

MCU device and part on board is shown below:

 - Device: LPC865
 - PartNumber: LPC865M201JBD64

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

Driver API Reference Manual
****************************

This section provides a link to the Driver API RM, detailing available drivers and their usage to help you integrate hardware efficiently.

:ref:`LPC865_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.


FreeMASTER
==========

:doc:`freemaster <../../../middleware/freemaster/doc/index>`


FreeRTOS
========

:ref:`freertos`
