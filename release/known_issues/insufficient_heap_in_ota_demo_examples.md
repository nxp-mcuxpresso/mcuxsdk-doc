# Insufficient heap in ota_demo examples

The ota_demo examples, especially ota_demo_wifi, may run out of heap in the out-of-the-box configuration.

To increase the heap size, change line 62:

```
#define configTOTAL_HEAP_SIZE ( ( size_t ) ( 200 * 1024 ) )
```

**Workaround:** Therefore, increasing the heap size to 200 KB in FreeRTOSConfig.h is recommended.