# MNE-BIDS-Pipeline: MEEG preprocessing

This Brainlife App imports and preprocess MEG (and EEG) files using MNE-BIDS-Pipeline (https://mne.tools/mne-bids-pipeline).
Input data should follow the Brain Imaging Data Structure (BIDS).

It allows to: 

 1) Import raw data (and apply Maxwell filter, for Elekta data). 
 1) Apply low- and high-pass filters. 
 1) Extract epochs. 
 1) Run spatial filters to detect and remove artifacts (e.g.eye blink and heart beat artifacts).
 1.1) Run Independant Component Analysis (ICA) for artifact correction. 
 1.1) Run Signal Subspace Projections (SSP) for artifact correction.
 1) Apply the stimated spatial filters (e.g. ICA, SSP) projections and obtain the cleaned epochs. 


## Authors
- Guiomar Niso (guiomar.niso@ctb.upm.es)

## Contributors
- Richard Höchenberger (richard.hochenberger@inria.fr)
- Aurore Bussalb (aurore.bussalb@icm-institute.org)
- Soichi Hayashi (hayashis@iu.edu)

## References

MEEG Pipeline
Jas M, Larson E, Engemann DA, Leppäkangas J, Taulu S, Hämäläinen M, Gramfort A
**A reproducible MEG/EEG group study with the MNE software: recommendations, quality assessments, and good practices**
Frontiers in neuroscience, 12, 2018. https://doi.org/10.3389/fnins.2018.00530

MNE-BIDS
Appelhoff S, Sanderson M, Brooks T, Vliet M, Quentin R, Holdgraf C, Chaumon M, Mikulan E, Tavabi K, Höchenberger R, Welke D, Brunner C, Rockhill A, Larson E, Gramfort A & Jas M. 
**MNE-BIDS: Organizing electrophysiological data into the BIDS format and facilitating their analysis** Journal of Open Source Software, 4:1896, 2019. https://doi.org/10.21105/joss.01896

MNE-Python package
Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Goj R, Jas M, Brooks T, Parkkonen L, and Hämäläinen MS. 
**MEG and EEG data analysis with MNE-Python**
Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

MNE inverse imaging implementations
Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Parkkonen L, and Hämäläinen MS. 
**MNE software for processing MEG and EEG data**
NeuroImage, 86:446–460, 2014. https://doi.org/10.1016/j.neuroimage.2013.10.027.


