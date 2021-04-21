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
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)


bids_root = str(config['output']) 
deriv_root = 'out_dir'

subjects = ['0001']
runs = ['01']

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
    f.write('find_flat_channels_meg = {}'.format(config['find_flat_channels_meg'])+'\n')
    f.write('find_noisy_channels_meg = {}'.format(config['find_noisy_channels_meg'])+'\n')
    
    # MAXFLTER (for fif)
    f.write('use_maxwell_filter = {}'.format(config['use_maxwell_filter'])+'\n')
    if config['mf_st_duration']:    f.write('mf_st_duration = {}'.format(config['mf_st_duration'])+'\n')
    if config['mf_head_origin']:    f.write('mf_head_origin = {}'.format(config['mf_st_dmf_head_originuration'])+'\n')
    if config['mf_reference_run']:  f.write('mf_reference_run = {}'.format(config['mf_reference_run'])+'\n')
    if config['mf_cal_fname']:      f.write('mf_cal_fname = {}'.format(config['mf_cal_fname'])+'\n')
    if config['mf_ctc_fname']:      f.write('mf_ctc_fname = {}'.format(config['mf_ctc_fname'])+'\n')
    
    # STIMULATION ARTIFACT    
    f.write('fix_stim_artifact = {}'.format(config['fix_stim_artifact'])+'\n')
    if config['stim_artifact_tmin']:  f.write('stim_artifact_tmin = {}'.format(config['stim_artifact_tmin'])+'\n')
    if config['stim_artifact_tmax']:  f.write('stim_artifact_tmax = {}'.format(config['stim_artifact_tmax'])+'\n')
    
    # FILTER
    if config['l_freq']:    f.write('l_freq = {}'.format(config['l_freq'])+'\n')
    if config['h_freq']:    f.write('h_freq = {}'.format(config['h_freq'])+'\n')

    # RESAMPLING
    if config['resample_sfreq']:    f.write('resample_sfreq = {}'.format(config['resample_sfreq'])+'\n')
    if config['decim']:             f.write('decim = {}'.format(config['decim'])+'\n')   

    # AUTOMATIC REJECTION OF ARTIFACTS
    if config['reject']:            f.write("reject = {}".format(config['reject'])+'\n') 
    if config['reject_tmin']:       f.write("reject_tmin = '{}'".format(config['reject_tmin'])+'\n')
    if config['reject_tmax']:       f.write("reject_tmax = '{}'".format(config['reject_tmax'])+'\n')

    # RENAME EXPERIMENTAL EVENTS
    if config['rename_events']:             f.write("rerename_eventsject = '{}'".format(config['rerename_eventsject'])+'\n')
    if config['on_rename_missing_events']:  f.write("on_rename_missing_events = '{}'".format(config['on_rename_missing_events'])+'\n')
    if config['event_repeated']:            f.write("event_repeated = '{}'".format(config['event_repeated'])+'\n')



    f.write('ch_types = {}'.format(ch_types)+'\n')
    f.write('conditions = {}'.format(conditions)+'\n')
    f.write('contrasts = {}'.format(contrasts)+'\n')
    f.write('decode = {}'.format(decode)+'\n')
 
    f.close()




# Run mne-study-template python script
os.system( mnest_path + '/run.py --config=' + __location__+'/mne_config1.py \
    --steps=preprocessing,sensor,report')


# Find the reports and make a copy in out_html folder
for dirpath, dirnames, filenames in os.walk(__location__+"/out_dir"):
    for filename in [f for f in filenames if f.endswith(".html")]:
        print(filename)
        copyfile(os.path.join(__location__,"out_dir", dirpath,filename), os.path.join(__location__,"html_report",filename))