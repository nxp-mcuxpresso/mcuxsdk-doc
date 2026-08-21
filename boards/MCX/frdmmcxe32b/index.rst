.. _frdmmcxe32b:

FRDM-MCXE32B
####################

Overview
********

The FRDM-MCXE32B board is a design and evaluation platform based on the NXP MCXE32B
microcontroller (MCU). Arm Cortex-M7 cores running at speeds of up to 160 MHz and operates from a 2.97–5.5 V supply.
The FRDM-MCXE32B board consists of one MCXE32B device with a 64 Mbit external serial
flash. The board also features FXLS8974CFR3 I2C accelerometer
sensor, one NMH1000 I2C Magnetic switch, three TJA1057GTK/3Z CAN PHY, Ethernet PHY,
RGB LED, push buttons, and MCU-Link debug probe circuit.
The board is compatible with the Arduino shield modules, Pmod boards, and mikroBUS.
For debugging the MCXE32B MCU, the FRDM-MCXE32B board uses an onboard (OB) debug
probe, MCU-Link OB, which is based on another NXP MCU: LPC55S16.

.. image:: ./frdmmcxe32b.png
   :width: 240px
   :align: center
   :alt: FRDM-MCXE32B

MCU device and part on board is shown below:

 - Device: MCXE32B
 - PartNumber: MCXE32BMPB


SDK Introduction
*******************

.. only:: html

   For an introduction to the MCUXpresso SDK, see :doc:`MCUXpresso Software Development Kit (SDK) </introduction/README>`.

.. only:: latex

   .. toctree::
      :maxdepth: 1

      /introduction/README

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

:ref:`MCXE32B_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.

FreeRTOS
========

:ref:`freertos`
