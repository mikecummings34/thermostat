# thermostat
This is a simple, light-weight application for a home thermostat. This is a good starting point if you want to quickly get your own thermostat up and running. The point of this project was to keep it SIMPLE, LIGHT_WEIGHT and RESPONSIVE. All of the base functionality is in place. Including multiprocessing to allow the server and thermostat to function simultansously and a minimalistic and stylish web application so you can control the temperature from your computer or mobile device.

## Requirements
Hardware:
1. Rasberry-Pi (Zero-W is reccomended)
2. DS18b20 Thermometer
3. 4 port digital relay switch(number of channels and voltage requirements depends on your home HVAC system).

Software:
1. any linux distro(Debian is recommended and the latest version)
2. Add support for thermometer- this is a good tutorial: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20
3. And of course the thermostat repo.

## Installation
1. Connect the appropriate I/O headers from the RPi to the thermometer and the relay switch board(I will leave the details out since there are plenty of guides online to achieve this)
2. Follow the tutorial to initiate the DS1820b thermometer
3. copy and paste thermostat repo into a new directory in /home/pi/directory-name
4. From a new terminal, cd into the current working directory and type "python3 directory-name/app.py
5. You should now be able to pull up the web app and test the relay switches. You should also see the current temperature displayed on the screen.


  
