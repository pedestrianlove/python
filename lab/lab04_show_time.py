from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

# init I2C protocol
i2c = I2C (scl = Pin (5), sda = Pin (4))

# init OLED display, and direct to i2c
oled = SSD1306_I2C (128, 64, i2c)


# display text
while True:
	system_time = utime.ticks_ms ()

	oled.fill (0)
	oled.text ("System time: ", 0, 0)
	oled.text (str (system_time), 0, 16)
	oled.show ()

	utime.sleep_ms (100)
