# Maestro_playback limitation

FLAC decoder has missing samples in the beginning of the stream when sample rate convertor is enabled (by default).

**Workaround:** Disabling the sample rate convertor can fix the issue (Remove the SSRC_PROC from project defined symbols).