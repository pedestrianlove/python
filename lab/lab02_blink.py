from machine import Pin
import time

# define led pin location
led = Pin (2, Pin.OUT)

# flash the led repeatedly
while True:
	led.value (0)
	time.sleep (0.5)
	led.value (1)
	time.sleep (0.5)
