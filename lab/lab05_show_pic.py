from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf


# init oled display
i2c = I2C (scl = Pin (5), sda = Pin (4))
oled = SSD1306_I2C (128, 64, i2c)

# init pixel list
pixel_list = [0x1e, 0x3f, 0x7e, 0xfc, 0x3f, 0x1e, 0x00]

# init buffer
pic_buffer = bytearray (pixel_list)
pic = framebuf.FrameBuffer (pic_buffer, 8, 8, framebuf.MONO_VLSB)

# show display
oled.text ("I", 8, 8)
oled.blit (pic, 20, 8)
oled.text ("JESUS", 32, 8)
oled.rect (4, 4, 80, 16, 1)
oled.show ()
