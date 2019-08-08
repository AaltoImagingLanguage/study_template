"""
Compute grand average across all subjects
"""
import numpy as np

# All parameters are defined in config.py
from config import fname, subjects

# Load the data, compute grand average and save the result
data = []
for subject in subjects:
    data.append(np.loadtxt(fname.output(subject=subject)))
grand_average = np.mean(data, axis=0)
np.savetxt(fname.grand_average, grand_average)
