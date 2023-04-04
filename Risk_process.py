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
from scipy.stats import poisson

"""Generowanie poissona jednorodnego"""
def poison(lam,T):
    I=0
    t=0
    ListI=[0]
    S=[0]
    u=rand()
    t=t-1/lam*math.log(u)
    S.append(t)
    I += 1
    ListI.append(I)
    while t<T:
        u = rand()
        t = t - 1 / lam * math.log(u)
        if t<T:
            S.append(t)
            I += 1
            ListI.append(I)
    return ListI,S

def proces_ryzyka(lam, T, mi, theta, u):
    listI, poisson = poison(lam, T)
    X = []
    for i in range(max(listI)):
        X.append(np.random.exponential(scale=1/3))
    c=lambda t: (1+theta)/3*lam*t
    N = lambda t: np.sum(poisson <= t) - 1
    R=lambda t: u+c(t)
    y=[]
    for i in np.array(poisson):
        if i==0:
            y.append(R(i) - np.sum(X[:N(i)]))
        else:
            y.append(R(i) - np.sum(X[:N(i) - 1]))
            y.append(R(i)-np.sum(X[:N(i)]))
    x=[0]
    for i in poisson:
        if i!=0:
            x.append(i)
            x.append(i)
    plt.plot(x,y,color="red")


def wykres():
    lam = 2
    T = 20
    theta = 1
    mi = 2
    u = 5
    for i in range(100):
        d = proces_ryzyka(lam, T, mi, theta, u)
    t=np.linspace(0,T,1000)
    c=lambda t: (1+theta)/3*lam*t
    plt.plot(t, u+c(t)-1/3*lam*t)
    plt.show()
wykres()