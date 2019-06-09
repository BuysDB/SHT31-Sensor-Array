#!/usr/bin/env python3.7
import Adafruit_GPIO
from Adafruit_SHT31 import SHT31
import Adafruit_GPIO.I2C as I2C
import matplotlib.pyplot as plt
import time

class SHT31_Array():

    def __init__(self, TCA9548A_address=0x70, N_SHTs = 8 ):
        self.sht = SHT31() # Handle to all sensors in the array!
        self.TCA9548A = I2C.get_i2c_device(TCA9548A_address)
        self.N_SHTs = N_SHTs
        gpio = Adafruit_GPIO.get_platform_gpio() #? is this neccessary?

    def select_sht(self, sht_index):
        self.TCA9548A.write8(0, 1<<sht_index)

    def read_sht(self, sht_index):
        self.select_sht(sht_index)
        return self.sht.read_temperature_humidity()

    def read_all_temperature_humidity(self):
        for i in range(self.N_SHTs):
            self.select_sht(i)
            self.sht.request_readout()
        time.sleep(0.015) # This could be lower @todo
        return [self.read_sht(i)   for i in range(self.N_SHTs)]

#while True:
#    print( read_all_temperature_humidity(sht, TCA9548A, N_SHTs) )


if __name__=='main':
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
