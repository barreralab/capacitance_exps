from cappy.config import DATA_PATH
from sweep.sweep_load import pload1d
from time import strftime, localtime
import numpy as np
from cappy.opener import Opener

# Path to your TSV.gz file
file_path = DATA_PATH

for idx in (37, 38):
    opened = Opener(file_path, idx)
    data = opened.getdata()
    opened.plotcfg(xscale="log")
    opened.plot(data, ["acdac_frequency", "lockin1_R", "lockin1_P"], save=True)

opened = Opener(file_path, 48)
data = opened.getdata()
keys = ["acdac_frequency", "capacitance", "conductance"]
opened.plotcfg(xscale="log")
opened.plot(data, keys, save=True)

for idx in (57, 59):
    opened = Opener(file_path, idx)
    data = opened.getdata()
    if idx == 57:
        data["balancing_scale"] = data["balancing_scale"] * 70
    if idx == 59:
        data["balancing_scale"] = data["balancing_scale"] * 7
    opened.plotcfg()
    opened.plot(data, keys=["balancing_scale", "capacitance", "conductance"], save=True)

opened = Opener(file_path, 28)
data = opened.getdata()
print(data["capacitance"])
