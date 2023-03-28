# Basic hardware / configuration issues


If the device is behaving eratically or not running as expected you can use the following tools trying to identify the root cause:

1. Internal logging (`config.ini`)
   --> Set to DEBUG log level
2. Reduced web interface (only error indication visualization, [Error codes on reduced webinterface](https://jomjol.github.io/AI-on-the-edge-device-docs/Error-Codes/))
2. Red board LED: [Status LED Blinkcodes](https://jomjol.github.io/AI-on-the-edge-device-docs/StatusLED-BlinkCodes/)
3. Serial log of the UART interface (USB access needed, only local, same as for flashing the firmware)


There are in principle two reboots types:

1. Sporadic random reboots (always different timing and situation)
2. Repeating boot loops (reoccuring, always stop working after same precondition)


______

### Sporadic random reboots

Sporadic random reboots could have the following reasons:

* In general: Unstable system due to software issues (e.g. overload during HTML access, ...)
  --> Trying the figure out what's the root cause to fix the issue
* Bad power supply
  --> The power supply need to stable to ensure proper operation of the device. If it's not stable the device tents to sporadic reboots (brownout detection)

In general: There are several mechanisms in the firmware (like saving previous values), to have a "smooth" reboot without too many notable disturbance.

##### System instabilities

If your system is sometimes running smoothly over several runs and sometimes reboots obviously randomly, you have an partially unstable device. 

You can check this in the standard log file on the SD card:


```
2021-12-26T06:34:09: task_autodoFlow - round done
2021-12-26T06:34:09: CPU Temperature: 56.1
2021-12-26T06:38:00: task_autodoFlow - next round - Round #23
```

Here you see, that the round #23 is starting, so obviously there were no reboots in the last 22 rounds. There is hardware (ESP32CAM), where only 2-3 stable rounds are possible and others, where way more than 100 rounds without any reboots is possible.
There is noting you can do about it, beside testing different hardware.


#### Overload during HTML access

If you frequently access the web server over HTML requests, the firmware tends to reboot. This especially happens during the first run and when the ESP32 is busy with the digitization flow. 

The reason for this are running out of memory during a flow, minor memory leakage in combination with missing error handling.

There is noting you can do about this kind of reboot, beside two thing:

1. Support the firmware development with improved and tested part of code
2. Be patient :-)


##### Bad or insufficient power supply

A good and stabilized power supply is essential to have error free operation. The device is quite picky in terms of proper power supply. Especially the wifi module have some load spikes which the power supply needs to cover. If the power is not stable enough, the brwonout mechanism is protecting against strange behaviour and force a reboot whenever the voltage drops below a specific level. You can see this in random reboots which indication is logfile: --> Reset reason: Brownout



______

### Repeating boot loops

Repeating boot loops at the same situation during the flow has a systematic problem either in the hardware or the configuration. It usually happens during initialization state or processing the first round as there all needed parts of the firmware have been loaded for the first time.

To identify the root cause the logfiles, the reduced web interface, the red board LED or the serial log of the UART interface (no remote access, USB access needed) is helpful. 

Possible issues:

* SD card related issues
* RAM related issues
* Configuration related issues



##### SD card related issues

The ESP32CAM is a little bit "picky" with the supported SD cards. Due to the limited availability of GPIOs the SD card can only be accessed via 1-wire mode. Therefore not all SD cards are supported. The following error cases can occur:


###### SD card: Wrong filesystem (only FAT32 is supported)

If this SD card error is detected only the following indications are available. No web interface will be accessible.

* Red board LED is blinking. The blinking codes are described here: [Status LED Blinkcodes](https://jomjol.github.io/AI-on-the-edge-device-docs/StatusLED-BlinkCodes/)
* Error messages on serial log (UART interface)


###### SD card not detected / not supported

If this SD card error is detected the following indication are available. No web interface will be accessible.

* Red board LED is blinking. The blinking codes are described here: [Status LED Blinkcodes](https://jomjol.github.io/AI-on-the-edge-device-docs/StatusLED-BlinkCodes/)
* Error messages on serial log (UART interface)


###### SD card detected but files are not readable / writeable

The SD card is detected, but the files cannot be read or written. A basic SD card check for SD reading / writing is performed on every boot. This not 100% guarantee that SD card is working but it's at least a indication.

If this SD card error is detected the following indications are available:

* The reduced web interface will be loaded to have visual feedback of error situation. Regualar processing is disabled, though. Within this reduced web interface logs can be viewed to have further indication what's the root cause. Error code desciption can be found here: [Error codes on reduced webinterface](https://jomjol.github.io/AI-on-the-edge-device-docs/Error-Codes/)
* Error messages in logfile
* Red board LED is blinking. The blinking codes are described here: [Status LED Blinkcodes](https://jomjol.github.io/AI-on-the-edge-device-docs/StatusLED-BlinkCodes/)
* Error messages on serial log (UART interface)



##### RAM related issues

In order to run the firmware, 4 MB of external RAM (PSRAM) are mandatory. Usually, the ESP32CAM is equipped with 8MB (64Mbit) PSRAM chip, whereof only 4MB can be used effectively (direct addressable).
Unfortunately, there is hardware around, where no PSRAM or only 2MB of PSRAM is present - **even if you have bought a device where a 8MB PSRAM was promoted**. These modules are not suiable for this firmware because the external RAM is needed to handle the CNN files and camera images. There is nothing to do, than to buy a new ESP32CAM with **really** 64MBit of PSRAM. 


###### Too less external RAM (PSRAM)

During the boot process the available RAM is going to be checked.

If there is too less RAM (PSRAM or total HEAP < 4MB) detected, the follwoing indications are available:

* The reduced web interface will be loaded to have visual feedback of error situation. Regualar processing is disabled, though. Within this reduced web interface logs can be viewed to have further indication what's the root cause. Error code desciption can be found here: [Error codes on reduced webinterface](https://jomjol.github.io/AI-on-the-edge-device-docs/Error-Codes/)
* Error messages in logfile
* Red board LED is blinking. The blinking codes are described here: [Status LED Blinkcodes](https://jomjol.github.io/AI-on-the-edge-device-docs/StatusLED-BlinkCodes/)
* Error messages on serial log (UART interface)



##### Configuration related issues


###### Folders and files missing

Most of the relevant folders and files are checked during boot. The complete list can be found here: [Error codes on reduced webinterface](https://jomjol.github.io/AI-on-the-edge-device-docs/Error-Codes/)

If a relevant folder or file is missing the following indications are available:

* The reduced web interface will be loaded to have visual feedback of error situation. Regualar processing is disabled, though. Within this reduced web interface logs can be viewed to have further indication what's the root cause. Error code desciption can be found here: [Error codes on reduced webinterface](https://jomjol.github.io/AI-on-the-edge-device-docs/Error-Codes/)
* Error messages in logfile
* Red board LED is blinking. The blinking codes are described here: [Status LED Blinkcodes](https://jomjol.github.io/AI-on-the-edge-device-docs/StatusLED-BlinkCodes/)
* Error messages on serial log (UART interface)


###### CNN model file not available / corrupt

Additionally for operation CNN model files on SD card are mandatory. 

* `/config/XXXXX.tflite` (one CNN model file for analog counter and for for digit numbers each, where XXXXX is the file name, that is written in the `config.ini`)

If the files which are configured in `config.ini` are not present or corrupt, the process is going to be interrupted (or at worst case a device crash occurs). Please check logs files to have an indicator for the root cause.

This a logfile extract (DEBUB log level) where digit CNN model file is not present. The system is initializing the system and trying to load the model files:
```
[0d00h05m11s] 2023-03-27T12:25:14 [TFLITE] CTfLiteClass::LoadModel
[0d00h05m11s] 2023-03-27T12:25:14 [TFLITE] CTfLiteClass::ReadFileToModel: /sdcard
[0d00h05m11s] 2023-03-27T12:25:14 [PSRAM] Failed to allocate 0 bytes in PSRAM for 'TFLITE->modelfile'!
[0d00h05m11s] 2023-03-27T12:25:14 [TFLITE] CTfLiteClass::ReadFileToModel: Can't allocate enough memory: 0
[0d00h05m12s] 2023-03-27T12:25:14 [HEAP] CTfLiteClass::ReadFileToModel Heap Total: 2266214 | SPI Free: 2205939 | SPI Large Block: 2162688 | SPI Min Free: 2205423 | Int Free: 60275 | Int Large Block: 55296 | Int Min Free: 46451
[0d00h05m12s] 2023-03-27T12:25:14 [CNN] Can't load tflite model -> Init aborted!
[0d00h05m12s] 2023-03-27T12:25:14 [HEAP] getNetworkParameter-LoadModel Heap Total: 2266214 | SPI Free: 2205939 | SPI Large Block: 2162688 | SPI Min Free: 2205423 | Int Free: 60275 | Int Large Block: 55296 | Int Min Free: 46451
[0d00h05m12s] 2023-03-27T12:25:14 [PSRAM] Freeing memory in PSRAM used for 'TFLITE->modelfile'...
[0d00h05m12s] 2023-03-27T12:25:14 [PSRAM] Freeing memory in PSRAM used for 'TFLITE->tensor_arena'...
[0d00h05m12s] 2023-03-27T12:25:14 [PSRAM] Allocated 819200 bytes in PSRAM for 'TFLITE->tensor_arena'
[0d00h05m12s] 2023-03-27T12:25:14 [TFLITE] CTfLiteClass::LoadModel
[0d00h05m12s] 2023-03-27T12:25:14 [TFLITE] CTfLiteClass::ReadFileToModel: /sdcard/config/ana-cont_1105_s2_q.tflite
[0d00h05m12s] 2023-03-27T12:25:15 [PSRAM] Allocated 53328 bytes in PSRAM for 'TFLITE->modelfile'
[0d00h05m12s] 2023-03-27T12:25:15 [TFLITE] CTfLiteClass::MakeAllocate
[0d00h05m12s] 2023-03-27T12:25:15 [PSRAM] Freeing memory in PSRAM used for 'TFLITE->modelfile'...
[0d00h05m12s] 2023-03-27T12:25:15 [PSRAM] Freeing memory in PSRAM used for 'TFLITE->tensor_arena'...
```

* Bad config example:
  - `[0d00h05m11s] 2023-03-27T12:25:14 [TFLITE] CTfLiteClass::ReadFileToModel: /sdcard`
    --> model file missing: check configuration or file presence 

* Good config example:
  - `[0d00h05m12s] 2023-03-27T12:25:14 [TFLITE] CTfLiteClass::ReadFileToModel: /sdcard/config/ana-cont_1105_s2_q.tflite`
    --> model file found: config OK
