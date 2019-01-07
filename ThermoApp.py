#/usr/bin/python
import os
import glob
import RPi.GPIO as GPIO
import time

#global variables for settings
SET_TEMP = 68.0
SET_MODE = 'OFF'
CUR_TEMP = 0

#DS18b20 sensor initiate
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#Relay Switch Initiate
GPIO.setmode(GPIO.BCM)
pinList = [2, 3, 4, 17]
for i in pinList:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)

#Main temperature reading loop
def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.0
		global CUR_TEMP
		CUR_TEMP = round(temp_f, 1)

def RunThermoApp():
	while True:
		try:
			read_temp()
			time.sleep(1)
		except KeyboardInterrupt:
			print("Quit")
			GPIO.cleanup()

#Setting and Retrieve Set Temp and thermo mode
def SetTargetTemp(target_temp = None):
	global SET_TEMP
	if target_temp == None:
		return SET_TEMP
	else:
		SET_TEMP = float(target_temp)

def SetThermoMode(thermo_mode = None):
	global SET_MODE
	if thermo_mode == None:
		return SET_MODE
	else:
		SET_MODE = thermo_mode

from datetime import datetime
def get_time():
	return(datetime.now().strftime("%b %d, %Y %I:%M:%S %p"))

def get_cur_temp():
    global CUR_TEMP
    return CUR_TEMP

#Main logic to control switch bases off of temperature
def RelayControl():
	global SET_MODE, SET_TEMP, CUR_TEMP
	if SET_MODE == "hot":
		try:
			GPIO.output(3, GPIO.HIGH)
			GPIO.output(4, GPIO.HIGH)
		except:
			pass
		if SET_TEMP <= CUR_TEMP:
			if GPIO.input(2) == 1:
				pass
			else:
				GPIO.output(2, GPIO.HIGH)
				GPIO.output(4, GPIO.HIGH)
		else:
			GPIO.output(2, GPIO.LOW)
			GPIO.output(4, GPIO.LOW)
	elif SET_MODE == "cold":
		try:
			GPIO.output(2, GPIO.HIGH)
			GPIO.output(4, GPIO.HIGH)
		except:
			pass
		if SET_TEMP >= CUR_TEMP:
			if GPIO.input(3) == 1:
				pass
			else:
				GPIO.output(3, GPIO.HIGH)
				GPIO.output(4, GPIO.HIGH)
		else:
			GPIO.output(3, GPIO.LOW)
			GPIO.output(4, GPIO.LOW)
	else:
		GPIO.output(2, GPIO.HIGH)
		GPIO.output(3, GPIO.HIGH)
		GPIO.output(4, GPIO.HIGH)
	#print(CUR_TEMP)
	time.sleep(1)
	exit()
	RelayControl()
