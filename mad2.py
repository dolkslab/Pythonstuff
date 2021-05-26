#!/usr/bin/python3
import numpy as np
import math

GM=4.282837*math.pow(10,13)
vid_size=481610.3226
transfer_rate=200
r_mars=3389.5*1000
height=0

mars_day=88642.66





def theta(h,a):
	return 2*(math.acos(r_mars/(r_mars+h))+math.acos(r_mars/a))
	
def T_orb(a):
	return math.sqrt(math.pow(a,3)/GM)




t_total=0
a=r_mars

for n in range(7):
	t_total=0
	while t_total<=(vid_size/transfer_rate):
		a+=math.pow(10,3-n)
		t_total=(theta(height,a)*(T_orb(a)))
		t_n_old=t_total
		for i in range(10):
			t_n=((math.tau/mars_day)*t_n_old)*(T_orb(a))
			t_total=t_total+t_n
			t_n_old=t_n

	print(t_total/60)
	print(a/1000)	
	print("")
	a-=math.pow(10,4-n)

	
a+=math.pow(10,4-n)
print((a-r_mars)/1000)


			

