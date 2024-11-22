#!/usr/bin/env python
# coding: utf-8

# In[1]:


import logging
import qcodes as qc
import numpy as np
from time import sleep

# Matplot plots
import matplotlib.pyplot as plt
import matplotlib

from qcodes.utils.dataset.doNd import plot as doNd_plot
from qcodes.logger import start_all_logging

# qcodes imports 
from qcodes.dataset import (
    LinSweep,
    Measurement,
    dond,
    experiments,
    initialise_or_create_database_at,
    load_by_run_spec,
    load_or_create_experiment,
    plot_dataset,
    plot_by_id, 
    do1d
)

from barreralabdrivers.utils.param_utils import paramp

from cappy.balancer import Balancer
from cappy.config import testconfig, qc_dbpath

# Live plotting with Plottr
import IPython.lib.backgroundjobs as bg
from plottr.apps import inspectr

import keyboard


# In[2]:


# Qcodes logger
# log = logging.getLogger("balance_logger")
# from qcodes.logger import start_all_logging
# # qc.logger.setLevel(logging.DEBUG)
# log.setLevel(logging.DEBUG)
# start_all_logging()


# In[3]:


# Global Constants
LIVE_PLOT = False
SAVE_DATA = True
EXP_NAME = "sweep_tests"
SAMPLE_NAME = "dry"
INT_TIME = 2    # lockin integration time

## Balancing arguements
FREQ = 50000
DELTA = (150, 150)
INITIAL = (10, 10)
Cstand = 10  # nF
DRIVE = 300


# In[ ]:


qc.Instrument.close_all()
station = qc.Station(config_file=str(testconfig))

dac = station.load_instrument("acdac")
li = station.load_instrument("lockin")
yoko = station.load_instrument("yoko")
keithley = station.load_instrument("keithley")

# station.close_all_registered_instruments()
# dac.display_mode('REMOTE')


# In[5]:


# parameter definitions 
vdd = yoko.channel1.voltage
vdd.label = "vdd"

vg = yoko.channel2.voltage
vg.label = "vg" 

idd = yoko.channel1.current
ig = yoko.channel2.current
vds = keithley.amplitude
vds.label="vds"


# In[6]:


vg.instrument.output(0)


# In[7]:


# Setup qcodes database
initialise_or_create_database_at(qc_dbpath)

# Initialize Experiment
balance_exp = load_or_create_experiment(
    experiment_name=EXP_NAME,
    sample_name=SAMPLE_NAME
)


# # Run Experiment

# In[8]:


START = 0 
STOP = -0.7
SAMPLES = 20
INT_TIME = 0.5


def setup():
    dac.frequency(10000)

    dac.ch4.voltage(400)
    dac.ch3.voltage(300)
    dac.display_mode("REMOTE")

    vdd(0.1)
    dac.ch1.voltage(100)
    dac.ch2.voltage(0)

    vg.instrument.output(1)
    vdd.instrument.output(1)

def teardown():
    paramp(vg)
    paramp(vdd)
    vg.instrument.output(0)
    vdd.instrument.output(0) 


# In[9]:


# # run measurement
matplotlib.rcParams['font.family'] = 'DejaVu Sans'  # Default fallback font in Matplotlib

dep_params = [vds, li.R, li.P]
if LIVE_PLOT:
    jobs = bg.BackgroundJobManager()
    jobs.new(inspectr.main, qc_dbpath)
    


# In[ ]:


do1d(vg, START, STOP, SAMPLES, INT_TIME, *dep_params, write_period=0.1, do_plot=not LIVE_PLOT, enter_actions=[setup], exit_actions=[teardown], exp=balance_exp, show_progress=True)


# In[ ]:


# ramp(dac.ch2.voltage)
dac.display_mode("NORMAL")


# In[11]:


dac.ch3.voltage(10)
teardown()


# In[8]:


station.close_all_registered_instruments()
# station.close_and_remove_instrument("acdac")


# ## TODO
# 
# - [ ] Quantum Designs Cryostatat 6000, Magnetic Field and Temperature params
# - [ ] Matplotlib font warnings: clear cache using `rm ~/.cache/matplotlib -rf `
# - [ ] Yokogs20 driver: functionality to read current while in voltage source mode and vv 
# - [ ] Use dond or measureme instead of annoying measurement object setup  
# - [ ] wsl bash version 1 
