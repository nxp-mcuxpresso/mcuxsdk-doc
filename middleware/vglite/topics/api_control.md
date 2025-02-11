# API control

Before calling any VGLite API function, the application must initialize the VGLite implicit \(global\) context by calling *vg\_lite\_init\(\)*, which will fill in a features table, reset the fast-clear buffer, reset the compositing target buffer and allocate the command and tessellation buffers.

The VGLite driver only supports one current context and one thread to issue commands to the Vivante Vector Graphics hardware. The VGLite driver does not support multiple concurrent contexts running simultaneously in multiple threads/processes, as the VGLite kernel driver does not support context switching. A VGLite application can only use a single context at any time to issue commands to the Vivante Vector Graphics hardware. If a VGLite application must switch contexts, `vg_lite_close()` must be called to close the current context in the current thread, then `vg_lite_init()` can be called to initialize a new context either in the current thread or from another thread/process.


```{include} ../topics/context_initialization_and_control_functions.md
:heading-offset: 1
```

