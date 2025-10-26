# Reference Image

!!! Note
    The Reference Image is the basis for the coordinate system of the ROIs. Therefore it is very important, to have a well aligned image, that is not rotated. 

At first an example image is shown.
To define a new reference image push the button `"Create new Reference" (2)` and afterwards `"Take Image" (2)`. It might take some seconds for processing, then your actual camera image should be shown.
Then play with the provided parameters to get a good result.

![](img/initial_setup_1_reference_image.jpg){: style="width:500px"}

## Focus
This is the first time, where you have access to the camera image. It most likely is out of focus and not sharp!
Ensure a sharp image of the camera by adjusting the focal length of the ESP OV2640 camera.

!!! Note
    Try to adjust the focus for the clearest possible image!


In order to use it for reading a meter, the focal-length  of the OV2640 camera has to be manipulated.
By default it only results in sharp image for distance bigger than around `~40cm` which is not ideal for our purpose.

Therefore you need to remove the fixing glue of the OV2640 lens with a sharp knife. After this you can rotate the lens in and out. Rotating it by about a quarter of a turn counterclockwise results in a focus plane shift of about 10cm. You need to figure out your best setting with a little bit of  trial and error for your specific environment.

!!! Error
    Be **very** carefully when rotating the lens. Best is to held the camera itself with one hand or a plier and rotate the lens with the other hand.
    Make sure **not** to rotate the whole camera as this can damage the ribbon cable!

!!! Warning
    This modification will void any warranty, as the sealing of the lens objective is broken!

!!! Warning
    This modification will render the camera unsuitable for general, web-cam type applications unless the focal length is changed back to the original setting.

![](img/focus_adjustment.jpg)



## Correct Horizontal Alignment

Ensure an **exact horizontal alignment** of the number:

| :heavy_check_mark: Okay     | :x: Not Okay                    |
| --------------------------- | ------------------------------- |
| ![](img/alignment_okay.jpg) | ![](img/alignment_not_okay.jpg) |

!!! Warning
    Updating the reference image also means that all alignment images and ROIs needs to be configured again.
    Therefore do this step later only with caution.

If everything is done, you can save the result with `"Update Reference Image" (4)`.

!!! Note
    A reboot is not required at this point of time.

As next you should update the [Alignment References](Alignment.md).

## Dealing with Reflections
Reflections can be caused by the flash LED and make it hard to provide a reliable detection.
There are various ways to deal with them:

- Attach a diffusor in front of the LED, eg. a filt (Filz) or parchment paper. Also white paper can do the job.
- Rotate the ESP-CAM so the LED is on another place.
- Reduce the LED intensity.
- Use external LED stripes, eg `WS2812x`.
