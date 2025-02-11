# iPerf host configuration and impact on throughput {#iperf_host_configuration_and_impact_on_throughput}

To get the highest throughput, the throughput values shown in [STA throughput](sta_throughput_02.md) and [Mobile AP throughput](mobile_ap_throughput_02.md) are measured with the maximum values of the default host configuration macros. [STA and AP throughput captured with the minimum values of the host configuration macros](sta_and_ap_throughput_captured_with_the_minimum_values_of_the_host_configuration_macros.md) shows the throughput numbers obtained when using the minimum values of the host configuration macros. The macro values are defined in *lwipopts.h* file.

The table below lists the minimum and maximum values of the host configuration macros.

**Values of the host configuration macros**

|**Parameter**|**Maximum value**|**Minimum value**|
|---------------|-------------------|-------------------|
|TCPIP\_MBOX\_SIZE|96|32|
|DEFAULT\_RAW\_RECVMBOX\_SIZE|32|12|
|DEFAULT\_UDP\_RECVMBOX\_SIZE|64|12|
|DEFAULT\_TCP\_RECVMBOX\_SIZE|64|12|
|TCP\_MSS|1460|536|
|TCP\_SND\_BUF|24 \* TCP\_MSS|2 \* TCP\_MSS|
|MEM\_SIZE|319160|41,080|
|TCP\_WND|15 \* TCP\_MSS|10 \* TCP\_MSS|
|MEMP\_NUM\_PBUF|20|10|
|MEMP\_NUM\_TCP\_SEG|96|12|
|MEMP\_NUM\_TCPIP\_MSG\_INPKT|80|16|
|MEMP\_NUM\_TCPIP\_MSG\_API|80|8|
|MEMP\_NUM\_NETBUF|32|16|

-   **[STA and AP throughput captured with the minimum values of the host configuration macros](../topics/sta_and_ap_throughput_captured_with_the_minimum_values_of_the_host_configuration_macros.md)**  


**Parent topic:**[Wi-Fi throughput](../topics/wi-fi_throughput_02.md)

