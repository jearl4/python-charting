# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:28:49 2017

@author: JT
"""
import numpy as np
import matplotlib.pyplot as plt

# without matplotlib function
#y = np.random.standard_normal((1000, 2))
#plt.figure(figsize = (7, 5))
#plt.plot(y[:, 0], y[:, 1], 'ro')
#plt.grid(True)
#plt.xlabel('1st')
#plt.ylabel('2nd')
#plt.title('Scatter Plot')

# with matplotlib function
#y = np.random.standard_normal((1000, 2))
#plt.figure(figsize=(7,5))
#plt.scatter(y[:, 0], y[:, 1], marker='o')
#plt.grid(True)
#plt.xlabel('1st')
#plt.ylabel('2nd')
#plt.title('Scatter Plot')

# 3D scatter plot
y = np.random.standard_normal((1000, 2))
c = np.random.randint(0, 10, len(y))
plt.figure(figsize=(7,5))
plt.scatter(y[:,0], y[:,1], c=c, marker='o')
plt.colorbar()
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')