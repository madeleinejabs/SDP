import pandas
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sps

# Read in Excel data and extract as lists
filename = 'fakepressuredata.xlsx' # Put name of excel file here
data = pandas.read_excel(filename)
time = np.array(data.Time)
pressure = np.array(data.Pressure)

# Determine peaks or local maximums
peaks = sps.find_peaks(pressure)[0]
peak_times = time[peaks]
peak_pressures = pressure[peaks]

# Scatter plot data
plt.title('Peak Pressures')
plt.xlabel('Time (s)')
plt.ylabel('Pressure (psi)')
plt.scatter(time, pressure)
plt.scatter(peak_times, peak_pressures, marker='X', s=100)
plt.show()