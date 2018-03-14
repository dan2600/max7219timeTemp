# -*- coding: utf-8 -*-

import internetWeather
import re
import time
import argparse
import lTrainTimes
from datetime import datetime, timedelta

theWeather = internetWeather.getWeather()
weatherExpires = datetime.now() + timedelta(minutes=5)
mtaExpires = datetime.now() + timedelta(seconds=30)
nextTrain = lTrainTimes.lookupTime()


def showMsg():
    global loops, theTime, theWeather, weatherExpires, mtaExpires, nextTrain
    if weatherExpires - datetime.now() < timedelta(seconds=0):
        print("Updating Weather")
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
    print(msg)
    time.sleep(1)

while True:
    showMsg();

