This page lists possible blink codes of the red LED located on the ESP32-CAM board, their meaning and possible solutions.

The effective error codes can be found [here](https://github.com/jomjol/AI-on-the-edge-device/blob/rolling/code/components/jomjol_helper/statusled.h).

# General design approach:

  * 250ms blink code to identify source
  * 500ms defined LED off
  * 250ms blink code to identify error / status code
  * 1,5s LED off to signal repetition
  * e.g. 3x blinks | 500ms LED off | 2x blinks --> error: SD card not found

| **source**    | source blink count| error / status                        | status blink count| repeat infinite |
| ------------- | ----------------- |---------------------------------------| ---------------- | -----------------|
| FLASHLIGHT    | N/A               | LED on when flashlight is on (lowest prio) | solid, no blinking
| WLAN_CONN     | 1                 | Disconnected (No Access Point)        | 1                |
| WLAN_CONN     | 1                 | Disconnected (Authentication failure) | 2                |
| WLAN_CONN     | 1                 | Disconnected (Timeout)                | 3                |
| WLAN_CONN     | 1                 | Disconnected (Error code, misc error) | 4                |  
| WLAN_INIT     | 2                 | WLAN.ini empty or not readable        | 1                | X
| WLAN_INIT     | 2                 | SSID or password empty                | 2                | X
| WLAN_INIT     | 2                 | WIFI init error (details console)     | 3                | X
| SDCARD_INIT   | 3                 | SD card filesystem mount failed       | 1                | X
| SDCARD_INIT   | 3                 | SD card not found (0x107)             | 2                | X
| SDCARD_INIT   | 3                 | SD card init failed (details console) | 3                | X
| SDCARD_CHECK  | 4                 | Basic check: file creation/write error| 1                | X
| SDCARD_CHECK  | 4                 | Basic check: file read/CRC error      | 2                | X
| SDCARD_CHECK  | 4                 | Basic check: file delete error        | 3                | X
| SDCARD_CHECK  | 4                 | Basic check: folder/file presence     | 4                | X
| CAM_INIT      | 5                 | Camera init failed (details console)  | 1                | X
| CAM_INIT      | 5                 | Camera framebuffer check failed       | 2                | 
| PSRAM_INIT    | 6                 | PSRAM init failed: Not found/defective| 1                | X
| PSRAM_INIT    | 6                 | External PSRAM < 4MB                  | 2                | X
| PSRAM_INIT    | 6                 | Total heap < 4MB                      | 3                | X
| TIME_CHECK    | 7                 | Missing time sync (check every round) | 1                |
| OTA_OR_AP     | 8                 | OTA process ongoing                   | 1                | X
| OTA_OR_AP     | 8                 | Soft AP started                       | 2                | X


From here -->TODO!!!

## Error
Those errors make the normal operation of the device impossible.
Most likely they are caused by a hardware issue!

### `0x00000001` PSRAM bad
Your device most likely has no PSRAM at all or it is too small (needs to have at least 4 MBytes)!
See [Hardware Compatibility](../Hardware-Compatibility).

Usually the log shows something like this:
```
psram: PSRAM ID read error: 0xffffffff
cpu_start: Failed to init external RAM!
```

## Status
Those Errors can be caused by an error during initialization. It is possible that the error has no impact at all or that a reboot solves it.

### `0x00000100` Cam Framebuffer bad
The firmware was unable to initialize the Camera Framebuffer.
The firmware will continue to work, but other consequential error might arise.
A reboot of the device might help.
