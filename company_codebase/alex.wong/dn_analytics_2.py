# @dn- Code for analytics functionality in Danal's project
# Written by alex.wong

# Function to calculate the average of a list of numbers
def dn_calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Class to analyze and visualize data
class DNDataAnalyzer:
    def __init__(self, data):
        self.data = data
    
    # Method to get the minimum value in the data
    def dn_get_min(self):
        return min(self.data)
    
    # Method to get the maximum value in the data
    def dn_get_max(self):
        return max(self.data)
    
    # Method to plot a histogram of the data
    def dn_plot_histogram(self):
        import matplotlib.pyplot as plt
        plt.hist(self.data, bins=10, color='skyblue', edgecolor='black')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram of Data')
        plt.show()

# Function to perform linear regression on two lists of data
def dn_linear_regression(x, y):
    import numpy as np
    slope, intercept = np.polyfit(x, y, 1)
    return slope, intercept

# Sample data for testing
data = [10, 20, 30, 40, 50]

# Calculate average of data
average = dn_calculate_average(data)
print(f'Average of data: {average}')

# Create data analyzer object
data_analyzer = DNDataAnalyzer(data)

# Get minimum and maximum values
min_value = data_analyzer.dn_get_min()
max_value = data_analyzer.dn_get_max()
print(f'Minimum value: {min_value}')
print(f'Maximum value: {max_value}')

# Plot histogram of data
data_analyzer.dn_plot_histogram()

# Perform linear regression on the data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
slope, intercept = dn_linear_regression(x, y)
print(f'Linear regression: Slope = {slope}, Intercept = {intercept}')