"""
General config.py file for MNE Study Template
"""

study_name=''
bids_root = None
deriv_root
subjects_dir
interactive = False
crop = None
sessions = 'all'
task: str = ''
runs = 'all'
acq = None
proc = None
rec = None
space = None
subjects = 'all'
exclude_subjects = []
process_er = False
ch_types = []
data_type = None
eog_channels = None
eeg_bipolar_channels = None
eeg_reference = 'average'
eeg_template_montage = None
drop_channels = []
analyze_channels = 'all'

# MAXWELL FILTER PARAMETERS
# -------------------------
# for 01-import_and_maxfilter.py

find_flat_channels_meg = False
find_noisy_channels_meg = False
use_maxwell_filter = False
mf_st_duration = None
mf_head_origin = 'auto'
mf_reference_run = None

# STIMULATION ARTIFACT
# --------------------
# for 01-import_and_maxfilter.py

fix_stim_artifact = False
stim_artifact_tmin = 0.
stim_artifact_tmax: float = 0.01

# FREQUENCY FILTERING AND RESAMPLING
# ----------------------------------
# for 02-frequency_filter.py

l_freq = None
h_freq = 40.
resample_sfreq = None
decim = 1

# AUTOMATIC REJECTION OF ARTIFACTS
# --------------------------------

reject = {'grad': 4000e-13, 'mag': 4e-12, 'eeg': 150e-6}
reject_tmin = None
reject_tmax = None

# RENAME EXPERIMENTAL EVENTS
# --------------------------

rename_events = dict()
on_rename_missing_events = 'raise'

# EPOCHING
# --------

conditions = ['left', 'right']
tmin = -0.2
tmax = 0.5
baseline = (None, 0)
contrasts = []

# ARTIFACT REMOVAL
# ----------------
use_ssp = True
use_ica = False
ica_algorithm = 'picard'
ica_l_freq = 1.
ica_max_iterations = 200
ica_n_components = 0.8
ica_decim = None
ica_ctps_ecg_threshold = 0.1

# DECODING
# --------
decode = True
decoding_metric = 'roc_auc'
decoding_n_splits = 5
n_boot = 5000

# GROUP AVERAGE SENSORS
# ---------------------
interpolate_bads_grand_average = True

# TIME-FREQUENCY
# --------------
time_frequency_conditions = []

# SOURCE ESTIMATION PARAMETERS
# ----------------------------
bem_mri_images = 'auto'
recreate_bem = False
spacing = 'oct6'
mindist = 5
# loose = 0.2
# depth = 0.8
inverse_method = 'dSPM'
noise_cov = (None, 0)

# ADVANCED
# --------
l_trans_bandwidth = 'auto'
h_trans_bandwidth = 'auto'
N_JOBS = 1
random_state = 42
shortest_event = 1
allow_maxshield = False
log_level = 'info'
mne_log_level = 'error'
on_error = 'abort'