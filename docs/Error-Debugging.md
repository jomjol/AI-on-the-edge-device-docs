# Often observed issues

## Hardware failure
  * Camera not working --> check the interface, test another module
  * Low cost module with no or only 2MB memory instead of 4MB --> test another module
  * SD card issues --> test another SD card
  * Wifi reception bad / unstable --> bad antenna, test another module or use external antenna

More information in terms of hardware, component and basic configuration issues can be found here: [Reboot reasons](https://jomjol.github.io/AI-on-the-edge-device-docs/Frequent-Reboots/)

## ROI misaligned

<img src="https://user-images.githubusercontent.com/108122193/188264361-0f5038ce-d827-4096-93fb-5907d3b072b4.png" width=30% height=30%>

This typically happens if you have suboptimal "Alignment Marks". A very simple and working solution is to put put higly contrasted stickers on your meter and put "Alignment Marks" on it (see picture below)

<img src="https://user-images.githubusercontent.com/108122193/188264752-c0f2a2be-0c22-40de-afaf-fd55b2eb4182.png" width=30% height=30%>

If after those adjustment you still have some issues, you can try to adjust your alignment settings in expert mode:
<img src="https://user-images.githubusercontent.com/108122193/188382213-68c4a015-6582-4911-81bc-cdce8ef60ed2.png" width=75% height=75%>


## My Analog Meter are recognized as Digital Counter or vice versa 

<img src="https://user-images.githubusercontent.com/108122193/188265470-001a392f-d1f4-46a3-b1e8-f29ec41c8621.png" width=40% height=40%>


1. First, check that your ROI are correctly defined (yey!)
2. Second, verify that the name of your ROI analog and digital ROIs are different 

## Recognition is working well, but number aren't sorted correctly

You have to sort your ROI correctly (Bigger to smaller). Select your ROI and click either "move next" or "move previous". Repeat until your ROI are correctly sorted

<img src="https://user-images.githubusercontent.com/108122193/188264916-03befff1-4e61-4370-bd5a-9168a88c57f2.png" width=50% height=50%>

