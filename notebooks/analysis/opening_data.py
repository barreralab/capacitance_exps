from cappy.config import datapath
import numpy as np

# Path to your TSV.gz file
file_path = datapath / "24" / "data.tsv.gz"
data = np.transpose(np.loadtxt(file_path))
Vout_lockin = data[4]
print(np.argmax(Vout_lockin))
Vg = data[1]
print(Vg[93])
