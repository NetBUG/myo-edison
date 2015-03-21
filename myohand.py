# SOURCE: https://github.com/emutex/wiring-x86/blob/master/examples/analog_input.py
# Import the time module enable sleeps between turning the led on and off.
import time

# Import the GPIOEdison class from the wiringx86 module.
from wiringx86 import GPIOEdison as GPIO

# Create a new instance of the GPIOEdison class.
# Setting debug=True gives information about the interaction with sysfs.
gpio = GPIO(debug=False)
pin = 13
analogpin = 14

print 'Setting up all pins...'

# Set pin 14 to be used as an analog input GPIO pin.
gpio.pinMode(analogpin, gpio.ANALOG_INPUT)

# Set pin 13 to be used as an output GPIO pin.
gpio.pinMode(pin, gpio.OUTPUT)

print 'Analog reading from pin %d now...' % analogpin
try:
    while(True):
        # Read the voltage on pin 14
        value = gpio.analogRead(analogpin)

        # Turn ON pin 13
        gpio.digitalWrite(pin, gpio.HIGH)

        # Sleep for a while depending on the voltage we just read. The higher
        # the voltage the more we sleep.
        time.sleep(value / 1023.0)

        # Turn OFF pin 13
        gpio.digitalWrite(pin, gpio.LOW)

        # Sleep for a while depending on the voltage we just read. The higher
        # the voltage the more we sleep.
        time.sleep(value / 1023.0)

# When you get tired of seeing the led blinking kill the loop with Ctrl-C.
except KeyboardInterrupt:
    # Leave the led turned off.
    print '\nCleaning up...'
    gpio.digitalWrite(pin, gpio.LOW)

    # Do a general cleanup. Calling this function is not mandatory.
    gpio.cleanup()