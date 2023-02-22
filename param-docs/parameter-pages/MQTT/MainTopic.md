# Parameter `MainTopic`
Default Value: `watermeter`
MQTT main topic, under which the counters are published.
The single value will be published with the following key: `MAINTOPIC/NUMBER/RESULT_TOPIC` where:

- `NUMBER` is the name of the value (a meter might have more than one value). 
  The names get defined in the analog and digital ROI configuration (defaults to `main`).
- `RESULT_TOPIC` can be one of `value`, `rate`, `timestamp`, `error`, ....

The general connection status can be found in `MAINTOPIC/CONNECTION`. 
See [MQTT Result Topics](../MQTT-API#result) for a full list of topics.

