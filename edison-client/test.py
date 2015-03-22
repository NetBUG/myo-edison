from wiringx86 import GPIOEdison as GPIO
import time
gpio = GPIO(debug=False)
gpio.setPWMPeriod(3, 20000000)
gpio.pinMode(3, gpio.PWM)
while 1:
	gpio.analogWrite(3, 6)
	time.sleep(1023.0)
	gpio.analogWrite(3, 15)
	time.sleep(1023.0)
