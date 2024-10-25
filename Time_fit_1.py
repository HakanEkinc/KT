import numpy as np
from math import sqrt
import matplotlib
import scipy.optimize

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



#Read the file

def read_spe_file(file_path):
    """
    :param file_path: path to the SPE file
    :return: array of counts
    """
    counts = []
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file.readlines()[12:]):
            counts.append(float(line.strip()))
            if line_num == 16383:  # Stop reading at line 16396
                break
    return counts


dataset = read_spe_file("Measurements/Time_calibration_4ns_spacing.Spe")



#define a gaussian for the fit
def gaussian(x,amplitude, mean, std_dev):
            return amplitude * np.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))




#plot the dataset
'''
plt.plot(dataset)
plt.xlabel('Time')
plt.ylabel('Counts')
#plt.show()
'''



#curvefit the first gaussian in dataset from position 950 to 1000
x = np.arange(910, 930)
y = dataset[910:930]


params,cov  = scipy.optimize.curve_fit(gaussian, x, y, p0=[2000,917 ,1.5])

fitted_amplitude, fitted_mean, fitted_std_dev = params

x_fit = np.linspace(910, 930, 100)
y_fitted = gaussian(x_fit,*params)
#plot the gaussian isolated

plt.plot(x, y, 'b.', label='Data')  # Plot the original data as points
plt.plot(x_fit, y_fitted, 'r-', label='Fitted Gaussian')
plt.axvline(fitted_mean, color='k', linestyle='--', label='Mean')

nonzeroes = np.nonzero(dataset)
print(nonzeroes)
#plt.show()


