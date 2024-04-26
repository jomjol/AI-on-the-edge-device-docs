# Frequently Asked Questions

## My device reboots frequently. What can I do?

There are several reasons for frequent reboots:

* Frequent HTML requests
* Wrong configuration, missing configuration files
* Unstable hardware - see [Hardware Compatibility](../Hardware-Compatibility).

There is a dedicated page about this: [Frequent Reboots](../Frequent-Reboots/).


## Bad WebUI responsiveness. What can I do?

This is usually due to hardware or WLAN issues. There are already many entries in discussion section, some of which have good tipps.

Possible checks / ideas:

* ESP32CAM hardware antenna design is very poor in connection with camera frequency.
  * Simple test: When the device is in operation, putting your thumb on the camera connector and the directly adjacent components should make the device respond more quickly.
  * Possible optimization: Here, an attempt was made to dampen the frequency influences somewhat by shielding. 
[Shielding Example](https://www.reddit.com/r/esp32/comments/r9g5jc/fixing_ymmv_the_poor_frame_rate_on_the_esp32cam/)
* WLAN channel: Preferably use channel 1, 6 or 11
* Performance can vary depending on the AP manufacturer. If necessary, check with a mobile hotspot or other device to exclude AP influence
* Try with an external antenna
* Avoid VLAN, currently not fully supported
* Temporarily deactivate virus scanner / firewall on the end device for testing purpose
* Use sufficiently dimensioned power supply
* Use a branded SD card (formatted with Windows, MAC often causes problems)

Check [discussion section](https://github.com/jomjol/AI-on-the-edge-device/discussions) for possible further tipps.


## How accurate are the detections?

It is hard to give a specific accuracy number. It depends on many factors, e.g.

* How in-focus is your camera?
* How sturdy is the camera mount? Does it slightly move over extended periods of time?
* What type of meter are you reading? Is the meter already in the training data set?
* Are you trying to read digits, an analog dial, or both?
* etc.

Anecdotally, the authors of this page have great success with the meter. While the AI algorithm itself is not perfect and sometimes returns `NaN` or incorrect values, other post-processing / prevalue / sanity checks help ensure such invalid values are filtered out. With the correct settings, one author has been running this device for 1 month without any incorrect values reported. 

See the FAQs below for more details and configuration hints.


## My numbers are not correctly detected. What can I do?

* There is a dedicated page about the correct setting [ROI Configuration](../ROI-Configuration/).
* This page also includes the instructions for gathering new images for the training.

## How can I ensure invalid numbers are never reported?

As mentioned above, the AI algorithm is not perfect. Sometimes it may read an incorrect value.

We can tune the software to _almost_ never report an incorrect value. There is a tradeoff though: the software may report _stale_ values - i.e. it will drop incorrect values for a potentially long period of time, resulting in the meter reading being outdated by hours. If never receiving an incorrect value is important to you, consider tolerating this tradeoff.

You can change the following settings to reduce incorrect readings (but potentially increase staleness of data):

* Set a prevalue via the UI, then change `PostProcessing` configuration option `PreValueAgeStartup` to a much larger number (e.g. `43200` = 30 days).
* Change `PostProcessing` configuration option `MaxRateType` to be time based instead of absolute. Set `MaxRateValue` to something realistic (e.g. `5` gal/min). You can often find the max flow rate your meter supports directly on the cover.
* Reduce `AutoTimer` configuration option `Interval` to the lowest it can be (e.g. `3` min). The more often you take readings, the less likely for data staleness to occur.

## Even after I have setup everything perfect there is a false reading - especially around the zero crossing (roll over to next number)

* The roll over behavior is different for the different meters. E.g.:
  * Rolling over start with different previous position (e.g. at 7, 8 or 9)
  * The neutral position (no rolling) is not perfectly at zero, but rather at something like 7.9 or 8.1, even if it should be exactly 8

* The "PostProcessingAlgo" is trying to judge out of the individual readings, what number it should be. 
  * For example if the previous number is a "1", but the next number seems to be a "8.9", most probably there was a "zero crossing" and the number is a "9" and not still an "8"

* Currently the setting of the algorithm is set to fit most of the meters and cases. But the parameters do not fit perfectly for all situations. Therefore there might be intermediate states, where the reading is false. 
  This is especially the case, at the positions, where the roll over (zero crossing) is just starting.
* To prevent a sending of false parameters, there is the possibility to limit the maximum allowed change (MaxRateChange).
  Usually after some time and movement of the counters a bit further, the reading is getting back to a stable reading.
* To handle this, a parametrized setting would be needed. This is rather complicated to implement as subtle changes make a relevant difference. Currently this is not implemented. 
  So please be a bit patient with your meter :-)

## Pre-Value

PreValue is here a bit missleading, because normally it is the same as the last value. In the next round of reading it will be used to check nagtive rates, high rates (MaxRateValue / MaxRateType) and CheckDigitIncreaseConsistency (dig-class11 only). Either from a previous correctly identified value or manual setting by the user.

If you use post processes, enable the pre-value. The pre-value must be set at first time. Set it to the current raw value. 

If the device runs in errors, the pre-value will not be updated, as long as the `preValueAgeStartup` time between the last valid value (or startup time) and current time is not exceeded. After it the preValue will be set again, if no other error occured. So the device can not run in an endless error, like high rate.

## "Rate too high - Read: ..."

In configuration you can set the `MaxRateValue` and `MaxRateType`. The settings suppress improbably high values that can come from false readings. To do this, the value must be set correctly depending on your meter.

Before doing this, you should be clear about the type of rating you want to use.

- `Absolute change` is the interval between two readings - no matter how often the readings happen. 
- `RateCange` is the change per minute. This is calculated from the time difference between the last and the current reading. 

If there is an interval of 5 minutes between readings and a MaxRateValue of 1, an error "Rate too high - Read: ..." if 

- Absolute change: the difference is `> 1`
- RateChange: the difference is `> 1 / 5`

# Train on my own images

Look at [Learn models with your own images](https://jomjol.github.io/AI-on-the-edge-device-docs/Learn-models-with-your-own-images/)
and [Cookbook running the jupyter notebook with my own data](https://github.com/haverland/Tenth-of-step-of-a-meter-digit/wiki/Cookbook-running-the-jupyter-notebook-with-my-own-data).
