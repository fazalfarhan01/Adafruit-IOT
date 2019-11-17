import time
import requests as r
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pins = [3,5,7,11]
gas_pin = 40
servo_door_pin = 29
servo_windows1 = 31
servo_windows2 = 33
for i in pins:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, 1)
GPIO.setup(servo_door_pin,GPIO.OUT)
GPIO.setup(servo_windows1,GPIO.OUT)
GPIO.setup(servo_windows2,GPIO.OUT)
GPIO.output(servo_door_pin,0)
GPIO.output(servo_windows1,0)
GPIO.output(servo_windows2,0)
GPIO.setup(gas_pin,GPIO.IN)
servo_door = GPIO.PWM(servo_door_pin,50)
servo_win1 = GPIO.PWM(servo_windows1,50)
servo_win2 = GPIO.PWM(servo_windows2,50)
servo_door.start(2.5)
servo_win1.start(2.5)
servo_win2.start(2.5)
"""servo_door.start(2.6)
time.sleep(.5)
servo_door.ChangeDutyCycle(12.6)
time.sleep(.5)
servo_door.ChangeDutyCycle(2.6)"""
print("Pin Setup Done!")

from Adafruit_IO import Client

def ServoSetAngle (type,angle):
	if type == "door":
		servo_door.ChangeDutyCycle(angle)
	if type == "windows":
		print("Servo1")
		servo_win1.ChangeDutyCycle(angle)
		print("Servo2")
		servo_win2.ChangeDutyCycle(angle)



def gas_leak():
	gas = GPIO.input(gas_pin)
	if gas == 0:
		print("Gas Leakage\n")
		response = r.get(URL)
		print("opening all windows......!")
		ServoSetAngle("windows",12.5)
		aio.send_data(one.key, "OFF")
		aio.send_data(two.key, "OFF")
		aio.send_data(three.key, "OFF")
		aio.send_data(four.key, "OFF")
		for i in pins:
			GPIO.output(i, 1)
		print("Everything OFF")
		#aio.send_data(one.key, "OFF")
		


UserId = "farhanf1"
ApiKey = "fbdeb00ffbd747cea31dabfa326261ad"
print("Service Started")
URL = "https://maker.ifttt.com/trigger/GasLeakage/with/key/fF4qlToV-EsuTm-nC9lQno2ZHcZeTCjBEv78wxq9YVi"

aio = Client(UserId, ApiKey)
try:
	print("Initialising Feeds, please wait..!!")
	one = aio.feeds('one')
	print("Connected to One")
	two = aio.feeds('two')
	print("Connected to Two")
	three = aio.feeds('three')
	print("Connected to Three")
	four = aio.feeds('four')
	print("Connected to Four")
	door = aio.feeds("door")
	print("Connected to Door")
	time.sleep(.5)
	print("Connected to all Feeds Successfully!\n")
	i=1
except:
	print("Error Occured..!!")
	exit()

try:
	while 1:
		gas_leak()							#GAS_LEAK
		data5 = aio.receive(door.key)
		print(str(data5.value))
		if str(data5.value) == "CLOSE":
			ServoSetAngle('door',7.5)
		else:
			ServoSetAngle('door',2.6)
		gas_leak()							#GAS_LEAK
		data1 = aio.receive(one.key)
		gas_leak()							#GAS_LEAK
		if str(data1.value) == "OFF":
			print("One is OFF")
			GPIO.output(3,1)
		elif str(data1.value) == "ON":
			print("One is ON")
			GPIO.output(3,0)
		data2 = aio.receive(two.key)
		gas_leak()							#GAS_LEAK
		if str(data2.value) == "OFF":
			print("Two is OFF")
			GPIO.output(5,1)
		elif str(data2.value) == "ON":
			print("Two is ON")
			GPIO.output(5,0)
		data3 = aio.receive(three.key)
		gas_leak()							#GAS_LEAK
		if str(data3.value) == "OFF":
			print("Three is OFF")
			GPIO.output(7,1)
		elif str(data3.value) == "ON":
			print("Three is ON")
			GPIO.output(7,0)
		data4 = aio.receive(four.key)
		gas_leak()							#GAS_LEAK
		if str(data4.value) == "OFF":
			print("Four is OFF")
			GPIO.output(11,1)
		elif str(data4.value) == "ON":
			print("Four is ON")
			GPIO.output(11,0)
		
		print(str(i) + " times ran\n")
		i+=1
except KeyboardInterrupt:
	print("exiting.........")
	servo_door.stop()
	servo_win1.stop()
	servo_win2.stop()
	exit()
time.sleep(.2)

