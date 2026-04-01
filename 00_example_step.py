"""Perform bandpass filtering."""

import argparse

import mne
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import butter, filtfilt

# All parameters are defined in config.py.
from config import fmax, fmin, fname, sample_rate

# Handle command line arguments.
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "subject", metavar="SUBJECT", help="The subject to process [sub01 or sub02]"
)
args = parser.parse_args()
subject = args.subject
print("Processing subject:", subject)

# Load the data, filter it and save the result.
data = np.loadtxt(fname.input(subject=subject))
b, a = butter(4, [fmin / (sample_rate / 2), fmax / (sample_rate / 2)], btype="band")
data = filtfilt(b, a, data)
np.savetxt(fname.output(subject=subject), data)

# Add a plot of the data to the HTML report.
with mne.open_report(fname.report(subject=subject)) as report:
    fig = plt.figure()
    plt.plot(data.T)
    report.add_figure(fig, title="Filtered data", section="filtering", replace=True)
    report.save(fname.report_html(subject=subject), overwrite=True, open_browser=False)
