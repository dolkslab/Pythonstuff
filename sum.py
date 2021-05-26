#!bin/python

import numpy as np
import matplotlib.pyplot as plt
import math

def intf(x):
	S=0
	for n in range(1,5):
		S=S+((pow(-1,n-1))/(n*(3*n+1))*pow(x,3*n+1))
	return(S)
	
def sin(x):
	S=0
	for n in range(10):
		S=S+((pow(-1,n))/math.factorial(2*n+1))*pow(x,2*n+1)
	return(S)


def cos(x):
	S=0
	for n in range(10):
		S=S+((pow(-1,n))/math.factorial(2*n))*pow(x,2*n)
	return(S)


print(intf(0.5))

xs = np.arange(-2*math.pi,2*math.pi,0.01)


##plt.plot(xs,cos(xs), "r")
##plt.show()
