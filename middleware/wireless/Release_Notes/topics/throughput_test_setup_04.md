# Throughput test setup {#topic_78bf6607-e9d3-4911-b215-e826d34fddf8}

-   Environment: Shield Room - Over the Air
-   Access Point: Asus AX88u
-   DUT: AW611 uBlox \(Module: U-BLOX\_Jody\_W5 M.2\) with EVK-MIMXRT1180 EVKA platform
-   DUT Power Source: External power supply
-   Client: Apple MacBook Air
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

The throughput numbers are captured with default configurations using *wifi\_wpa\_supplicant* sample application.

**Parent topic:**[Wi-Fi throughput](../topics/wi-fi_throughput_04.md)
