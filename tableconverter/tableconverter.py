import os
import re
with open('data.dat', 'r') as infile:
	col0=[]
	col1=[]
	col2=[]
	col3=[]
	cols = [col0, col1, col2, col3]
	curcol = 3
	for line in infile:
		if line.strip()[0].isalpha():
			print(line.strip())
			curcol += 1
			if curcol == 4:
				curcol =0
		cols[curcol].append(line.strip().replace(',','.'))
	

		 
print (cols[3])
with open('dataout.dat', 'w') as outfile:

	for i in range(len(cols[0])-1):
		outfile.write(str(cols[0][i]) + '	' + str(cols[1][i]) + '	' + str(cols[2][i]) + '	' + str(cols[3][i] +'\n' ))
		
		 
