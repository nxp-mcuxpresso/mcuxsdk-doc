# LPSPI b2b examples transfer fail on iar/armgcc flash target 

Due to the latency of instruction retrieval \(XiP\), LPSPI-related flash target examples may fail. The failure happens because the data is not retrieved in time from FIFO on the receiving end.

To prevent the failure and boost the instruction fetch performance, place the fsl\_lpspi.c file in the SRAM.

Apply the patch as below,

```
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
```

