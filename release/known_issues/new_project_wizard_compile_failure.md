# New Project Wizard compile failure

The following components request the user to manually select other components that they depend upon in order to compile.

These components depend on several other components and the New Project Wizard \(NPW\) is not able to decide which one is needed by the user.

**Note:** xxx means core variants, such as, cm0plus, cm33, cm4, cm33\_nodsp.

**Components:**issdk\_mag3110, issdk\_host, systick, gpio\_kinetis, gpio\_lpc, issdk\_mpl3115, sensor\_fusion\_agm01, sensor\_fusion\_agm01\_lpc, issdk\_mma845x, issdk\_mma8491q, issdk\_mma865x, issdk\_mma9553, and CMSIS\_RTOS2.CMSIS\_RTOS2, and components which include cache driver, such as enet\_qos.

Also for low-level adapter components, currently the different types of the same adapter cannot be selected at the same time.

For example, if there are two types of timer adapters, gpt\_adapter and pit\_adapter, only one can be selected as timer adapter

in one project at a time. Duplicate implementation of the function results in an error.

**Note:** Most of middleware components have complex dependencies and are not fully supported in new project wizard. Adding a middleware component may result in compile failure.


