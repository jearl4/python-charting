# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 23:21:06 2017

@author: JT
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#%matplotlib inline

np.random.seed(1000)
y = np.random.standard_normal(20)

#x = range(len(y))
#plt.plot(x, y)
#plt.plot(y)
#plt.plot(y.cumsum())
#plt.plot(y.cumsum())
#plt.grid(True) # adds grid
#plt.axis('tight') # adjusts the axis ranges
#plt.xlim(-1, 20)
#plt.xlim(np.min(y.cumsum()) - 1, np.max(y.cumsum()) + 1)
plt.figure(figsize=(7,4)) # fig size is size in (width, height)
plt.plot(y.cumsum(), 'b', lw=1.5)
plt.plot(y.cumsum(), 'ro')
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')