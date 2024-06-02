# Prometheus/OpenMetrics

A set of metrics is exported via the `/metrics` REST API path on the device. Besides the current value, a set of device properties are exported. Multiple sequences (aka *numbers*) are supported via a label. The metrics are provided in text wire format.

Example:

```bash
$ curl http://<IP>/metrics
# HELP ai_on_the_edge_device_flow_value current value of meter readout
# TYPE ai_on_the_edge_device_flow_value gauge
ai_on_the_edge_device_flow_value{sequence="main"} 240.7064
# HELP ai_on_the_edge_device_cpu_temperature_celsius current cpu temperature in celsius
# TYPE ai_on_the_edge_device_cpu_temperature_celsius gauge
ai_on_the_edge_device_cpu_temperature_celsius 41
# HELP ai_on_the_edge_device_rssi_dbm current WiFi signal strength in dBm
# TYPE ai_on_the_edge_device_rssi_dbm gauge
ai_on_the_edge_device_rssi_dbm -67
# HELP ai_on_the_edge_device_memory_heap_free_bytes available heap memory
# TYPE ai_on_the_edge_device_memory_heap_free_bytes gauge
ai_on_the_edge_device_memory_heap_free_bytes 716303
# HELP ai_on_the_edge_device_uptime_seconds device uptime in seconds
# TYPE ai_on_the_edge_device_uptime_seconds gauge
ai_on_the_edge_device_uptime_seconds 214267
# HELP ai_on_the_edge_device_rounds_total data aquisition rounds since device startup
# TYPE ai_on_the_edge_device_rounds_total counter
ai_on_the_edge_device_rounds_total 239
```

## Prometheus Scrape Config

The following scrape config (add to `prometheus.yml`) can be used as an example to ingest available metrics with prometheus:

```
scrape_configs:
  - job_name: watermeter
    scrape_interval: 300s
    metrics_path: /metrics
    static_configs:
      - targets: ['<IP>']
```

## References

- [OpenMetrics](https://github.com/OpenObservability/OpenMetrics/blob/main/specification/OpenMetrics.md)