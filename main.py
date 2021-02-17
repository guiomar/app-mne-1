# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# Required libraries
# pip install mne-bids coloredlogs tqdm pandas scikit-learn json_tricks fire

# set up environment
#import mne-study-template
import os
import json


# Path to mne-study-template 
mypath = '/Users/guiomar/Documents/GitHub/mne-study-template'
# Path to config file (eventually this should be extracted from brainlife config.json)
mneconfigpath = '/Users/guiomar/Documents/GitHub/app-mne-1/mne_config.py'

# Populate mne_config.py file with brainlife config.json
# - load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

#data_file = str(config['fif'])


# Run mne-study-template python script
os.system( mypath + '/run.py --config=' + mneconfigpath + '\
    --steps=preprocessing,sensor,report')
