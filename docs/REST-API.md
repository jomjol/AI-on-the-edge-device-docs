# REST API
Various information is directly accessible over specific REST calls.

For an up-to-date list search the Github repository for [registered handlers](https://github.com/jomjol/AI-on-the-edge-device/search?q=camuri.uri)

To use it, just append them to the IP, separated with a `/`, eg. `http://192.168.1.1/json`

## Control
* ### flow_start
  Trigger a flow start (if not running)

* ### gpio
  - The `gpio` entrypoint also support parameters:
    - `/GPIO?GPIO={PinNumber}&Status=high`
    - `/GPIO?GPIO={PinNumber}&Status=low`
  - Example: `/GPIO?GPIO=12&Status=high`

* ### ota

* ### ota_page.html
  Opens the Over-The-Air update page

* ### reboot
  Trigger a reboot of the device

## Results
* ### json
  Show result in JSON syntax
  - -> Example: 
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
  The `value` entrypoint also support parameters:
   - `http://<IP>/value?all=true&type=value`
   - `http://<IP>/value?all=true&type=raw`
   - `http://<IP>/value?all=true&type=error`
   - `http://<IP>/value?all=true&type=prevalue`

* ### img_tmp/raw.jpg
  Caputre and show a new raw image

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

* ### starttime
  Show starttime
  - Example: `20230113-154634`

* ### uptime
  Show uptime
  - Example: `0d 00h 15m 50s`

## Camera
* ### lighton

* ### lightoff

* ### capture

* ### capture_with_flashlight

* ### save
  The `save` entrypoint also support parameters:
   - `http://<IP>/save?filename=test.jpg&delay=3`

## Logs
* ### log 
  Last part of todays log

* ### logfileact 
  Full log of today

* ### log.html

## Diagnostics
* ### heap
  print all relevant memory (heap) information
