Known issues
================

.. contents::
   :local:
   :depth: 3

Known issues listed on this page *and* tagged with the :ref:`latest official release version <release_notes>` are valid for the current state of development.
Use the drop-down filter to see known issues for previous releases and check if they are still valid.

A known issue can list one or both of the following entries:

* **Affected platforms:**

  If a known issue does not have any specific platforms listed, it is valid for all hardware platforms.

* **Workaround:**

  Some known issues have a workaround.
  Sometimes, they are discovered later and added over time.

.. version-filter::
  :default: v2024-09-00
  :container: dl/dt
  :tags: [("wontfix", "Won't fix")]

.. page-filter::
  :name: issues

  wontfix    Won't fix

.. HOWTO

   When adding a new version, set it as the default value of the version-filter directive.
   Once the version is updated, only issues that are valid for the new version will be displayed when entering the page.

   When updating this file, add entries in the following format:

   .. rst-class:: wontfix vXXX vYYY

   JIRA-XXXX: Title of the issue (with mandatory JIRA issue number since nRF Connect SDK v1.7.0)
     Description of the issue.
     Start every sentence on a new line and pay attention to indentations.

     There can be several paragraphs, but they must be indented correctly.

     **Affected platforms:** Write what hardware platform is affected by this issue.
     If an issue touches all hardware platforms, this line is not needed.

     **Workaround:** The last paragraph contains the workaround.
     The workaround is optional.

Examples
*********
.. rst-class:: v2024-09-00 v2024-12-00

LPSPI b2b examples transfer fail on iar/armgcc flash target.
    Due to the latency of instruction retrieval \(XiP\), LPSPI-related flash target examples may fail. The failure happens because the data is not retrieved in time from FIFO on the receiving end. 
    
    **Affected platforms:** evkmcimx7ulp
    
    **Workaround:** To prevent the failure and boost the instruction fetch performance, place the fsl\_lpspi.c file in the SRAM. Apply the patch as below,
    
    .. code-block:: none
        
        $ git diff  MCIMX7U5xxxxx_cm4_flash.ld
        diff --git a/MCIMX7U5/gcc/MCIMX7U5xxxxx_cm4_flash.ld b/MCIMX7U5/gcc/MCIMX7U5xxxxx_cm4_flash.ld
        index b29b41a2b1..91dc0782e5 100644
        --- a/MCIMX7U5/gcc/MCIMX7U5xxxxx_cm4_flash.ld
        +++ b/MCIMX7U5/gcc/MCIMX7U5xxxxx_cm4_flash.ld
        @@ -68,10 +68,22 @@ SECTIONS
        .text :
        {
            . = ALIGN(4);
        -    *(.text)                 /* .text sections (code) */
        -    *(.text*)                /* .text* sections (code) */
        -    *(.rodata)               /* .rodata sections (constants, strings, etc.) */
        -    *(.rodata*)              /* .rodata* sections (constants, strings, etc.) */
        +    *(EXCLUDE_FILE(
        +        /* Exclude flash and frequently executed functions from XIP */
        +        */fsl_lpspi.c.obj
        +    ) .text)                 /* .text sections (code) */
        +    *(EXCLUDE_FILE(
        +        /* Exclude flash and frequently executed functions from XIP */
        +        */fsl_lpspi.c.obj
        +    ) .text*)                /* .text* sections (code) */
        +    *(EXCLUDE_FILE(
        +        /* Exclude flash and frequently executed functions from XIP */
        +        */fsl_lpspi.c.obj
        +    ) .rodata)               /* .rodata sections (constants, strings, etc.) */
        +    *(EXCLUDE_FILE(
        +        /* Exclude flash and frequently executed functions from XIP */
        +        */fsl_lpspi.c.obj
        +    ) .rodata*)              /* .rodata* sections (constants, strings, etc.) */
            *(.glue_7)               /* glue arm to thumb code */
            *(.glue_7t)              /* glue thumb to arm code */
            *(.eh_frame)
        @@ -173,6 +185,7 @@ SECTIONS
            __quickaccess_start__ = .;
            . = ALIGN(32);
            *(CodeQuickAccess)
        +    /* Explicit placement of flash and frequently executed functions in SRAM  */
        +    */fsl_lpspi.c.obj(.text .text* .rodata .rodata*)
            *(DataQuickAccess)
            . = ALIGN(128);
            __quickaccess_end__ = .;


