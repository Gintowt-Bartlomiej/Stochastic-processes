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

"""Generowanie procesu jednorodnego Poissona"""
def jednorodny_poisson(lam, T):
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


"""Generowanie procesu Poissona za pomocą przyrostów"""
def poisson_z_przyrostow(lam, T):
    n = T*100
    N = []
    h = T/n
    for i in range(n):
        if i != 0:
            U = np.random()
            if U <= lam * h:
                N.append(N[-1]+1)
            else:
                k = N[-1]
                N.append(k)
        else:
            N.append(0)
    return N

"""Generowanie procesu Poissona przy pomocy rozkładu Poissona """
def poisson_z_rozkladu(lam, T):
    n = np.random.poisson(lam*T)
    if n != 0:
        U = [uniform(0, T) for i in range(n)]
        U.sort()
        s = U
        ys = [i for i in range(len(s))]
        ts = list(s)
    return (ts, ys)