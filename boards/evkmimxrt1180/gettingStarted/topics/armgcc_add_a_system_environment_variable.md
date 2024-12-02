# Add a system environment variable for ARMGCC\_DIR

Create a `system`environment variable and name it as `ARMGCC_DIR`. The value of this variable should point to the Arm GCC Embedded tool chain installation path. For this example, the path is:

*C:\\Program Files \(x86\)\\GNU Tools ARM Embedded\\8 2018-q4-major*

See the installation folder of the GNU Arm GCC Embedded tools for the exact path name of your installation.

Short path should be used for path setting, you could convert the path to short path by running the `for %I in (.) do echo %~sI` command in above path.

![](../images/armgcc_convert_path_to_short_path.jpg "Convert path to short path")

![](../images/armgcc_add_armgcc_dir_system_variable.png "Add ARMGCC_DIR system variable")

**Parent topic:**[Set up toolchain](../topics/armgcc_set_up_toolchain.md)

