:pdf-download: ../../../_assets/boards/evkmimxrt1040/mcuxsdk-evkmimxrt1040.pdf
.. _evkmimxrt1040:

MIMXRT1040-EVK
####################

Overview
********

MIMXRT1040-EVK development kit provides the ideal platform for evaluation of and development with the 600MHz i.MX RT1040 Crossover MCU based on the Arm Cortex-M7 architecture. The board includes a high-performance onboard debug probe, audio subsystem, accelerometer, networking and USB plus expansion options for displays and other add-on boards. The Kit includes a Murata Wifi module based on NXP's IW416 2.4/5 GHz Dual-Band 1x1 Wi-Fi 4 (802.11n) + Bluetooth 5.2 Solution.

.

The MIMXRT1040-EVK is designed to be a reference for low cost board designs, utilizing a 2 layer PCB design. A design files are available to provide a starting point for your design.

.. image:: ./evkmimxrt1040.png
   :width: 240px
   :align: center
   :alt: MIMXRT1040-EVK

MCU device and part on board is shown below:

 - Device: MIMXRT1042
 - PartNumber: MIMXRT1042XJM5B

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

:ref:`MIMXRT1042_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.


MCU Boot
========

:doc:`mcuboot_opensource<../../../middleware/mcuboot_opensource/README.md>`

Audio Voice components
======================

:ref:`components`

Maestro Audio Framework for MCU
===============================

:ref:`maestro`

eIQ
===

:ref:`eiq`

FreeMASTER
==========

:doc:`freemaster <../../../middleware/freemaster/doc/index>`


AWS IoT
=======

:ref:`aws_iot`

NXP Wi-Fi
=========

:ref:`wifi-bluetooth-802.15.4`

FreeRTOS
========

:ref:`freertos`

Wireless EdgeFast Bluetooth PAL
===============================

:ref:`edgefast_bluetooth`

lwIP
====

:ref:`lwip`

File systemFatfs
================

:ref:`fatfs`
