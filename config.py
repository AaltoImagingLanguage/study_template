"""
===========
Config file
===========

Configuration parameters for the study.
"""

import getpass
import os
from socket import getfqdn

from filename_templates import FileNames

###############################################################################
# Determine which user is running the scripts on which machine and set the path
# where the data is stored and how many CPU cores to use.

user = getpass.getuser()  # Username of the user running the scripts
host = getfqdn()  # Hostname of the machine running the scripts

# You want to add your machine to this list.
if user == "vanvliet":
    # My laptop
    raw_data_dir = "./data"
    n_jobs = 14  # My laptop has 14 cores
elif host == "deepthought1" and user == "vanvlm1":
    # My workstation
    raw_data_dir = "./data"
    n_jobs = 32  # My workstation has 32 cores
else:
    raise ValueError(f"Please add your system to config.py ({user=} {host=}).")

# For numpy to use the right amount of cores
os.environ["OMP_NUM_THREADS"] = str(n_jobs)


###############################################################################
# These are all the relevant parameters for the analysis.

sample_rate = 1000  # Hz
fmin = 1.0  # Hz
fmax = 20.0  # Hz

# All subjects
subjects = ["sub01", "sub02"]

###############################################################################
# Templates for filenames
#
# This part of the config file uses the FileNames class. It provides a small
# wrapper around string.format() to keep track of a list of filenames.
# See fnames.py for details on how this class works.
fname = FileNames()

# Some directories
fname.add("raw_data_dir", raw_data_dir)
fname.add("processed_data_dir", "{raw_data_dir}/processed", mkdir=True)
fname.add("figures_dir", "./figures", mkdir=True)

# The data files that are used and produced by the analysis steps
fname.add("input", "{raw_data_dir}/input-{subject}.txt")
fname.add("output", "{processed_data_dir}/output-{subject}.txt", mkdir=True)
fname.add("grand_average", "{processed_data_dir}/grand_average.txt", mkdir=True)

# The figures
fname.add("figure1", "{figures_dir}/figure1.pdf", mkdir=True)
fname.add("figure_grand_average", "{figures_dir}/figure_grand_average.pdf", mkdir=True)

# Filenames for MNE reports
fname.add("reports_dir", "./reports/", mkdir=True)
fname.add("report", "{reports_dir}/{subject}-report.h5", mkdir=True)
fname.add("report_html", "{reports_dir}/{subject}-report.html", mkdir=True)

# File produced by check_system.py
fname.add("system_check", "./system_check.txt")
