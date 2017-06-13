# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:37:12 2017

@author: JT
"""
import numpy as np
import matplotlib.pyplot as plt

#boxplot
y = np.random.standard_normal((1000, 2))
plt.boxplot(y)
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('data set')
plt.ylabel('value')
plt.title('Boxplot')