import numpy as np
import math


def magnitude(a):
	return np.linalg.norm(a)
	
def normalize(a):
	return a/magnitude(a)
	

