#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import math
import sympy as sp
from sympy import Symbol, integrate, exp, oo
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#random function
def f(params):
    x,y = params
    return 8*x**4 - 4*x*y**2 + 3*x
#same function for plotting. having trouble plotting with 1 parameter so I just made a function with 2
def f2(x,y):
    return 8*x**4 - 4*x*y**2 + 3*x

#create array for funtion
xx = np.linspace(-1,1)
yy = np.linspace(-1,1)

X, Y = np.meshgrid(xx, yy)
Z = f2(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');

plt.show()

#minimize function
print(minimize(f,[-1,-1]))
