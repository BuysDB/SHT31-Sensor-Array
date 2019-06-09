from setuptools import setup
setup(
	name='sht31array',
	version='0.01',
	author='Buys de Barbanson',
	author_email='code@buysdb.nl',
	description='Sample from multiple sht31 sensors in real time',
	url='https://github.com/BuysDB/SHT31-Sensor-Array',
	py_modules=['SHT31_array'],
	scripts=['SHT31_array_realtime.py'],
	install_requires=['numpy']
)
