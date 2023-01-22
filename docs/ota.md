# Over-The-Air (OTA) Update
You can do an OTA (over-the-air) update via the Web Interface.
Grab the firmware from the

 *  [Releases page](https://github.com/jomjol/AI-on-the-edge-device/releases) (Stable, tested versions), or the
 *  [Automatically build development branch](https://github.com/jomjol/AI-on-the-edge-device/actions?query=branch%3Arolling) (experimental, untested versions). Please inform yourself on [Living on the Edge](../rolling-installation) first!

## Update Procedure
1. Create a backup of your configuration. Either use the Backup/Restore function of your device for this (menu `System > Backup/Restore`) or back the files manually up using the File Server (menu `File Server`, folder `config`). It is recommended to at least save the config file `config.ini`!
1. Head to the menu `System > OTA Update` and follow the instructions there.

If you do an update between major versions, it might be needed to modify the config file `config.ini` as it's syntax or context has changed.
To do so, go to the menu `Settings > Configuration` (after the update completed and the device restarted) and check if it warns you about an unset parameter.
