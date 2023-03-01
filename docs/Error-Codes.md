This page lists the possible error codes, their meaning and possible solutions.

The effective error codes can be found [here](https://github.com/jomjol/AI-on-the-edge-device/blob/rolling/code/components/jomjol_helper/Helper.h).

# Critical Errors
Those Errors make the normal operation of the device impossible.
Most likely they are caused by a hardware issue!

## `0x00000001` PSRAM bad
Your device most likely has no PSRAM at all or it is too small (needs to have at least 4 MBytes)!
See [Hardware Compatibility](../Hardware-Compatibility).

Usually the log shows something like this:
```
psram: PSRAM ID read error: 0xffffffff
cpu_start: Failed to init external RAM!
```

## `0x00000002` Heap too small
The firmware failed to allocate enough memory. This most likely is a consequential error of a bad PSRAM!

## `0x00000004` Cam bad
The attached camera can not be initialized.
This usually is because on of the following reasons:
 - The camera is not supported, see [Hardware Compatibility](../Hardware-Compatibility)
 - The camera is not attached properly -> Try to remove and attach it again. Make sure you move the black part enough into the socket!
 - The camera or the camera cable is damaged

## `0x00000008` SD card basic check failed
One or more basic SD card checks failed.

The following checks are performed during boot sequence:
- Write a file (sdcard/sdcheck.txt) to SD card with some generic text
- Read the written file back
- CRC check
- Delete the file

Detailed error indication (write, rerad or delete error) can be derived from blinking code of red board status LED. Please have a look to !!!TODO!!!

Recommendation: Reformat SD card and check again or try another SD card

## `0x00000010` SD folder or file presence check failed
Oned or more mandatory folders and/or files are missing on SD card.
To have early indication that SD card is potentially ready for operation, some folder and files, which are mandatory are presence checked. This is not a 100% check and a successful test does not mean everthing is OK.

The following folders / files get checked during boot sequence:
- /sdcard/config
- /sdcard/html
- /sdcard/demo --> created automatically in firmware
- /sdcard/firmware --> created automatically in firmware
- /sdcard/img_tmp --> created automatically in firmware
- /sdcard/log --> created automatically in firmware
- /sdcard/wlan.ini
- /sdcard/config/config.ini
- /sdcard/html/index.html
- /sdcard/html/ota_page.html
- /sdcard/html/log.html
- /sdcard/html/common.js
- /sdcard/html/gethost.js
- /sdcard/html/version.txt

Recommendation: Check logs and / or redo a Over-The-Air Update (OTA Update) to ensure proper SD card structure

# Non-Critical Errors
Those Errors can be caused by an error during initialization. It is possible that the error has no impact at all or that a reboot solves it.

## `0x00000100` Cam Framebuffer bad
The firmware was unable to initialize the Camera Framebuffer.
The firmware will continue to work, but other consequential error might arise.
A reboot of the device might help.

## `0x00000200` NTP failed
The firmware failed to get the world time from an NTP server. The firmware will continue to work, but has a wrong time.
