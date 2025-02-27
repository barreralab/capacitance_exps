"""
    configuration file 
"""

from pathlib import Path
import os


# TODO use os library to make this device agnostic
root = Path(
    "C:/Users/barreralab/OneDrive - University of Toronto/Documents/capacitance_exps"
)

measurement_ids = {}

datapath = root / "data"
data2path = root / "data2"
data4path = root / "data4term"
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
