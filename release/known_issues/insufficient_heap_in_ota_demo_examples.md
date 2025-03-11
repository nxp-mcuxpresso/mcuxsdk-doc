# Insufficient heap in ota\_demo examples

The ota\_demo examples, especially ota\_demo\_wifi, may run out of heap in the out-of-the-box configuration.

Therefore, increasing the heap size to 200 KB in FreeRTOSConfig.h is recommended.

To increase the heap size, change line 62:

```
#define configTOTAL_HEAP_SIZE ( ( size_t ) ( 200 * 1024 ) )
```