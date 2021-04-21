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
from shutil import copyfile

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



bids_root = str(config['output']) 
deriv_root = 'out_dir'

subjects = ['0001']
runs = ['01']

# Bad channels
find_flat_channels_meg = bool(config['find_flat_channels_meg'])
find_noisy_channels_meg = bool(config['find_noisy_channels_meg'])

# MAXFLTER (for fif)
use_maxwell_filter = bool(config['use_maxwell_filter'])
if config['mf_st_duration']:    mf_st_duration = float(config['mf_st_duration'])
if config['mf_head_origin']:    mf_head_origin = str(config['mf_head_origin']) 
if config['mf_reference_run']:  mf_reference_run = str(config['mf_reference_run']) 
if config['mf_cal_fname']:      mf_cal_fname = str(config['mf_cal_fname']) ##
if config['mf_ctc_fname']:      mf_ctc_fname = str(config['mf_ctc_fname']) ##

# STIMULATION ARTIFACT  
fix_stim_artifact = bool(config['fix_stim_artifact'])
if config['stim_artifact_tmin']:  stim_artifact_tmin = float(config['stim_artifact_tmax'])
if config['stim_artifact_tmax']:  stim_artifact_tmax = float(config['stim_artifact_tmax'])

# FILTER
if config['l_freq']:            l_freq = float(config['l_freq'])
if config['h_freq']:            h_freq = float(config['h_freq'])
 
# RESAMPLING
if config['resample_sfreq']:    resample_sfreq = float(config['resample_sfreq'])
if config['decim']:             decim = int(config['decim'])

# AUTOMATIC REJECTION OF ARTIFACTS
if config['reject']:            reject = dict(config['reject']) 
if config['reject_tmin']:       reject_tmin = float(config['reject_tmin'])
if config['reject_tmax']:       reject_tmax = float(config['reject_tmax'])

# RENAME EXPERIMENTAL EVENTS
if config['rename_events']:             rename_events = dict(config['rename_events']) 
if config['on_rename_missing_events']:  on_rename_missing_events = Literal(config['on_rename_missing_events']) 
if config['event_repeated']:            event_repeated = Literal(config['event_repeated']) 

# EPOCHING



'''
#study_name = 'ds000246'
bids_root = str(config['output']) # '/Users/guiomar/Projects/ds000246'
deriv_root = 'out_dir'

l_freq = .3
h_freq = 100.
decim = 10 #4
reject = dict(mag=4e-12, eog=250e-6)

'''


conditions = ['standard', 'deviant', 'button']
contrasts = [('deviant', 'standard')]
decode = True
daysback = -365 * 110
on_error = 'debug'


ch_types = ['meg']


'''

#study_name = 'ds000248'
subjects = ['01']
rename_events = {'Smiley': 'Emoji','Button': 'Switch'}
conditions = ['Auditory', 'Visual', 'Auditory/Left', 'Auditory/Right']
contrasts = [('Visual', 'Auditory'),('Auditory/Right', 'Auditory/Left')]
ch_types = ['meg']
#mf_reference_run = '1' ##bl2bids just 1 not 01
find_flat_channels_meg = True
find_noisy_channels_meg = True
use_maxwell_filter = True
process_er = True
#noise_cov = 'emptyroom'

bem_mri_images = 'FLASH'
recreate_bem = True

#reject = dict(mag=4e-12, eog=250e-6)
'''

# Create new MNE config .py file

fname = 'mne_config1.py'

with open(fname, 'w') as f: 


    f.write("bids_root = '{}'".format(bids_root)+'\n')
    f.write("deriv_root = '{}'".format(deriv_root)+'\n')
    f.write('subjects = {}'.format(subjects)+'\n')
    f.write('runs = {}'.format(runs)+'\n')

    # Bad channels
    f.write('find_flat_channels_meg = {}'.format(find_flat_channels_meg)+'\n')
    f.write('find_noisy_channels_meg = {}'.format(find_noisy_channels_meg)+'\n')
    
    # MAXFLTER (for fif)
    f.write('use_maxwell_filter = {}'.format(use_maxwell_filter)+'\n')
    if config['mf_st_duration']:    f.write('mf_st_duration = {}'.format(mf_st_duration)+'\n')
    if config['mf_head_origin']:    f.write('mf_head_origin = {}'.format(mf_head_origin)+'\n')
    if config['mf_reference_run']:  f.write('mf_reference_run = {}'.format(mf_reference_run)+'\n')
    if config['mf_cal_fname']:      f.write('mf_cal_fname = {}'.format(mf_cal_fname)+'\n')
    if config['mf_ctc_fname']:      f.write('mf_ctc_fname = {}'.format(mf_ctc_fname)+'\n')
    
    # STIMULATION ARTIFACT    
    f.write('fix_stim_artifact = {}'.format(fix_stim_artifact)+'\n')
    if config['stim_artifact_tmin']:  f.write('stim_artifact_tmin = {}'.format(stim_artifact_tmin)+'\n')
    if config['stim_artifact_tmax']:  f.write('stim_artifact_tmax = {}'.format(stim_artifact_tmax)+'\n')
    
    # FILTER
    if config['l_freq']:    f.write('l_freq = {}'.format(l_freq)+'\n')
    if config['h_freq']:    f.write('h_freq = {}'.format(h_freq)+'\n')

    # RESAMPLING
    if config['resample_sfreq']:    f.write('resample_sfreq = {}'.format(resample_sfreq)+'\n')
    if config['decim']:             f.write('decim = {}'.format(decim)+'\n')   

    # AUTOMATIC REJECTION OF ARTIFACTS
    if config['reject']:            f.write('reject = {}'.format(reject)+'\n') 
    if config['reject_tmin']:       f.write('reject_tmin = {}'.format(reject_tmin)+'\n')
    if config['reject_tmax']:       f.write('reject = {}'.format(reject_tmax)+'\n')

    # RENAME EXPERIMENTAL EVENTS
    if config['rename_events']:             f.write('reject = {}'.format(reject)+'\n')
    if config['on_rename_missing_events']:  f.write('reject = {}'.format(reject)+'\n')
    if config['event_repeated']:           f.write('reject = {}'.format(reject)+'\n')



    f.write('ch_types = {}'.format(ch_types)+'\n')
    f.write('reject = {}'.format(reject)+'\n')
    f.write('conditions = {}'.format(conditions)+'\n')
    f.write('contrasts = {}'.format(contrasts)+'\n')
    f.write('decode = {}'.format(decode)+'\n')
 
    f.close()

# Run mne-study-template python script
os.system( mnest_path + '/run.py --config=' + __location__+'/mne_config1.py \
    --steps=preprocessing,sensor,report')


# Find the reports and make a copy in out_html folder
for file in os.listdir("/out_dir"):
    if file.endswith(".html"):
        copyfile(os.path.join("/out_dir", file), os.path.join("/html_report", file))