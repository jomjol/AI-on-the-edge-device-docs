This page lists possible blink codes of the red LED located on the ESP32-CAM board, their meaning and possible solutions.

The error code source definition can be found [here](https://github.com/jomjol/AI-on-the-edge-device/blob/rolling/code/components/jomjol_helper/statusled.h).

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
| PSRAM_INIT    | 6                 | RAM init failed: Not found/defective  | 1                | X
| PSRAM_INIT    | 6                 | External SPI RAM < 4MB                | 2                | X
| PSRAM_INIT    | 6                 | Total heap < 4MB                      | 3                | X
| TIME_CHECK    | 7                 | Missing time sync (check every round) | 1                |
| OTA_OR_AP     | 8                 | OTA process ongoing                   | 1                | X
| OTA_OR_AP     | 8                 | Soft AP started (for remote config)   | 2                | X
| FLASHLIGHT    | N/A               | LED on when flashlight is on          | solid, <br> no blink



# ERROR / WARNING

## Source WLAN_CONN: WLAN disconnected

!!! NOTE
    Only warning indication, blink code repetition: 2x

### `WLAN disconnected (No Access Point)`
WLAN connection is interrupted due to no access point in range.

### `WLAN Disconnected (Authentication failure)`
WLAN connection is interrupted due to an authentication failure. If error repeats check WLAN config in WLAN.INI (username, password)

### `WLAN Disconnected (Timeout)`
WLAN connection is interrupted due to an timeout because no beacon from AP is received in a timely manner. Most probably access point  is not available anymore or connection is not reliable.

### `WLAN Disconnected (Further reasons)`
WLAN connection is interrupted due to further reasons. Disconnect reason is printed in warining message. Please check serial console output or logfile from sd card (using another device to retrieve logfile /sdcard/log/message/). Please refer to this page to have additional infos in terms of WLAN disconnect reasons. --> `TODO - LINK TO PAGE`



## Source WLAN_INIT: WLAN initialization

!!! NOTE 
    All critical errors, regular boot not possible

### `WLAN.ini empty or not readable`
The WLAN.INI file is present but content is either not readable or no content present. Please check for further errors in terms of SD card readability or content of WLAN.INI which is located in /sdcard (most top folder od SD card) 

### `SSID or password empty`
The mandatory parameters SSID (name of WIFI network) and / or password is empty. Please configure those parameters in WLAN.INI and try again.

### `WIFI init error (details console)`
A general WIFI initialization error occured. Please check serial console output or logfile from sd card (using another device to retrieve logfile /sdcard/log/message/) 



## Source SDCARD_INIT: SD card initialization

!!! NOTE
    All critical errors, regular boot not possible

### `SD card filesystem mount failed`
Failed to mount FAT filesystem on SD card. Check SD card filesystem (only FAT supported) or try another card. Possible further infos: Please check serial console output.

### `SD card not found (Error code 0x107)`
SD card init failed. Check if SD card is properly inserted into SD card slot or try another card. Possible further infos: Please check serial console output.

### `SD card init failed (details console)`
A general SD card initialization error occured. Please check serial console output.



## Source SDCARD_CHECK: SD card basic check

### `File creation / write error`

!!! NOTE
    Critical error, regular boot not possible
    
A basic check of SD card is performed at boot. Failed to create the test file or writing content to the file failed. Most likely SD card is defective or not supported. Please check for further errors or try another card.

### `File read / CRC verfication error`

!!! NOTE
    Critical error, regular boot not possible
    
A basic check of SD card is performed at boot. Failed to read the test file or CRC of read back content failed. Most likely SD card is defective. Please check for further errors or try another card.

### `File delete error`

!!! NOTE
    Critical error, regular boot not possible

A basic check of SD card is performed at boot. Failed to delelte the test file. Most likely SD card is defective. Please check for further errors or try another card.


### `Folder / File presence failed`

!!! NOTE
   Critical error, normal boot not possible. Reduced WebUI is going to be loaded for further diagnostic possiblities or redo firmware update.

A basic check of SD card is performed at boot. One or more menadatory folder / file are not found on SD card. Please check logs with logfile viewer in reduced web interface or serial console output.



## Source CAM_INIT: Camera initialization
### `Camera init failed (details console)`

!!! NOTE
    Critical error, normal boot not possible. Reduced WebUI is going to be loaded for further diagnostic possiblities or redo firmware update.
    
A general camera initialization error occured. Please check logs with logfile viewer in reduced web interface or serial console output.

### `Camera framebuffer check failed`
The framebuffer of the camera was not readable. The firmware will trying to continue regular boot, but further errors can occur which block regular processing. Please check logs with logfile viewer if processing is behaving irregular.



## Source PSRAM_INIT: External RAM (SPI RAM) initialization

!!! NOTE
    A critical errors, normal boot not possible. Reduced WebUI is going to be loaded for further diagnostic possiblities or redo firmware update.
    
### `SPI RAM init failed: Not found/defective`   
External RAM (SPI RAM) initialization failed. Most likely external RAM not accessable or defective. Normal operation is not possible without having external RAM.

### `External SPI RAM < 4MB`
External RAM (SPI RAM) initialization successful, but external RAM size is too small. A size of >= 4MB is necessary to run this firmware. 

### `Total heap < 4MB`
Total available system memory (heap) is too small. A size of >= 4MB is necessary to run this firmware. 



## Source TIME_CHECK: External RAM (SPI RAM) initialization
### `Missing time sync (check every round)`

!!! NOTE
    Only warning indication, blink code repetition: 2x

If system is configured to be synced with a NTP server the sync status is checked after every round (in state: "Flow finished". An warming message is also printed to log). If the time is not synced after serveral rounds, please check for proper configuration.




# STATUS

!!! NOTE
    All only status indication


## Source OTA_OR_AP: OTA Update / Access point mode

### `OTA process ongoing`
An OTA is performed right now. Please wait until OTA is completed. System is rebooting automatically. If system is not coming up, please check serial console output.

### `Soft AP started (for remote config)`
The built-in access point functionality is started to perform initial remote remote setup. Further description: [Installtion --> Section Remote Setup using the built-in Access Point](https://jomjol.github.io/AI-on-the-edge-device-docs/Installation/)



## Source FLASHLIGHT: Flashlight

### `LED on when flashlight is on`
The LED is solid on as long the flashlight is on. This feature has lower priority than the other LED codes. Whenever another code occurs this feature will be overrided.
