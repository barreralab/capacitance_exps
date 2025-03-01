"""
    configuration file 
"""

from pathlib import Path
import os

root = Path(
    r"C:/Users/barreralab/OneDrive - University of Toronto/Documents/capacitance_exps"
)

measurement_ids = {}

datamainpath = root / "Data"
datapath = datamainpath / "data"
data2path = datamainpath / "data2"
data4path = datamainpath / "data4term"
qc_dbpath = datapath / "qc.db"
mm_dpath = datapath / "mm"

testconfig = (
    root / "src" / "cappy" / "station_configs" / "insts.yml"
)  # insts.yml is the config file which has all our addresses


# Qcodes station yaml config paths
coolconfig = root / "src" / "cappy" / "station_configs" / "ppms_exps.yml"
dualhemtconfig = root / "src" / "cappy" / "station_configs" / "dual_hemt.yml"

term4config = root / "src" / "cappy" / "station_configs" / "4term.yml"


def save_measurement_id(idx: int, description: str):
    if idx in measurement_ids:
        raise IndexError(f"ID {idx} already stored")
