from functions import *

dataset = read_spe_file("measurements/time_calibration_8ns_spacing.Spe")


#plot the dataset
plt.plot(dataset)
plt.title("Time calibration raw dataset, spacing 8ns")
plt.xlabel('Bin position')
plt.ylabel('Counts')
plt.xlim(1500, 4000)
plt.savefig("plots/time_calibration_dataset_8ns_spacing.pdf")
plt.close()
#plt.show()

#curvefit the first gaussian in dataset from position 950 to 1000

'''
nonzeroes = np.nonzero(dataset)
print(nonzeroes)
'''


#fit all the  gaussians in the dataset
x1, y1, x_fit1, y_fitted1, fitted_amplitude1, fitted_mean1, fitted_std_dev1 = fit_gaussian(dataset, 2295, 2305)

x2, y2, x_fit2, y_fitted2, fitted_amplitude2, fitted_mean2, fitted_std_dev2 = fit_gaussian(dataset, 2676, 2689)

x3, y3, x_fit3, y_fitted3, fitted_amplitude3, fitted_mean3, fitted_std_dev3 = fit_gaussian(dataset, 3058, 3067)

x4, y4, x_fit4, y_fitted4, fitted_amplitude4, fitted_mean4, fitted_std_dev4 = fit_gaussian(dataset, 3440, 3450)



#plot each gaussian isolated and save the plot

plot_function(x1, y1, x_fit1, y_fitted1, fitted_mean1, "plots/time_calibration_45ns_Gaussian.pdf","45 ")
plot_function(x2, y2, x_fit2, y_fitted2, fitted_mean2, "plots/time_calibration_53ns_Gaussian.pdf","53")
plot_function(x3, y3, x_fit3, y_fitted3, fitted_mean3, "plots/time_calibration_61ns_Gaussian.pdf","61")
plot_function(x4, y4, x_fit4, y_fitted4, fitted_mean4, "plots/time_calibration_69ns_Gaussian.pdf","69")



#now we do a linear plot of the means of the gaussians vs the time

time =[45, 53, 61, 69] #in nanoseconds

means = [fitted_mean1, fitted_mean2, fitted_mean3, fitted_mean4]

slope, intercept = linear_fit( means,time)

linear_plot(means, time, slope, intercept,"8","plots/time_calibration_means_vs_time_8ns_spacing.pdf")

print(slope, intercept)


