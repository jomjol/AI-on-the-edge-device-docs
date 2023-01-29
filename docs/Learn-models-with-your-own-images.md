# Learn a model with your own images
If your device has new, different digits and the existing models don't recognize them well, you can collect your own images and so we can train the model better. This helps you and also others as the models get more accurate. this also applies if you have a model that is already known, but the neural models do not produce good results.

For experienced users, the training can also done by yourself (see below). 

Before you go ahead, please check if your digits/pointers are not yet contained in the training data. A visual overview is available at [digits](https://jomjol.github.io/neural-network-digital-counter-readout) resp. [pointers](https://jomjol.github.io/neural-network-analog-needle-readout/).

## Before you start
Poor recognition is often caused by blurred images, low contrast or incorrect setting of the ROIs. Therefore, check these possibilities first, as additional training will bring little improvement here.

You do not need train the models by yourself if you don't want (see section [Share your images](#share-your-images)). In most cases we will integrate your images in the training dataset of the models. Only if we fear a degradation of the models or you need a different behaviour, we might not include the data in the standard models (see at bottom of page for reasons).

## Collecting images
The neural network is trained based on a set of images that have already been collected over time. If your digits are included or at least very similar to included images, the chance is very high that the neural network is working fine for you as well.

The neural network configuration is stored in the TensorFlow Lite format as `*.tfl` or `*.tflite` in the `/config` directory on the SD-Card. A model can be updated (or a new one added) by uploading the new file and activating it on the configuration page or in the config file `/config/config.ini`.

In order to incorporate new digits a training set of images is required. The training images needs to be collected in the final setup with the help of the `Digits` or `Analog` log settings (not to be confused with the `Data` or `Debug` log). Enable the logging of the images on the configuration page or in the config file `/config/config.ini`:

![](img/enable_log_image.jpg)

Now be patient! You have to wait until it has collected an image of each digit of every type. They wil lbe placed on the SD-Card inthe folder `/log/digit/` resp. `/log/anaolog/`. The fastest way to get the images to your PC is to remove the SD-card from the ESP32 module and insert it into the card reader of yur PC.
Then search for two..three images of each digit (**not more! :-)**). We provide programs which will sort out duplicate images for you, see below.

## Collecting images for dig-class100/dig-cont/ana-class100
For digits, [Collectmeterdigits](https://github.com/haverland/collectmeterdigits) resp for pointers [collectmeteranalog](https://github.com/haverland/collectmeteranalog) can be sused to collect the images easily. Read the project readme for detailed instructions.

## Train the model by yourself (optional)
For training the model you will need a python and Jupyter installation.
**This is optional and only suggested if you want to get into it deeper yourself!**

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

If you not able to create a pull request or don't know what it is, open an [issue](https://github.com/jomjol/AI-on-the-edge-device/issues) and put the zipped images in it.

### Images can be rejected if
* As same as dig-class11 collected, more than 1000 images of your device are really to much. 
* images are not good configured (ROIs) will be rejected. It reduces the accuracy of the networks.
* Images with too little focus will be rejected. 
* Images with too much blur are rejected.

Our models are to small to recognize everything in any quality. So we use only images of medium or good quality.
