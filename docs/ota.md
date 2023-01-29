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


### Update from version `v12.0.0` or newer
You can use the over the air update mechanism, which uploads the update via a ZIP files.

The update file is located on the [release page](https://github.com/jomjol/AI-on-the-edge-device/releases). Please choose the zip file with the following naming: `AI-on-the-edge-device__update__*.zip`

Go to the menu `System --> OTA Update` and follow the instructions there. After a final automatic reboot you should have the new version running.

### Update from version older than `v12.0.0`
If you update from an version older than 12.0.1, you should firstly update to version 12.0.1. Background are not fully backward compatible changes in the `config.ini`, that are taken care of in this version.

:bangbang: **Make sure to read the instructions below carefully!**

1.  Backup your configuration (use the `System -> Backup/Restore` page)!

2.  Upload and update the `update-*.zip` file from the release  **`12.0.1`**  [see here](https://github.com/jomjol/AI-on-the-edge-device/releases/tag/v12.0.1) .

4.  Let it restart and check on the `System -> Info` page that the Firmware as well as the Web UI got updated. If only one got updated, redo the update. If it fails several times, you also can update the Firmware and the Web UI separately.

5.  Safe way: 
    1.  Update first the `firmware.bin` (extract it from one of the provided zip files) and do the Reboot
    2.  Update with the full zip file (`update-*.zip`, ignore the version warning after the reboot)

6.  Please go to `Settings -> Configuration` and address the changed parameters:
    -   DataLogging (storing the values for data graph)
    -   Debug (extended by different debug reporting levels)

7.  Make sure it starts to do the digitalization (check the Error field on the overview page). If it does not start a round within a minute, restart the device.

:bangbang: **If the system is working now without any issues, please open the configuration editor once and save the `config.ini`. This will update the file to the newest content**:bangbang:

Now you can safely update to the newest version.

