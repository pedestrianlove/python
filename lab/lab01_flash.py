from machine import Pin
import time

# define led pin
led = Pin (2, Pin.OUT)

# flash the light
led.value (0)
time.sleep (2)
led.value (1)

