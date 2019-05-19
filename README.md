# SHT31 Array

Get 8 temperature and humidity measurements per second from 8 SHT31 sensors.

### Prerequisites

The prerequisites are Python 3.6 or higher, my fork of [Adafruit_Python_SHT31](https://github.com/BuysDB/Adafruit_Python_SHT31) and numpy

### Installation
```

pip3 install https://github.com/BuysDB/Adafruit_Python_SHT31/archive/master.zip https://github.com/BuysDB/SHT31-Sensor-Array/archive/master.zip
```
### Example usage:
Generate stream of humidity values and plot using feedgnuplot:
```
python3.7 SHT31_array_realtime.py -dt 1 -n 8 -s 0 | feedgnuplot --lines --stream 0.01 --xlen 50
```
