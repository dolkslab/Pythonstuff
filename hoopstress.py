#!bin/python

import numpy as np
import matplotlib.pyplot as plt

#deltap in pa
deltap=0.5*100000
mega=1000*1000
kilo=1000



def tlongstress(r, stressallow):
	return (deltap*r)/(2*stressallow)
	
def thoopstress(r, stressallow):
	return (deltap*r)/stressallow
	
def weightforcylinder(r, t, rho):
    return np.pi*rho*(2*r*t+t*t)


#diameters array

class Material:
	def __init__(self, name, stressallow, ud, rho, t, relweight):
		self.name = name
		self.stressallow = stressallow
		self.ud = ud
		self.rho =rho
		self.t = t 
		self.relweight = relweight
		




alum_alloy = Material("Aluminium alloy 2024-T3", 85*mega, False, 2.8*kilo, 0, 0)
tita_alloy = Material("Titanium alloy Ti6Al4V", 200*mega, False, 4.8*kilo, 0, 0)
hs_steel = Material("HS steel", 400*mega, False,7.8*kilo, 0, 0)
carbon_steel = Material("Carbon steel", 95*mega, False, 7.8*kilo, 0, 0)
c_epox_ud = Material("Carbon-epoxy UD50", 250*mega, True, 1.8*kilo, 0, 0) 
glass_epoxy_ud = Material("Glass-epoxy UD50", 150*mega, True, 2.1*kilo, 0, 0)

#materials
mats = [alum_alloy, tita_alloy, hs_steel, carbon_steel, c_epox_ud, glass_epoxy_ud]


#diameters
radii = np.array([1, 2, 3])

for mat in mats:
	ts = np.array([])
	weights = np.array([])
	for r in radii:	
		t=0
		if mat.ud == False:
			t=thoopstress(r, mat.stressallow)
		else:  
			t=thoopstress(r, mat.stressallow)+tlongstress(r, mat.stressallow)
		ts=np.append(ts,t*1000)
		weight=weightforcylinder(r, t, mat.rho)
		weights=np.append(weights, weight)
	mat.t=ts
	mat.relweight=weights
	print(mat.name + " " + str(mat.t) + "mm " + str(mat.relweight)+"kg")




#for plotting
radii = np.array([1, 2, 3])
res = np.array([])

stresses = np.arange(85*mega, 400*mega, mega)
for r in radii:
	ts = np.array([])
	for x in stresses:
		ts=np.append(ts, thoopstress(r,x))
	res=np.append(res, ts)

print(res[0])
"""
plt.plot(stresses, ts)
plt.suptitle('Stress vs thickness for r=' + str(r))
plt.xlabel("Stress [Pa]")
plt.ylabel("thickness [m]")
plt.show()
"""

		
		
