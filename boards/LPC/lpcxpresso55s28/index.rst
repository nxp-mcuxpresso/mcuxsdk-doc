:pdf-download: ../../../_assets/boards/lpcxpresso55s28/mcuxsdk-lpcxpresso55s28.pdf
.. _lpcxpresso55s28:

LPCXpresso55S28
####################

Overview
********

The LPCXpresso55S28 board is an LPCXpresso V3 style board, the latest generation of the original and highly successful LPCXpresso board family. "Arduino UNO" compatible shield connectors are included, with additional expansion ports around the Arduino footprint, along with a PMod/host interface port and Mikroelekronika Click module site. The board features an on-board LPC-Link2 debug probe based on the LPC4322 MCU for a performance debug experience over high speed USB, with easy firmware update options to support CMSIS-DSP or a special version of J-link LITE from SEGGER. The board can also be used with an external debug probe such as those from SEGGER and P&E.

The LPC5500 series is fully supported by NXPs` \ `MCUXpresso suite <https://www.nxp.com/mcuxpresso>`__\  of free software and tools, which include an Eclipse-based IDE, configuration tools and extensive SDK drivers/examples available at \ `https://mcuxpresso.nxp.com <https://mcuxpresso.nxp.com/>`__\. MCUXpresso SDK includes project files for use with IDEs from lead partners Keil and IAR.

.. image:: ./lpcxpresso55s28.png
   :width: 240px
   :align: center
   :alt: LPCXpresso55S28

MCU device and part on board is shown below:

 - Device: LPC55S28
 - PartNumber: LPC55S28JBD100


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

:ref:`LPC55S28_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.


FreeMASTER
==========

:doc:`freemaster <../../../middleware/freemaster/doc/index>`


FreeRTOS
========

:ref:`freertos`

File systemFatfs
================

:ref:`fatfs`
