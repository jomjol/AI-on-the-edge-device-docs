# Parameter `RSSIThreshold`
Default Value: `0`

Possible values: `-100` .. `0` (`0` = disabled).

!!! Warning
    This is an **Expert Parameter**! Only change it if you understand what it does!

WIFI AP switching functionality:

This parameter activates a client triggered AP switching functionality (simplified roaming).
If (actual RSSI  + 5dBm) lower than RSSIThreshold, all WIFI channels will be scanned for configured SSID and then trying to connect to access point with better RSSI. The scan is only get initiated at the end of each round.

!!! Note
    It gets automatically transferred to `/wlan.ini` on the SD-Card at next startup.
