"""
Perform bandpass filtering.
"""
import argparse
import mne
import numpy as np
from scipy.signal import butter, filtfilt
from matplotlib import pyplot as plt

# All parameters are defined in config.py
from config import fname, fmin, fmax, sample_rate

# Handle command line arguments
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('subject', metavar='sub###', help='The subject to process')
args = parser.parse_args()
subject = args.subject
print('Processing subject:', subject)

# Load the data, filter it and save the result
data = np.loadtxt(fname.input(subject=subject))
b, a = butter(4, [fmin / (sample_rate / 2), fmax / (sample_rate / 2)], btype='band')
data = filtfilt(b, a, data)
np.savetxt(fname.output(subject=subject), data)

# Add a plot of the data to the HTML report
with mne.open_report(fname.report(subject=subject)) as report:
    fig = plt.figure()
    plt.plot(data.T)
    report.add_figs_to_section(fig, 'Filtered data', section='filtering',
                               replace=True)
    report.save(fname.report_html(subject=subject), overwrite=True,
                open_browser=False)
