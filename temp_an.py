#!/usr/nim/python3

import spidev
import time
import os

#open spi bus
spi= spidev.SpiDev()
spi.open(0,0)

#function that will the adc value from the selected channel
def readchannel(channel):
    adc= spi.xfer2([1,(8+channel)<<4,0])
    data= ((adc[1]&3<<8)+adc[2])
    return data
           
#function that will covert voltage levels
def ConvertVolts(data, places):
    volts= data*(3.3/256)
    volts= round(volts,places)
    return volts

#to calaculate temperature
def ConvertTemp(data,places):
    temp= ((data*330)/1023)
    return temp

#while True:
for num in range(0,1):
    #pot_levels= readchannel(0)
    #pot_volts= ConvertVolts(pot_levels,2)
    read=int(input("What channel are you using ?  "))
    if read>-1:
        if read<8:
            temp_level= readchannel(read)
            temp_volts= ConvertVolts(temp_level,2)
            temper= ConvertTemp(temp_level,2)
        #print("------------------------------------------------------------")
        #print("Potentometer: {}".format(pot_volts))
        #print(" value:{}".format(readchannel(0)))
            print("------------------------------------------------------------")
            print("temperature: {}".format(temper))
        #print(" value:{}".format(readchannel(1)))
   
        time.sleep(5)
    else:
        print("try again")
        time.sleep(5)
