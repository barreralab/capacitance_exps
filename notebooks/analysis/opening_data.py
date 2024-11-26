from cappy.config import datapath
from sweep.sweep_load import pload1d
from time import strftime, localtime
import numpy as np

# Path to your TSV.gz file
idx = 24
file_path = datapath / "test_archive"
data = pload1d(file_path, idx)
print(strftime("%Y-%m-%d %H:%M:%S", localtime(data["time"][0])))
