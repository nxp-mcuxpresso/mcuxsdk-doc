# Throughput test setup {#topic_0189ff7b-35ce-4711-86ff-e492e2042b10}

-   Environment: Shield Room - Over the Air
-   External Access Point: Asus-AX88U
-   DUT: W8801 Murata \(Module: 2DS M.2\) with EVK-MIMXRT1060 platform
-   DUT Power Source: External power supply
-   External Client: IW620-Kestrel
-   Channel: 6
-   Wi-Fi application: wifi\_cli
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

The throughput numbers are captured with the default configurations.

**Parent topic:**[Wi-Fi throughput](../topics/wi-fi_throughput_05.md)

