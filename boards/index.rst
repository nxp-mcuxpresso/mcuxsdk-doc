.. _boards:

Supported Boards
=================
The MCUXpresso SDK provides comprehensive support for development boards, enabling optimized prototyping across a wide range of embedded applications. Boards are organized by processor family, with detailed information including overviews, getting started guides, and board-specific documentation available for each category.

**DSC (Digital Signal Controllers) Series**: Features NXP DSC development boards like the MC56F80000 EVK, optimized for real-time control, motor control, and power conversion applications.

**i.MX Series**: Includes i.MX Evaluation Kits (EVKs) such as i.MX 8M Plus EVK，providing high-performance computing, multimedia processing, and AI acceleration.

**i.MX RT Series**: EVK boards (e.g., MIMXRT1050-EVK, MIMXRT1170-EVK) for high-performance edge computing.

**Kinetis Series**: FRDM (Freedom) and Tower System boards (e.g., FRDM-K22F, TWR-KM35Z75M) for versatile MCU development.

**LPC Series**: LPCXpresso boards (e.g., LPCXpresso55S69, LPCXpresso55S28) for low-power and secure applications.

**MCX Series**: Features MCX NXP Evaluation Kits (EVKs) like the MCX N947 EVK, designed for scalable performance, low power consumption, and AI/ML capabilities in embedded applications.

**Wireless Series**: Includes K32W, KW, and RW series development kits, such as the KW45 EVK/LOC, and RW612 BGA/FRDM, supporting Bluetooth, Zigbee, Thread, and Wi-Fi for secure IoT connectivity.

.. toctree::
   :maxdepth: 1

   DSC/index
   i.MX/index
   RT/index
   Kinetis/index
   LPC/index
   MCX/index
   Wireless/index

Development Systems and Quality
================================

The following table summarizes the supported development boards and their quality classification for this release, including device variants, supported development tools, and quality status.

Quality Levels
--------------

- **RFP** - Release for Production. Fully functional and tested for production use.
- **EAR** - Early Access Release. Available for evaluation and early adoption; may have limited feature support.
- **PVW** - Preview. Snapshot of upcoming features and patches provided for evaluation only.

Supported Boards by Quality
----------------------------

.. include:: ../release/release_quality.md
   :parser: myst_parser.sphinx_
