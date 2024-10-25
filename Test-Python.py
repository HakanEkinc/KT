import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define a multi-Gaussian function
def multi_gaussian(x, *params):
    n = len(params) // 3  # Each Gaussian has 3 parameters: amplitude, mean, std_dev
    y = np.zeros_like(x)
    for i in range(n):
        amplitude = params[i * 3]
        mean = params[i * 3 + 1]
        std_dev = params[i * 3 + 2]
        y += amplitude * np.exp(-(x - mean)**2 / (2 * std_dev**2))
    return y

# Example data - Replace with your actual dataset
x_data = np.linspace(-10, 10, 1000)
y_data = (
    3 * np.exp(-(x_data - (-4))**2 / (2 * 1.5**2)) +
    2 * np.exp(-(x_data - (-1))**2 / (2 * 0.5**2)) +
    4 * np.exp(-(x_data - 2)**2 / (2 * 0.8**2)) +
    1.5 * np.exp(-(x_data - 5)**2 / (2 * 1.2**2)) +
    2.5 * np.exp(-(x_data - 7)**2 / (2 * 0.7**2)) +
    np.random.normal(0, 0.1, x_data.size)
)

# Initial guess for parameters (amplitude, mean, std_dev for each peak)
initial_guess = [
    3, -4, 1.5,   # First peak
    2, -1, 0.5,   # Second peak
    4, 2, 0.8,    # Third peak
    1.5, 5, 1.2,  # Fourth peak
    2.5, 7, 0.7   # Fifth peak
]

# Fit the multi-Gaussian model
params, _ = curve_fit(multi_gaussian, x_data, y_data, p0=initial_guess)

# Plot the data and the fitted curve
plt.plot(x_data, y_data, 'b-', label='Data')
plt.plot(x_data, multi_gaussian(x_data, *params), 'r--', label='Fitted Curve')

# Optionally, plot each individual Gaussian component
for i in range(5):
    plt.plot(
        x_data,
        params[i * 3] * np.exp(-(x_data - params[i * 3 + 1])**2 / (2 * params[i * 3 + 2]**2)),
        linestyle='--'
    )

plt.legend()
plt.show()
