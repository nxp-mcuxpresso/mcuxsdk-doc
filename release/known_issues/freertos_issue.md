# FreeRTOS issue 

When generating a new FreeRTOS project with New Project Wizard tool, the user should de-assert the macro option "configUSE\_PORT\_OPTIMISED\_TASK\_SELECTION” in the “FreeRTOSConfig.h” file while it is not being used in the template project for some Cortex-M0+ devices or it may not pass the compiling.



