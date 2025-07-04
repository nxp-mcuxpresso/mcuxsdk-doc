:pdf-download: ../../../_assets/boards/mcxw72evk/mcuxsdk-mcxw72evk.pdf
.. _mcxw72evk:

MCX-W72-EVK
####################

Overview
********

The MCXW72 EVK is an IIOT evaluation kit development board for advanced development of the MCXW72 wireless MCU. It offers exhaustive evaluation of the MCX W72's multiprotocol wireless support for Bluetooth LE, Zigbee, Thread and Matter and CAN connectivity.
The MCXW72 highly sensitive, optimized 2.4 GHz radio features a PCB meandered-antenna which can be bypassed to test via µ-RF connection.
The MCXW72 EVK is a modular platform composed of the connectivity mother board KW-MCXW-EVK-MB and an M.2 meandered antenna module MCXW72-M10.
The board includes an advanced  MCU-Link debug probe, Power and low power option, CAN transceiver, buttons, switches, LEDs and integrated sensors, Arduino shield connectors, a MikroE Click connector and other headers.


.. image:: ./mcxw72evk.png
   :width: 240px
   :align: center
   :alt: MCX-W72-EVK

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
