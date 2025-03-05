# Flexcan\_ping\_pong\_buffer\_transfer case loses first 8 bytes data for armgcc flash\_debug 

To prevent flexcan\_ping\_pong\_buffer\_transfer case from losing the first 8 bytes data for armgcc flash\_debug, apply the fix below.

```
a/flexcan/example/ping_pong_buffer_transfer/flexcan_ping_pong_buffer_transfer.c
+++ b/flexcan/example/ping_pong_buffer_transfer/flexcan_ping_pong_buffer_transfer.c
@@ -539,10 +539,11 @@ int main(void)
         else
         {
             /* Wait until Rx queue 1 full. */
-            while (rxQueueNum != 1U)
+            while (rxQueueNum == 0U)
             {
             };
-            rxQueueNum = 0;
+            if (rxQueueNum == 1)
+                rxQueueNum = 0;
             LOG_INFO("Read Rx MB from Queue 1.\r\n");
             for (i = 0; i < RX_QUEUE_BUFFER_SIZE; i++)
             {
```

**Parent topic:**[Known issues](../topics/known_issues.md)

