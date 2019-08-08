"""
This script performs a series of checks on the system to see if everything is
ready to run the analysis pipeline.
"""

import os
import warnings

# Scientific stack message
stack_msg = ('Make sure the basic Python scientific stack (Numpy/Scipy/Matplotlib) is installed.'
             'We recommend using the Anaconda Python distribution for this: http://docs.continuum.io/anaconda/install')

# Check if dependencies are present
try:
    import numpy
except:
    raise ValueError('numpy is not installed. ' + stack_msg)

try:
    import scipy
except:
    raise ValueError('scipy is not installed. ' + stack_msg)

try:
    from matplotlib import pyplot
except:
    raise ValueError('matplotlib is not installed. ' + stack_msg)

try:
    import doit
except:
    raise ValueError('doit is not installed. Please run `pip install doit` to install it.')

try:
    import mne
    mne.sys_info()  # Prints some information about the system
except:
    raise ValueError('mne is not installed. Please run `pip install mne` to install it.')


# TODO: Add tests for any further packages your analys pipeline needs

# Check that the data is present on the system
from config import fname
if not os.path.exists(fname.raw_data_dir):
    raise ValueError('The `raw_data_dir` points to a directory that does not exist: ' + fname.raw_data_dir)

# Make sure the output directories exist
os.makedirs(fname.processed_data_dir, exist_ok=True)
os.makedirs(fname.figures_dir, exist_ok=True)
os.makedirs(fname.reports_dir, exist_ok=True)

with open(fname.system_check, 'w') as f:
    f.write('System check OK.')

print("\nAll seems to be in order.\nYou can now run the entire pipeline with: python -m doit")
