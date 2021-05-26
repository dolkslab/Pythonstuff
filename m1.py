#!\bin\python
import numpy as np
import matplotlib.pyplot as plt
import math
n=10

P_el=15
P_cam=6.5
P_comm=5

T_day=11.417
T_night=13.2

g=0.37
rho=0.013213535

solar_eff=0.0485
E_sun=589
rho_solar=0.32

rho_batt=200

C_L_opt=0.6360154327
C_d_opt=0.02164
e=0.9
span=7.5
chord=0.3

n_motor=0.87
n_prop=0.79

m_cam=1
m_struct=0.25
rho_al=2702
t_wingskin=0.001

pels=np.array([])


def find_vel(C_L,rho,W,S):
	return math.sqrt((2*W)/(rho*S*C_L))
	
def CD(C_L,C_d,A,e):
	return C_d+(pow(C_L,2))/(math.pi*A*e)

for x in range(n):
	P_day=P_el+P_cam+P_comm
	P_night=P_el+P_comm
	
	P_solar=((P_cam*T_day+P_el*(T_night+T_day)+P_comm*(T_night+T_day))/T_day)
	E_solar=math.sin(math.pi/4)*solar_eff*E_sun
	A_solar=P_solar/E_solar
	m_solar=rho_solar*A_solar
	
	E_batt=T_night*(P_comm+P_el)
	m_batt=E_batt/rho_batt
	
	m_wings=span*chord*t_wingskin*rho_al*2
	
	W_total=(m_batt+m_solar+m_cam+m_struct+m_wings)*g
	spd=find_vel(C_L_opt,rho,W_total,(span*chord))
	
	P_r=pow(spd,3)*0.5*(span*chord)*rho*CD(C_L_opt,C_d_opt,(span/chord),e)
	P_el=(P_r/(n_motor*n_prop))+4
	print(P_el)
	

print(span*chord)
print(W_total/g)
print(CD(C_L_opt,C_d_opt,(span/chord),e))
print(spd)
print(P_r)




