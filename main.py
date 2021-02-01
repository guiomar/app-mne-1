# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# set up environment
#import sys
import json
import numpy as np
import mne
from matplotlib import pyplot as plt

# load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Load into variables predefined code inputs
data_file = str(config['fif'])

#data_file=(sys.argv[1])

# Read meg .fif file
raw = mne.io.read_raw_fif(data_file)

# Print info
f=open('out_dir/output.txt', 'w')
print(raw.info, file=f)
f.close()

# Plot psd
raw.plot_psd(fmax=50)
plt.savefig('out_dir/psd.png')
plt.close('all')