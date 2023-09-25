# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:09:23 2023

@author: atrij
"""

import h5py

# Open the HDF5 file in read mode
with h5py.File("C:\\Users\\atrij\OneDrive\Desktop\DeepLearning\ECG\data\data\ecg_tracings.hdf5", 'r') as file:
    # Get the list of object names in the HDF5 file
    object_names = list(file.keys())

print("Object names in the HDF5 file:", object_names)
