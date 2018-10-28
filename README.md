# Robofriend

Robofriend - a semi-autonomous, remotely controllable robot companion.

Robofriend - initially created by Tom Heike 2002 - was exhibited at several Roboexotica events, serving drinks at the Vienniese Cocktail Robot Festival.
In 2014, two Robofriends were donated by Tom to us, and were further developed by Dr. Wummi and Karima Khlousy-Neirukh and other students at UAS Technikum Wien, in order to make Robofriend a playful companion robot which can be evaluated together with kids with special needs in selected schools in Vienna.
For this purpose, several game applications were developed which involve robot movements and expressions.


## Features
* live video transmission (low latency, < 300ms)
* remote control via webbrowser or game apps
* proximity sensors for collision avoidance & activity detection
* facial expressions, sound/voice playback, illuminated ears
* RFID reader - utilized for game interaction
* unique design (with CRT-head) by Tom Heike

## System Architecture / Components

The Robofriend uses a Teensy++ 2.0 microcontroller to handle motor control, led lights, servos, proximity sensors and battery status...
The Teensy is connected to the RaspberryPi via USB (/dev/ttyACM0). The RaspberryPi communicates with the Teensy via a simple protocol (ASCII-commands).
The RaspberryPi handles most of the robot's functions such as: RFID reader, CRT monitor, video camera, LED ears, speech output, ...

## User Interface and Control Options

The RaspberryPi starts a webserver which provides a webpage with live video feed and control interface.
It can be reached via http://<ip-adress-of-raspberry>:8765

The webpage uses an API to control the robots functions - this API is described in the theses of Karima Khlousy Neirukh (folder /documentation).
Furthermore, dedicated games have been developed by Karima which utilize the RFID-reader so that kids can use physical objects to interact with the robo and play litte games (identify animal sounds, emotions etc.)
These game applications are also written in python and are usually launched on a seperated tablet computer. The tablet connect to the python main script via a UDP connection (port 9000) and uses the same commands as the web GUI. It is planned to use a REST API for both (webpage and tablet GUI).

## Requirements

To get the existing *Python2* code compatible for *Python3* following packages should be installed:
*  mjpg-streamer: [MJPEG-Streamer Install & Setup](https://github.com/cncjs/cncjs/wiki/Setup-Guide:-Raspberry-Pi-%7C-MJPEG-Streamer-Install-&-Setup-&-FFMpeg-Recording)
* speech engine:
  * pip install pyttsx3
  * (pip install pyttsx --user)
  * sudo apt-get update && sudo apt-get install espeak
* pygame: python3 -m pip install -U pygame --user
* serial: pip install pyserial --user
* flask: pip install flask
* yaml: pip3 install pyyaml --user

**OpenCV 3:**
* to install OpenCV 3 on a Raspberry Pi 3 follow the following tutorial (except the virtual environment part):
[OpenCV 3 on Raspberry Pi 3](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/)

**Roboter Operating System (ROS):**
* to install ROS on a Rasberry Pi 3 follow the following tutorial:
[ROS on Raspberry PI 3](https://www.intorobotics.com/how-to-install-ros-kinetic-on-raspberry-pi-3-running-raspbian-stretch-lite/)

* following ROS-packages should also be installed:
    * sudo apt-get install python-rospkg
    * (pip3 install rospkg --user)

* *additional information:*
    * in case of a frozen screen at the installation part: **"sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/kinetic -j2"**
         try **"-j1"** instead of **"-j2"**
    * add the ROS workspace to your .bashrc file through the following command: *echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc*

## StartUp

Startup scripts are provided in folder /src/Pi/scripts

## Future Plans

As next steps, several high-levels skills for Robofriend are planned:
* indoor localisation using IR / BLE-beacons (in order to find charging station)
* speech interaction (mic-array, beamforming, DOA, hotword detection)
* image analysis of live camera feed (face detection, facial landmark classification)
