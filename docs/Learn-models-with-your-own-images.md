# Learn a model with your own images
Once you have collected and selected your own images (see [Collect images to improve the models](collect-new-images.md)), you can train your very own model with them.

**This is an optional step and only suggested for advances users!**

For training the model you will need a python and Jupyter installation.

All current labeled images you can find under [ziffer_sortiert_raw](https://github.com/jomjol/neural-network-digital-counter-readout/tree/master/ziffer_sortiert_raw)

### dig-class11 models (digits)
Fork and checkout [neural-network-digital-counter-readout](https://github.com/jomjol/neural-network-digital-counter-readout).

Install all requirements for running the notebooks.

```shell
pip install -r requirements.txt
```

Put your labeled images into `/ziffer_sortiert_raw` folder and run

1. [Image_Preparation.ipynb](https://github.com/jomjol/neural-network-digital-counter-readout/blob/master/Image_Preparation.ipynb)
2. [Train_CNN_Digital-Readout-Small-v2.ipynb](https://github.com/jomjol/neural-network-digital-counter-readout/blob/master/Train_CNN_Digital-Readout-Small-v2.ipynb)

It creates a dig-class11_xxxx_s2.tflite model, you can upload to the `config` folder on your device and test it. 

### dig-class100 / dig-cont models (digits)
Fork and checkout [neural-network-analog-needle-readout](https://github.com/jomjol/neural-network-analog-needle-readout).

All labeled images you can find under [Images](https://github.com/haverland/Tenth-of-step-of-a-meter-digit/tree/master/images)

Install all requirements for running the notebooks.

```shell
pip install -r requirements.txt
```

Put your labeled images into `images/collected/<typeofdevice>/<your_short>/`

Run [dig-class100-s2.ipynb](https://github.com/haverland/Tenth-of-step-of-a-meter-digit/blob/master/dig-class100-s2.ipynb). The model to upload to your device you can find under '/output'.

### ana-class100/ana-cont models (analog pointers)
Fork and checkout [neural-network-analog-needle-readout](https://github.com/jomjol/neural-network-analog-needle-readout).

All labeled images you can find under [data_raw_all](https://github.com/jomjol/neural-network-analog-needle-readout/tree/main/data_raw_all)

Install all requirements for running the notebooks.

```shell
pip install -r requirements.txt
```

Put your labeled images into `images/collected/<typeofdevice>/<your_short>/`

After every adding of images you need to run [Image_Preparation.ipynb](https://github.com/jomjol/neural-network-analog-needle-readout/blob/main/Image_Preparation.ipynb) before you train the models.

Run [Train_CNN_Analog-Readout_100-Small1_Dropout.ipynb](https://github.com/jomjol/neural-network-analog-needle-readout/blob/main/Train_CNN_Analog-Readout_100-Small1_Dropout.ipynb) and/or [Train_CNN_Analog-Readout_Version-Small2.ipynb](https://github.com/jomjol/neural-network-analog-needle-readout/blob/main/Train_CNN_Analog-Readout_Version-Small2.ipynb). The model to upload to your device you can find in the project folder.

## Share your images
If the results are good you can share the images as pull-request. Please images only!

See [Share your images](collect-new-images.md#share-your-images) for details.