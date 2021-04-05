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

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Path to mne-study-template 
mnest_path = '/Users/guiomar/Documents/GitHub/mne-bids-pipeline'


# Populate mne_config.py file with brainlife config.json
# - load inputs from config.json
#with open(__location__+'/config.json') as config_json:
#    config = json.load(config_json)

#bids_root = str(config['fif'])


# Run mne-study-template python script
os.system( mnest_path + '/run.py --config=' + __location__+'/mne_config.py \
    --steps=preprocessing,sensor,report')
