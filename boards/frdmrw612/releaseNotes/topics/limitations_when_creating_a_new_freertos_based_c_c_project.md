# Limitations when creating a new FreeRTOS-based C/C++ project 

Due to the missing component dependencies definition, there are several limitations when creating a new FreeRTOS-based C/C++ project in MCUXpresso IDE. When the **FreeRTOS kernel** component is selected \(under Operating Systems/RTOS/Core menu\), you must manually select the **FreeRTOS cm33 non trustzone port** component \(under Middleware/RTOS menu\) for projects without TrustZone. For FreeRTOS TrustZone projects creation, the support is not ready.

**Parent topic:**[Known issues](../topics/known_issues.md)

