#!\bin\python
import numpy as np
import matplotlib.pyplot as plt
n=9


g=10
wtotal=1000000
wfuel=40000
weng=30000

tmax=0
weng_new=0
weng_red=0
wfuel_red=0

crthrust = tmax*0.2
weightreds=np.array([])

wtotal=wtotal-2000*10
for x in range(n):
	tcruise=(0.05*wtotal)/4
	tmax=tcruise*5
	weng_new=tmax/2.083333
	weng_red=weng-weng_new
	wfuel_new=(weng_new/weng)*wfuel
	wfuel_red=wfuel-wfuel_new
	wtotal=wtotal-4*weng_red-wfuel_red
	weightreds=np.append(weightreds, 1000000-wtotal)
	wfuel=wfuel_new
	weng=weng_new
	print(1000000-wtotal)
	

	

plt.plot(np.arange(1,n+1,1), weightreds, "r")
plt.suptitle("Total weight reduction vs iterations n")
plt.xlabel("n")
plt.ylabel("Total Weight Reduction [N]")
plt.show()

