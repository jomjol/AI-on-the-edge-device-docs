This page lists possible blink codes of the red LED located on the ESP32-CAM board, their meaning and possible solutions.

The effective error codes can be found [here](https://github.com/jomjol/AI-on-the-edge-device/blob/rolling/code/components/jomjol_helper/statusled.h).

TODO!!!

# Error
Those errors make the normal operation of the device impossible.
Most likely they are caused by a hardware issue!

## `0x00000001` PSRAM bad
Your device most likely has no PSRAM at all or it is too small (needs to have at least 4 MBytes)!
See [Hardware Compatibility](../Hardware-Compatibility).

Usually the log shows something like this:
```
psram: PSRAM ID read error: 0xffffffff
cpu_start: Failed to init external RAM!
```

# Status
Those Errors can be caused by an error during initialization. It is possible that the error has no impact at all or that a reboot solves it.

## `0x00000100` Cam Framebuffer bad
The firmware was unable to initialize the Camera Framebuffer.
The firmware will continue to work, but other consequential error might arise.
A reboot of the device might help.

## `0x00000200` NTP failed
The firmware failed to get the world time from an NTP server. The firmware will continue to work, but has a wrong time.
