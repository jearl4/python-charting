# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 00:01:29 2017

@author: JT
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2000)
y = np.random.standard_normal((20, 2)).cumsum(axis=0)
#
#plt.figure(figsize=(7,4))
#fig, ax1 = plt.subplots()
#plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
#plt.plot(y[:, 0], 'ro')
#plt.grid(True)
#plt.legend(loc=8)
#plt.axis('tight')
#plt.xlabel('index')
#plt.ylabel('value 1st')
#plt.title('A Simple Plot')
#
#ax2 = ax1.twinx()
#plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
#plt.plot(y[:, 1], 'ro')
#plt.legend(loc=0)
#plt.ylabel('value 2nd')

# two seperate subplots
#plt.figure(figsize=(7,5))
#plt.subplot(211)
#plt.plot(y[:, 0], lw=1.5, label='1st')
#plt.plot(y[:, 0], 'ro')
#plt.grid(True)
#plt.legend(loc=0)
#plt.axis('tight')
#plt.ylabel('value')
#plt.title('A Simple Plot')
#plt.subplot(212)
#plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
#plt.plot(y[:, 1], 'ro')
#plt.grid(True)
#plt.legend(loc=0)
#plt.axis('tight')
#plt.xlabel('index')
#plt.ylabel('value')

# Two subplots with different graphs
plt.figure(figsize=(9,4))
plt.subplot(121)
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
plt.title('1st Data Set')
plt.subplot(122)
plt.bar(np.arange(len(y)), y[:, 1], width=0.5, color='g', label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.title('2nd Data Set')