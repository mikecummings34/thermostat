# WiFi Raspberry Pi Thermostat
This is a project to convert your standard button-and-switch thermostat into something worthy of the 21st century without breaking the bank.  Utilizing a cheap Raspberry Pi 0 W and keeping the application simple and light you can create an easy to use and responsive IoT device.  The Thermostat consists of two main applications. One is the thermostat itself which will sample the temperature and then send digital outputs to the pins attached to the relay switch. The other part is the web application that will give you a GUI to control your thermostat via the local wifi network.

## Requirements
Hardware:
1. Rasberry-Pi (Zero-W is recomended)
2. DS18b20 Thermometer
3. 4 port digital relay switch(Note-number of channels and voltage requirements depends on your home HVAC system).
4. A Wifi enabled network
4. 5 inch touch screen display compatible with the Pi(not required)

Software:
1. Linux distro of your choosing(Latest version is recomended).
2. Thermometer drivers- this is a good tutorial: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20
3. And of course the Wifi Raspberry Pi Thermostat repo.

## Installation
### Hardware Setup
1. Connect the appropriate I/O headers from the RPi to the thermometer and the relay switch board
  Thermostat(This should be in the linked tutorial above)
  Switch: Connect ground(GND) from I/O header on Pi to ground(GND) on switch. 
  Connect 5v header pin to the Vin on the switch. 
  Then connect each digital pin from the switch to one of the digital I/O pins on the Pi header. Keep track of the GPIO pin number.
2. If you havent already, follow the tutorial link above to initiate the DS1820b thermometer.
3. copy and paste thermostat repo into a new directory in /home/pi/create-and-name-new-directory.
4. Open up thermoapp.py and under the GPIO variables, change each GPIO pin number to corrospond to each channel on the relay switch with the I/O pins you are using on the Pi.
5. From a new terminal console, cd into the current working directory and type `python3 directory-name/app.py`
6. You should now be able to pull up the web app and test the relay switches. You should also see the current temperature displayed on the screen.

### Auto-Start on System Boot
If you are running Debian distro, you can edit the rc.local file to allow the python script to start when the computer is turned on.
1. Open a new terminal
2. navigate to /etc/ and type:
3. `sudo nano rc.local`
4. next add the line
5. `sudo ../home/pi/dir-name/app.py`
6. save the file and you are good to go.

# Disclaimer
This is not meant to be used as a real thermostat. It is meant to be a mach thermostat.  Please understand that HVAC systems can utilize deadly high voltage so do not tinker, work or play around with any part of the HVAC system- You do not get a second chance. Other than that, have fun creating! 


  
