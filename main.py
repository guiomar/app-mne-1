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
#mnest_path = '/Users/guiomar/Documents/GitHub/mne-bids-pipeline'
mnest_path = '/mne-bids-pipeline'

# Populate mne_config.py file with brainlife config.json
# - load inputs from config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

'''
#study_name = 'ds000246'
bids_root = str(config['output']) # '/Users/guiomar/Projects/ds000246'
deriv_root = 'out_dir'
subjects = ['0001']
runs = ['01']
l_freq = .3
h_freq = 100.
decim = 10 #4
ch_types = ['meg']
reject = dict(mag=4e-12, eog=250e-6)
conditions = ['standard', 'deviant', 'button']
contrasts = [('deviant', 'standard')]
decode = True
##daysback = -365 * 110
on_error = 'debug'
'''

#study_name = 'ds000248'
bids_root = str(config['output']) # '/Users/guiomar/Projects/ds000246'
deriv_root = 'out_dir'
subjects = ['01']
rename_events = {'Smiley': 'Emoji','Button': 'Switch'}
conditions = ['Auditory', 'Visual', 'Auditory/Left', 'Auditory/Right']
contrasts = [('Visual', 'Auditory'),('Auditory/Right', 'Auditory/Left')]
ch_types = ['meg']
mf_reference_run = '01'
find_flat_channels_meg = True
find_noisy_channels_meg = True
use_maxwell_filter = True
process_er = True
#noise_cov = 'emptyroom'

bem_mri_images = 'FLASH'
recreate_bem = True

#reject = dict(mag=4e-12, eog=250e-6)


# Create new MNE config .py file

fname = 'mne_config1.py'

with open(fname, 'w') as f:
    #f.write('bids_root = '  + repr(bids_root)+'\n')
    '''
    f.write("bids_root = '{}'".format(bids_root)+'\n')
    f.write("deriv_root = '{}'".format(deriv_root)+'\n')
    f.write('subjects = {}'.format(subjects)+'\n')
    f.write('runs = {}'.format(runs)+'\n')
    f.write('l_freq = {}'.format(l_freq)+'\n')
    f.write('h_freq = {}'.format(h_freq)+'\n')
    f.write('decim = {}'.format(decim)+'\n')
    f.write('ch_types = {}'.format(ch_types)+'\n')
    f.write('reject = {}'.format(reject)+'\n')
    f.write('conditions = {}'.format(conditions)+'\n')
    f.write('contrasts = {}'.format(contrasts)+'\n')
    f.write('decode = {}'.format(decode)+'\n')
    '''

    f.write("bids_root = '{}'".format(bids_root)+'\n')
    f.write("deriv_root = '{}'".format(deriv_root)+'\n')
    f.write('subjects = {}'.format(subjects)+'\n')
    f.write('ch_types = {}'.format(ch_types)+'\n')
    f.write('rename_events = {}'.format(rename_events)+'\n')
    f.write('conditions = {}'.format(conditions)+'\n')
    f.write('contrasts = {}'.format(contrasts)+'\n')
    f.write('mf_reference_run = {}'.format(mf_reference_run)+'\n')
    f.write('find_flat_channels_meg = {}'.format(find_flat_channels_meg)+'\n')
    f.write('find_noisy_channels_meg = {}'.format(find_noisy_channels_meg)+'\n')
    f.write('use_maxwell_filter = {}'.format(use_maxwell_filter)+'\n')
    f.write('process_er = {}'.format(process_er)+'\n')

    f.close()

# Run mne-study-template python script
os.system( mnest_path + '/run.py --config=' + __location__+'/mne_config1.py \
    --steps=preprocessing,sensor,report')


# Find the reports and make a copy in out_html folder