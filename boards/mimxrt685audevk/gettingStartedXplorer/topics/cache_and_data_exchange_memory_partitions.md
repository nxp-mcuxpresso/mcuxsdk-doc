# Cache and Data Exchange Memory Partitions

You may have noticed that HiFi4 DSP has a small non-cached area that starts from 0x20040000. The non-cached are used for data exchange between two cores. As both M33 and HiFi DSP have shared access to all SRAM partitions, shared memory access is the most effective way to exchange data between two cores. The given physical addresses are read/ written by both cores at same address, no memory mapping or address converting is required. For example, if a piece of data array is passed from Cortex M33 to HiFi4 DSP, only the start pointer and the size of the array is passed, and conversely. It is convenient for system programming and simplifies the inter-core communications.

Consider cache here. Cortex M33 has no cache, the entire SRAM is considered as its local memory. Therefore, any memory write is flushed immediately. HiFi4 has 32 K instruction cache and 64 K data cache, and both cache are enabled by default. Therefore, the memory write is not flushed immediately. To make a tradeoff between performance and IPC convenience, set the non-cached area for data exchange memory partitions.

The above memory map has specified the non-cached region, and in DSP code, and HAL functions are called to disable the cache. For details, see the audio framework example in `SDK path\boards\evkmimxrt685\dsp_examples\xaf_demo\dsp\xaf_main_dsp.c`. For more details about HAL cache function, see the Xtensa System Software Reference Manual, section 3.11 Cache

```
/* Disable DSP cache for RPMsg-Lite shared memory. */
xthal_set_region_attribute((void *)RPMSG_LITE_SHMEM_BASE, RPMSG_LITE_SHMEM_SIZE, XCHAL_CA_BYPASS, 0);
/* Disable DSP cache for noncacheable sections. */
xthal_set_region_attribute((uint32_t *)&NonCacheable_start,
                               (uint32_t)&NonCacheable_end - (uint32_t)&NonCacheable_start, XCHAL_CA_BYPASS, 0);

```

Note that the XHAL call sets cache attribute of the whole region/ 512 M bytes even if the set size is passed. This is also one reason why non-cached attribute is set on the overlapping SRAM address and starts from 0x2000 0000. This also distinguished the physical SRAM addresses starting from 0x0000 0000, which is cacheable area for HiFi4.

Data exchange memory partitions are flexible and can be configured as per application's requirement. However, to mitigate the possible AHB arbitration between the two cores, use of the first eight 32 K and following four 64 K memory partitions is recommended. DSP Data TCM is also used as data exchange area for those data have high demand on timing performance. You must avoid accessing same partition at same time for frequent data exchange between two cores. You can keep one core in Sleep or Wait for Interrupt while another core operating, or set up a ping pong data exchange/ DMA such that when one core fills one partition, another core fetches another partition, and conversely.

For more details about the RT6xx memory map, see the user manual, section 2 Memory Map, and section 2.1.11 HiFi4 memory map.

**Parent topic:**[HiFi4 Boot Loader and Memory Map](../topics/hifi4_boot_loader_and_memory_map.md)

