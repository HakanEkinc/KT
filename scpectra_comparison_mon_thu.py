import matplotlib.pyplot as plt

from functions import *


data = read_spe_file("measurements/leftside_spectra.Spe")
data2=read_spe_file("measurements/leftside_spectra_Thursday.Spe")

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)
x_vals = x_vals[90:8000]
y_vals = y_vals[90:8000]


x_vals2 = np.arange(0, len(data2), 1)
y_vals2 = np.array(data2)
x_vals2 = x_vals2[90:8000]
y_vals2 = y_vals2[90:8000]



# plot the whole spectru
plt.plot(x_vals, y_vals, label='Total spectrum Monday')
plt.plot(x_vals2, y_vals2, label='Total spectrum Thursday')



# reduce the plotting height to 14400
plt.ylim(0, 1400)

plt.legend()
#plt.show()