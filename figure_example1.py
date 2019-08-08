"""
Create the first figure in the manuscript.
"""
from matplotlib import pyplot as plt
from config import fname

plt.figure()
plt.plot([1, 2, 3, 4])
plt.title('Figure 1')
plt.savefig(fname.figure1)
