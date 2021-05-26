#!\bin\python
import numpy as np
import matplotlib.pyplot as plt
import math


def I_circ(d, t):
	return math.pi*((0.5*d)**3)*t
	
def stress_buckling(d, L, E, t):
	return E*(9*(((2*t)/d)**1.6)+0.16*((t/L)**1.3))
	
def stress_load(d, L ,g_y, g_x, m, t):
	return (g_y*m*g_0*L*0.5*d)/(2*I_circ(d,t))+(g_x*g_0*m)/(math.pi*(0.5*d)**2)
##safety factors
j_q=1.25
j_u=2


#Other data
E = 71*(10**9)
sigma_ult = 517
d = 0.937
L = 1.8
m = 3000

g_x = 4.4
g_y = 2
g_0 = 9.81

 
tlist=np.arange(0.5, 4, 0.01)*0.001

x_buckling = stress_buckling(d, L, E, tlist)*(10**(-6))
x_ult = j_q*j_u*stress_load(d, L, g_y, g_x, m, tlist)*(10**(-6))

tlist_short = [0.5*0.001, 4.0*0.001]
sigma_ult_list= [sigma_ult, sigma_ult]



fig, ax = plt.subplots()


ax.plot(tlist, x_buckling, "b", label='Buckling stress')
ax.plot(tlist, x_ult, "r", label='Stress at ult load')
ax.plot(tlist_short, sigma_ult_list, "g", label='UTS of material')


plt.xlabel("thickness t [mm]")
plt.ylabel("Stress [MPa]")
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
#legend.get_frame().set_facecolor('C0')

plt.show()



