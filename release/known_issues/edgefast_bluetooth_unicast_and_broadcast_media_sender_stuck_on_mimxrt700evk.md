# EdgeFast_Bluetooth unicast_media_sender, broadcast_media_sender example stuck

A "Usage Fault" from "Unaligned Access" stops the examples on the MCUX release target.

**Solution**: To fix this problem, align the audio_buff to 4 bytes. The misaligned audio_buff exists in broadcast_media_sender.c and unicast_media_sender.c. Use the SDK_ALIGN() macro to align audio_buff. This fixes the problem.

**Examples**: unicast_media_sender, broadcast_media_sender

**Affected platforms**: mimxrt700evk

