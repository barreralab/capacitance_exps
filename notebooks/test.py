import qcodes as qc
from cappy.config import testconfig

station = qc.Station(config_file=str(testconfig))

li = station.load_instrument("lockin")
y = station.load_instrument("yoko")
k = station.load_instrument("keithley")
