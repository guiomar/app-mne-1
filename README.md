# MNE-BIDS-Pipeline: MEEG preprocessing

This Brainlife App imports and preprocess MEG (and EEG) files using MNE-BIDS-Pipeline.
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

Tadel F, Baillet S, Mosher JC, Pantazis D, Leahy RM (2011)
**Brainstorm: A User-Friendly Application for MEG/EEG Analysis**
Computational Intelligence and Neuroscience. https://doi.org/10.1155/2011/879716

Tadel F, Bock E, Niso G, Mosher JC, Cousineau M, Pantazis D, Leahy RM, Baillet S
**MEG/EEG Group Analysis With Brainstorm**
Frontiers in Neuroscience, 13, 76. https://doi.org/10.3389/fnins.2019.00076

Niso G, Tadel F, Bock E, Cousineau M, Santos A, Baillet S
**Brainstorm Pipeline Analysis of Resting-State Data from the Open MEG Archive**
Frontiers in Neuroscience, 13, 284. https://doi.org/10.3389/fnins.2019.00284

Test app for Brainlife to read MEEG files using MNE

