# Alignment References

The alignment references are used in every round to re-align the taken image to the reference coordinates. 
Two alignment structures must be defined and the taken image then in each round is shifted and rotated according to their position
with the target to be in exactly the same position as the reference image.

!!! Note
    The alignment structures needs to be unique and have a good contrast. 
    It is advised to have them as far apart as possible.



## Precondition
Please make sure to have setup your camera properly and taken a good [Reference Image](../Reference-Image).

## Define two Reference Images

![](img/initial_setup_2_alignment_marks.jpg){: style="width:500px"}

You can switch between this two marks with `(1)`.

Then define the reference area in the image by either directly drag and drop with the mouse or use the input boxes below.
To apply the currently marked image part you need to push `"Update Reference" (2)`. 

In some cases it might be useful to use a reference with a higher contrast. This can be achieved by pushing `Enhance Contrast" (3)`.
The result will be calculated on the ESP32 - so be a bit patient, before you see it active.

To save push `"Save to config.ini" (4)`.

!!! Note
    A reboot is not required at this point of time.

As next you should define the [Digit and Analog ROIs](ROI-Configuration.md).
