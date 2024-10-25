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




#define a gaussian for the fit
def gaussian(x,amplitude, mean, std_dev):
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




def plot_function(x, y, x_fit, y_fitted, fitted_mean, filename):
    plt.plot(x, y, 'b.', label='Data')  # Plot the original data as points
    plt.plot(x_fit, y_fitted, 'r', label='Fitted Gaussian')
    plt.axvline(fitted_mean, color='k', linestyle='--', label='Mean')
    plt.savefig(filename)
    plt.close()



dataset = read_spe_file("Measurements/Time_calibration_4ns_spacing.Spe")


#plot the dataset

'''plt.plot(dataset)
plt.xlabel('Time')
plt.ylabel('Counts')
plt.show()
'''



#curvefit the first gaussian in dataset from position 950 to 1000
'''
x = np.arange(910, 930)
y = dataset[910:930]
'''


'''
nonzeroes = np.nonzero(dataset)
print(nonzeroes)
'''


#fit all the  gaussians in the dataset
x1, y1, x_fit1, y_fitted1, fitted_amplitude1, fitted_mean1, fitted_std_dev1 = fit_gaussian(dataset, 910, 925)

x2, y2, x_fit2, y_fitted2, fitted_amplitude2, fitted_mean2, fitted_std_dev2 = fit_gaussian(dataset, 1095, 1109)

x3, y3, x_fit3, y_fitted3, fitted_amplitude3, fitted_mean3, fitted_std_dev3 = fit_gaussian(dataset, 1290, 1306)

x4, y4, x_fit4, y_fitted4, fitted_amplitude4, fitted_mean4, fitted_std_dev4 = fit_gaussian(dataset, 1475, 1490)

x5,y5,x_fit5,y_fitted5,fitted_amplitude5,fitted_mean5,fitted_std_dev5 = fit_gaussian(dataset, 1670, 1686)

#plot each gaussian isolated and save the plot

plot_function(x1, y1, x_fit1, y_fitted1, fitted_mean1, "Time_calibration_8ns_Gaussian1.pdf")
plot_function(x2, y2, x_fit2, y_fitted2, fitted_mean2, "Time_calibration_8ns_Gaussian2.pdf")
plot_function(x3, y3, x_fit3, y_fitted3, fitted_mean3, "Time_calibration_8ns_Gaussian3.pdf")
plot_function(x4, y4, x_fit4, y_fitted4, fitted_mean4, "Time_calibration_8ns_Gaussian4.pdf")
plot_function(x5, y5, x_fit5, y_fitted5, fitted_mean5, "Time_calibration_8ns_Gaussian5.pdf")
