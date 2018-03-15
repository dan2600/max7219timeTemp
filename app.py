# -*- coding: utf-8 -*-
import internetWeather
import re
import time
import argparse
import lTrainTimes
from datetime import datetime, timedelta
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
print("Created device")
device.contrast(1)
theWeather = internetWeather.getWeather()
weatherExpires = datetime.now() + timedelta(minutes=5)
mtaExpires = datetime.now() + timedelta(seconds=30)
nextTrain = "loading"
def showMsg():
    global loops, theTime, theWeather, weatherExpires, mtaExpires, nextTrain
    if weatherExpires - datetime.now() < timedelta(seconds=0):
        theWeather = internetWeather.getWeather()
        weatherExpires = datetime.now() + timedelta(minutes=5)
    if mtaExpires - datetime.now() < timedelta(seconds=0):
        lookup = lTrainTimes.lookupTime()
        if lookup == "Error":
        	print("train update Error")
                mtaExpires = datetime.now()          
        else:
        	nextTrain = lookup
                mtaExpires = datetime.now() + timedelta(seconds=30)
    msg = theWeather[0].text()+" "+theWeather[0].temp()+"F "+nextTrain
    show_message(device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.035)
while True:
    showMsg()
