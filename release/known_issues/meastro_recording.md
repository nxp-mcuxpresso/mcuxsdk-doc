# Maestro recording to a file has missing audio samples

When recording audio from the on-board mic and saving the output to a file on SD card, there are missing samples in the output pcm file. The maestro_demo design causes the issue. Writing data to SD card should be buffered and handled in a separate thread. The fix for the issue is planned for the next release.