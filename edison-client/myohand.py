# SOURCE: https://github.com/emutex/wiring-x86/blob/master/examples/analog_input.py
# Import the time module enable sleeps between turning the led on and off.
import time
# Import the GPIOEdison class from the wiringx86 module.
from wiringx86 import GPIOEdison as GPIO
import requests

# Create a new instance of the GPIOEdison class.
# Setting debug=True gives information about the interaction with sysfs.
gpio = GPIO(debug=False)
outpins = [9, 10]
analogpins = range(14, 17)
url_finger = "http://dev.studalt.ru/store.php?mode=r&id=finger"
url_sensor = "http://dev.studalt.ru/store.php?mode=w&id=sensor"

print 'Setting up all pins...'

# Set pin 14 to be used as an analog input GPIO pin.
for analogpin in analogpins:
    gpio.pinMode(analogpin, gpio.ANALOG_INPUT)

# Set pin 13 to be used as an output GPIO pin.
for pin in outpins:
    gpio.pinMode(pin, gpio.PWM)
    setPWMPeriod(pin, 20000000)

#print 'Analog reading from pin %d now...' % analogpin
try:
    while(True):
	data = []
	level = 12
	for analogpin in analogpins:
            data.append(gpio.analogRead(analogpin))
	l = requests.get(url_sensor + "&data=" + str(data))
	l = requests.get(url_finger + "&data=" + str(data))
	if l.status_code == 200:
	    level = int(l.text)

	for pin in outpins:
	    gpio.analogWrite(pin, level)
        time.sleep(1023.0)

# When you get tired of seeing the led blinking kill the loop with Ctrl-C.
except KeyboardInterrupt:
    # Leave the led turned off.
    print '\nCleaning up...'
    #gpio.digitalWrite(outpin, gpio.LOW)

    # Do a general cleanup. Calling this function is not mandatory.
    gpio.cleanup()