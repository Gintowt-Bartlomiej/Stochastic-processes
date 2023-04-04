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

def proces_ryzyka(lam, T, theta, u):
    listI, poisson = poison(lam, T)
    X = []
    mi = 4
    for i in range(max(listI)):
        X.append(np.random.exponential(scale=1/mi))
        
    c=lambda t: (1+theta)/mi*lam*t
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

    for i in range(len(y)):
        if y[i] < 0:
            return 1
    return 0

def ruina():
    lam = 3
    theta = 4/3 - 1
    T1 = 3
    T2 = 200

    u = 1
    N = 1000
    n1 = 0
    for i in range(N):
        n1 = n1 + proces_ryzyka(lam, T1, theta, u)
    print(n1/N)

    n2 = 0
    for j in range(N):
        n2 = n2 + proces_ryzyka(lam, T2, theta, u)
    print(n2/N)
ruina()



def chinczyn(theta, lam, mi, u): #ruina w nieskończonym czasie za pomoca monte carlo
    I = 0
    k = np.random.geometric(theta/(1+theta))
    #c=lambda t: (1+theta)/mi*lam*t
    y = np.random.exponential(scale=1/4, size=k-1)
    y_sum = sum(y)
    if y_sum > u:
        return 1
    else:
        return 0

def wartosc_chin():
    theta = 1/3
    u = 1
    beta = 4
    T = 200
    lam = 4
    mi = 1/lam
    N = 1000
    n = 0 
    for i in range(N):
        n = n + chinczyn(theta, lam, mi, u)
    print(n/N)
    print(1/(1+theta) * np.exp(-u*beta*theta/(1+theta)))
wartosc_chin() #ma wyjsc 0.27