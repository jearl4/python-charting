# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:40:27 2017

@author: JT
"""
import numpy as np
import matplotlib.pyplot as plt

#transform both 1D arrays into 2D arrays
strike = np.linspace(50, 150, 24)
ttm = np.linspace(0.5, 2.5, 24)
strike, ttm = np.meshgrid(strike, ttm)

#generate fake volatilities
impliedVol = (strike - 100) ** 2 / (100 * strike) / ttm
          
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(30, 60)
ax.scatter(strike, ttm, impliedVol, zdir='z', s=25, c='b', marker='^')
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied Volatility')