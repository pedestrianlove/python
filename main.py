from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# init I2C protocol
i2c = I2C (scl = Pin (5), sda = Pin (4))

# init OLED display, and direct to i2c
oled = SSD1306_I2C (128, 64, i2c)


# show text
oled.text ("The Lord", 0, 0)
oled.text ("is my shepherd,", 0, 20)
oled.text ("I shall not want.", 0, 40)
oled.show ()
