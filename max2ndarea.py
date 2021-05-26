#!\bin\python
import numpy as np
import matplotlib.pyplot as plt
import math


def secmomAsq(b,t):
	return (2/3)*pow(b,3)*t
	
def invsecmomAsq(b,I):
	return 1.5*(I/pow(b,3)) 
	
def invsecmomAsq2(t,I):
	return pow((I/((2/3)*t)), (1/3))
	
def Asq(b,t):
	return 4*t*b
	
def invsecmomAcirc(r,I):
	return I/(math.pi*pow(r,3))
	
def invpolmomAcirc(r,J):
	return J/(2*math.pi*pow(r,3))
	
def Acirc(r, t):
	return 2*math.pi*r*t
	

##safety factor
S=1.4

Ireq=2.384*0.5*pow(10,-6)*S
Kreq=2.549*pow(10,-7)*S

blist=np.arange(20, 200, 0.1)*0.001

tsqlist=invsecmomAsq(blist, Kreq)
Asqlist=Asq(blist,tsqlist)

tcirclist = invsecmomAcirc(0.5*blist, Ireq)
Acirclist = Acirc(0.5*blist,tcirclist)




print(invsecmomAsq(0.13, Ireq))



outfile=open("out.dat","w")



outfile.write("b	tsq 	asq	tcirc  	acirc\n")
for b in blist:
	tsq=invsecmomAsq(b, Ireq)
	tcirc=invsecmomAcirc(0.5*b, Ireq)
	outfile.write(str(b*1000)+" "+ str(tsq*1000) +" "+ str(Asq(b,tsq)*1000*1000)+" "+str(tcirc*1000)+" "+ str(Acirc(0.5*b,tcirc)*1000*1000)+"\n")
	

outfile.close()

plt.figure()


plt.subplot(111)
plt.plot(blist, Asqlist, "b", label="Hollow square")
plt.plot(blist, Acirclist, "r", label="Hollow cylindrical")

plt.suptitle("Area vs width")
plt.xlabel("Width[m]")
plt.ylabel("Area[m2]")




legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
# Put a nicer background color on the legend.

plt.show()



