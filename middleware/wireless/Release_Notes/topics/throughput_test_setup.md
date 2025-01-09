# Throughput test setup {#topic_0609d20a-0f45-4530-8021-c0d3eea77c06}

-   Environment: Shield Room - Over the Air
-   External Access Point: ASUS AX88U
-   DUT: W8987 Murata \(Module: **1ZM M.2**\) with EVK-MIMXRT1060 EVKC platform
-   DUT Power Source: External power supply
-   External Client: Apple MacBook Air
-   Channel: 6 \| 36
-   Wi-Fi application: wifi\_wpa\_supplicant
-   Compiler used to build application: armgcc
-   Compiler Version: gcc-arm-none-eabi-13.2
-   iPerf commands used in test:

TCP TX

```
iperf -c <remote_ip> -t 60
```

TCP RX

```
iperf -s
```

UDP TX

```
iperf -c <remote_ip> -t 60 -u -B <local_ip> -b 120
```

**Note:** The default rate is 100 Mbps.

UDP RX

```
iperf -s -u -B <local_ip>
```

**Note:** Read more about the throughput test setup and topology in [2](references.md#item_um11442).

**Parent topic:**[Wi-Fi throughput](../topics/wi-fi_throughput.md)

