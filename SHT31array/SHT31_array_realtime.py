#!/usr/bin/env python3.7
import Adafruit_GPIO
from Adafruit_SHT31 import SHT31
import Adafruit_GPIO.I2C as I2C
import time
import sys
import argparse


argparser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description="Generate data stream from SHT31 sensor array")
argparser.add_argument('-n', help="Amount of SHT31 sensors", type=int, default=8)
argparser.add_argument('-dt', help="datatype (0 : temp,1 : hum) ", type=int, default=0)
argparser.add_argument('-s', help="waiting time", type=float, default=0.010)

args = argparser.parse_args()
if args.dt not in [0,1]:
    raise ValueError("-dt has to be either 0 or 1")

sht = SHT31() # Handle to all sensors in the array!

TCA9548A = I2C.get_i2c_device(0x70)

N_SHTs = args.n # Amount of SHT sensors
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
    time.sleep(args.s)
    return [read_sht(i)   for i in range(N_SHTs)]

while True:
    print('\t'.join(  [ str(d[args.dt])  for d in read_all_temperature_humidity(sht, TCA9548A, N_SHTs)]  ))
    sys.stdout.flush()
