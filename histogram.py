# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:28:14 2017

@author: JT
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#histogram
#y = np.random.standard_normal((1000, 2))
#plt.figure(figsize=(7,4))
#plt.hist(y, label=['1st', '2nd'], bins=25)
#plt.grid(True)
#plt.legend(loc=0)
#plt.xlabel('value')
#plt.ylabel('frequency')
#plt.title('Histogram')

#histogram stacked bars
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7,4))
plt.hist(y, label=['1st', '2nd'], color=['b', 'g'], stacked=True, bins=20)
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')