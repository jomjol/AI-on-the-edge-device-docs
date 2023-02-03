# Welcome

Welcome to the AI-on-the-edge-device project!

This is the documentation. For the source code, please head to [github.com/jomjol/AI-on-the-edge-device](https://github.com/jomjol/AI-on-the-edge-device).

Artificial intelligence based systems have been established in our everyday lives. Just think of speech or image recognition. Most of the systems rely on either powerful processors or a direct connection to the cloud for doing the calculations up there. With the increasing power of modern processors the AI systems are coming closer to the end user - which is usually called **edge computing**.
Here this edge computing is brought into a practice-oriented example, where a AI network is implemented on a ESP32 device so: **AI on the edge**.

## Key features
- Tensorflow Lite (TFlite) integration - including easy to use wrapper
- Inline image processing (feature detection, alignment, ROI extraction)
- **Small** and **cheap** device (3x4.5x2 cm³, < 10 EUR)
- Camera and illumination integrated
- Web surface to administrate and control
- OTA-Interface to update directly through the web interface
- Full integration into Home Assistant
- Support for Influx DB 1
- MQTT
- REST API

## Idea

![Idea](img/idea.jpg){: style="width:600px"}


### Hardware

![](img/watermeter_all.jpg){: style="width:200px"}
![](img/main.jpg){: style="width:200px"}
![](img/size.png){: style="width:200px"}


### Web interface

![](img/watermeter.jpg){: style="width:600px"}

### Configuration Interface

![](img/edit_reference.jpg){: style="width:600px"}


**Have fun in studying the new possibilities and ideas**

This is about image recognition and digitalization, done totally on a cheap ESP32 board using artificial intelligence in form of convolutional neural networks (CNN). Everything, from image capture (OV2640), image preprocessing (auto alignment, ROI identification) all the way down to the image recognition (CNN structure) and result plausibility is done on a cheap 10 EUR device.

This all is integrated in an easy to do setup and use environment, taking care for all the background processing and handling, including regular job scheduler. The user interface is an integrated web server, that can be easily adjusted and offers the data as an API in different options.

The task to be demonstrated here is an automated readout of an analog water meter. The water consumption is to be recorded within a house automatization and the water meter is totally analog without any electronic interface. Therefore, the task is solved by regularly taking an image of the water meter and digitizing the reading.

There are two types of CNN implemented, a classification network for reading the digital numbers and a single output network for digitalize the analog pointers for the sub digit readings.

This project is an evolution of the [water-meter-system-complete](https://github.com/jomjol/water-meter-system-complete), which uses ESP32-CAM just for taking the image and a 1GB-Docker image to run the neural network's backbone. Here everything is integrated in an ESP32-CAM module with 8MB of RAM and a SD card as data storage.
