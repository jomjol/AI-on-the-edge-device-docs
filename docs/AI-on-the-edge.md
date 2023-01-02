# Welcome to the AI-on-the-edge-device wiki!

Artifical inteligence based systems have been established in our every days live. Just think of speech or image recognition. Most of the systems relay on either powerfull processors or a direct connection to the cloud for doing the calculations up there. With the increasing power of modern processors the AI systems are coming closer to the end user - which is usally called **edge compution**.
Here this edge computing is brough into a practical example, where a AI network is implemented on a ESP32 device so: **AI on the edge**.

**Have fun in studying the new posibilities and ideas**

This is about image recognition and digitalization, done totally on a cheap ESP32 board using artifical intelligence in form of convolutional neural networks (CNN). Everything, from image capture (OV2640), image preprocessing (auto alignment, ROI idenficiation) all the way down to the image recognition (CNN structure) and result plausiblisation is done on a cheap 10 EUR device.

This all is integrated in an easy to do setup and use environment, taking care for all the background processing and handling, including regular job scheduler. The user interface is an integrated web server, that can be easily adjusted an offers the data as an API in different options.

The task to be demonstrated here is an automated readout of an analog water meter. The water consumption is to be recorded within a house automatization and the water meter is totally analog without any electronic interface. Therefore the task is solved by taking regularly an image of the water meter and digitize the reading.

There are two types of CNN implemented, a classification network for reading the digital numbers and a single output network for digitize the analog pointers for the sub digit readings.

This project is a evolution of the [water-meter-system-complete](https://github.com/jomjol/water-meter-system-complete), which uses ESP32-CAM just for taking the image and a 1GB-Docker image to run the neural networks backbone. Here everything is integrated in an ESP32-CAM module with 4MB of SDRAM and a SD-Card as data storage.



This systems implements several functions: 

* (water) meter readout - it can handle also dual meters with two or even more readings
* picture provider
* fileserver
* OTA functionality
* web server

The details can be found here: [[Integrated Functions]]

