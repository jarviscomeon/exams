# -*- coding: utf-8 -*-
"""ML4A For a given set of training data examples stored in a .CSV file implement LeastSquare Regression algorithm..ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NtbWiramMH7RXsMYK8HGlD4ptU5hY2Mw
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv('/content/DS4.csv')
data.head()

# Coomputing X and Y
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values
# Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Total number of values
n = len(X)

# Using the formula to calculate 'm' and 'c'
numer = 0
denom = 0
for i in range(n):
  numer += (X[i] - mean_x) * (Y[i] - mean_y)
  denom += (X[i] - mean_x) ** 2
m = numer / denom
c = mean_y - (m * mean_x)

# Printing coefficients
print("Coefficients")
print(m, c)

#OUTPUT

# Plotting Values and Regression Line
max_x = np.max(X) + 100
min_x = np.min(X) - 100

# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = c + m * x

# Ploting Line
plt.plot(x, y, color='#58b970', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()