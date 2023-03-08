This page lists possible blink codes of the red LED located on the ESP32-CAM board, their meaning and possible solutions.

The effective error codes can be found [here](https://github.com/jomjol/AI-on-the-edge-device/blob/rolling/code/components/jomjol_helper/statusled.h).

# General design approach:

  * 250ms blink code to identify source
  * 500ms defined LED off
  * 250ms blink code to identify error / status code
  * 1,5s LED off to signal repetition
  * Either repeat infinite for critical errors or repeat the status / warning blink code 2x
  * e.g. 3x blinks | 500ms LED off | 2x blinks --> error: SD card not found

| **source**    | source <br> blink count| error / warning / status         | status <br> blink count| repeat <br> infinite |
| ------------- | ----------------- |---------------------------------------| ---------------- | -----------------|
| WLAN_CONN     | 1                 | Disconnected (No Access Point)        | 1                |
| WLAN_CONN     | 1                 | Disconnected (Authentication failure) | 2                |
| WLAN_CONN     | 1                 | Disconnected (Timeout)                | 3                |
| WLAN_CONN     | 1                 | Disconnected (further reasons)        | 4                |  
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
| FLASHLIGHT    | N/A               | LED on when flashlight is on (lowest prio) | solid, no blinking



# ERROR / WARNING

## Source WLAN_CONN: WLAN disconnected

!!! NOTE
    Only warning indication, not blocking futher processing

### `WLAN disconnected (No Access Point)`
WLAN connection is interrupted due to no AP in range.

### `WLAN Disconnected (Authentication failure)`
WLAN connection is interrupted due to an authentication failure. If error repeats check WLAN config (username, password)

### `WLAN Disconnected (Timeout)`
WLAN connection is interrupted due to an timeout because no beacon from AP is received in a timely manner. Most probably AP is not available anymore or connection is not reliable.

### `WLAN Disconnected (Further reasons)`
WLAN connection is interrupted due to further reasons. Disconnect reason is printed in waring message. Please check serial console output or logfile from sd card (using another device to retrieve logfile /sdcard/log/message/). Please refer to this page to have additional infos in terms of WLAN disconnect reasons.



## Source WLAN_INIT: WLAN initialization

!!! NOTE 
    Critical error, normal boot not possible.

### `WLAN.ini empty or not readable`
The WLAN.INI file is present but content is either not readable or no content present. Please check for further errors in terms of SD card readability or content of WLAN.INI which is located in /sdcard (most top folder od SD card) 

### `SSID or password empty`
The mandatory parameters SSID (name of WIFI network) and / or password is empty. Please configure those parameters and try again.

### `WIFI init error (details console)`
A general WIFI initialization error occured. Please check serial console output or logfile from sd card (using another device to retrieve logfile /sdcard/log/message/) 



## Source SDCARD_INIT: SD card initialization
!!! NOTE
    Critical error, normal boot not possible.

### `SD card filesystem mount failed`
Failed to mount FAT filesystem on SD card. Check SD card filesystem (only FAT supported) or try another card.

### `SD card not found (Error code 0x107)`
SD card init failed. Check if SD card is properly inserted into SD card slot or try another card.

### `SD card init failed (details console)`
A general SD card initialization error occured. Please check serial console output or logfile from sd card (using another device to retrieve logfile /sdcard/log/message/) 



## Source SDCARD_CHECK: SD card basic check

!!! NOTE
    Critical error, normal boot not possible. 

### `File creation / write error`
A basic check of SD card is performed at boot. Failed to create the test file or writing content to the file failed. Most likely SD card is defective or not supported. Please check for further errors or try another card.

### `File read / CRC verfication error`
A basic check of SD card is performed at boot. Failed to read the test file or CRC of read back content failed. Most likely SD card is defective. Please check for further errors or try another card.
### `File delete error`
A basic check of SD card is performed at boot. Failed to delelte the test file. Most likely SD card is defective. Please check for further errors or try another card.


### `Folder / File presence failed`

!!! NOTE
   Reduced WebUI is going to be loaded for further diagnostic possiblities or redo firmware update.

A basic check of SD card is performed at boot. One or more menadatory folder / file are not found on SD card. Please check logs with logfile viewer in redurced web interface or serial console output.



## Source CAM_INIT: Camera initialization
### `Camera init failed (details console)`

!!! NOTE
    Critical error, normal boot not possible. Reduced WebUI is going to be loaded for further diagnostic possiblities or redo firmware update.
    
A general camera initialization error occured. Please check logs with logfile viewer in redurced web interface or serial console output.

### `Camera framebuffer check failed`
The framebuffer of the camera was not readable. The firmware will trying to continue regular boot, but further errors can occur which block regular processing


TODO --> from HERE
