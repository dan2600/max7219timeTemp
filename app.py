# -*- coding: utf-8 -*-

import internetTime
import internetWeather
import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
print("Created device")

def showMsg():
    msg = theTime.strftime("%b %d %y %H:%M:%S")+" Current condition: "+theWeather[0].text()+"Current Temp "+theWeather[0].temp()+"° F"
    print(msg)
    show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.1)



theTime = internetTime.getDateTime()
theWeather = internetWeather.getWeather()
showMsg();

