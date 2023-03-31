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
`MainTopic`/{status topic}, e.g. `watermeter/status`

* #### Connection

* #### Interval

* #### MAC

* #### IP

* #### Hostname

* #### Uptime

* #### FreeMem

* #### WifiRSSI

* #### CPUTemp

* #### Status

### Result
`MainTopic`/{NumberName}/{result topic}, e.g. `watermeter/main/value`

* #### Value

* #### Raw

* #### Error

* #### JSON

* #### Rate

* #### Rate_per_time_unit
  The time Unit gets set with the Home Assistant Discovery, e.g. `h` or `m` (minutes)

* #### Rate_per_digitalization_round
  The `interval` defines when the next round gets triggered

* #### Changeabsolut

* #### Timestamp

* #### JSON
  All relevant results in JSON syntax

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
    - any character
    - length > 0

* #### ctrl/set_prevalue
  Set the last valid value (previous value) to given value or the actual RAW value. Payload needs to be provided in JSON notation.

  + Payload:
    - Set to given value (value >= 0): `{"numbersname": "main", "value": 12345.67890}`
       * "numbersname": Provide name of number sequence, e.g. `"main"`  
       * "value": provide the value to be set
     
     - Set to actual RAW value (value < 0, a valid RAW value is mandatory): `{"numbersname": "main", "value": -1}`
       * "numbersname": Provide name of number sequence, e.g. `"main"`  
       * "value": Provide any negative number

* #### GPIO/GPIO{PinNumber}
  Depending on device configuration (`Settings` --> `Configuration` --> section `GPIO`)
