import numpy as np
import math


def mag(a):
	return np.linalg.norm(a)
	
def normalize(a):
	return a/mag(a)
	
def screencoords(pos, res, scale):
    pos = np.array(pos)
    
    if pos.shape == (2,):
        out = np.array([pos[0]*scale, res[1] - pos[1]*scale])
    else:
        out = np.stack((pos[:,0]*scale, res[1] - pos[:,1]*scale), axis=1)
    return out
	
def angle(a):
	#compute angle to origin of 2d vector
	x = a[0]
	y = a[1]
	return math.atan2(y,x)
	

