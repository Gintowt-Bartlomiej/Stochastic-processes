#!/usr/bin/env python
from numpy.random import *
import  numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import statsmodels.api as sm
import pylab as py
import seaborn as sns
import random
import math
from scipy.stats import norm

def proces_wienera(n, h):
    zeta = np.random.normal(loc=0, scale=1, size=n)
    W = [0]
    w = 0
    for i in range(n):
        w = w + h**(1/2) * zeta[i]
        W.append(w)
    return W
    

def wykres_wien():
    T = 10
    n = 100
    N = 120
    h = T/n
    t = [i*h for i in range(n+1)]
    wienery = []
    for i in range(n):
        W = proces_wienera(n, h)
        wienery.append(W)
        plt.plot(t, W, color='green')
    
    #kwantyle teoretyczne
    qp1 = norm.ppf([0.05], loc=0, scale=1)
    qp2 = norm.ppf([0.95], loc=0, scale=1)
    plt.plot(t, qp1 * np.sqrt(t), color='red')
    plt.plot(t, qp2 * np.sqrt(t), color='red')

    #kwantyle empiryczne
    tn = [[] for i in range(n+1)]
    kwantyle1 = []
    kwantyle2 = []
    for i in range(n+1):
        for j in range(len(wienery)):
            win_j = wienery[j]
            wartosci_i = win_j[i]
            tn[i].append(wartosci_i)
        kwantyle1.append(np.quantile(tn[i], 0.05))
        kwantyle2.append(np.quantile(tn[i], 0.95))
    plt.plot(t, kwantyle1, color='orange')
    plt.plot(t, kwantyle2, color='orange')
    plt.show()

wykres_wien()