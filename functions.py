from cProfile import label

import numpy as np
import matplotlib
import scipy.optimize

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Read the file
def read_spe_file(file_path):
    """
    Read an SPE file and return the counts as an array
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




#define a gaussian for the fit
def gaussian(x,amplitude, mean, std_dev):
    """
    Gaussian function
    :param x:
    :param amplitude:
    :param mean:
    :param std_dev:
    :return: gauss function of x
    """
    return amplitude * np.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))


#define function to fit a given interval of the dataset
def fit_gaussian(dataset, start, end):
    x = np.arange(start, end)
    y = dataset[start:end]
    params, cov = scipy.optimize.curve_fit(gaussian, x, y, p0=[5000,(start+end)/2,1.5])
    fitted_amplitude, fitted_mean, fitted_std_dev = params
    x_fit = np.linspace(start, end, 100)
    y_fitted = gaussian(x_fit, *params)
    return x, y, x_fit, y_fitted, fitted_amplitude, fitted_mean, fitted_std_dev



#plot the function
def plot_function(x, y, x_fit, y_fitted, fitted_mean, filename, time):
    plt.plot(x_fit, y_fitted, 'r', label='Fitted Gaussian')
    plt.plot(x, y, 'b.', label='Data points')  # Plot the original data as points
    plt.axvline(fitted_mean, color='k', linestyle='--', label='Mean')
    plt.xlabel('Bin position')
    plt.title("Gaussian fit for time intervall "+time+"ns")
    plt.ylabel('Counts')
    plt.legend()
    plt.savefig(filename)
    plt.close()

#
def linear_fit(x, y):
    slope, intercept = np.polyfit(x, y, 1)
    return slope, intercept

def linear_plot(x, y, slope, intercept,spacing):
    plt.plot(x, [slope * t + intercept for t in x], 'r--', label="Linear fit")
    plt.plot(x, y, 'b.',label="mean values of time calibration")
    plt.xlabel('Mean values of time calibration)')
    plt.ylabel('time (ns)')
    plt.title("Time calibration means vs time with " +spacing+"ns spacing")
    plt.legend()
    plt.savefig("plots/time_calibration_means_vs_time.pdf")
    plt.close()

