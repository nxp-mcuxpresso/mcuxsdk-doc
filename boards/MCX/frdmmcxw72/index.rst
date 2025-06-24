:pdf-download: ../../../_assets/boards/frdmmcxw72/mcuxsdk-frdmmcxw72.pdf
.. _frdmmcxw72:

FRDM-MCXW72
####################

Overview
********

The FRDM-MCXW72 is a compact and scalable IIoT development board for rapid prototyping of the MCX W72 wireless MCU. It offers easy evaluation of the MCX W72's multiprotocol wireless support for Bluetooth LE, Zigbee, Thread and Matter.
The board includes an on-board MCU-Link debugger, industry standard headers for easy access to the MCU’s I/Os, an accelerometer, a light sensor and external SPI flash memory.
The MCXW72 highly sensitive, optimized 2.4 GHz radio features a PCB meandered-antenna which can be bypassed to test via µ-RF connection.
Multiple add-on boards are available through NXP's `Expansion Board Hub <https://mcuxpresso.nxp.com/eb-hub>`_ while the `Application Code Hub <https://mcuxpresso.nxp.com/appcodehub>`_ provides ready to use software examples as part of the `MCUXpresso Developer Experience <https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-:MCUXPRESSO>`_.


.. image:: ./frdmmcxw72.png
   :width: 240px
   :align: center
   :alt: FRDM-MCXW72

MCU device and part on board is shown below:

 - Device: MCXW727C
 - PartNumber: MCXW727CMFTA

Getting Started with MCUXpresso SDK Package
*******************************************
.. toctree::
   :maxdepth: 1

   gettingStarted/gsindex.md

Getting Started with MCUXpresso SDK GitHub
*******************************************
.. toctree::
   :maxdepth: 1

   ../../../gsd/repo.rst

Release Notes
*******************************************

**This is an early adopter release provided as preview for development with pre-production devices.**

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

:ref:`MCXW727C_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.


Wireless Bluetooth LE host stack and applications
=================================================

:ref:`examples__wireless_examples__bluetooth_docs`

Wireless zigbee stack
=====================

:ref:`zigbee`

IEEE 802.15.4 MACPHY Software
=============================

:ref:`middleware_wireless_ieee_802_15_4`

Wireless Connectivity Framework
===============================

:doc:`framework <../../../middleware/wireless/framework/index>`

Multicore
=========

:ref:`multicore`

FreeMASTER
==========

:doc:`freemaster <../../../middleware/freemaster/doc/index>`


FreeRTOS
========

:ref:`freertos`
