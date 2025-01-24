"""
    configuration file 
"""

from pathlib import Path

root = Path(
    "C:/Users/barreralab/OneDrive - University of Toronto/Documents/capacitance_exps"
)

measurement_ids = {}

datapath = root / "data"
qc_dbpath = datapath / "qc.db"
mm_dpath = datapath / "mm"

testconfig = (
    root / "src" / "cappy" / "station_configs" / "insts.yml"
)  # insts.yml is the config file which has all our addresses

coolconfig = root / "src" / "cappy" / "station_configs" / "ppms_exps.yml"


def save_measurement_id(idx: int, description: str):
    if idx in measurement_ids:
        raise IndexError(f"ID {idx} already stored")
