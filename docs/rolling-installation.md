# Living on the Edge

The [Github repository](https://github.com/jomjol/AI-on-the-edge-device) contains multiple branches:

 - The [master](https://github.com/jomjol/AI-on-the-edge-device/tree/master) branch contains the same firmware version as provided on the [release page](https://github.com/jomjol/AI-on-the-edge-device/releases).
 - The [rolling](https://github.com/jomjol/AI-on-the-edge-device/tree/rolling) branch contains the **latest** version of the Firmware and the Web Interface. It might already contain a fix for your issue. But it is work in progress, don't expect it to work stable or be an improvement for your AI-on-the-edge-device! Also it might break the [OTA Update](../ota) and thus require manual flashing over USB!
 - Any other branch is used to develop a feature or fix, only use them when you know what it is about!

## I still want to try it

Ok, then grab the latest `rolling` build from [Github Actions](https://github.com/jomjol/AI-on-the-edge-device/actions/workflows/build.yaml?query=branch%3Arolling) Page and proceed as following:

1. Pick the most top successful (green) build:
  ![](actions.png)  
2. Scroll down and download the `AI-on-the-edge-device__update__*.zip`:
  ![](update-artifact.png)  
5. Flash the zip file using the [OTA Update](../ota) page of your device.
