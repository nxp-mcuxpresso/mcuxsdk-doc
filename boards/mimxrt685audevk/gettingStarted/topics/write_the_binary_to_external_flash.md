# Write the binary to external flash

Take J-Link Commander as an example to write the hello\_world.bin to external flash.

Run the J-Link Commander, run the following command to connect to the core.

```
J-Link>connect
J-Link>?
```

Select the correct device from the pop-up window **Target device settings**.

Specify targets interface as SWD and the target interface speed as per the guide in the command window. The **Cortex-M33 identified** appears when it is connected successfully.

**Parent topic:**[Run a demo using the prebuilt binary](../topics/run_a_demo_using_the_prebuilt_binary.md)

