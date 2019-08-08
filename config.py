"""
===========
Config file
===========

Configuration parameters for the study.
"""

import os
from socket import getfqdn
from fnames import FileNames

###############################################################################
# Determine which user is running the scripts on which machine and set the path
# where the data is stored and how many CPU cores to use.

user = os.environ['USER']  # Username of the user running the scripts
host = getfqdn()  # Hostname of the machine running the scripts

# You want to add your machine to this list
if user == 'vanvliet':
    # My laptop
    raw_data_dir = './data'
    n_jobs = 4  # My laptop has 4 cores
elif host == 'nbe-024.org.aalto.fi' and user == 'vanvlm1':
    # My workstation
    raw_data_dir = './data'
    n_jobs = 8  # My workstation has 8 cores
else:
    raise RuntimeError('Please edit config.py and set the raw_data_dir '
                       'variable to point to the location where the data '
                       'should be stored and the n_jobs variable to the '
                       'number of CPU cores the analysis is allowed to use.')

# For BLAS to use the right amount of cores
os.environ['OMP_NUM_THREADS'] = str(n_jobs)


###############################################################################
# These are all the relevant parameters for the analysis.

sample_rate = 1000  # Hz
fmin = 1.0  # Hz
fmax = 20.0  # Hz

# All subjects
subjects = ['sub01', 'sub02']

###############################################################################
# Templates for filenames
#
# This part of the config file uses the FileNames class. It provides a small
# wrapper around string.format() to keep track of a list of filenames.
# See fnames.py for details on how this class works.
fname = FileNames()

# Some directories
fname.add('raw_data_dir', raw_data_dir)
fname.add('processed_data_dir', './processed')
fname.add('figures_dir', './figures')

# The data files that are used and produced by the analysis steps
fname.add('input', '{raw_data_dir}/input-{subject}.txt')
fname.add('output', '{processed_data_dir}/output-{subject}.txt')
fname.add('grand_average', '{processed_data_dir}/grand_average.txt')

# The figures
fname.add('figure1', '{figures_dir}/figure1.pdf')
fname.add('figure_grand_average', '{figures_dir}/figure_grand_average.pdf')

# Filenames for MNE reports
fname.add('reports_dir', './reports/')
fname.add('report', '{reports_dir}/{subject}-report.h5')
fname.add('report_html', '{reports_dir}/{subject}-report.html')

# File produced by check_system.py
fname.add('system_check', './system_check.txt')
