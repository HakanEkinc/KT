from functions import *

dataset = read_spe_file("measurements/time_calibration_4ns_spacing.Spe")


#plot the dataset

#plot the dataset
plt.plot(dataset)
plt.title("Time calibration raw dataset spacing 4ns ")
plt.xlabel('Bin position (a.u.)')
plt.ylabel('Counts')
plt.xlim(500, 2000)
plt.savefig("plots/time_calibration_dataset_4ns_spacing.pdf")
plt.close()
#plt.show()



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

x3, y3, x_fit3, y_fitted3, fitted_amplitude3, fitted_mean3, fitted_std_dev3 = fit_gaussian(dataset, 1290, 1303)

x4, y4, x_fit4, y_fitted4, fitted_amplitude4, fitted_mean4, fitted_std_dev4 = fit_gaussian(dataset, 1477, 1490)

x5,y5,x_fit5,y_fitted5,fitted_amplitude5,fitted_mean5,fitted_std_dev5 = fit_gaussian(dataset, 1674, 1686)

#plot each gaussian isolated and save the plot

plot_function(x1, y1, x_fit1, y_fitted1, fitted_mean1, "plots/time_calibration_16ns_Gaussian.pdf","16 ")
plot_function(x2, y2, x_fit2, y_fitted2, fitted_mean2, "plots/time_calibration_20ns_Gaussian.pdf","20")
plot_function(x3, y3, x_fit3, y_fitted3, fitted_mean3, "plots/time_calibration_24ns_Gaussian.pdf","24")
plot_function(x4, y4, x_fit4, y_fitted4, fitted_mean4, "plots/time_calibration_28ns_Gaussian.pdf","28")
plot_function(x5, y5, x_fit5, y_fitted5, fitted_mean5, "plots/time_calibration_32ns_Gaussian.pdf","32")


#now we do a linear plot of the means of the gaussians vs the time

time =[16, 20, 24, 28, 32] #in nanoseconds

means = [fitted_mean1, fitted_mean2, fitted_mean3, fitted_mean4, fitted_mean5]

slope, intercept = linear_fit( means,time)

linear_plot(means, time, slope, intercept,"4","plots/time_calibration_means_vs_time_4ns_spacing.pdf")
print(means)
print(slope, intercept)


