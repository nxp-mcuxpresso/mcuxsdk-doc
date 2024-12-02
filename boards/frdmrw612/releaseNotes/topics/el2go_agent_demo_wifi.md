# El2go\_agent\_demo\_wifi issue

The `el2go_agent_demo_wifi` project does not work on MCUXpresso for VSCode. However, Arm GCC standalone, MCUXpresso IDE, MDK, or IAR have no limitations.

**Note:** The above issue is not really a limitation of the SDK release, as it gets fixed by a toolchain update. The issue also partially applies to all other examples using TF-M.

When using MCUX IDE, do not specify a custom prefix or suffix while importing the example.

However, if it is a custom prefix or suffix is added, you must adapt the names of the library projects `el2go_mbedtls_lib` and `el2go_tfm_psa_ns_lib` in the `el2go_agent_demo_wifi_ns` project. To change the linker import paths to the right name, select **Project settings \> C/C++ Build \> Settings \> MCU linker \> Miscellaneous \> Other Objects**.

**Note:** This limitation stays as it depends on the SDK generator fixes.

**Parent topic:**[Known issues](../topics/known_issues.md)

