from wiringx86 import GPIOEdison as GPIO
import time
gpio = GPIO(debug=False)
time.sleep(2)
gpio.setPWMPeriod(3, 20000000)
gpio.pinMode(3, gpio.PWM)
gpio.pinMode(14, gpio.ANALOG_INPUT)
gpio.pinMode(15, gpio.ANALOG_INPUT)
gpio.pinMode(16, gpio.ANALOG_INPUT)
time.sleep(1)
while 1:
	gpio.analogWrite(3, 6)
	time.sleep(3)
	gpio.analogWrite(3, 16)
	time.sleep(2)
	print "14: " + str(gpio.analogRead(14))
	print "15: " + str(gpio.analogRead(15))
	time.sleep(1)
