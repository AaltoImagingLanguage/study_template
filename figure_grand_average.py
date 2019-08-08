"""
Plot the grand average
"""
import numpy as np
from matplotlib import pyplot as plt
from config import fname, sample_rate

data = np.loadtxt(fname.grand_average)
times = np.arange(data.shape[1]) / sample_rate
plt.figure()
plt.plot(times, data.T)
plt.title('Grand average')
plt.savefig(fname.figure_grand_average)
