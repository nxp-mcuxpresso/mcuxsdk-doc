# Messaging Unit, Semaphore, and IPC

Message Unit/ MU and Semaphore/ SEMA42 are essential for DSP programming. The inter-core communications a.k.a IPC on RT600 is based on MU and SEMA42. SDK provides three simple examples about standalone MU and SEMA 42. SDK path \\boards\\evkmimxrt685\\dsp\_examples\\mu\_interrupt, mu\_polling, and sema42. These bare-metal examples show how IPC work between two cores. Furthermore, the audio framework demo/ SDK path \\boards\\evkmimxrt685\\dsp\_examples\\xaf\_demo is complete. It uses rpmsg\_lite as IPC protocol, which based on MU to transfer messages between the two cores.

First Cortex M33 side initializes rpmsg master, main\_cm33.c in app\_task\(\)

```
g_my_rpmsg = rpmsg_lite_master_init((void *)RPMSG_LITE_SHMEM_BASE, RPMSG_LITE_SHMEM_SIZE, RPMSG_LITE_LINK_ID, RL_NO_FLAGS);
  g_my_queue = rpmsg_queue_create(g_my_rpmsg);
  g_my_ept   = rpmsg_lite_create_ept(g_my_rpmsg, LOCAL_EPT_ADDR, rpmsg_queue_rx_cb, g_my_queue);
```

Rpmsg initialize MU interrupts for MUA/ master in rpmsg\_platform.c platform\_init\_interrupt\(\)

```
/* Register ISR to environment layer */
env_register_isr(vector_id, isr_data);
env_lock_mutex(platform_lock);
RL_ASSERT(0 <= isr_counter);
if (isr_counter == 0)
{
    MU_EnableInterrupts(APP_MU, (1UL << 27U) >> RPMSG_MU_CHANNEL);
```

For DSP side, it also initializes rpmsg client and tries to hook with the master, in xaf\_main\_dsp.c:DSP\_Main\(\)

```
/* Initialize standard SDK demo application pins */
my_rpmsg = rpmsg_lite_remote_init((void *)RPMSG_LITE_SHMEM_BASE, RPMSG_LITE_LINK_ID, RL_NO_FLAGS, &rpmsg_ctxt);
while (!rpmsg_lite_is_link_up(my_rpmsg))
{
```

It has rpmsg porting as well, initialize MU interrupts for MUB/ client in rpmsg\_platform.c platform\_init\_interrupt\(\) and enable it in platform\_interrupt\_enable\(\)

```
xos_register_interrupt_handler(6, MU_B_IRQHandler, ((void *)0));
xos_interrupt_enable(6);
```

Once they hooked up both sides are ready for message exchange. SDK defines various SRTM message structures to pass the commands/ messages. In SDK example, it shows how to pass an MP3 decoding message, a AAC decoding message, a DMIC recording message and so on. Using MP3 decoding message as an example, It fills SRTM structure with input buffer address pointer, input buffer size, output buffer address pointer, output buffer size and so on. And then calling rpmsg to send it to DSP and waiting for the response.

```
rpmsg_lite_send(g_my_rpmsg, g_my_ept, g_remote_addr, (char *)msg, sizeof(THE_MESSAGE), RL_BLOCK);
rpmsg_queue_recv(g_my_rpmsg, g_my_queue, (unsigned long *)&g_remote_addr, (char *)msg, sizeof(THE_MESSAGE), len,
                 RL_BLOCK);
```

DSP side listens to rpmsg event.

```
my_ept = rpmsg_lite_create_ept(my_rpmsg, DSP_EPT_ADDR, my_ept_read_cb, (**void** *)&rpmsg_user_data, &my_ept_context);
```

Once received, it handles message and proceeds the command. For MP3 decoding case, it decodes the MP3 data in the input buffer, and flushes the output buffer. It also fills out the SRTM message structure with actual read data size and actual write data size, and eventually sends the response message back to Cortex M33 side.

```
/*Send response message*
    /rpmsg_lite_send(my_rpmsg, my_ept, remote_addr, (**char** *)&msg, **sizeof**(THE_MESSAGE), RL_DONT_BLOCK);
```

For this example, DSP is considered as a coprocessor and rpmsg has been used for a light-weight IPC for both cores. All modules are open-sourced and could be easily adapted to whatever application needs.

**Parent topic:**[HiFi4 System Programming](../topics/hifi4_system_programming.md)

