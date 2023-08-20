#NUMPY
"""NumPy is a fundamental package for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, 
   as well as a wide range   of mathematical functions to operate on these arrays."""
import numpy as np
arr = np.array([11, 12, 23, 34, 15, 36, 74, 69])
print('1-Dimensional:\n',arr)
#Multidimensional Array-
arr1 = np.array([[1,2,3,4,5],[6,7,8,9,0],[11,12,13,14,15],[16,17,18,19,20]])
print('Multi-dimensional:\n',arr1)
print('Dimension:',arr1.ndim)
#Array Operations- to find the MAXIMUM, MEAN, SUM of an array
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)
arr_max = np.max(arr)
print()
print('sum of all elements:',arr_sum)
print('Mean:',arr_mean)
print('Element with maximum value:',arr_max)
print()
#Array Manipulation- to RESHAPE or SLICE the array
reshaped_arr = arr.reshape(8,1)
print('Reshaped array:\n',reshaped_arr)
sliced_arr = arr[2:6]
print('Sliced array:',sliced_arr)
#TASK-Using Numpy access the random package and then the randint package the in the range of0 to 50 retrieve any 30 random integers
a = np.random.randint(0,50,30)
print('Random:\n',a)

#MATPLOTLIB
"""matplotlib is a widely used library for creating static, interactive, and animated visualizations in Python. 
   The pyplot module provides a MATLAB-like interface for plotting."""
#LINE PLOT
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 14, 8, 20, 6]
plt.plot(x, y,color='orange', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()
#Using NumPy
u = np.array([1,3,5,7,9])
v = np.array([18,25,37,19,21])
plt.plot(u,v,marker = '.')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot - NumPy')
plt.show()
#SCATTER PLOT
x = [1, 2, 3, 4, 5]
y = [10, 14, 8, 20, 6]
plt.scatter(x, y, color = 'green',marker ='h')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()
#BAR PLOT
#plt.bar(attributes)- for a vertical bar plot
#plt.barh(attributes)- for a horizantal bar plot
categories = ['A', 'B', 'C','D','E']
values = [25, 40, 30, 15, 45]
plt.barh(categories, values, color = ['orange','gold','green','blue','red'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.show()

#PANDAS
"""pandas is a powerful library for data manipulation and analysis. 
   It provides data structures like Series (1D) and DataFrame (2D) to efficiently work with structured data.
   DATAFRAME- tabled data(it is data in table format)"""
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie','Michael','Jackson','Percy','Pearson','Miguel','Arthur','Edward','Stuart','Leonard','Raj','Sheldon','Howard'],
        'Age': [25, 30, 22, 18, 31, 23, 39, 31, 38, 34, 24, 26, 19, 29, 29]}
df = pd.DataFrame(data)
print(df)
#Data Exploration---
print()
print('First few rows:\n',df.head())  # Display first few rows
print('Statistics:\n',df.describe())  # Summary statistics
print(df['Age'].mean() )            # Mean of the 'Age' column
#Data Filtering---
print()
young_people = df[df['Age'] < 30]
print(young_people)
print(type(df))

