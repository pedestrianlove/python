from machine import Pin, I2C
from ssd1306 import SSD1305_I2C
from hcsr04 import HCSR04
import utime

# init oled display
i2c = I2C (scl = Pin (5), sda = Pin (4))
oled = SSD1306_I2C (128, 64, i2c)

#init sonar
sonar = HCSR04 (trigger_pin = 14, echo_pin = 12)


#detect distance in action
while True:
	distance = sonar.distance_cm ()
	
	# show distance on oled
	oled.fill (0)
	oled.text ("Distance: ", 0, 0)
	oled.text (str (distance) + " cm", 0, 16)
	oledoled.show ()

	# show distance on console
	print ("Distance: " + str (distance) + " cm")

	# wait 25ms
	utime.sleep_ms (25)
