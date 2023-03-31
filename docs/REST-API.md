# REST API
Various information is directly accessible over specific REST calls.

To use it, just append them to the IP, separated with a `/`, e.g. `http://192.168.1.1/json`

Note: For more detailed information to the REST handler, have a look to the code in the repository: [registered handlers](https://github.com/jomjol/AI-on-the-edge-device/search?q=camuri.uri)

## Control
* ### flow_start
  Trigger a flow start (if not running)
     + Payload:
        - No payload needed
  
 
* ### setPreValue
  Set the last valid value (previous value) to given value or the actual RAW value.
     + Payload:
        - Set to given value (value >= 0), e.g. `/setPreValue?numbers=main&value=1234.5678`  
           * `numbers=` Provide name of number sequence, e.g. main
           * `value=` provide the value to be set
    
        - Set to actual RAW value (value < 0, a valid RAW value is mandatory), e.g. `/setPreValue?numbers=main&value=-1`
           * `numbers=` Provide name of number sequence, e.g. main
           * `value=` provide yna negative number

* ### GPIO
   - Control a GPIO output
     - The `GPIO` entrypoint also support parameters:
       - `/GPIO?GPIO={PinNumber}&Status=high`
       - `/GPIO?GPIO={PinNumber}&Status=low`
     - Example: `/GPIO?GPIO=12&Status=high`

   - Read a GPIO input 
     - The `GPIO` entrypoint also support parameters:
       - `/GPIO?GPIO={PinNumber}`
     - Example: `/GPIO?GPIO=12`

* ### ota

* ### ota_page.html
  Opens the Over-The-Air update html page

* ### reboot
  Trigger a reboot of the device

## Results
* ### json
  Show result in JSON syntax
  - Example: 
  `{
  "main":
    {
      "value": "521.17108",
      "raw": "521.17108",
      "pre": "521.17108",
      "error": "no error",
      "rate": "0.023780",
      "timestamp": "2023-01-13T16:00:42+0100"
    }
  }`

* ### value
  Show single result values
  - The `value` entrypoint also support parameters:
   - `http://<IP>/value?all=true&type=value`
   - `http://<IP>/value?all=true&type=raw`
   - `http://<IP>/value?all=true&type=error`
   - `http://<IP>/value?all=true&type=prevalue`

* ### img_tmp/raw.jpg
  Capture and show a new raw image

* ### img_tmp/alg.jpg
  Show last aligned image

* ### img_tmp/alg_roi.jpg
  Show last aligned image including ROI overlay

## Status
* ### statusflow
  Show the actual step of the flow incl. timestamp
  - Example: `Take Image (15:56:34)`

* ### rssi
  Show the WIFI signal strength (Unit: dBm)
  - Example: `-51`

* ### cpu_temperature
  Show the CPU temperature (Unit: °C)
  - Example: `38`

* ### sysinfo
  Show system infos in JSON syntax
  - Example: `[{"firmware": "","buildtime": "2023-01-25 12:41","gitbranch": "HEAD","gittag": "","gitrevision": "af13c68+","html": "Development-Branch: HEAD (Commit: af13c68+)","cputemp": "64","hostname": "WaterMeterTest","IPv4": "192.168.xxx.xxx","freeHeapMem": "2818330"}]`

* ### starttime
  Show starttime
  - Example: `20230113-154634`

* ### uptime
  Show uptime
  - Example: `0d 00h 15m 50s`

## Camera
* ### lighton
  Switch the camera flashlight on 

* ### lightoff
  Switch the camera flashlight off

* ### capture
  Capture a new image (without flashlight)

* ### capture_with_flashlight
  Capture a new image with flashlight

* ### save
  Save a new image to SD card
  - The `save` entrypoint also support parameters:
   - `http://<IP>/save?filename=test.jpg&delay=1000`

## Logs
* ### log 
  Last part of todays log (last 80 kBytes))

* ### logfileact 
  Full log of today

* ### log.html
  Opens the log html page

## Diagnostics
* ### heap
  print relevant memory (heap) information
  - Example: `Heap info: Heap Total: 1888926 | SPI Free: 1827431 | SPI Larg Block: 1802240 | SPI Min Free: 758155 | Int Free: 61495 | Int Larg Block: 55296 | Int Min Free: 36427`
