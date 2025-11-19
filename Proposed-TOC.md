<style>
r { color: Red }
b { color: Cyan }
o { color: Orange }
g { color: Green }
</style>

## SABINA'S TOC
<b>INTRODUCTION</b>  

MCUXPresso SDK  
Supported Boards

<b>RELEASES </b>

Release Notes  
Migration Guides

<b>GETTING STARTED</b>

Github Repository  
Zip Package

<b>DEVELOPMENT</b>

Build And Configuration System  
Developing with MCUXpresso SDK

<b>Platform Components</b>

Drivers  
Examples  
Middleware  
RTOS  

---
---
## KYLE'S TOC

<o>INTRODUCTION</o>  

Overview  

<o>RELEASES </o>  

The current TOC links to individual ReleaseNotes for every board.
Content in these docs is DIFFERENT and/or COPIED from the main TOC.  Overview, MCUXpresso SDK, Dev Tools, Devices, Description of all sections/folders.  

- **Device Support**  
*Existing table lists along with boards*; Currently call them Development Systems?)  
- **Migration Guides**  
What changed release-to-release   
- **Metrics**  
*Coverity Static Analysis*

<o>GETTING STARTED</o>  

Current section has 2 paths based on GitHub SDK or Archive SDK packages.  This will change in 25.12.00 when Archive SDK packages for Arm GCC CMake projects will be the same for Github and Archive.
Suggest
- **INSTALL SDK**  
HOW DO YOU WANT TO RECEIVE SDK PACKAGE? WHAT ECOSYSTEM?  
Have intro paragraph that differentiates the methods and contents. So the customer knows differences and benefits to their decision.
    - *IDE Import Wizard*  
    Share ability to get SDK directly inside VS Code / Eclipse environment.   
    - *GitHub*  
    Encourage MCUXpresso Installer for Tool setup.  HIDE DIY list of instructions.  
    Have section on Custom Manifests to show how to clone manifest, modify yml, then use west init/update to install.
    - *SDK Builder*    
    Archive Package for MDK, IAR, IDE, ARMGCC

- **FIRST PROJECT**  
HOW DO YOU BUILD YOUR FIRST PROJECT. START WITH HELLO WORLD or BLINKY.  
Have option for all popular SDK use cases.
    - VS Code
    - MCUXpresso IDE
    - CLI
    - MDK
    - IAR

<o>USER GUIDES</o>

The Current USER GUIDE is more of *API Reference* material.  There are no GUIDES... just information.  That section should be moved down and replaced with a section dedicated to GUIDES and REFERENCES.  
Each User Guide will be a unique File that can be added/revised or removed without impacting other guides.

- **CMAKE USER GUIDE**  
HOW DOES MCUXPRESSO USE CMAKE. WALKTHROUGH USE CASE.  
Outline how user might use CMAKE manually to modify project for custom use cases.  

- **KCONFIG USER GUIDE**  
HOW DOES MCUXPRESSO USE KCONFIG. WALKTHROUGH USE CASE.  
Share how Kconfig is used. How they can identify Kconfig. When would they use Kconfig.

- **MEMORY MANAGEMENT USER GUIDE**  
Show how a user works with different Memory Configurations. Modify and View settings in VS CODE.  No GUI like in IDE.  
Pepe working on this document.  On chip vs. external flash memory. What files are used in CMake to define build?

- **MULTICORE PROJECT USER GUIDE**  
HOW DO YOU BUILD MULTICORE PROJECT. DEBUG.  
Have option for NXP Supported use cases. Not IAR and MDK.
    - VS Code
    - MCUXpresso IDE
    - CLI

- **TRUSTZONE PROJECT USER GUIDE**  
HOW DO YOU BUILD TRUSTZONE PROJECT. DEBUG.  
Have option for all popular SDK use cases.
    - VS Code
    - MCUXpresso IDE
    - CLI



<o>SDK REFERENCES</o>

- **DRIVERS**
- **EXAMPLES**
- **MIDDLEWARE** 
- **RTOS**

- **BUILD AND CONFIGURATION SYSTEM**  
This section is rich in detail on HOW MCUXpresso builds and configures the SDK and projects.  It is pretty good, but needs more people to read/review. Possible Co-Pilot revision?  Lots of gramatical errors.

- **DEVELOPING WITH MCUXPRESSO SDK**  
This section is probably mislabeled.  It is helpful for INTERNAL developers on how to build projects and middleware to interact with SDK.  I think it is not EXTERNAL content?  IF SO... the target audience of writing needs to change.  It reads like a message to NXP employees vs. **Customer Developers**.  

