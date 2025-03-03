Introduction   {#index}
=========================

<P>The MCUXpresso Software Development Kit (MCUXpresso SDK) is a collection of software enablement for NXP Microcontrollers
that includes peripheral drivers, multicore support and integrated RTOS support for FreeRTOS<SUP>TM</SUP>. In addition
to the base enablement, the MCUXpresso SDK is augmented with demo applications, driver example projects, and API documentation
to help users quickly leverage the support provided by MCUXpresso SDK. The <a href="http://mcuxpresso.nxp.com/">MCUXpresso SDK Web Builder</a> is available to
provide access to all MCUXpresso SDK packages. See the <i>MCUXpresso Software Development Kit (SDK) Release Notes</i> (document MCUXSDKRN) in the Supported Devices section
at <a href="http://www.nxp.com/products/software-and-tools/run-time-software/mcuxpresso-software-and-tools/mcuxpresso-software-development-kit-sdk:MCUXpresso-SDK">MCUXpresso-SDK: Software Development Kit for MCUXpresso</a> for details.

<P>The MCUXpresso SDK is built with the following runtime software components:

<UL>
<LI>Arm<sup>®</sup> and DSP standard libraries, and CMSIS-compliant device header files which provide direct access to the peripheral registers.
<LI>Peripheral drivers that provide high-performance, ease-of-use APIs. Communication drivers provide higher-level transactional APIs for a higher-performance option.
<LI>RTOS wrapper driver built on top of MCUXpresso SDK peripheral drivers and leverage native RTOS services to better comply to the RTOS cases.
<LI>Real time operation systems (RTOS) for FreeRTOS OS.
<LI>Stacks and middleware in source or object formats including:
<UL>
<LI>CMSIS-DSP, a suite of common signal processing functions.
<LI>The MCUXpresso SDK comes complete with software examples demonstrating the usage of the peripheral drivers, RTOS wrapper drivers, middleware, and RTOSes.
</UL>

<P> All demo applications and driver examples are provided with projects for the following toolchains:
<UL>
<LI>IAR Embedded Workbench
<LI>GNU Arm Embedded Toolchain
</UL>
</UL>

<P>The peripheral drivers and RTOS driver wrappers can be used across multiple devices within the product family without modification.
The configuration items for each driver are encapsulated into C language data structures. Device-specific configuration information is
provided as part of the MCUXpresso SDK and need not be modified by the user. If necessary, the user is able to modify the peripheral driver and RTOS wrapper driver configuration during runtime.
The driver examples demonstrate how to configure the drivers by passing the proper configuration data to the APIs.
The folder structure is organized to reduce the total number of includes required to compile a project.

<table>
<caption id="multi_row">MCUXpresso SDK Folder Structure</caption>
<tr> <th>Deliverable</th><th>Location</th></tr>
<tr><td>Demo Applications</td><td>\<install_dir\>/boards/\<board_name\>/demo_apps</td></tr>
<tr><td>Driver Examples</td><td>\<install_dir\>/boards/\<board_name\>/driver_examples</td></tr>
<tr><td>Documentation</td><td>\<install_dir\>/docs</td></tr>
<tr><td>Middleware</td><td>\<install_dir\>/middleware</td></tr>
<tr><td>Drivers</td><td>\<install_dir\>/\<device_name\>/drivers/</td></tr>
<tr><td>CMSIS Standard Arm Cortex-M Headers, math and DSP Libraries</td><td>\<install_dir\>/CMSIS</td></tr>
<tr><td>Device Startup and Linker</td><td>\<install_dir\>/\<device_name\>/\<toolchain\>/</td></tr>
<tr><td>MCUXpresso SDK Utilities</td><td>\<install_dir\>/devices/\<device_name\>/utilities</td></tr>
<tr><td>RTOS Kernel Code</td><td>\<install_dir\>/rtos</td></tr>
</table>

<P>The rest of this document describes the API references in detail for the peripheral drivers and RTOS wrapper drivers.
For the latest version of this and other MCUXpresso SDK documents, see the
<a href="http://mcuxpresso.nxp.com/apidoc/">mcuxpresso.nxp.com/apidoc/</a>.
