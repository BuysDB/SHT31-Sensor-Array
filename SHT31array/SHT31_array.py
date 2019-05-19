#!/usr/bin/env python3.7
import Adafruit_GPIO
from Adafruit_SHT31 import SHT31
import Adafruit_GPIO.I2C as I2C
import matplotlib.pyplot as plt


import time
sht = SHT31() # Handle to all sensors in the array!

TCA9548A = I2C.get_i2c_device(0x70)

N_SHTs = 8 # Amount of SHT sensors
gpio = Adafruit_GPIO.get_platform_gpio()

def select_sht(sht_index):
    TCA9548A.write8(0, 1<<sht_index)

def read_sht(sht_index):
    select_sht(sht_index)
    return sht.read_temperature_humidity()

def read_all_temperature_humidity(sht, TCA9548A, N_SHTs):
    for i in range(N_SHTs):
        select_sht(i)
        sht.request_readout()
    time.sleep(0.015)
    return [read_sht(i)   for i in range(N_SHTs)]

#while True:
#    print( read_all_temperature_humidity(sht, TCA9548A, N_SHTs) )


if True:
    plt.ion()
    fig, ax = plt.subplots()
    fig.canvas.draw()
    plt.show(block=False)
    dots = ax.scatter(list(range(N_SHTs)), [0]*N_SHTs)
    d = dots.get_offsets()
    ax.set_ylim(30, 80)
    for q in range(10000):
        for i in range(N_SHTs):
            select_sht(i)
            sht.request_readout()
        #time.sleep(0.015)
        #fig.canvas.draw()
        #plt.pause(0.001)
        d[:,1] = [read_sht(i)[1]   for i in range(N_SHTs)]
        dots.set_offsets(d)
        #ax.set_ylim(d[:,1].mean()-2, d[:,1].mean()+2)
