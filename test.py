#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x=[-6,-4.4,-2.8,-1.2,0.4,2.0]
cl=[-0.14283976,0.04842823,0.23821588,0.42949522,0.61754143,0.80724514]
cd=[0.00704654,0.00739093,0.00773458,0.00811582,0.00804468,0.00814308]

cl_0=cl[1]-x[1]*((cl[0]-cl[5])/(x[0]-x[5]))
print(cl_0)


plt.plot(x,cd)

plt.show()
