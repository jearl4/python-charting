# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:07:26 2017

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
             
#plot
fig = plt.figure(figsize=(9,6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(strike, ttm, impliedVol, rstride=2, cstride=2,
                       cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
fig.colorbar(surf, shrink=0.5, aspect=5)