# Throughput test setup

-   Environment: Shield Room - Over the Air
-   Access Point: Asus AX88u
-   DUT: IW610
-   External Client: Intel AX210
-   Channel: 6 \| 36
-   Wi-Fi application: wifi\_cli
-   Compiler used to build application: armgcc
-   Compiler version gcc-arm-none-eabi-13.2
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

**Note:** Read more about the throughput test setup and topology in [3](references.md#item_um11799).

**Parent topic:**[Wi-Fi throughput](../topics/wi-fi_throughput_06.md)

