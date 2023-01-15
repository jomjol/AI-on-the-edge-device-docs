# REST API
Various information is directly accessible over specific REST calls.

For an up-to-date list search the Github repository for [registered handlers](https://github.com/jomjol/AI-on-the-edge-device/search?q=camuri.uri)

To use it, just append them to the IP, separated with a `/`, eg. `http://192.168.1.1/json`

## Control
* ### flow_start
  Trigger a flow start (if not running)

* ### gpio
  Control a GPIO output
  - The `gpio` entrypoint also support parameters:
    - `/GPIO?GPIO={PinNumber}&Status=high`
    - `/GPIO?GPIO={PinNumber}&Status=low`
  - Example: `/GPIO?GPIO=12&Status=high`

  Read a GPIO input
  - The `gpio` entrypoint also support parameters:
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

* ### img_tmp/roi.jpg
  Show last aligned image

* ### img_tmp/alg_roi.jpg
  Show last aligned image incuding ROI overlay

## Status
* ### statusflow
  Show the actual step of the flow incl. timestamp
  - Example: `Take Image (15:56:34)`

* ### rssi
  Show the WIFI signal strength
  - Example: `-51dBm`

* ### cpu_temperature
  Show the CPU temperature
  - Example: `38.5 °C`

* ### sysinfo
  Show system infos in JSON syntax
  - Example: `[ { "firmware" : "xxx", "buildtime" : "2023-01-15 21:27", "gitbranch" : "xxx", "gittag" : "", "gitrevision" : "a5e533f+", "html" : "Development-Branch: xxx (Commit: a5e533f+)", "cputemp" : "67.777779", "hostname" : "xxx", "IPv4" : "192.168.xxx.xxx", "freeHeapMem" : "2789466" } ]`

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
   - `http://<IP>/save?filename=test.jpg&delay=1`

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
  - Example: `Heap: 3003978 Min Free: 1413058 larg. Block: 2949120 SPI Heap: 2957579 NOT_SPI Heap: 46399 Internal Heap: 46399 Internal Min Heap free: 10523`
