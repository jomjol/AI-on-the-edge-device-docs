# Parameter `AlignmentAlgo`
Default Value: `Default`

!!! Warning
    This is an **Expert Parameter**! Only change it if you understand what it does!

## Description
Algorithm used for the alignment step.

- `Default`: Use only red color channel
- `HighAccuracy`: Use all 3 color Channels (3x slower)
- `Fast`: First time use `HighAccuracy`, then only check if the image is shifted
