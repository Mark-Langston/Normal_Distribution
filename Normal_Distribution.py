# CSC220 Applied Probability & Stats.
# Mark Langston            6/12/2024 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Minimum parameters for the normal distribution
mu = 5  # Mean
sigma = 1  # Standard deviation

# Samples
num_samples = 1000

# normal distribution with mean = 5 and standard deviation = 1
normal_distribution = np.random.normal(loc=mu, scale=sigma, size=num_samples)

# Converts the numpy array to a pandas data frame
df = pd.DataFrame(normal_distribution, columns=['value'])

# Plots histogram
plt.figure(figsize=(10, 6))
plt.hist(df['value'], bins=30, edgecolor='k', alpha=0.7)
plt.title('Histogram of Normal Distribution\nMean = 5, Std Dev = 1')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Displays basic statistics
print("Basic Statistics of Generated Data:")
print(df.describe())