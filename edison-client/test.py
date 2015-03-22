from wiringx86 import GPIOEdison as GPIO
import time
gpio = GPIO(debug=False)
time.sleep(2)
gpio.setPWMPeriod(3, 20000000)
gpio.pinMode(3, gpio.PWM)
time.sleep(1)
while 1:
	print "Cycle..."
	gpio.analogWrite(3, 6)
	time.sleep(1.5)
	gpio.analogWrite(3, 15)
	time.sleep(1.5)
