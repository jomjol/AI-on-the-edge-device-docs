# MQTT API
The device is capable to register to a MQTT broker to publish data and subscribe to specific topics.

!!! Note
    Only MQTT v3.1.1 is supported.

The MQTT service has to be enabled and configured properly in the device configuration via web interface (`Settings` -> `Configuration` -> section `MQTT`)

The following parameters have to be defined:
* URI
* MainTopic (optional, if not set, the hostname is used)
* ClientID (optional, if not set, `AIOTED-` + the MAC address gets used to make sure the ID is unique)
* User (optional)
* Password (optional)
* RetainFlag (optional)

## Published topics

### Status

The following overhead data are available under the main topic (i.e. `watermeter`):

Topic | Description
-|-
`watermeter/MAC` | The MAC address of the ESP module.
`watermeter/IP` | The IP address of the ESP module.
`watermeter/Hostname` | The network host name of the ESP module.
`watermeter/Interval` | The round interval as configured during setup or in [Parameters -> Interval](https://jomjol.github.io/AI-on-the-edge-device-docs/Parameters/#section-autotimer).
`watermeter/Connection` | Network connection status.
`watermeter/Uptime` | Seconds up since last boot.
`watermeter/FreeMem` | Free memory in kB.
`watermeter/wifiRSSI` | Quality of WiFi signal.
`watermeter/CPUTemp` | Temperature of the ESP CPU in degrees celsius.

### Result

The following calculation data are available under the sup-topic `main` (i.e. `watermeter/main`):

Topic | Description
-|-
`watermeter/main/error` | Informs about the flow status. On success, the value is `no error`.
`watermeter/main/raw` | The value **before** performing [post processing](https://jomjol.github.io/AI-on-the-edge-device-docs/Parameters/section-postprocessing).
`watermeter/main/value` | The value **after** performing [post processing](https://jomjol.github.io/AI-on-the-edge-device-docs/Parameters/section-postprocessing).
`watermeter/main/rate` | How much flow was consumed in one minute.
`watermeter/main/rate_per_time_unit` | How much flow was consumed in one minute. The time unit gets set with the Home Assistant Discovery, e.g. `h` (hours) or `m` (minutes).
`watermeter/main/changeabsolut` | Difference between the previous and actual read value.
`watermeter/main/rate_per_digitalization_round` | How much flow was consumed in one minute.
`watermeter/main/timestamp` | Timestamp of the last valid reading (equal to timestamp of previous value)
`watermeter/main/Status` | Informs about the last performed step of the watermeter (i.e. `Flow finished`).
`watermeter/main/json` | This is a JSON formatted object containing the following values: `value`, `raw`, `pre`, `error`, `rate`, `timestamp`.

### GPIO
`MainTopic`/{GPIO topic}, e.g. `watermeter/GPIO/GPIO12`

* #### GPIO/GPIO{PinNumber}
  Depending on device configuration (`Settings` --> `Configuration` --> section `GPIO`)


## Subscribed topics
`MainTopic`/{subscribed topic}, e.g. `watermeter/ctrl/flow_start`

### Control

* #### ctrl/flow_start
  Trigger a flow start by publishing to this topic 
    + Payload:
       - any character, length > 0

* #### ctrl/set_prevalue
  
  !!! Note
      This feature is available since version [15.2.0](https://github.com/jomjol/AI-on-the-edge-device/releases/tag/v15.2.0)!
 
  Set the last valid value (previous value) to given value or the actual RAW value. Payload needs to be provided in JSON notation.
    + Payload:
       - Set to given value (value >= 0): `{"numbersname": "main", "value": 12345.67890}`
           * `"numbersname":`Provide name of number sequence, e.g. `"main"`  
           * `"value":` provide the value to be set
            
       - Set to actual RAW value (value < 0, a valid RAW value is mandatory): `{"numbersname": "main", "value": -1}`
           * `"numbersname":` Provide name of number sequence, e.g. `"main"`  
           * `"value":` Provide any negative number

* #### GPIO/GPIO{PinNumber}
  Depending on device configuration (`Settings` --> `Configuration` --> section `GPIO`)
